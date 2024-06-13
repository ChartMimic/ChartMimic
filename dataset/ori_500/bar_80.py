# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Example data
groups = ["3", "5", "7", "10"]
llama_default = [-1, -1.5, -2, -2.5]
llama_hag = [0.5, -0.5, 1, -1.5]
vicuna_default = [-0.5, -1, -1.5, -2]
vicuna_hag = [0.5, 0, 1, -1]

# Reduce the number of negative bars to two per group,
# for the sake of the example, I'll keep the first and third bar negative and make the rest positive.
llama_default = [1, 1.5, -2, 2.5]
llama_hag = [0.5, 0.5, -1, 1.5]
vicuna_default = [0.5, 1, -1.5, 2]
vicuna_hag = [0.5, 1, 1, -1]

n_groups = len(groups)

labels = ["LLAMA-Default", "LLAMA-HAG", "Vicuna-Default", "Vicuna-HAG"]
xlabel = "Num of Constraint Words"
ylabel = "Score"
title = "Taboo"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create the plot
fig, ax = plt.subplots(figsize=(10, 5))

index = np.arange(n_groups)
bar_width = 0.2

opacity = 0.8

rects1 = ax.bar(
    index - 1.5 * bar_width,
    llama_default,
    bar_width,
    alpha=opacity,
    color="#8ECFC9",
    label=labels[0],
)

rects2 = ax.bar(
    index - 0.5 * bar_width,
    llama_hag,
    bar_width,
    alpha=opacity,
    color="#FFBE7A",
    label=labels[1],
)

rects3 = ax.bar(
    index + 0.5 * bar_width,
    vicuna_default,
    bar_width,
    alpha=opacity,
    color="#82B0D2",
    label=labels[2],
)

rects4 = ax.bar(
    index + 1.5 * bar_width,
    vicuna_hag,
    bar_width,
    alpha=opacity,
    color="#E7DAD2",
    hatch="+",
    label=labels[3],
)


ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)
ax.set_title(title)
ax.set_xticks(index)
ax.set_xticklabels(groups)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.yaxis.grid(True, linestyle="--")
plt.legend()

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig("bar_80.pdf", bbox_inches="tight")
