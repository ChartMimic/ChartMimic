from .openai import OPENAI_GPT
from .gemini import GEMINI
from .deepseekvl import DeepSeekVL
from .qwenvl import QwenVL
from .internvl import InternVL
from .idefics2 import Idefics2
from .llava import Llava
from .cogvlm2 import Cogvlm2
from .phi3 import Phi3
from .minicpm import Minicpm
from .claude import Claude
from common.registry import registry

__all__ = [
    "OPENAI_GPT",
    "GEMINI",
    "DeepSeekVL",
    "QwenVL",
    "InternVL",
    "Idefics2",
    "Llava",
    "Cogvlm2",
    "Phi3",
    "Minicpm",
    "Claude",
]


def load_llm(name, config):
    llm = registry.get_llm_class(name).from_config(config)
    return llm
