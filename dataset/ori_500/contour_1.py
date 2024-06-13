# ===================
# Part 1: Importing Libraries
# ===================
import numpy as np

np.random.seed(0)

import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal
from matplotlib.patches import Patch

# ===================
# Part 2: Data Preparation
# ===================
# Sample data generation (replace with actual data)
x = np.linspace(-80, 80, 400)
y = np.linspace(-80, 80, 400)
X, Y = np.meshgrid(x, y)
pos = np.dstack((X, Y))
rv1 = multivariate_normal([50, 0], [[1000, 0], [0, 1000]])
rv2 = multivariate_normal([-50, 0], [[1000, 0], [0, 1000]])
Z1 = rv1.pdf(pos)
Z2 = rv2.pdf(pos)
title = "T-SNE plot for the output variable Y3"
labels = ["Ground Truth", "Generated"]
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plotting
plt.figure(figsize=(10, 6))
contour1 = plt.contourf(X, Y, Z1, cmap="Blues")
contour2 = plt.contourf(X, Y, Z2, cmap="Reds", alpha=0.5)
plt.title(title)

# Create legend with color patches
legend_patches = [
    Patch(color="blue", label=labels[0]),
    Patch(color="red", label=labels[1]),
]
plt.legend(handles=legend_patches)

# Adjust plot to match the original image's dimensions
plt.gca().set_aspect("equal", adjustable="box")

# ===================
# Part 4: Saving Output
# ===================
# Reduce whitespace around the plot
plt.tight_layout()
plt.savefig("contour_1.pdf", bbox_inches="tight")
