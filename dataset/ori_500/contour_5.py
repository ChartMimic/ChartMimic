# ===================
# Part 1: Importing Libraries
# ===================
import numpy as np

np.random.seed(0)

import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Data
X, Y = np.meshgrid(np.linspace(-5, 10, 100), np.linspace(-5, 10, 100))
Z = np.sqrt(X**2 + Y**2)

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Filled contour with labels
fig, ax = plt.subplots(figsize=(6, 6))
cnt = ax.contour(X, Y, Z, colors="k", linewidths=0.5)
ax.clabel(cnt, cnt.levels, inline=True, fontsize=10)
ax.contourf(X, Y, Z, cmap='coolwarm')

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig("contour_5.pdf", bbox_inches="tight")
