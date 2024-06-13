from agents.base_agent import BaseAgent
from common.registry import registry
import json
import base64
import PyPDF2
import os
import pandas as pd

from dotenv import load_dotenv

load_dotenv()


@registry.register_agent("EditAgent")
class EditAgent(BaseAgent):
    def __init__(
        self,
        llm_model,
        prompt_path=None,
    ):
        super().__init__()
        self.llm_model = llm_model
        self.dimensions_info = pd.read_json(
            f"{os.environ['PROJECT_PATH']}/dimentions_info_edit.jsonl",
            lines=True,
        )

    def run(self, file):
        width, height, instruction = self._get_pdf_dimensions(file)
        conversation = self._constract_conversation(file, width, height, instruction)
        response = self.llm_model.generate(conversation)
        return response

    def _get_pdf_dimensions(self, pdf_path):
        file_idx = "{}_{}".format(
            pdf_path.split("/")[-1].split("_")[0],
            pdf_path.split("/")[-1].split("_")[1],
        ).replace(".pdf", "")
        width = self.dimensions_info[self.dimensions_info["idx"] == file_idx][
            "width"
        ].values[0]
        height = self.dimensions_info[self.dimensions_info["idx"] == file_idx][
            "height"
        ].values[0]
        instruction = self.dimensions_info[self.dimensions_info["idx"] == file_idx][
            "instruction"
        ].values[0]
        return width, height, instruction

    def _constract_conversation(self, file, width, height, instruction):
        conversation = [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": instruction
                        + f"\nNote that it is necessary to use figsize=({width}, {height}) to set the image size.\n",
                    },
                    {"type": "image", "image_url": file.replace(".pdf", ".png")},
                ],
            }
        ]
        return conversation

    @classmethod
    def from_config(cls, llm_model, config):
        init_prompt_path = config.get("prompt_path", None)
        return cls(llm_model, init_prompt_path)
