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
truthful_recall = np.array(
    [
        [66.3, 61.9, 53.8],
        [49.3, 45.7, 41.6],
        [48.0, 42.6, 36.5],
        [43.8, 40.2, 30.6],
        [22.3, 25.9, 22.5],
    ]
)
misleading_recall = np.array(
    [
        [10.1, 13.6, 13.7],
        [36.3, 41.0, 31.5],
        [40.5, 49.6, 36.5],
        [49.5, 56.8, 42.8],
        [64.7, 59.6, 43.4],
    ]
)
x = [0, 1, 2]

# Titles for subplots
titles = [
    "Truthful:Misleading = 2:0",
    "Truthful:Misleading = 2:1",
    "Truthful:Misleading = 2:2",
    "Truthful:Misleading = 1:2",
    "Truthful:Misleading = 0:2",
]

labels = ["Truthful Recall", "Misleading Recall"]
ylim = [-80, 80]
xticks = [0, 1, 2]
xticklabels = [5, 10, 20]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Set the figure size to match the original image's dimensions
plt.figure(figsize=(14, 4))

# Create subplots
for i in range(5):
    ax = plt.subplot(1, 5, i + 1)
    ax.bar(x, truthful_recall[i], width=0.5, label=labels[0], color="#8a9ee7")
    ax.bar(
        x, -misleading_recall[i], width=0.5, label=labels[1], color="#dc7b75"
    )
    ax.set_title(titles[i])
    ax.set_ylim(ylim)
    ax.set_xticks(xticks)
    ax.set_xticklabels(xticklabels)
    # ax.axhline(0, color='black', linewidth=0.8)
    ax.yaxis.grid(True, linestyle="--")
    ax.set_axisbelow(True)

    # Annotate bars with their values
    for j in range(3):
        ax.text(
            x[j], truthful_recall[i][j] - 7, str(truthful_recall[i][j]), ha="center"
        )
        ax.text(
            x[j],
            -misleading_recall[i][j] + 5,
            str(misleading_recall[i][j]),
            ha="center",
        )

# Add legend to the first subplot
plt.subplot(1, 5, 1).legend(loc="lower right", frameon=False)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save the figure
plt.tight_layout()
plt.savefig("bar_41.pdf", bbox_inches="tight")
