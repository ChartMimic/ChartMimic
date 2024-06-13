# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Placeholder data for confusion matrices
data_live = np.array(
    [
        [44, 0, 0, 0, 0, 0],
        [23, 42, 0, 0, 0, 0],
        [45, 18, 53, 0, 0, 0],
        [0, 0, 0, 44, 0, 0],
        [0, 0, 0, 23, 50, 0],
        [0, 0, 0, 42, 44, 16],
    ]
)
data_csiq = np.array(
    [
        [0, 0, 0, 41, 0, 0],
        [0, 0, 0, 32, 34, 0],
        [0, 0, 0, 15, 22, 18],
        [24, 0, 0, 0, 0, 0],
        [43, 12, 0, 0, 0, 0],
        [15, 28, 43, 0, 0, 0],
    ]
)

# Titles for the subplots
titles = ["LIVE", "CSIQ"]
ylabel = "Labeling Function Similarity"
xlabel = "Predicted category"
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Increase the figure height and adjust subplot layout
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(6, 5))


# Function to create a single confusion matrix plot
def plot_confusion_matrix(ax, data, title):
    im = ax.imshow(data, interpolation="nearest", cmap="Purples")
    ax.set(
        title=title,
        ylabel=ylabel,
        xlabel=xlabel,
        xticks=np.arange(data.shape[1]),
        yticks=np.arange(data.shape[0]),
    )
    ax.axhline(y=2.5, color="black", linewidth=4)
    ax.axvline(x=2.5, color="black", linewidth=4)
    # unset the ticks
    ax.set_xticks([])
    ax.set_yticks([])
    # unset the spines
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["left"].set_visible(False)
    return im


# Plot each confusion matrix
im1 = plot_confusion_matrix(axes[0], data_live, titles[0])
im2 = plot_confusion_matrix(axes[1], data_csiq, titles[1])

# Adjust the position and size of the colorbars
cbar_ax1 = fig.add_axes([0.05, 0.15, 0.45, 0.02])  # Adjusted for the first subplot
cbar_ax2 = fig.add_axes([0.55, 0.15, 0.45, 0.02])  # Adjusted for the second subplot
fig.colorbar(im1, cax=cbar_ax1, orientation="horizontal")
fig.colorbar(im2, cax=cbar_ax2, orientation="horizontal")

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
fig.tight_layout()
plt.savefig("heatmap_12.pdf", bbox_inches="tight")
