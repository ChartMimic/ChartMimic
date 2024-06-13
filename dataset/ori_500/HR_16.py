# ===================
# Part 1: Importing Libraries
# ===================
import numpy as np

np.random.seed(0)

import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Data and labels
theta = [0, 0.65, 2.0, 3.8, 5.2]  # Angles for the bars
radii = np.array([6, 4, 7, 2, 9])  # Radii of the bars
width = [0.8, 0.5, 2.2, 1.4, 1.4]  # Width of the bars
categories = [
    "En.QA",
    "En.Sum",
    "Retrieve.KV",
    "Retrieve.Number",
    "Retrieve.PassKey",
]  # Labels for the bars
colors = plt.cm.viridis(radii / 10.0)  # Colors mapped to the radii values

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create the figure
plt.figure(figsize=(8, 8))
ax = plt.subplot(111, projection="polar")  # Set up polar plot

# Plot the bars
bars = ax.bar(theta, radii, width=width, bottom=0, color=colors, alpha=0.5, zorder=3)

# Add labels to the bars
for bar, angle, label in zip(bars, theta, categories):
    rotation = np.degrees(angle)  # Convert angle to degrees
    alignment = "center"  # Center align the labels
    # Place the text inside the bar, rotated correctly
    ax.text(
        angle,
        bar.get_height() + 0.5,
        label,
        ha=alignment,
        va="center",
        rotation_mode="anchor",
    )

# Remove the polar angle labels to declutter the plot
ax.set_xticklabels([])

# Remove the radial labels
ax.set_yticklabels([])

# ===================
# Part 4: Saving Output
# ===================
# Save the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig("HR_16.pdf", bbox_inches="tight")
