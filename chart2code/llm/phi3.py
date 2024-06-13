from PIL import Image 
import torch
from transformers import AutoModelForCausalLM, AutoProcessor 
from common.registry import registry

@registry.register_llm("phi3")
class Phi3:
    def __init__(
        self,
        engine="phi3",
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
        self.processor = AutoProcessor.from_pretrained(
            self.engine,
            trust_remote_code=True
        )
        self.model = AutoModelForCausalLM.from_pretrained(
            self.engine,
            torch_dtype=torch.bfloat16,
            trust_remote_code=True,
            device_map="auto"
        ).eval()
        self.generation_config = dict(
            max_new_tokens=self.max_tokens,
            temperature=self.temperature,
            top_p=self.top_p,
            do_sample=(self.temperature != 0),
        )


    def generate(self, conversation):
        image = Image.open(conversation[0]['content'][1]['image_url'])
        messages = [ 
            {"role": "user", "content": f"{conversation[0]['content'][0]['text']}\n<|image_1|>"}, 
        ] 
        prompt = self.processor.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        inputs = self.processor(prompt, [image], return_tensors="pt").to(self.model.device) 
        generate_ids = self.model.generate(**inputs, eos_token_id=self.processor.tokenizer.eos_token_id, **self.generation_config) 
        generate_ids = generate_ids[:, inputs['input_ids'].shape[1]:]
        response = self.processor.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0] 
        return response

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
