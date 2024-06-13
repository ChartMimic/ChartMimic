from openai import OpenAI
import os
import time
from common.registry import registry
import base64


@registry.register_llm("gpt")
class OPENAI_GPT:
    def __init__(
        self,
        engine="gpt-4-vision-preview",
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
        self.client = OpenAI(
            base_url=os.environ["OPENAI_BASE_URL"], api_key=os.environ["OPENAI_API_KEY"]
        )

    def generate(self, conversation):
        conversation = self._convert_conversation(conversation)
        for _ in range(self.max_retry_iters):
            try:
                response = self.client.chat.completions.create(
                    model=self.engine,
                    messages=conversation,
                    max_tokens=self.max_tokens,
                    top_p=self.top_p,
                    temperature=self.temperature,
                )
            except Exception as e:
                time.sleep(self.retry_delays)
                print(str(e))
                continue
            return response.json()
        return None

    def _convert_conversation(self, conversation):
        converted_conversation = []
        for message in conversation:
            converted_message = {}
            converted_message["role"] = message["role"]
            converted_message["content"] = []
            for content in message["content"]:
                if content["type"] == "text":
                    converted_message["content"].append(
                        {"type": "text", "text": content["text"]}
                    )
                elif content["type"] == "image":
                    base64_image = self._encode_base_image(content["image_url"])
                    converted_message["content"].append(
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}"
                            },
                        }
                    )
                else:
                    raise NotImplementedError
            converted_conversation.append(converted_message)
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
