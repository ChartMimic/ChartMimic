import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Make data
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = 15 * np.outer(np.cos(u), np.sin(v))
y = 20 * np.outer(np.sin(u), np.sin(v))
z = 5 * np.outer(np.ones(np.size(u)), np.cos(v))

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(projection="3d")

# Plot the surface
ax.plot_surface(x, y, z, color="mediumvioletred")

# Set an equal aspect ratio
ax.set_aspect("equal")

ax.set_xticks(np.arange(int(x.min()) - 1, int(x.max()) + 2, 5))
ax.set_yticks(np.arange(int(y.min()) - 1, int(y.max()) + 2, 5))
ax.set_zticks(np.arange(int(z.min()) - 1, int(z.max()) + 2, 5))

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig("3d_11.pdf", bbox_inches="tight")
