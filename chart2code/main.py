import sys
import os
import re
import wandb
import warnings
import yaml
import json
import time
import argparse
from dotenv import load_dotenv
from tasks import load_task


TASKS = [
    "chart2code",
    "gpt4evaluation",
    "code4evaluation",
    "autoevaluation",
    "chartedit",
]


def parse_args():
    parser = argparse.ArgumentParser(description="Testing")

    parser.add_argument("--cfg_path", required=True, help="path to configuration file.")
    parser.add_argument(
        "--tasks", required=True, type=str, nargs="+", help="specify the tasks"
    )
    parser.add_argument(
        "--model", default="gpt-4-vision-preview", type=str, help="specify the model"
    )
    parser.add_argument(
        "--evaluation_dir", type=str, help="specify the evaluation file"
    )
    args = parser.parse_args()

    return args


def path_constructor(loader, node):
    path_matcher = re.compile(r"\$\{([^}^{]+)\}")
    """ Extract the matched value, expand env variable, and replace the match """
    value = node.value
    match = path_matcher.match(value)
    env_var = match.group()[2:-1]
    return os.environ.get(env_var) + value[match.end() :]


def load_config(cfg_path, args):
    path_matcher = re.compile(r"\$\{([^}^{]+)\}")
    yaml.add_implicit_resolver("!path", path_matcher)
    yaml.add_constructor("!path", path_constructor)
    with open(cfg_path, "r") as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    llm_config = config["llm"]
    agent_config = config["agent"]
    run_config = config["run"]
    return llm_config, agent_config, run_config


def check_log_paths_are_ready(log_dir, baseline_dir):

    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    if not os.path.exists(os.path.join(log_dir, "logs")):
        os.makedirs(os.path.join(log_dir, "logs"))

    if not os.path.exists(baseline_dir):
        os.makedirs(baseline_dir)

    if not os.path.exists(os.path.join(log_dir, "all_results.txt")):
        with open(os.path.join(log_dir, "all_results.txt"), "w") as f:
            f.write("")
            f.close()

    return True


def main():
    load_dotenv(
        override=True
    )  # take environment variables from .env., load openai api key, project path...

    args = parse_args()
    llm_config, agent_config, run_config = load_config(args.cfg_path, args)
    llm_config = llm_config[args.model]
    llm_config["model"] = args.model

    # ------------------------------------------------- start evaluation -------------------------------------------
    s = time.time()
    for task_name in args.tasks:
        if task_name == "gpt4evaluation" or task_name == "autoevaluation":
            run_config[task_name]["generated_dataset_dir"] = args.evaluation_dir
        if task_name not in TASKS:
            raise ValueError(f"Task {task_name} is not supported")
        task = load_task(task_name, run_config[task_name], llm_config, agent_config)

        task.run()
    print("Time taken: ", time.time() - s)


if __name__ == "__main__":
    main()
