from .chart2code import Chart2Code
from .gpt4evaluation import GPT4Evaluation
from .code4evaluation import Code4Evaluation
from .chartedit import ChartEdit
from common.registry import registry

__all__ = [
    "Chart2Code",
    "GPT4Evaluation",
    "Code4Evaluation",
    "ChartEdit",
]


def load_task(name, run_config, llm_config, agent_config):
    task = registry.get_task_class(name).from_config(
        run_config, llm_config, agent_config
    )

    return task
