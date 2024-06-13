# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data
models = [
    "AR",
    "LSTMADalpha",
    "LSTMADbeta",
    "AE",
    "EncDecAD",
    "SRCNN",
    "AnomalyTransformer",
    "TimesNet",
    "Donut",
    "TFAD",
][::-1]
scores = [
    np.random.uniform(-10, 10, 10) for _ in models * 2
]  # Placeholder for actual scores
scores = [(score - np.min(score)) / (np.max(score) - np.min(score)) for score in scores]

xlabels = ["one by one", "all in one"]
ylims = [[0, 11], [0, 11]]
xlims = [[-0.05, 1.05], [-0.05, 1.05]]

yticks = [range(1, len(models) + 1), range(1, len(models) + 1)]


# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Figure and Axes
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5), sharey=True)
medianprops = dict(linestyle="-", linewidth=1, color="black")
colors = [
    "#b0525d",
    "#cc7760",
    "#dca174",
    "#e8cc94",
    "#f3ebb8",
    "#edf1bd",
    "#d2e2ac",
    "#a9ccac",
    "#77aaa2",
    "#557fa7",
][::-1]
backcolors = ["#f3d2c9", "#fefae6", "#d3e8e5", "#c7d9e8"][::-1]

# Subplot 1: one by one
bplot1 = ax1.boxplot(
    scores[:10], vert=False, medianprops=medianprops, patch_artist=True
)
ax1.set_ylim(ylims[0])
ax1.set_yticks(yticks[0])
ax1.set_yticklabels(models)
ax1.set_xlim(xlims[0])
ax1.set_xlabel(xlabels[0])
ax1.set_facecolor("#FFF7E6")
ax1.xaxis.grid(True)
ax1.set_axisbelow(True)

for patch, color in zip(bplot1["boxes"], colors):
    patch.set_facecolor(color)

# Set background colors
ax1.add_patch(
    plt.Rectangle(
        (-0.05, 0.5), 1.1, 1.5, facecolor=backcolors[0], edgecolor="none", zorder=0
    )
)
ax1.add_patch(
    plt.Rectangle(
        (-0.05, 1.5), 1.1, 1.5, facecolor=backcolors[1], edgecolor="none", zorder=0
    )
)
ax1.add_patch(
    plt.Rectangle(
        (-0.05, 2.5), 1.1, 5.5, facecolor=backcolors[2], edgecolor="none", zorder=0
    )
)
ax1.add_patch(
    plt.Rectangle(
        (-0.05, 7.5), 1.1, 3, facecolor=backcolors[3], edgecolor="none", zorder=0
    )
)

# Subplot 2: all in one
bplot2 = ax2.boxplot(
    scores[10:], vert=False, medianprops=medianprops, patch_artist=True
)
ax2.set_ylim(ylims[1])
ax2.set_yticks(yticks[1])
ax2.set_yticklabels(models)
ax2.set_xlim(xlims[1])
ax2.set_xlabel(xlabels[1])
ax2.set_facecolor("#FFF7E6")
ax2.xaxis.grid(True)
ax2.set_axisbelow(True)

for patch, color in zip(bplot2["boxes"], colors):
    patch.set_facecolor(color)

# Set background colors
ax2.add_patch(
    plt.Rectangle(
        (-0.05, 0.5), 1.1, 1.5, facecolor=backcolors[0], edgecolor="none", zorder=0
    )
)
ax2.add_patch(
    plt.Rectangle(
        (-0.05, 1.5), 1.1, 1.5, facecolor=backcolors[1], edgecolor="none", zorder=0
    )
)
ax2.add_patch(
    plt.Rectangle(
        (-0.05, 2.5), 1.1, 5.5, facecolor=backcolors[2], edgecolor="none", zorder=0
    )
)
ax2.add_patch(
    plt.Rectangle(
        (-0.05, 7.5), 1.1, 3, facecolor=backcolors[3], edgecolor="none", zorder=0
    )
)

# Gradient background
for ax in [ax1, ax2]:
    ax.set_facecolor("white")

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save the figure
plt.tight_layout()
plt.savefig("box_18.pdf", bbox_inches="tight")
