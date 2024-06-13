from agents.base_agent import BaseAgent
from common.registry import registry
import json
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

@registry.register_agent("SelfRevisionAgent")
class SelfRevisionAgent(BaseAgent):
    def __init__(
        self,
        llm_model,
        prompt_path=None,
    ):
        super().__init__()
        self.llm_model = llm_model
        self.dimensions_info = pd.read_json(
            f"{os.environ['PROJECT_PATH']}/dimentions_info.jsonl",
            lines=True,
        )
        if prompt_path is not None:  # load from file
            self.init_prompt_dict = json.load(open(prompt_path, "r"))
            self.instruction = self.init_prompt_dict["instruction"]
        else:
            raise Exception("init_prompt_path is None")

    def run(self, file):
        width, height = self._get_pdf_dimensions(file)
        code = self._get_direct_code(file)
        conversation = self._constract_conversation_two_figs(file, width, height, code)
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
        return width, height

    def _get_direct_code(self, pdf_path):
        file_idx = "{}_{}".format(
            pdf_path.split("/")[-1].split("_")[0],
            pdf_path.split("/")[-1].split("_")[1],
        ).replace(".pdf", "")
        direct_code = self.dimensions_info[self.dimensions_info["idx"] == file_idx][
            "code"
        ].values[0]
        return direct_code

    def _constract_conversation(self, file, width, height, code):
        conversation = [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": self.instruction.format(
                            height=height,
                            width=width,
                            python_function=code,
                        ),
                    },
                    {"type": "image", "image_url": file.replace(".pdf", ".png")},
                ],
            }
        ]
        return conversation

    def _constract_conversation_two_figs(self, file, width, height, code):
        conversation = [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "You are an expert Python developer who specializes in writing matplotlib code based on a given picture.\n\nHere is the reference picture:\n",
                    },
                    {"type": "image", "image_url": file.replace(".pdf", ".png")},
                    {
                        "type": "text",
                        "text": "\nNow, I have the Python matplotlib code for implementing the reference picture as follows:\n```python\n{python_function}\n```\n\nThe rendered picture of the code is:\n".format(python_function=code),
                    },
                    {"type": "image", "image_url": file.replace(".pdf", ".png").replace("dataset/ori", "results/gpt_Direct")},
                    {
                        "type": "text",
                        "text": """\nNow, please compare whether the renderer picture is the same as the reference picture. The difference may cover, but not be limited to, the following aspects:
1. Chart Types: Does the AI-generated image include all chart types present in the reference image (e.g., line charts, bar charts, etc.)?
2. Layout: Does the arrangement of subplots in the AI-generated image match the reference image (e.g., number of rows and columns)?
3. Text Content: Does the AI-generated image include all text from the reference image (e.g., titles, annotations, axis labels), excluding axis tick labels?
4. Data: How accurately do the data trends in the AI-generated image resemble those in the original image and is the number of data groups the same as in the reference image?
5. Style: Does the AI-generated image match the original in terms of colors (line colors, fill colors, etc.), marker types (point shapes, line styles, etc.), legends, grids, and other stylistic details?
6. Clarity: Is the AI-generated image clear and free of overlapping elements?

- If the generated picture matches the reference, please output the original implementation code.
- If there are discrepancies, first list the specific differences between the two pictures. Then, modify the existing code to address these differences, ensuring the revised code is capable of reproducing the reference picture. Finally, output the revised code which can be run directly.

Note that it is necessary to use figsize=({width}, {height}) to set the image size to match the original size.
""".format(width=width, height=height),
                    }
                ],
            }
        ]
        return conversation
    
    @classmethod
    def from_config(cls, llm_model, config):
        init_prompt_path = config.get("prompt_path", None)
        return cls(llm_model, init_prompt_path)
