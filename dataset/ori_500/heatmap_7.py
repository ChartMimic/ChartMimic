# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Sample data for correlation coefficients
data = np.array(
    [
        [1.00, 0.90, 0.89, 0.88, 0.64, 0.65, 0.68, 0.71, 0.82],
        [0.90, 1.00, 0.93, 0.92, 0.67, 0.69, 0.72, 0.75, 0.82],
        [0.89, 0.93, 1.00, 0.95, 0.66, 0.68, 0.70, 0.74, 0.81],
        [0.88, 0.92, 0.95, 1.00, 0.68, 0.69, 0.72, 0.75, 0.82],
        [0.64, 0.67, 0.66, 0.68, 1.00, 0.85, 0.90, 0.83, 0.77],
        [0.65, 0.69, 0.68, 0.69, 0.85, 1.00, 0.89, 0.86, 0.75],
        [0.68, 0.72, 0.70, 0.72, 0.90, 0.89, 1.00, 0.86, 0.79],
        [0.71, 0.75, 0.74, 0.75, 0.83, 0.86, 0.86, 1.00, 0.80],
        [0.82, 0.82, 0.81, 0.82, 0.77, 0.75, 0.79, 0.80, 1.00],
    ]
)

labels = ["en", "fr", "es", "pt", "bn", "ur", "hi", "ar", "zh"]
title = "Correlation Coefficients"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Adjust the figure size to match the original image's dimensions
fig, ax = plt.subplots(
    figsize=(10, 8)
)  # Adjust the figure size to match the original image's dimensions

# Create the heatmap
cax = ax.matshow(data, cmap="coolwarm")

# Adjust color bar width
cbar = fig.colorbar(
    cax,
    fraction=0.046,
    pad=0.04,
    ticks=[0.65, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95, 1.00],
)
cbar.ax.set_yticklabels(
    ["0.65", "0.70", "0.75", "0.80", "0.85", "0.90", "0.95", "1.00"]
)

# Set axis labels
ax.set_xticks(np.arange(len(labels)))
ax.set_yticks(np.arange(len(labels)))
# x label should be at the bottom
ax.xaxis.set_ticks_position("bottom")
ax.set_xticklabels(labels)
ax.set_yticklabels(labels)

# Display the correlation values in the cells
for i in range(len(labels)):
    for j in range(len(labels)):
        ax.text(
            j,
            i,
            f"{data[i, j]:.2f}",
            va="center",
            ha="center",
            color="white" if data[i, j] < 0.5 else "black",
            fontsize=10,
        )

# Set title
ax.set_title(title, pad=20)

# ===================
# Part 4: Saving Output
# ===================
# Adjust figure size and show the plot
fig.set_size_inches(10, 8)
fig.tight_layout()
plt.savefig("heatmap_7.pdf", bbox_inches="tight")
