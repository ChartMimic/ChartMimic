# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Sample data for demonstration purposes
ratings_data = [np.random.normal(2.6, 0.1, 100), np.random.normal(2.4, 0.1, 100)]
intrusion_data = [np.random.normal(0.75, 0.05, 100), np.random.normal(0.7, 0.05, 100)]

title_1 = "Ratings"
title_2 = "Intrusion"
xticklabels = ["Our Model", "NTM+CL"]
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Set the figure size to match the original image's dimensions
plt.figure(figsize=(8, 6))

# Create subplots
fig, axs = plt.subplots(2, 2)

# Plot the boxplots
bp1 = axs[0, 0].boxplot(
    ratings_data,
    patch_artist=True,
    widths=0.5,
    showfliers=False,
    medianprops=dict(color="black"),
)
bp2 = axs[0, 1].boxplot(
    intrusion_data,
    patch_artist=True,
    widths=0.5,
    showfliers=False,
    medianprops=dict(color="black"),
)
bp3 = axs[1, 0].boxplot(
    ratings_data,
    patch_artist=True,
    widths=0.5,
    showfliers=False,
    medianprops=dict(color="black"),
)
bp4 = axs[1, 1].boxplot(
    intrusion_data,
    patch_artist=True,
    widths=0.5,
    showfliers=False,
    medianprops=dict(color="black"),
)

# Set the colors of the boxes
bp1["boxes"][0].set_facecolor("#d98694")
bp1["boxes"][1].set_facecolor("#5d9c97")
bp2["boxes"][0].set_facecolor("#d98694")
bp2["boxes"][1].set_facecolor("#5d9c97")
bp3["boxes"][0].set_facecolor("#d98694")
bp3["boxes"][1].set_facecolor("#5d9c97")
bp4["boxes"][0].set_facecolor("#d98694")
bp4["boxes"][1].set_facecolor("#5d9c97")

# Set titles and labels
axs[0, 0].set_title(title_1)
axs[0, 0].grid("both")
axs[0, 1].set_title(title_2)
axs[0, 1].grid("both")
axs[0, 0].set_xticklabels(xticklabels)
axs[0, 1].set_xticklabels(xticklabels)
axs[1, 0].set_title(title_1)
axs[1, 0].grid("both")
axs[1, 1].set_title(title_2)
axs[1, 1].grid("both")
axs[1, 0].set_xticklabels(xticklabels)
axs[1, 1].set_xticklabels(xticklabels)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save the figure
plt.tight_layout()
plt.savefig("box_2.pdf", bbox_inches="tight")
