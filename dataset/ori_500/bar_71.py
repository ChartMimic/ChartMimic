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
categories = ["coreutils", "gzip", "scp", "libq.", "mcf", "omnet.", "perl."]
# Generate three lists
RegOpt, BIOpt, LoopOpt = np.random.dirichlet(np.ones(3), size=len(categories)).T

RegOpt = RegOpt * 100
BIOpt = BIOpt * 100
LoopOpt = LoopOpt * 100

labels = ["RegOpt", "BIOpt", "LoopOpt"]
yticks = np.arange(0, 101, 20)
ylim = [0, 100]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Stacked bar chart setup
bar_width = 0.9
r = np.arange(len(categories))

# Plot
fig, ax = plt.subplots(figsize=(8, 4))
bar1 = ax.bar(
    r,
    RegOpt,
    color="#7e9671",
    edgecolor="white",
    hatch="++",
    width=bar_width,
    label=labels[0],
)
bar2 = ax.bar(
    r,
    BIOpt,
    bottom=RegOpt,
    color="#d3c475",
    edgecolor="white",
    hatch="--",
    width=bar_width,
    label=labels[1],
)
bar3 = ax.bar(
    r,
    LoopOpt,
    bottom=RegOpt + BIOpt,
    color="#4e78bf",
    edgecolor="white",
    hatch="\\\\\\",
    width=bar_width,
    label=labels[2],
)

ax.set_xticks(r)
ax.set_xticklabels(categories, rotation=-90, ha="center")
ax.set_yticks(yticks)
ax.set_ylim(ylim)
ax.set_yticklabels(["{}%".format(i) for i in range(0, 101, 20)])
ax.legend(loc="upper center", bbox_to_anchor=(0.5, 1.15), ncol=3)

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["bottom"].set_visible(False)
# Grid lines
ax.yaxis.grid(True, linestyle="--", color="gray")

# ===================
# Part 4: Saving Output
# ===================
# Show plot
plt.tight_layout()
plt.savefig("bar_71.pdf", bbox_inches="tight")
