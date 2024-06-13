# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Fixing random state for reproducibility

# Define custom histogram data for 4 bars decreasing along the diagonal
hist = np.array([[4, 0, 0, 0], [0, 3, 0, 0], [0, 0, 2, 0], [0, 0, 0, 1]])

# Define the edges of the bins
xedges = np.array([0, 1, 2, 3, 4])
yedges = np.array([0, 1, 2, 3, 4])

# Construct arrays for the anchor positions of the 4 bars.
xpos, ypos = np.meshgrid(xedges[:-1] + 0.25, yedges[:-1] + 0.25, indexing="ij")
xpos = xpos.ravel()
ypos = ypos.ravel()
zpos = 0

# Only keep positions where there is a non-zero bar
non_zero_indices = hist.ravel() > 0
xpos = xpos[non_zero_indices]
ypos = ypos[non_zero_indices]
dz = hist.ravel()[non_zero_indices]

# All bars have the same width and depth
dx = dy = 0.5 * np.ones_like(dz)

# Axes Limits and Labels
ax_xlabel = "Height"
ax_ylabel = "Width"
ax_zlabel = "Count"
zticks_values = [0, 1, 2, 3, 4]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create a new figure for the modified 3D bar plot
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(projection="3d")

ax.bar3d(xpos, ypos, zpos, dx, dy, dz, zsort="average", color="red")

ax.set_xlabel(ax_xlabel)
ax.set_ylabel(ax_ylabel)
ax.set_zlabel(ax_zlabel)

ax.set_zticks(zticks_values)

ax.set_box_aspect(aspect=None, zoom=0.8)

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig("3d_10.pdf", bbox_inches="tight")
