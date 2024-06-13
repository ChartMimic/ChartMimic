# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

from matplotlib import cm

# ===================
# Part 2: Data Preparation
# ===================
# Make data.
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.cos(R)

# Axes Limits and Labels
xlabel_value = "Time"
ylabel_value = "Bus"
zlim_values = [-1.01, 1.01]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw={"projection": "3d"})

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)

# Customize the z axis.
ax.set_zlim(zlim_values)

# A StrMethodFormatter is used automatically
ax.zaxis.set_major_formatter("{x:.02f}")
ax.set_xlabel(xlabel_value)
ax.set_ylabel(ylabel_value)

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=10)

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig("3d_6.pdf", bbox_inches="tight")
