# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Sample data for demonstration purposes
accuracy = [
    np.random.normal(0.88, 0.04, 100),
    np.random.normal(0.87, 0.05, 100),
    np.random.normal(0.83, 0.03, 100),
]
error = [
    np.random.normal(7.26, 1.5, 100),
    np.random.normal(9.27, 2, 100),
    np.random.normal(9.48, 2.5, 100),
]

titles = ["Region Classification Accuracy", "Slice Mean Error (ms)"]
xticklabels = ["DENSE (ref)", "Joint Multimodal\nFramework\n (ours)", "Cine"]
ylabels = ["LMA Region Classification Accuracy", "Slice Mean Error (ms)"]
yticks = [np.arange(0.6, 1.1, 0.1), np.arange(2.5, 22.6, 2.5)]
ylims = [[0.5, 1], [2.4, 22.6]]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create figure and subplots with specified figure size
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
medianprops = dict(linestyle="-", linewidth=1, color="black")
# Left subplot - Region Classification Accuracy
bplot1 = ax1.boxplot(
    accuracy,
    patch_artist=True,
    showfliers=True,
    widths=0.6,
    medianprops=medianprops,
    flierprops=dict(marker="D", color="black", markerfacecolor="black", markersize=5),
)
ax1.set_title(titles[0])
ax1.set_xticklabels(xticklabels)
ax1.set_ylabel(ylabels[0])
ax1.set_yticks(yticks[0])
ax1.set_ylim(ylims[0])
ax1.set_facecolor("#eaeaf2")
ax1.yaxis.grid(True, color="white")

# Add median value annotations
for i, line in enumerate(bplot1["medians"]):
    x, y = line.get_xydata()[1]
    ax1.text(x - 0.3, y, f"{y:.2f}", horizontalalignment="center", color="black")

# Right subplot - Slice Mean Error
bplot2 = ax2.boxplot(
    error,
    patch_artist=True,
    showfliers=True,
    widths=0.6,
    medianprops=medianprops,
    flierprops=dict(marker="D", color="black", markerfacecolor="black", markersize=5),
)
ax2.set_title(titles[1])
ax2.set_xticklabels(xticklabels)
ax2.set_ylabel(ylabels[1])
ax2.set_yticks(yticks[1])
ax2.set_ylim(ylims[1])
ax2.set_facecolor("#eaeaf2")
ax2.yaxis.grid(True, color="white")

# Add median value annotations
for i, line in enumerate(bplot2["medians"]):
    x, y = line.get_xydata()[1]
    ax2.text(x - 0.3, y, f"{y:.2f}", horizontalalignment="center", color="black")

# Set colors for boxplots
colors = ["#5e74a0", "#c38c6a", "#6e9d72"]
for bplot in (bplot1, bplot2):
    for patch, color in zip(bplot["boxes"], colors):
        patch.set_facecolor(color)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout to prevent overlap
plt.tight_layout()
plt.savefig("box_14.pdf", bbox_inches="tight")
