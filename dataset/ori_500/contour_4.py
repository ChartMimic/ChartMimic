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
x = np.linspace(-5, 10, 100)
y = np.linspace(-5, 10, 100)
X, Y = np.meshgrid(x, y)
Z = np.sqrt(X**2 + Y**2)

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Contour
fig, ax = plt.subplots(figsize=(6, 6))
cnt = ax.contour(X, Y, Z, cmap="winter")
ax.clabel(cnt, cnt.levels, inline=True, fontsize=10)

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig("contour_4.pdf", bbox_inches="tight")
