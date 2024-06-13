import torch
from PIL import Image
from transformers import AutoModelForCausalLM, AutoTokenizer
from common.registry import registry

@registry.register_llm("cogvlm2")
class Cogvlm2:
    def __init__(
        self,
        engine="cogvlm2",
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
            pad_token_id=128002, 
        )


    def generate(self, conversation):
        query = conversation[0]['content'][0]['text'].replace("the image below.", "the image above.")
        image = Image.open(conversation[0]['content'][1]['image_url']).convert('RGB')
        input_by_model = self.model.build_conversation_input_ids(self.tokenizer,
            query=query,
            history=None,
            images=[image],
            template_version='chat'
        )
        inputs = {
            'input_ids': input_by_model['input_ids'].unsqueeze(0).to(self.model.device),
            'token_type_ids': input_by_model['token_type_ids'].unsqueeze(0).to(self.model.device),
            'attention_mask': input_by_model['attention_mask'].unsqueeze(0).to(self.model.device),
            'images': [[input_by_model['images'][0].to(self.model.device).to(torch.bfloat16)]] if image is not None else None,
        }
        with torch.no_grad():
            outputs = self.model.generate(**inputs, **self.generation_config)
            outputs = outputs[:, inputs['input_ids'].shape[1]:]
            response = self.tokenizer.decode(outputs[0])
            response = response.split("<|end_of_text|>")[0]
        return response

    def _convert_conversation(self, conversation):
        converted_conversation = []
        if len (conversation) !=1 :
            print("Llava only supports 1-turn conversation")
            raise NotImplementedError
        for message in conversation:
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
