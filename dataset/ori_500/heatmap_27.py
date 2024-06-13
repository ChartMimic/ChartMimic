# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

from matplotlib.colors import LogNorm

# ===================
# Part 2: Data Preparation
# ===================
Z = np.random.rand(6, 10)
titles = ["default: no edges", "thick edges"]
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
fig, (ax0, ax1) = plt.subplots(2, 1, figsize=(6, 4))

# Change the color map to 'plasma' for the first subplot
c = ax0.pcolor(Z, cmap="plasma")
ax0.set_title(titles[0])

# Change the color map to 'plasma' and add thick edges for the second subplot
c = ax1.pcolor(Z, edgecolors="k", linewidths=4, cmap="plasma")
ax1.set_title(titles[1])

# ===================
# Part 4: Saving Output
# ===================
fig.tight_layout()
plt.savefig("heatmap_27.pdf", bbox_inches="tight")
