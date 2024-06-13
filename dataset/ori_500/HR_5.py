# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Generate theta values
theta = np.linspace(0, 2 * np.pi, 100)
# Calculate the x and y coordinates
x = np.cos(theta)
y = np.sin(theta)

distances_from_minus_one = np.sqrt((x + 1) ** 2 + (y + 1) ** 2)

# Normalize these new distances for color mapping
normalized_distances_from_minus_one = (
    distances_from_minus_one - np.min(distances_from_minus_one)
) / (np.max(distances_from_minus_one) - np.min(distances_from_minus_one))

# Creating a custom linear color map from light blue to dark blue based on these new normalized distances
colors = [plt.cm.Blues(distance) for distance in normalized_distances_from_minus_one]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Set the figure size to match the original image's dimensions
plt.figure(figsize=(6, 6))

# Plot the points
plt.scatter(x, y, c=colors, s=100, edgecolor="none")

# Set the aspect of the plot to be equal
plt.axis("equal")

# Add axis lines
plt.axhline(0, color="gray", linewidth=0.5)
plt.axvline(0, color="gray", linewidth=0.5)

# Add tick labels
plt.xticks([])
plt.yticks([])

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig("HR_5.pdf", bbox_inches="tight")
