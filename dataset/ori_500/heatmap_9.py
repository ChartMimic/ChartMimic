# ===================
# Part 1: Importing Libraries
# ===================
import numpy as np

np.random.seed(0)

import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Sample data for demonstration
data_upper = np.random.rand(9, 16)  # Data for the upper subplot
data_lower = np.random.rand(9, 16)  # Data for the lower subplot

# Common labels for both subplots
words = [
    "<endoftext>",
    "No / The",
    "athlete",
    "that",
    "loved",
    "the",
    "ministers",
    "has",
    "landed",
]
layers = list(range(15))

# Axes Limits and Labels
title = "pythia-1b"
xlabel_value = "Layers"
xticks_values = [0, 5, 10, 15]
xticklabels = [0, 5, 10, 15]
yticks_values = range(len(words))

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create a figure and two subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(5, 6))  # Adjust figsize as needed

# First subplot
im1 = ax1.imshow(data_upper, cmap="Purples")
ax1.set_title(title)
# Hide x-axis labels and ticks for the first subplot
ax1.set_yticks(range(len(words)))
ax1.set_yticklabels(words)

# Second subplot
im2 = ax2.imshow(data_lower, cmap="Purples")
# Set x-axis label and ticks for the second subplot
ax2.set_xlabel(xlabel_value)
ax2.set_xticks(xticks_values)  # Show ticks at [0, 5, 10, 15]
ax2.set_xticklabels(xticklabels)  # Label ticks at [0, 5, 10, 15]
ax2.set_yticks(yticks_values)
ax2.set_yticklabels(words)

# ===================
# Part 4: Saving Output
# ===================
# Show the entire figure with tight layout to minimize white space
plt.tight_layout()
plt.savefig("heatmap_9.pdf", bbox_inches="tight")
