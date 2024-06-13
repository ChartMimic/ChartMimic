# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

import matplotlib.colors as mcolors

# ===================
# Part 2: Data Preparation
# ===================
# Data in the heatmap
data = np.array(
    [
        [169, 547, 662, 271, 145, 1248],
        [115, 439, 753, 239, 141, 1355],
        [219, 585, 557, 259, 153, 1269],
        [67, 941, 708, 432, 162, 732],
        [177, 554, 661, 235, 169, 1246],
    ]
)

# Labels for rows and columns
row_labels = ["Qwen", "ChatGLM3", "Baichuan2", "LLaMA-2", "Xverse"]
column_labels = ["0", "1", "2", "3", "4", "5"]
title = "Question Type: All three types of questions"
xlabel = "Response Action Category"
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Initialize the matplotlib figure
f, ax = plt.subplots(figsize=(9, 6))

# Get the colors from the original colormap
original_cmap = plt.get_cmap("Paired_r")
colors = original_cmap(np.linspace(0, 1, original_cmap.N))

# Set the colormap with reverse order
cmap = mcolors.LinearSegmentedColormap.from_list("Paired_r", colors[::-1])

# Draw the heatmap with the reversed colormap
cax = ax.imshow(data, cmap=cmap)

# Set the title
ax.set_title(title, fontsize=18)

# Set labels for axes
ax.set_xlabel(xlabel, fontsize=18)
ax.set_xticks(range(len(column_labels)))
ax.set_xticklabels(column_labels)
ax.set_yticks(range(len(row_labels)))
ax.set_yticklabels(row_labels)

# Increase font size of the tick labels
ax.tick_params(axis="both", which="major", labelsize=14)

# Rotate the row labels to horizontal and set the font size
ax.set_yticklabels(ax.get_yticklabels(), rotation=0, fontsize=14)

# Add the text annotations
for i in range(len(row_labels)):
    for j in range(len(column_labels)):
        text = ax.text(
            j, i, data[i, j], ha="center", va="center", color="w", fontsize=14
        )

# Create colorbar
cbar = f.colorbar(cax, ax=ax)
cbar.ax.tick_params(labelsize=14)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout to fit the figure size
plt.tight_layout()

# Show the plot
plt.savefig("heatmap_2.pdf", bbox_inches="tight")
