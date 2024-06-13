# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

import matplotlib.ticker as ticker

# ===================
# Part 2: Data Preparation
# ===================
# Data for the heatmap
data = np.random.rand(6, 6)

# Masks to separate the upper triangle and lower triangle
mask_upper = np.triu(np.ones_like(data, dtype=bool))
mask_lower = np.tril(np.ones_like(data, dtype=bool))
xticklabels = ["ada", "mis", "dis", "mpn", "Min", "qad"]
yticklabels = ["ada", "mistral", "distilroberta", "mpnet", "MiniLM", "qa-distilbert"]
color_bar_labels = ["Wasserstein Distance", "Bottleneck Distance"]
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create the figure and axis
fig, ax = plt.subplots(figsize=(8, 6))

# Create the heatmap with the lower triangle in blue
cax1 = ax.matshow(np.ma.masked_array(data, mask=mask_upper), cmap="Blues")

# Create the heatmap with the upper triangle in green
cax2 = ax.matshow(np.ma.masked_array(data, mask=mask_lower), cmap="Greens")

# Set ticks and labels
ax.set_xticks(np.arange(data.shape[1]))
ax.set_yticks(np.arange(data.shape[0]))
ax.set_xticklabels(xticklabels, rotation=0)
ax.set_yticklabels(yticklabels)

# Set the tick labels on the x-axis to not be rotated
plt.setp(ax.get_xticklabels(), rotation=0, ha="center")

# Hide the axis spines and ticks
ax.tick_params(top=False, bottom=True, labeltop=False, labelbottom=True)
for spine in ax.spines.values():
    spine.set_visible(False)

# Formatter to display ticks with two decimal places
formatter = ticker.FuncFormatter(lambda x, _: f"{x:.2f}")

# Colorbar for the blue scale
cbar1 = fig.colorbar(cax1, ax=ax, orientation="vertical", fraction=0.039, pad=0.14)
cbar1.ax.yaxis.set_major_formatter(formatter)
cbar1.ax.set_ylabel(color_bar_labels[0], rotation=90, labelpad=8)

# Colorbar for the green scale. Adjust pad if they overlap.
cbar2 = fig.colorbar(cax2, ax=ax, orientation="vertical", fraction=0.047, pad=0.03)
cbar2.ax.yaxis.set_major_formatter(formatter)
cbar2.ax.set_ylabel(color_bar_labels[1], rotation=90, labelpad=8)

# Set the colorbar ticks
cbar1.ax.yaxis.set_major_locator(ticker.MaxNLocator(nbins=11))
cbar2.ax.yaxis.set_major_locator(ticker.MaxNLocator(nbins=11))

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and show the plot
fig.tight_layout()
plt.savefig("heatmap_3.pdf", bbox_inches="tight")
