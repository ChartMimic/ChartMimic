import os
from llm import load_llm
from agents import load_agent
from data.data_utils import Chart2CodeDataset, GPT4EvaluationDataset
from tasks.base_task import BaseTask
from common.registry import registry
from utils.logging.logger import TaskLogger
from utils.logging.agent_logger import AgentLogger
import time
from multiprocessing import Process
from tqdm import tqdm
import json
import pandas as pd

logger = AgentLogger(__name__)


@registry.register_task("gpt4evaluation")
class GPT4Evaluation(BaseTask):
    def __init__(
        self,
        run_config=None,
        llm_config=None,
        agent_config=None,
    ):

        self.run_config = run_config
        self.agent_config = agent_config
        self.llm_config = llm_config

        os.makedirs(self.run_config["result_dir"], exist_ok=True)
        self.results_file = os.path.join(
            self.run_config["result_dir"],
            "{}_{}_{}_{}_results.json".format(
                self.run_config["name"],
                self.llm_config["engine"],
                self.agent_config["name"],
                self.run_config["generated_dataset_dir"].split("/")[-1],
            ),
        )

    def _load_dataset(self, dataset_name, original_dataset_dir, generated_dataset_dir):
        if dataset_name == "gpt4evaluation":
            dataset = GPT4EvaluationDataset(
                original_dataset_dir=original_dataset_dir,
                generated_dataset_dir=generated_dataset_dir,
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
        )
        # import pdb

        # pdb.set_trace()
        if os.path.exists(self.results_file):
            data = pd.read_json(self.results_file, lines=True)
            raw = []
            for _ in self.dataset.raw_data:
                if _ in list(data["orginial"]):
                    continue
                raw.append(_)
            self.dataset.raw_data = raw
        processes = []
        for rank in range(self.run_config["num_processes"]):
            p = Process(target=self._muti_process_run, args=(rank,))
            p.start()
            processes.append(p)
        for p in processes:
            p.join()
        # Debug use
        # import pdb

        # pdb.set_trace()
        # for rank in range(self.run_config["num_processes"]):
        #     self._muti_process_run(rank=rank)
        total = pd.DataFrame()
        for rank in range(min(len(self.dataset), self.run_config["num_processes"])):
            total = pd.concat(
                [total, pd.read_json(self.results_file + str(rank), lines=True)]
            )
            os.system("rm " + self.results_file + str(rank))
        if os.path.exists(self.results_file):
            data = pd.read_json(self.results_file, lines=True)
            total = pd.concat([total, data])
        total.to_json(self.results_file, orient="records", lines=True)

    def _muti_process_run(self, rank):
        sub_index = [_ for _ in range(len(self.dataset))][
            rank :: self.run_config["num_processes"]
        ]
        llm = load_llm(self.llm_config["name"], self.llm_config)
        agent = load_agent(self.agent_config["name"], self.agent_config, llm)
        for i in tqdm(range(len(sub_index)), disable=rank != 0):
            originial_png_file = self.dataset[sub_index[i]]["file"].replace(
                ".pdf", ".png"
            )
            generated_png_file = originial_png_file.replace(
                self.run_config["original_dataset_dir"],
                self.run_config["generated_dataset_dir"],
            )
            response = agent.run(originial_png_file, generated_png_file)
            with open(self.results_file + str(rank), "a", encoding="utf-8") as f:
                json_str = json.dumps(
                    {
                        "orginial": self.dataset[sub_index[i]]["file"],
                        "generated": generated_png_file,
                        "response": response,
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

        return cls(
            run_config=run_config,
            llm_config=llm_config,
            agent_config=agent_config,
        )
