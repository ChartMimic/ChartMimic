# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data
categories = [
    "coreutils",
    "gzip",
    "scp",
    "tar",
    "exim",
    "memc.",
    "nginx",
    "astar",
    "bzip2",
    "gcc",
    "gobmk",
    "h264.",
    "hmmer",
    "libq.",
    "mcf",
    "omnet.",
    "perl.",
    "sjeng",
    "xalan",
    "PHP",
    "MySQL",
    "Avg",
]
# Generate three lists
RegOpt, BIOpt, LoopOpt = np.random.dirichlet(np.ones(3), size=len(categories)).T

RegOpt = RegOpt * 100
BIOpt = BIOpt * 100
LoopOpt = LoopOpt * 100
# Stacked bar chart setup
bar_width = 0.9
r = np.arange(len(categories))
labels = ["RegOpt", "BIOpt", "LoopOpt"]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plot
fig, ax = plt.subplots(figsize=(8, 4))
bar1 = ax.bar(
    r,
    RegOpt,
    color="white",
    edgecolor="#4f7c56",
    hatch="\\\\\\",
    width=bar_width,
    label=labels[0],
)
bar2 = ax.bar(
    r,
    BIOpt,
    bottom=RegOpt,
    color="white",
    edgecolor="#d3c475",
    hatch="--",
    width=bar_width,
    label=labels[1],
)
bar3 = ax.bar(
    r,
    LoopOpt,
    bottom=RegOpt + BIOpt,
    color="white",
    edgecolor="#2d4aac",
    hatch="++",
    width=bar_width,
    label=labels[2],
)

# Labels, title and legend
# ax.set_xlabel('Benchmarks', fontsize=12)
# ax.set_ylabel('Optimization (%)', fontsize=12)

ax.set_xticks(r)
ax.set_xticklabels(categories, rotation=-45, ha="center")
ax.set_yticks(np.arange(0, 101, 20))
ax.set_ylim(0, 100)
ax.set_yticklabels(["{}%".format(i) for i in range(0, 101, 20)])
ax.legend(loc="upper center", bbox_to_anchor=(0.5, 1.15), ncol=3)

# Grid lines
ax.yaxis.grid(True, linestyle="--")

# ===================
# Part 4: Saving Output
# ===================
# Show plot
plt.tight_layout()
plt.savefig("bar_34.pdf", bbox_inches="tight")
