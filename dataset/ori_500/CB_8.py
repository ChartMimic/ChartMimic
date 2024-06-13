# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

import matplotlib.gridspec as gridspec

# ===================
# Part 2: Data Preparation
# ===================
# Sample data
x = np.random.rand(1000)
y = np.random.rand(1000)
xlabel = "TMScore"
ylabel = "Sequence ID"
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create figure and gridspec
fig = plt.figure(figsize=(8, 8))
gs = gridspec.GridSpec(2, 2, width_ratios=[5, 1], height_ratios=[1, 5])

# Main hexbin plot
ax = plt.subplot(gs[1, 0])
ax.hexbin(x, y, gridsize=25, cmap="Blues", mincnt=1)
ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)
ax.set_xlim(0.2, 1.0)
ax.set_ylim(0, 0.6)
ax.axhline(0.5, color="gray", linestyle="--", linewidth=1)
ax.axvline(0.5, color="gray", linestyle="--", linewidth=1)

# Histogram on the top
ax_histx = plt.subplot(gs[0, 0], sharex=ax)
ax_histx.hist(x, bins=25, color="white", edgecolor="#3b76af", linewidth=2)
ax_histx.axis("off")  # Hide axis

# Histogram on the right
ax_histy = plt.subplot(gs[1, 1], sharey=ax)
ax_histy.hist(
    y,
    bins=25,
    orientation="horizontal",
    color="white",
    edgecolor="#3b76af",
    linewidth=2,
)
ax_histy.axis("off")  # Hide axis

# ===================
# Part 4: Saving Output
# ===================
# Adjust the layout and save the figure
plt.tight_layout()
plt.savefig("CB_8.pdf", bbox_inches="tight")
