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
products = ["iPhone 13", "Samsung S21", "Google Pixel 6", "OnePlus 9"]
truthful_recall = [46.3, 57.9, 53.8, 19.4]
misleading_recall = [30.1, 34, 43.7, 20]
error_truthful = [5, 3, 4, 2]  # Error values for truthful recall
error_misleading = [4, 3, 5, 2]  # Error values for misleading recall
x = np.arange(len(truthful_recall))  # x-coordinates for the bars
labels = ["Truthful Recall", "Misleading Recall"]
title = "Comparison of Recall Rates Across Products"
ylims = [[0, 70], [0, 50]]
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Set the figure size
fig, ax1 = plt.subplots(figsize=(8, 5))
# Bar width
width = 0.35

# Plotting 'truthful_recall' on the primary y-axis
bars1 = ax1.bar(
    x - width / 2,
    truthful_recall,
    width,
    label=labels[0],
    color="#4695a2",
    yerr=error_truthful,
    capsize=5,
    edgecolor="black",
)

# Create the secondary y-axis for 'misleading_recall'
ax2 = ax1.twinx()
bars2 = ax2.bar(
    x + width / 2,
    misleading_recall,
    width,
    label=labels[1],
    color="coral",
    yerr=error_misleading,
    capsize=5,
    edgecolor="black",
)

# Adding annotations directly on the bars for clarity
for i, bar in enumerate(bars1):
    height = bar.get_height()
    label_x_pos = bar.get_x() + bar.get_width() / 2
    ax1.text(
        label_x_pos,
        height - error_truthful[i] - 1,
        f"{height}%",
        rotation=90,
        ha="center",
        va="bottom" if height < 0 else "top",
    )
for j, bar in enumerate(bars2):
    height = bar.get_height()
    label_x_pos = bar.get_x() + bar.get_width() / 2
    ax2.text(
        label_x_pos,
        height - error_misleading[j] - 1,
        f"{height}%",
        rotation=90,
        ha="center",
        va="bottom" if height < 0 else "top",
    )


fig.suptitle(title)
# Adding labels, title, and custom x-axis tick labels
ax1.set_ylabel(labels[0], color="#5b93a0")
ax2.set_ylabel(labels[1], color="coral")
ax1.set_xticks(x)
ax1.set_xticklabels(products)

# Add a horizontal line at y=0 if needed
ax1.axhline(0, color="grey", linewidth=0.8)

# Adjusting y-axis limits to fit the annotations and errors
ax1.set_ylim(ylims[0])
ax2.set_ylim(ylims[1])

# Adding grid lines for better readability
ax1.yaxis.grid(linestyle="--", linewidth="0.5", color="grey")
ax1.set_axisbelow(True)

ax2.yaxis.grid(linestyle="--", color="grey")
ax2.set_axisbelow(True)
# Adding legend
fig.legend(loc="upper center", bbox_to_anchor=(0.5, 1.05), ncol=2)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout
plt.tight_layout()
plt.savefig("errorbar_25.pdf", bbox_inches="tight")
