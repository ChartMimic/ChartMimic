import openai
import os
import time
from common.registry import registry
import google.generativeai as genai
import PIL.Image

@registry.register_llm("gemini")
class GEMINI:
    def __init__(self,
                 engine="gemini-pro-vision",
                 temperature=0,
                 max_tokens=4096,
                 use_azure=True,
                 top_p=1,
                 stop=None,
                 retry_delays=60, # in seconds
                 max_retry_iters=5,
                 context_length=4096,
                 system_message=''
                 ):
        
        self.engine = engine
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.use_azure = use_azure
        self.top_p = top_p
        self.stop = stop
        self.retry_delays = retry_delays
        self.max_retry_iters = max_retry_iters
        self.context_length = context_length
        self.system_message = system_message
        self.init_api_key()

    def init_api_key(self):
        if 'GOOGLE_API_KEY' not in os.environ:
            raise Exception("GOOGLE_API_KEY environment variable not set.")
        else:
            genai.configure(api_key=os.environ["GOOGLE_API_KEY"], transport="rest")

    def llm_inference(self, conversation):
        model = genai.GenerativeModel(self.engine)
        response = model.generate_content(
            contents = conversation,
            stream = False,
            generation_config=genai.types.GenerationConfig(
                candidate_count=1,
                stop_sequences=self.stop,
                max_output_tokens=self.max_tokens,
                temperature=self.temperature,
            )
        )
        response.resolve()

        return response.text

    def generate(self, conversation):
        conversation = self._convert_conversation(conversation)
        for _ in range(self.max_retry_iters):
            try:
                response = self.llm_inference(conversation)
            except Exception as e:
                time.sleep(self.retry_delays)
                print(str(e))
                continue
            return response
        return None

    def _convert_conversation(self, conversation):
        converted_conversation = []
        for message in conversation:
            converted_message = {}
            converted_message["role"] = message["role"]
            converted_message["parts"] = []
            for content in message["content"]:
                if content["type"] == "text":
                    converted_message["parts"].append(content["text"])
                elif content["type"] == "image":
                    converted_message["parts"].append(PIL.Image.open(content["image_url"]))
                else:
                    raise NotImplementedError
            converted_conversation.append(converted_message)
        return converted_conversation

    @classmethod
    def from_config(cls, config):
        
        engine = config.get("engine", "gemini-pro")
        temperature = config.get("temperature", 0)
        max_tokens = config.get("max_tokens", 100)
        system_message = config.get("system_message", "You are a helpful assistant.")
        use_azure = config.get("use_azure", True)
        top_p = config.get("top_p", 1)
        stop = config.get("stop", ["\n"])
        retry_delays = config.get("retry_delays", 10)
        context_length = config.get("context_length", 4096)
        return cls(engine=engine,
                   temperature=temperature,
                   max_tokens=max_tokens,
                   use_azure=use_azure,
                   top_p=top_p,
                   retry_delays=retry_delays,
                   system_message=system_message,
                   context_length=context_length,
                   stop=stop)