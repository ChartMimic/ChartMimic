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
hist = np.array(
    [
        [8.0, 7.0, 5.0, 8.0],
        [4.0, 5.0, 8.0, 6.0],
        [5.0, 4.0, 13.0, 7.0],
        [5.0, 5.0, 9.0, 1.0],
    ]
)
xedges = np.array([0.0, 1.25, 2.5, 3.75, 5.0])
yedges = np.array([0.0, 1.25, 2.5, 3.75, 5.0])

# ===================
# Part 3: Plot Configuration and Rendering
# ===================

# Construct arrays for the anchor positions of the 16 bars.
xpos, ypos = np.meshgrid(xedges[:-1] + 0.25, yedges[:-1] + 0.25, indexing="ij")
xpos = xpos.ravel()
ypos = ypos.ravel()
zpos = 0

# Construct arrays with the dimensions for the 16 bars.
dx = dy = 0.5 * np.ones_like(zpos)
dz = hist.ravel()

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(projection="3d")

# Create a colormap for the color bar
colors = plt.cm.rainbow(dz / 10)
bar3d = ax.bar3d(xpos, ypos, zpos, dx, dy, dz, zsort="average", color=colors)

# Add color bar which maps values to colors.
sm = plt.cm.ScalarMappable(
    cmap=plt.cm.rainbow, norm=plt.Normalize(vmin=dz.min(), vmax=dz.max())
)
sm.set_array([])
fig.colorbar(sm, ax=ax, shrink=0.5, aspect=10)  # Adjust colorbar position and size

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig("3d_7.pdf", bbox_inches="tight")
