import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)

import matplotlib.tri as tri

# ===================
# Part 2: Data Preparation
# ===================
# First create the x and y coordinates of the points.
n_points = 32
n_categories = 4
min_value = 0.1
values = np.linspace(min_value, 0.75, n_categories)

categories = np.linspace(0, 2 * np.pi, n_points, endpoint=False)
categories = np.repeat(categories[..., np.newaxis], n_categories, axis=1)
categories[:, 1::2] += np.pi / n_points

x = (values * np.cos(categories)).flatten()
y = (values * np.sin(categories)).flatten()
z = (np.sin(values) * np.sin(3 * categories)).flatten()
title = "Distribution of Values Across Categories"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create the Triangulation; no triangles so Delaunay triangulation created.
triang = tri.Triangulation(x, y)

# Mask off unwanted triangles.
triang.set_mask(
    np.hypot(x[triang.triangles].mean(axis=1), y[triang.triangles].mean(axis=1))
    < min_value
)
fig1, ax1 = plt.subplots(figsize=(8, 6))
ax1.set_aspect("equal")
tpc = ax1.tripcolor(triang, z, shading="flat",cmap='plasma')
fig1.colorbar(tpc)
ax1.set_title(title)

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig('HR_24.pdf', bbox_inches='tight')
