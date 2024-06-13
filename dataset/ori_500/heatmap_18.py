# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data for the heatmaps (randomly generated for demonstration purposes)
data_autoformer = np.random.rand(4, 4)
data_informer = np.random.rand(4, 4)
data_reformer = np.random.rand(4, 4)
data_transformer = np.random.rand(4, 4)
titles = ["Autoformer", "Informer", "Reformer", "Transformer"]
fig_title = "Weather"
colorbar_label = "Correlation coefficient"
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create a figure with subplots
fig, axs = plt.subplots(2, 2, figsize=(7, 6))


# Function to add text annotations
def add_annotations(ax, data):
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            ax.text(j, i, f"{data[i, j]:.2f}", ha="center", va="center", color="w")


# Autoformer heatmap
im1 = axs[0, 0].imshow(data_autoformer, cmap="YlOrBr", vmin=-1, vmax=1)
axs[0, 0].set_title(titles[0])
add_annotations(axs[0, 0], data_autoformer)

# Informer heatmap
im2 = axs[0, 1].imshow(data_informer, cmap="YlOrBr", vmin=-1, vmax=1)
axs[0, 1].set_title(titles[1])
add_annotations(axs[0, 1], data_informer)

# Reformer heatmap
im3 = axs[1, 0].imshow(data_reformer, cmap="YlOrBr", vmin=-1, vmax=1)
axs[1, 0].set_title(titles[2])
add_annotations(axs[1, 0], data_reformer)

# Transformer heatmap
im4 = axs[1, 1].imshow(data_transformer, cmap="YlOrBr", vmin=-1, vmax=1)
axs[1, 1].set_title(titles[3])
add_annotations(axs[1, 1], data_transformer)

# Adjust layout and add overall title
fig.suptitle(fig_title, fontsize=16)

# Add color bar and shift it to the right
cbar = fig.colorbar(im1, ax=axs.ravel().tolist(), shrink=0.75)
cbar.set_label(colorbar_label)

# Set tick labels
for ax in axs.flat:
    ax.set_xticks(np.arange(4))
    ax.set_yticks(np.arange(4))
    ax.set_xticklabels(["96", "192", "336", "720"])
    ax.set_yticklabels(["96", "192", "336", "720"])

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout to minimize white space
plt.tight_layout(rect=[0, 0, 0.2, 0.1])
# Save the figure to a file
plt.savefig("heatmap_18.pdf", bbox_inches="tight")
