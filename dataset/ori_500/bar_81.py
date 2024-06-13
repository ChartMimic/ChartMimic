# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data for the bar charts
truthful_recall = [46.3, 56.9, 53.8, 19.4]
truthful_recall2 = [45, 34, 40, 27]

misleading_recall = [30.1, 34, 43.7, 20]
x = np.arange(len(truthful_recall)) * 1.5  # x-coordinates for the bars
labels = ["CaA Recall", "CaB Recall", "Misleading Recall"]
ylabel1 = "Truthful Recall"
ylabel2 = "Missleading Recall"
title = "Truthful:Misleading = 2:0"
xticklabels = ["LLaMA", "Vicuna", "Alpaca", "WizardLM"]
ylim1 = [-60, 60]
ylim2 = [-50, 50]
yticks1 = [0, 20, 40, 60]
yticks2 = [-40, -20, 0]
ytickslabels2 = ["40", "20", "0"]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Set the figure size to match the original image's dimensions
fig, ax1 = plt.subplots(figsize=(8, 4))

# Create the first subplot for 'truthful_recall' using the left y-axis
ax1.bar(
    x - 0.4,
    truthful_recall,
    width=0.4,
    label=labels[0],
    edgecolor="black",
    color="#3f81bb",
    align="center",
)
ax1.bar(
    x,
    truthful_recall2,
    width=0.4,
    label=labels[1],
    edgecolor="black",
    color="#33756f",
    align="center",
)

ax1.set_ylabel(ylabel1, color="black")
ax1.tick_params(axis="y", labelcolor="black")

# Create the second y-axis for 'misleading_recall'
ax2 = ax1.twinx()
ax2.bar(
    x + 0.4,
    [-i for i in misleading_recall],
    width=0.4,
    label=labels[2],
    edgecolor="black",
    color="#dc9dae",
    align="center",
)
ax2.set_ylabel(ylabel2, color="black")
ax2.tick_params(axis="y", labelcolor="black")

# Title for the plot
ax1.set_title(title)

# Set x-axis labels (empty in this case as per original code)
ax1.set_xticks(x)
ax1.set_xticklabels(xticklabels)

# Drawing a horizontal line at y=0
ax1.axhline(0, color="black", linewidth=0.8)

# Annotate bars with their values
for j in range(4):
    ax1.text(
        x[j] - 0.4,
        truthful_recall[j] - 6,
        f"{truthful_recall[j]}",
        ha="center",
        color="white",
    )
    ax1.text(
        x[j],
        truthful_recall2[j] - 6,
        f"{truthful_recall2[j]}",
        ha="center",
        color="white",
    )
    ax2.text(
        x[j] + 0.4,
        -misleading_recall[j] + 4,
        f"{misleading_recall[j]}",
        ha="center",
        color="white",
    )

ax1.set_ylim(ylim1)
ax1.set_yticks(yticks1)

ax2.set_ylim(ylim2)
ax2.set_yticks(yticks2)
ax2.set_yticklabels(ytickslabels2)
# Add legend to the subplot
ax1.legend(loc="upper left", bbox_to_anchor=(0.0, 1.2))
ax1.set_axisbelow(True)
ax2.legend(loc="upper right", bbox_to_anchor=(1, 1.2))
ax2.set_axisbelow(True)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout
plt.tight_layout()
plt.savefig("bar_81.pdf", bbox_inches="tight")
