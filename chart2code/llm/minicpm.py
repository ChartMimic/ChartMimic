from PIL import Image 
import torch
from transformers import AutoModel, AutoTokenizer
from common.registry import registry

@registry.register_llm("minicpm")
class Minicpm:
    def __init__(
        self,
        engine="minicpm",
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
        self.tokenizer = AutoTokenizer.from_pretrained(
            self.engine,
            trust_remote_code=True
        )
        self.model = AutoModel.from_pretrained(
            self.engine,
            trust_remote_code=True,
            torch_dtype=torch.bfloat16,
            device_map="auto"
        ).eval()
        self.generation_config = dict(
            max_new_tokens=self.max_tokens,
            temperature=self.temperature,
            top_p=self.top_p,
            do_sample=(self.temperature != 0),
        )


    def generate(self, conversation):
        image = Image.open(conversation[0]['content'][1]['image_url']).convert('RGB')
        messages = [ 
            {"role": "user", "content": f"{conversation[0]['content'][0]['text']}"}, 
        ]
        # import pdb; pdb.set_trace()
        response = self.model.chat(
            image=image,
            msgs=messages,
            tokenizer=self.tokenizer,
            temperature=self.temperature,
            # top_p=self.top_p,
            do_sample=True,
            # max_new_tokens=self.max_tokens,
        )
        
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
