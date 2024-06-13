# ===================
# Part 1: Importing Libraries
# ===================
import numpy as np

np.random.seed(0)

import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Generate random data for heatmap
data = np.random.rand(8, 12)
title = "ROC's AUC"
xlabel = "Timeshift"
ylabel = "Scales"
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create a new figure
plt.figure(figsize=(8, 6))

# Set the title of the heatmap
plt.title(title)

# Set the label for the x-axis
plt.xlabel(xlabel)

# Set the label for the y-axis
plt.ylabel(ylabel)

# Create a heatmap using pcolor function
# Edgecolors sets the color of the cell borders
# Linewidths sets the width of the cell borders
# cmap sets the color map
# vmin and vmax set the colorbar range
c = plt.pcolor(data, edgecolors="k", linewidths=4, cmap="RdBu", vmin=0.0, vmax=1.0)

# Add a colorbar to the figure
plt.colorbar(c)

# ===================
# Part 4: Saving Output
# ===================
# Display the figure with tight layout to minimize white space
plt.tight_layout()
plt.savefig("heatmap_30.pdf", bbox_inches="tight")
