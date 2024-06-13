# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Define the data for the original and adjusted values
original_values = [0.10, 0.08, 0.30, 0.60, 0.00, 0.50, 0.07, 0.10]
adjusted_values = [0.12, 0.22, 0.44, 0.30, 0.32, 0.44, 0.10, 0.00]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create a figure with two subplots (one for original and one for adjusted values)
fig, axs = plt.subplots(2, 1, figsize=(10, 6), sharex=True)

# Define the color palette
cmap = plt.get_cmap("Greys")

# Plot heatmap for original values
im1 = axs[0].imshow(pd.DataFrame([original_values], index=[""]), cmap=cmap)
axs[0].set_xticks([])
axs[0].set_yticks([])

# Add annotations for original values
for j in range(len(original_values)):
    if original_values[j] > np.mean(original_values):
        axs[0].text(
            j, 0, f"{original_values[j]:.2f}", ha="center", va="center", color="white"
        )
    else:
        axs[0].text(
            j, 0, f"{original_values[j]:.2f}", ha="center", va="center", color="black"
        )

# Plot heatmap for adjusted values
im2 = axs[1].imshow(pd.DataFrame([adjusted_values], index=[""]), cmap=cmap)
axs[1].set_xticks([])
axs[1].set_yticks([])

# Add annotations for adjusted values
for j in range(len(adjusted_values)):
    if adjusted_values[j] > np.mean(adjusted_values):
        axs[1].text(
            j, 0, f"{adjusted_values[j]:.2f}", ha="center", va="center", color="white"
        )
    else:
        axs[1].text(
            j, 0, f"{adjusted_values[j]:.2f}", ha="center", va="center", color="black"
        )

# ===================
# Part 4: Saving Output
# ===================
# Display the figure with tight layout to minimize white space
plt.tight_layout()
plt.savefig("heatmap_23.pdf", bbox_inches="tight")
