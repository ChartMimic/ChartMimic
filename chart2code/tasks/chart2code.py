import os
from llm import load_llm
from agents import load_agent
from data.data_utils import Chart2CodeDataset
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


@registry.register_task("chart2code")
class Chart2Code(BaseTask):
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
            "{}_{}_{}_results.json".format(
                self.run_config["name"],
                (
                    self.llm_config["engine"]
                    if "/" not in self.llm_config["engine"]
                    else self.llm_config["engine"].split("/")[-1]
                ),
                self.agent_config["name"],
            ),
        )

    def _load_dataset(self, dataset_name, dataset_dir, direct_dir=None):
        if dataset_name == "chart2code":
            dataset = Chart2CodeDataset(dataset_dir=dataset_dir, direct_dir=direct_dir)
        else:
            raise NotImplementedError("Dataset {} not implemented".format(dataset_name))
        return dataset

    def run(
        self,
    ):
        self.dataset = self._load_dataset(
            self.run_config["name"],
            self.run_config["dataset_dir"],
            self.run_config.get("direct_dir", None),
        )
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
        llm = load_llm(self.llm_config["name"], self.llm_config)
        agent = load_agent(self.agent_config["name"], self.agent_config, llm)
        for i in tqdm(range(len(sub_index)), disable=rank != 0):
            response = agent.run(self.dataset[sub_index[i]]["file"])
            with open(self.results_file + str(rank), "a", encoding="utf-8") as f:
                json_str = json.dumps(
                    {"file": self.dataset[sub_index[i]]["file"], "response": response}
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
