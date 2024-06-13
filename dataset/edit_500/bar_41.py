# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data for the bar charts
truthful_recall = np.array(
    [
        [72.5, 68.3, 61.9],
        [54.7, 50.4, 47.8],
        [53.2, 48.9, 43.5],
        [49.1, 45.7, 35.6],
        [29.4, 32.7, 29.1],
    ]
)
misleading_recall = np.array(
    [
        [12.5, 15.8, 16.1],
        [38.7, 43.5, 33.2],
        [42.9, 52.1, 38.4],
        [51.3, 58.7, 45.2],
        [67.2, 62.5, 46.7],
    ]
)
x = [0, 1, 2]

# Titles for subplots
titles = [
    "High : Low Confidence = 2:0",
    "High : Low Confidence = 2:1",
    "High : Low Confidence = 2:2",
    "High : Low Confidence = 1:2",
    "High : Low Confidence = 0:2",
]

labels = ["High Confidence Recall", "Low Confidence Recall"]
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
plt.savefig('bar_41.pdf', bbox_inches='tight')
