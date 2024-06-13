from .direct_agent import DirectAgent
from .hintenhanced_agent import HintEnhancedAgent
from .gpt4evaluation_agent import GPT4EvaluationAgent
from .selfrevision_agent import SelfRevisionAgent
from .scaffold_agent import ScaffoldAgent
from .edit_agent import EditAgent
from common.registry import registry

__all__ = [
    "DirectAgent",
    "HintEnhancedAgent",
    "SelfRevisionAgent",
    "ScaffoldAgent",
    "GPT4EvaluationAgent",
    "EditAgent",
]


def load_agent(name, config, llm_model):
    agent = registry.get_agent_class(name).from_config(llm_model, config)
    return agent
