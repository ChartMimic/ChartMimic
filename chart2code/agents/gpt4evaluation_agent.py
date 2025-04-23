from agents.base_agent import BaseAgent
from common.registry import registry
import json
import base64
import PyPDF2


@registry.register_agent("GPT4EvaluationAgent")
class GPT4EvaluationAgent(BaseAgent):
    def __init__(
        self,
        llm_model,
        prompt_path=None,
    ):
        super().__init__()
        self.llm_model = llm_model
        if prompt_path is not None:  # load from file
            self.init_prompt_dict = json.load(open(prompt_path, "r"))
            self.instruction = self.init_prompt_dict["instruction"]
        else:
            raise Exception("init_prompt_path is None")

    def run(self, orginal_png_file, generated_png_file):
        conversation = self._constract_conversation(
            orginal_png_file, generated_png_file
        )
        response = self.llm_model.generate(conversation)
        return response

    def _constract_conversation(self, orginal_png_file, generated_png_file):
        conversation = [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": self.instruction},
                    {"type": "image", "image_url": orginal_png_file},
                    {"type": "image", "image_url": generated_png_file},
                ],
            }
        ]
        return conversation

    @classmethod
    def from_config(cls, llm_model, config):
        init_prompt_path = config.get("prompt_path", None)
        return cls(llm_model, init_prompt_path)
