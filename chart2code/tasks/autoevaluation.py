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
import clip
import torch
from torchvision.transforms import Compose, Resize, CenterCrop, ToTensor, Normalize
from PIL import Image

logger = AgentLogger(__name__)


@registry.register_task("autoevaluation")
class AutoEvaluation(BaseTask):
    def __init__(
        self,
        run_config=None,
        llm_config=None,
        agent_config=None,
    ):

        self.run_config = run_config
        self.agent_config = agent_config
        self.llm_config = llm_config
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
        if dataset_name == "autoevaluation":
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

        # Only use one process
        # processes = []
        # for rank in range(self.run_config["num_processes"]):
        #     p = Process(target=self._muti_process_run, args=(rank,))
        #     p.start()
        #     processes.append(p)
        # for p in processes:
        #     p.join()
        # Debug use
        # import pdb

        # pdb.set_trace()
        for rank in range(self.run_config["num_processes"]):
            self._muti_process_run(rank=rank)
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
        os.environ["CUDA_VISIBLE_DEVICES"] = str(rank)
        device = "cuda" if torch.cuda.is_available() else "cpu"
        model, preprocess = clip.load("ViT-B/32", device=device)
        for i in tqdm(range(len(sub_index)), disable=rank != 0):
            originial_png_file = self.dataset[sub_index[i]]["file"].replace(
                ".pdf", ".png"
            )
            generated_png_file = originial_png_file.replace(
                self.run_config["original_dataset_dir"],
                self.run_config["generated_dataset_dir"],
            )

            response = self._calculate_clip_similarity(
                model, originial_png_file, generated_png_file, device
            )
            with open(self.results_file + str(rank), "a", encoding="utf-8") as f:
                json_str = json.dumps(
                    {
                        "orginial": self.dataset[sub_index[i]]["file"],
                        "generated": generated_png_file,
                        "response": response,
                    }
                )
                f.write(json_str + "\n")

    def _calculate_clip_similarity(self, model, image_path1, image_path2, device):
        image_transform = Compose(
            [
                Resize(256, interpolation=Image.BICUBIC),
                CenterCrop(224),
                ToTensor(),
                Normalize(
                    (0.48145466, 0.4578275, 0.40821073),
                    (0.26862954, 0.26130258, 0.27577711),
                ),
            ]
        )

        # Load and preprocess images
        image1 = Image.open(image_path1).convert("RGB")
        image2 = Image.open(image_path2).convert("RGB")
        image1 = image_transform(image1).unsqueeze(0).to(device)
        image2 = image_transform(image2).unsqueeze(0).to(device)

        # Calculate features
        with torch.no_grad():
            image_features1 = model.encode_image(image1)
            image_features2 = model.encode_image(image2)

        # Normalize features
        image_features1 /= image_features1.norm(dim=-1, keepdim=True)
        image_features2 /= image_features2.norm(dim=-1, keepdim=True)

        # Calculate cosine similarity
        similarity = (image_features1 @ image_features2.T).item()

        return similarity

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
