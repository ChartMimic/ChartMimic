import os
import torch

from transformers import AutoProcessor, AutoModelForVision2Seq
from transformers.image_utils import load_image
from common.registry import registry

@registry.register_llm("idefics2")
class Idefics2:
    def __init__(
        self,
        engine="Idefics2",
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
        self.model = AutoModelForVision2Seq.from_pretrained(
            self.engine,
            torch_dtype=torch.bfloat16,
            low_cpu_mem_usage=True,
            device_map='auto',
            _attn_implementation="flash_attention_2",
            trust_remote_code=True
        ).eval()
        self.processor = AutoProcessor.from_pretrained(self.engine, trust_remote_code=True)
        self.generation_config = self.model.generation_config
        self.generation_config.max_new_tokens = self.max_tokens
        self.generation_config.temperature=self.temperature
        self.generation_config.top_p=self.top_p
        self.generation_config.do_sample=(self.temperature != 0)


    def generate(self, conversation):
        # import pdb; pdb.set_trace()
        # conversation = self._convert_conversation(conversation)
        prompt = self.processor.apply_chat_template(conversation, add_generation_prompt=True)
        image = load_image(conversation[0]['content'][1]['image_url'])
        inputs = self.processor(text=prompt, images=[image], return_tensors="pt")
        inputs = {k: v.to(self.model.device) for k, v in inputs.items()}


        # Generate
        generated_ids = self.model.generate(**inputs, max_new_tokens=4096)
        generated_texts = self.processor.batch_decode(generated_ids, skip_special_tokens=True)

        return generated_texts[0]

    def _convert_conversation(self, conversation):
        converted_conversation = []
        if len (conversation) !=1 :
            print("QwenVL only supports 1-turn conversation")
            raise NotImplementedError
        for message in conversation:
            # import pdb; pdb.set_trace()
            # message_tmp = {}
            for content in message["content"]:
                if content["type"] == "text":
                    converted_conversation.append({
                        'type': 'text',
                        'text': content["text"]
                    })
                elif content["type"] == "image":
                    converted_conversation.append({
                        'type': 'image',
                        'url': content["image_url"]
                    })              
                else:
                    raise NotImplementedError
        return converted_conversation



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
