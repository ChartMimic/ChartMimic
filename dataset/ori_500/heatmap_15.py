# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Sample data to mimic the picture
data = np.array(
    [
        [0, 1, 2, 3, 4, 5],
        [np.nan, 1, 2, 3, 4, 5],
        [np.nan, np.nan, 1, 2, 3, 4],
        [np.nan, np.nan, np.nan, 1, 2, 3],
        [np.nan, np.nan, np.nan, np.nan, 1, 2],
        [np.nan, np.nan, np.nan, np.nan, np.nan, 1],
    ]
)
colorbar_label = "Increase in perplexity"
xlabel = "To layer"
ylabel = "Start removing from layer"
textstr = "mbert→sat\nPerplexity=7.59"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create the figure and axis
fig, ax = plt.subplots(figsize=(6, 8))

# Create the heatmap
cax = ax.matshow(data, cmap="inferno")

# Add colorbar
cbar = fig.colorbar(cax, label=colorbar_label, shrink=0.5)  # Add shrink parameter here

# Set axis labels
ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)

# Set axis ticks
ax.set_xticks(np.arange(6))
ax.set_yticks(np.arange(6))
ax.set_xticklabels([1, 3, 5, 9, 12, ""])
ax.set_yticklabels([1, 3, 5, 9, 12, ""])

# Add text box
props = dict(
    boxstyle="round",
    facecolor="white",
    alpha=0.5,
)
ax.text(
    0.05,
    0.15,
    textstr,
    transform=ax.transAxes,
    fontsize=12,
    verticalalignment="top",
    bbox=props,
)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save the plot
plt.tight_layout()
plt.savefig("heatmap_15.pdf", bbox_inches="tight")
