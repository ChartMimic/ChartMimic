# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

import matplotlib.tri as tri

# ===================
# Part 2: Data Preparation
# ===================
# First create the x and y coordinates of the points.
n_angles = 48
n_radii = 12
min_radius = 0.45
radii = np.linspace(min_radius, 0.95, n_radii)

angles = np.linspace(0, 2 * np.pi, n_angles, endpoint=False)
angles = np.repeat(angles[..., np.newaxis], n_radii, axis=1)
angles[:, 1::2] += np.pi / n_angles

x = (radii * np.cos(angles)).flatten()
y = (radii * np.sin(angles)).flatten()
z = (np.cos(radii) * np.cos(3 * angles)).flatten()
title = "tripcolor of Delaunay triangulation, flat shading"


# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create the Triangulation; no triangles so Delaunay triangulation created.
triang = tri.Triangulation(x, y)

# Mask off unwanted triangles.
triang.set_mask(
    np.hypot(x[triang.triangles].mean(axis=1), y[triang.triangles].mean(axis=1))
    < min_radius
)
fig1, ax1 = plt.subplots(figsize=(8, 6))
ax1.set_aspect("equal")
tpc = ax1.tripcolor(triang, z, shading="flat", cmap='plasma')
fig1.colorbar(tpc)
ax1.set_title(title)

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig("HR_24.pdf", bbox_inches="tight")
