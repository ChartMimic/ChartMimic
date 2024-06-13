import argparse
import os
import re
from dotenv import load_dotenv

load_dotenv()


def match_function(line):
    """
    Match pattern like ax.bar(ind, notre_dame, width, color='#495c80')
    """
    pattern = r".*\..*\(.*"
    return re.match(pattern, line)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_dir", type=str, default=f"{os.environ['PROJECT_PATH']}/dataset/ori")
    parser.add_argument("--output_file", type=str, default=f"{os.environ['PROJECT_PATH']}/trash/extracted_functions.txt")

    args = parser.parse_args()

    input_dir = args.input_dir
    output_file = args.output_file

    filter_functions = [
                        "set_xlabel", "set_ylabel", "set_xticks", "set_yticks", "set_xticklabels", \
                        "set_yticklabels", "set_xscale", "set_yscale", "legend", "subplots", "tight_layout", \
                        "savefig", "xticks", "yticks", "xlabel", "ylabel", "set_ylim", "set_xlim", "set_title", \
                        "np.arange", "random.seed", "xlim", "ylim", "set_visible", "gca", "invert_yaxis", "get_cmap", \
                        "suptitle", "grid", "np.zeros", "np.array", "tick_params", "set_edgecolor", "set_axisbelow", \
                        "figure", "title", "add_subplot", "GridSpec", "get_x", "get_y", "get_height", "get_width", \
                        "to_rgba", "set_facecolor", "get_legend_handles_labels", "set_hatch", "values", "items", \
                        "np.ones", "np.add", "keys", "cumsum", "set_major_formatter", "set_size_inches", "subplot", \
                        "set_color", "random.uniform", "random.randint", "hls_to_rgb", "random.rand", "np.linspace", \
                        "twinx", "subplots_adjust", "set_size", "set_minor_locator", "set_major_locator", "set_label", \
                        "random.choice", "text", "index", "np.sin", "np.cos", "np.clip", "get_label", "flatten", "setp", \
                        "viridis", "random.exponential", "np.exp", "np.full_like", "random.normal", "from_list", "add_artist", \
                        "random.randn", "np.where", "np.poly1d", "set_position", "xscale", "np.diff", "set_linewidth", \
                        "np.zeros_like", ".split", ".append", ".get_xydata", "np.min", ".add_patch", ".set", "np.argmax", \
                        ".min", ".max", "np.argmin", ".get_ydata", "random.beta", "np.mean", "np.std", "np.median", "np.percentile", \
                        "set_alpha", "np.histogram", "yscale", "np.concatenate", "np.random.gamma", "np.sqrt", ".ravel(", "set_zlabel", \
                        "set_zticks", "set_zticklabels", "set_zscale", "set_zlim", "set_ylim3d", "set_xlim3d", "set_xlim3d", "np.ones_like", \
                        "set_box_aspect", "vectorize", "linalg.lstsq", "set_zlim3d", ".axis", "np.random.poisson", ".set_ticks_position", "get_position", "set_aspect"
                        ]

    with open(output_file, "w") as f:
        for file in os.listdir(input_dir):
            if file.endswith(".py") and "HR" in file:
                with open(os.path.join(input_dir, file), "r") as f2:
                    f.write(f"<<<<<<<<<<<<<<<< File: {os.path.join(input_dir, file)} >>>>>>>>>>>>>>>>>>>>>>\n")
                    for line in f2:
                        # filtered = False
                        # replace text between "np."" and "(" with ""
                        orig_line = line
                        line = re.sub(r"np\..*\(", "", line)

                        for function in filter_functions:
                            if function+"(" in line:
                                # remove the function from the line string
                                line = line.replace("." + function + "(", "")
                                # filtered = True
                                # break
                        if match_function(line):
                            f.write(orig_line)
                            f.write("\n")