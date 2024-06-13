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
truthful_recall = [46.3, 57.9, 53.8, 19.4]
misleading_recall = [30.1, 34, 43.7, 20]
x = np.arange(len(truthful_recall))  # x-coordinates for the bars
labels = ["Truthful Recall", "Misleading Recall"]  # Labels for the legend
title = "Truthful:Misleading = 2:0"  # Title for the plot
ylim1 = [-60, 60]  # y-axis limits for the first subplot
ylim2 = [-50, 50]  # y-axis limits for the second subplot
yticks1 = [0, 20, 40, 60]  # y-ticks for the first subplot
yticks2 = [-40, -20, 0]  # y-ticks for the second subplot

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Set the figure size to match the original image's dimensions
fig, ax1 = plt.subplots(figsize=(6, 4))

# Create the first subplot for 'truthful_recall' using the left y-axis
ax1.bar(
    x,
    truthful_recall,
    width=0.4,
    label=labels[0],
    color="#404346",
    align="center",
)
ax1.set_ylabel(labels[0], color="#404346")
ax1.tick_params(axis="y", labelcolor="#404346")

# Create the second y-axis for 'misleading_recall'
ax2 = ax1.twinx()
ax2.bar(
    x,
    [-i for i in misleading_recall],
    width=0.4,
    label=labels[1],
    color="#dc9dae",
    align="center",
)
ax2.set_ylabel(labels[1], color="#dc9dae")
ax2.tick_params(axis="y", labelcolor="#dc9dae")

# Title for the plot
title = title
ax1.set_title(title)

# Set x-axis labels (empty in this case as per original code)
ax1.set_xticks(x)
ax1.set_xticklabels([])

# Drawing a horizontal line at y=0
ax1.axhline(0, color="black", linewidth=0.8)

# Annotate bars with their values
for j in range(4):
    ax1.text(
        x[j],
        truthful_recall[j] - 5,
        f"{truthful_recall[j]}%",
        ha="center",
        color="white",
    )
    ax2.text(
        x[j],
        -misleading_recall[j] - 5,
        f"{misleading_recall[j]}%",
        ha="center",
        color="#dc9dae",
    )

ax1.set_ylim(ylim1)
ax1.set_yticks(yticks1)

ax2.set_ylim(ylim2)
ax2.set_yticks(yticks2)
ax2.set_yticklabels(yticks2)
# Add legend to the subplot
ax1.legend(loc="upper left", bbox_to_anchor=(0.0, 1.2))
ax1.grid(axis="y", linestyle="--")
ax1.set_axisbelow(True)
ax2.legend(loc="upper right", bbox_to_anchor=(1, 1.2))
ax2.grid(axis="y", linestyle="--")
ax2.set_axisbelow(True)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout
plt.tight_layout()
plt.savefig("bar_75.pdf", bbox_inches="tight")
