import os
from llm import load_llm
from agents import load_agent
from data.data_utils import Chart2CodeDataset, GPT4EvaluationDataset, Code4EvaluationDataset
from tasks.base_task import BaseTask
from common.registry import registry
from utils.logging.logger import TaskLogger
from utils.logging.agent_logger import AgentLogger
import time
from multiprocessing import Process
from tqdm import tqdm
import json
import pandas as pd

from utils.evaluator.text_evaluator import TextEvaluator
from utils.evaluator.chart_type_evaluator import ChartTypeEvaluator
from utils.evaluator.legend_evaluator import LegendEvaluator
from utils.evaluator.grid_evaluator import GridEvaluator
from utils.evaluator.color_evaluator import ColorEvaluator
from utils.evaluator.layout_evaluator import LayoutEvaluator

logger = AgentLogger(__name__)


@registry.register_task("code4evaluation")
class Code4Evaluation(BaseTask):
    def __init__(
        self,
        run_config=None,
        llm_config=None,
        agent_config=None,
    ):

        self.run_config = run_config
        self.agent_config = agent_config
        self.llm_config = llm_config
        self.results_file = self.run_config["generated_dataset_dir"] + "_code4evaluation.json"
        print(self.results_file)
        # self.results_file = os.path.join(
            # self.run_config["result_dir"],
            # "{}_{}_{}_results.json".format(
                # self.run_config["name"],
                # self.llm_config["name"],
                # self.run_config["template_type"],
            # ),
        # )

    def _load_dataset(
        self, dataset_name, original_dataset_dir, generated_dataset_dir, template_type
    ):
        if dataset_name == "code4evaluation":
            dataset = Code4EvaluationDataset(
                original_dataset_dir=original_dataset_dir,
                generated_dataset_dir=generated_dataset_dir,
                template_type=template_type,
            )
        else:
            raise NotImplementedError("Dataset {} not implemented".format(dataset_name))
        return dataset

    def run(
        self,
    ):
        self.dataset = self._load_dataset(
            self.run_config["name"],
            self.run_config["original_dataset_dir"],
            self.run_config["generated_dataset_dir"],
            self.run_config["template_type"],
        )
        print("Length of dataset: ", len(self.dataset))
        processes = []
        for rank in range(self.run_config["num_processes"]):
            p = Process(target=self._muti_process_run, args=(rank,))
            p.start()
            processes.append(p)
        for p in processes:
            p.join()

        # Debug use
        # for rank in range(self.run_config["num_processes"]):
            # self._muti_process_run(rank)

        total = pd.DataFrame()
        for rank in range(self.run_config["num_processes"]):
            total = pd.concat(
                [total, pd.read_json(self.results_file + str(rank), lines=True)]
            )
            os.system("rm " + self.results_file + str(rank))
        total.to_json(self.results_file, orient="records", lines=True)

    def _muti_process_run(self, rank):
        sub_index = [_ for _ in range(len(self.dataset))][
            rank :: self.run_config["num_processes"]
        ]
        text_evaluator = TextEvaluator(use_position=False, use_axs=False)
        chart_type_evaluator = ChartTypeEvaluator()
        legend_evaluator = LegendEvaluator(use_position=True)
        grid_evaluator = GridEvaluator()
        color_evaluator = ColorEvaluator()
        layout_evaluator = LayoutEvaluator()

        for i in tqdm(range(len(sub_index)), disable=rank != 0):
            original_py_file = self.dataset[sub_index[i]]["file"]
            generated_py_file = original_py_file.replace(
                self.run_config["original_dataset_dir"],
                self.run_config["generated_dataset_dir"]
                + "/"
                + self.run_config["template_type"],
            )

            text_evaluator(
                generation_code_file=generated_py_file,
                golden_code_file=original_py_file
                )

            chart_type_evaluator(
                generation_code_file=generated_py_file,
                golden_code_file=original_py_file
            )

            color_evaluator(
                generation_code_file=generated_py_file,
                golden_code_file=original_py_file
            )

            layout_evaluator(
                generation_code_file=generated_py_file,
                golden_code_file=original_py_file
            )

            with open(self.results_file + str(rank), "a", encoding="utf-8") as f:
                json_str = json.dumps(
                    {
                        "orginial": self.dataset[sub_index[i]]["file"],
                        "generated": generated_py_file,
                        "text_metrics": text_evaluator.metrics,
                        "chart_type_metrics": chart_type_evaluator.metrics,
                        "layout_metrics": layout_evaluator.metrics,
                        "color_metrics": color_evaluator.metrics
                    }
                )
                f.write(json_str + "\n")

    @classmethod
    def from_config(
        cls,
        run_config,
        llm_config,
        agent_config,
    ):
        llm_config["name"] = llm_config.get("name", "gpt")
        agent_config["name"] = agent_config.get("name", "vanilla")
        if "EditAgent" in agent_config["name"]:
            run_config["generated_dataset_dir"] = run_config.get("generated_dataset_dir") + f"/chartedit_{llm_config['model']}_{agent_config['name']}_results"
        else:
            run_config["generated_dataset_dir"] = run_config.get("generated_dataset_dir") + f"/chart2code_{llm_config['model']}_{agent_config['name']}_results"

        return cls(
            run_config=run_config,
            llm_config=llm_config,
            agent_config=agent_config,
        )