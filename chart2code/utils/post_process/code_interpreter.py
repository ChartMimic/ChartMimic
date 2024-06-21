import re
import pandas as pd
import json
import os
from tqdm import tqdm
from argparse import ArgumentParser
from dotenv import load_dotenv
import json
from multiprocessing import Process

load_dotenv()


def extract_code(text):
    """Extract code from markdown text."""
    code = re.findall(r"```python(.*?)```", text, re.DOTALL)
    if len(code) == 0:
        code = ["import matplotlib.pyplot as plt"]
    return code

def get_variable_code(file):
    edit_ori_file = "{}/dataset/customized_500/".format(os.environ["PROJECT_PATH"]) + file
    with open(edit_ori_file, "r") as f:
        code = f.read()
        pattern = re.compile(r"# ===================\n# Part 2: Data Preparation\n# ===================\n(.*?)# ===================\n# Part 3: Plot Configuration and Rendering\n# ===================", re.DOTALL)
        match = pattern.search(code)

        if match:
            extracted_text = match.group(1)
            extracted_text = extracted_text.strip() 
            extracted_text = "#Variable Code Block\nimport warnings;warnings.filterwarnings('ignore', category=UserWarning);warnings.filterwarnings('ignore', category=FutureWarning);import matplotlib.pyplot as plt;import pandas as pd;import numpy as np;np.random.seed(0);import math;from matplotlib_venn import venn2;from matplotlib import cm;from scipy.stats import gaussian_kde;import networkx as nx;from matplotlib.gridspec import GridSpec;from scipy.stats import multivariate_normal;import colorsys;import matplotlib.colors as mcolors;from matplotlib.colors import LogNorm;from scipy.stats import norm;import matplotlib.gridspec as gridspec;import seaborn as sns\n" + extracted_text
        else:
            print(edit_ori_file)
            raise ValueError("No match found")
    return extracted_text

def _muti_process_run(rank, data):
    sub_index = [_ for _ in range(len(data))][
        rank :: 10
    ]
    # print("sub_index:", sub_index)
    # print("len:", len(sub_index))
    for i in tqdm(sub_index, disable=rank != 0):
        output_file = os.path.basename(data["file"][i]).replace(".pdf", ".py")
        output_file = output_dir + "/" + output_file
        # print("Get Output File", output_file)

        if "gpt" in input_file:
            try:
                code = json.loads(data["response"][i])["choices"][0]["message"]["content"]
            except Exception as e:
                code = ""
        elif "claude" in input_file:
            try:
                code = data["response"][i]["choices"][0]["message"]["content"]
            except Exception as e:
                code = ""
        else:
            code = data["response"][i] if data["response"][i] else ""
        
        if "idefics2" in input_file:
            if "```python" in code:
                code = extract_code(code)[0].replace("\n", "\n    ")
            else:
                code = code.split("Assistant: ")[1].replace("\n", "\n    ")
        else:
            code = extract_code(code)[0].replace("\n", "\n    ")
        if "chartedit" in output_file.lower():
            variable_code = get_variable_code( os.path.basename(output_file) )
            variable_code = variable_code.replace("\n", "\n    ")
            code = variable_code + "\n    " + code
        code = re.sub(r"plt\.savefig\(.*\n*", "", code, flags=re.S)
        code = re.sub(r"plt.show\(.*\n*", "", code, flags=re.S)
        code = (
            "try:\n    "
            + code.strip()
            + '\nexcept Exception as e:\n    pass\nplt.savefig("{}")'.format(
                output_file.replace(".py", f".pdf")
            )
        )

            # + '\nexcept Exception as e:\n    print(">>> Generated Code Runtime Error:", e)\nplt.savefig("{}")'.format(
        with open(output_file, "w") as f:
            f.write(code)

        # print("Execute File", output_file)
        if "llava-v1.6-mistral-7b-hf_EditAgent_results/edit/HR_11.py" not in output_file and "llava-v1.6-vicuna-13b-hf_EditAgent_results/edit/3d_4.py" not in output_file:
            os.system("python3 " + output_file)

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        "--input_file", type=str, default=""
    )
    parser.add_argument(
        "--template_type", type=str, default="direct"
    )
    args = parser.parse_args()
    input_file = args.input_file
    template_type = args.template_type
    print("input_file", input_file)

    data = pd.read_json(args.input_file, lines=True)

    output_dir = input_file.replace(".json", "") + "/" + template_type
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)


    processes = []
    num_processes = 20
    for rank in range(num_processes):
        # print("rank", rank)
        p = Process(target=_muti_process_run, args=(rank, data))
        p.start()
        processes.append(p)
    for p in processes:
        p.join()