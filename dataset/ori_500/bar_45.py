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
constraint_words = [3, 5, 7, 10]
LLAMA_Default = [-1, -1.5, -2, -3]
LLAMA_HAG = [-0.5, -1, -1.5, -2.5]
Vicuna_Default = [-1.5, -2, -2.5, -3.5]
Vicuna_HAG = [-1, -1.5, -2, -3]

# X-axis positions for each group
x = np.arange(len(constraint_words))

# Bar width
bar_width = 0.2

# Labels and Titles
ylabel = "Score"
xlabel = "Num of Constraint Words"
title = "Taboo"

# Legend labels
legend_labels = ["LLAMA-Default", "LLAMA-HAG", "Vicuna-Default", "Vicuna-HAG"]

# Colors
colors = ["#f1c5c1", "#dc7870", "#b9d0e5", "#8ab1d2"]

# Axis limits
ylim = (-3.5, 0)

# Axis tick labels
xticks = x
xticklabels = constraint_words

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Figure and axis
fig, ax = plt.subplots(figsize=(10, 7))

# Plotting bars
ax.bar(
    x - bar_width * 1.5,
    LLAMA_Default,
    width=bar_width,
    label=legend_labels[0],
    color=colors[0],
)
ax.bar(
    x - bar_width / 2,
    LLAMA_HAG,
    width=bar_width,
    label=legend_labels[1],
    color=colors[1],
)
ax.bar(
    x + bar_width / 2,
    Vicuna_Default,
    width=bar_width,
    label=legend_labels[2],
    color=colors[2],
)
ax.bar(
    x + bar_width * 1.5,
    Vicuna_HAG,
    width=bar_width,
    label=legend_labels[3],
    color=colors[3],
)

# Adding labels and title
ax.set_ylim(ylim)
ax.set_ylabel(ylabel)
ax.set_xlabel(xlabel)
ax.set_title(title)

# Adding x-axis tick labels
ax.set_xticks(xticks)
ax.set_xticklabels(xticklabels)

plt.tick_params(axis="both", which="both", length=0)

# Adding legend
ax.legend(loc="lower center", bbox_to_anchor=(0.5, -0.15), frameon=False, ncol=4)

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig("bar_45.pdf", bbox_inches="tight")
