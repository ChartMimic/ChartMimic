from openai import OpenAI
import os
import time
from common.registry import registry
import base64
import torch
from transformers import AutoModelForCausalLM
from deepseek_vl.models import VLChatProcessor, MultiModalityCausalLM
from deepseek_vl.utils.io import load_pil_images

@registry.register_llm("deepseekvl")
class DeepSeekVL:
    def __init__(
        self,
        engine="deepseek-vl-7b-chat",
        temperature=0.1,
        max_tokens=4096,
        top_p=0.95,
        stop=[""],
        retry_delays=1,
        max_retry_iters=100,
        context_length=4096,
        system_message="",
    ):
        self.engine = engine
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.top_p = top_p
        self.stop = stop
        self.retry_delays = retry_delays
        self.max_retry_iters = max_retry_iters
        self.context_length = context_length
        self.system_message = system_message
        self.vl_gpt = AutoModelForCausalLM.from_pretrained(
            self.engine, trust_remote_code=True, device_map="auto", torch_dtype=torch.bfloat16
        ).eval()
        self.vl_chat_processor = VLChatProcessor.from_pretrained(self.engine)
        self.tokenizer = self.vl_chat_processor.tokenizer
        self.img_pad_token = "<image_placeholder>"
        self.role_mapping = {
            "system": "System",
            "user": "User",
            "assistant": "Assistant",
        }

    def generate(self, conversation):
        conversation = self._convert_conversation(conversation)
        pil_images = load_pil_images(conversation)
        prepare_inputs = self.vl_chat_processor(
            conversations=conversation, images=pil_images, force_batchify=True
        ).to(self.vl_gpt.device)
        inputs_embeds = self.vl_gpt.prepare_inputs_embeds(**prepare_inputs)

        outputs = self.vl_gpt.language_model.generate(
            inputs_embeds=inputs_embeds,
            attention_mask=prepare_inputs.attention_mask,
            pad_token_id=self.tokenizer.eos_token_id,
            bos_token_id=self.tokenizer.bos_token_id,
            eos_token_id=self.tokenizer.eos_token_id,
            max_new_tokens=self.max_tokens,
            do_sample=self.temperature != 0,
            use_cache=True,
            top_p=self.top_p,
            temperature=self.temperature,)
        answer = self.tokenizer.decode(outputs[0].cpu().tolist(), skip_special_tokens=True)
        return answer

    def _convert_conversation(self, conversation):
        converted_conversation = []
        for message in conversation:
            converted_message = {}
            converted_message["role"] = self.role_mapping[message["role"]]
            converted_message["content"] = ""
            images = []
            for content in message["content"]:
                if content["type"] == "text":
                    converted_message["content"] += content["text"]
                elif content["type"] == "image":
                    converted_message["content"] += self.img_pad_token
                    images.append(content["image_url"])                    
                else:
                    raise NotImplementedError
            if images:
                converted_message["images"] = images
            converted_conversation.append(converted_message)
        converted_conversation.append({"role": "Assistant", "content": ""},)
        return converted_conversation

    def _encode_base_image(self, file):
        with open(file, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode("utf-8")

    @classmethod
    def from_config(cls, config):
        engine = config.get("engine", "gpt-35-turbo")
        temperature = config.get("temperature", 0)
        max_tokens = config.get("max_tokens", 100)
        system_message = config.get("system_message", "")
        top_p = config.get("top_p", 1)
        stop = config.get("stop", ["\n"])
        retry_delays = config.get("retry_delays", 10)
        context_length = config.get("context_length", 4096)
        return cls(
            engine=engine,
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=top_p,
            retry_delays=retry_delays,
            system_message=system_message,
            context_length=context_length,
            stop=stop,
        )
