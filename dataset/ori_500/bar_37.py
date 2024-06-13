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
models = ["ResNet18", "AlexNet", "ResNet50"]
speedup = {
    "0%": [1.0, 1.0, 1.0],
    "50%": [1.8, 1.9, 1.6],
    "4:8": [2.6, 2.9, 1.8],
    "75%": [3.3, 3.4, 2.7],
    "6:8": [4.6, 5.2, 2.9],
    "87.50%": [4.5, 6.1, 3.9],
    "7:8": [7.4, 8.7, 4.3],
}

# Colors for the bars
colors = ["#de9aa4", "#bc9c58", "#8ea654", "#65ab91", "#67a9b6", "#a3ade5", "#da8fdc"]

# Plot labels and types
ylabel_text = "Speedup"
xlabel_text = "Models"
title_text = "Model Speedup Comparison"
legend_title = "Perturbation"
bar_label_fontsize = 10
ylabel_fontsize = 12

# Plot limits and ticks
ylim_values = (0, 10)
yticks_values = [0, 2, 4, 6, 8, 10]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Setup the figure and axes
fig, ax = plt.subplots(figsize=(12, 4))

# Bar width
bar_width = 0.1

# Positions of the bars on the x-axis
r = np.arange(len(models))

# Create bars for each perturbation
for i, (perturbation, values) in enumerate(speedup.items()):
    ax.bar(
        r + i * bar_width,
        values,
        color=colors[i],
        width=bar_width,
        edgecolor="white",
        label=perturbation,
    )

# Add labels on top of the bars
for i, (perturbation, values) in enumerate(speedup.items()):
    for j, value in enumerate(values):
        ax.text(
            j + i * bar_width,
            value + 0.1,
            str(value),
            ha="center",
            va="bottom",
            fontsize=bar_label_fontsize,
        )

# General layout
ax.set_ylabel(ylabel_text, fontsize=ylabel_fontsize)
ax.set_xticks(r + bar_width * (len(speedup) - 1) / 2)
ax.set_xticklabels(models)
ax.set_ylim(*ylim_values)
ax.set_yticks(yticks_values)
ax.legend(
    title=legend_title,
    loc="upper center",
    bbox_to_anchor=(0.5, 1.2),
    frameon=False,
    ncol=7,
)
ax.set_facecolor("#eaeaf2")
ax.yaxis.grid(True, color="white")
ax.set_axisbelow(True)

# Remove spines
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.spines["left"].set_visible(False)

plt.tick_params(axis="both", which="both", length=0)

# ===================
# Part 4: Saving Output
# ===================
fig.set_size_inches(12, 4)
plt.tick_params(axis="both", which="both", length=0)
plt.tight_layout()
plt.savefig("bar_37.pdf", bbox_inches="tight")
