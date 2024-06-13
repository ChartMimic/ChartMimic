import torch

from transformers import LlavaNextProcessor, LlavaNextForConditionalGeneration
import torch
from PIL import Image
from common.registry import registry

@registry.register_llm("llava")
class Llava:
    def __init__(
        self,
        engine="llava",
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
        self.processor = LlavaNextProcessor.from_pretrained(self.engine)
        self.model = LlavaNextForConditionalGeneration.from_pretrained(
            self.engine,
            torch_dtype=torch.bfloat16,
            low_cpu_mem_usage=True, 
            device_map='auto',
            trust_remote_code=True,
            use_flash_attention_2=True
        ).eval()
        self.generation_config = self.model.generation_config
        self.generation_config.max_new_tokens = self.max_tokens
        self.generation_config.temperature=self.temperature
        self.generation_config.top_p=self.top_p
        self.generation_config.do_sample=(self.temperature != 0)


    def generate(self, conversation):
        image = Image.open(conversation[0]['content'][1]['image_url'])
        if "mistral" in self.engine:
            prompt = f"[INST] {conversation[0]['content'][0]['text']}<image>[/INST]"
        elif "vicuna" in self.engine:
            prompt = f"A chat between a curious human and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the human's questions. USER: {conversation[0]['content'][0]['text']}<image> ASSISTANT:"
        elif "llava-v1.6-34b-hf" in self.engine:
            prompt = f"<|im_start|>system\nAnswer the questions.<|im_end|><|im_start|>user\n{conversation[0]['content'][0]['text']}\n<image><|im_end|><|im_start|>assistant\n"
        else:
            prompt = f"USER: {conversation[0]['content'][0]['text']}<image> ASSISTANT:"
        inputs = self.processor(prompt, image, return_tensors="pt").to(self.model.device)
        output = self.model.generate(**inputs, generation_config=self.generation_config)

        return self.processor.decode(output[0], skip_special_tokens=True)

    def _convert_conversation(self, conversation):
        converted_conversation = []
        if len (conversation) !=1 :
            print("Llava only supports 1-turn conversation")
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
