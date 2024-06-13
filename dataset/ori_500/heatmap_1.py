# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data in the heatmap
data = np.array(
    [
        [0.61, 0.74, 0.70, 0.70, 0.57],
        [1.00, 0.69, 0.64, 0.67, 0.45],
        [np.nan, 1.00, 0.77, 0.88, 0.62],
        [np.nan, np.nan, 1.00, 0.72, 0.69],
        [np.nan, np.nan, np.nan, 1.00, 0.54],
        [np.nan, np.nan, np.nan, np.nan, 1.00],
    ]
)

# Labels for the rows and columns
row_labels = ["AVG", "CoreNLP", "Stanza", "Biaffine", "StackPointer", "TowerParse"]
col_labels = ["CoreNLP", "Stanza", "Biaffine", "StackPointer", "TowerParse"]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create the figure and the axes
fig, ax = plt.subplots(figsize=(8, 8))

# Create the heatmap
cax = ax.matshow(data, cmap="Reds")

# Set the ticks
ax.set_xticks(np.arange(len(col_labels)))
ax.set_yticks(np.arange(len(row_labels)))

# Set the tick labels
ax.set_xticklabels(col_labels)
ax.set_yticklabels(row_labels)

# Rotate the tick labels and set their alignment
plt.setp(ax.get_xticklabels(), rotation=45, ha="left", rotation_mode="anchor")

# Move the row labels to the right side
ax.yaxis.tick_right()

# Loop over data dimensions and create text annotations
for i in range(len(row_labels)):
    for j in range(len(col_labels)):
        if not np.isnan(data[i, j]):
            text = ax.text(
                j, i, f"{data[i, j]:.2f}", ha="center", va="center", color="black"
            )

# Set the visibility of the spines
ax.spines["top"].set_visible(True)
ax.spines["right"].set_visible(True)
ax.spines["left"].set_visible(False)
ax.spines["bottom"].set_visible(False)

# Set the visibility of the ticks with only the top and right axes
ax.xaxis.set_ticks_position("top")
ax.yaxis.set_ticks_position("right")

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save the figure
plt.tight_layout()
plt.savefig("heatmap_1.pdf", bbox_inches="tight")
