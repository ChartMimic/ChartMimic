# ===================
# Part 1: Importing Libraries
# ===================

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# ===================
# Part 2: Data Preparation
# ===================
# Data for DE plot
de_x = [0.88, 0.82, 0.92, 0.72, 0.96]
de_y = [0.096, 0.096, 0.105, 0.125, 0.095]
de_colors = ["#a0cf63", "#a0cf63", "#56bcba", "#e69c55", "#c43932"]
de_labels = ["iTrm-All", "iTrm-En", "PatchTST", "TiDE", "TimeXer"]

# Data for PJM plot
pjm_x = [0.88, 0.62, 0.86, 0.89, 0.92]
pjm_y = [0.48, 0.48, 0.46, 0.58, 0.44]
pjm_colors = ["#a0cf63", "#a0cf63", "#56bcba", "#e69c55", "#c43932"]
pjm_labels = ["iTrm-All", "iTrm-En", "PatchTST", "TiDE", "TimeXer"]

# Extracted variables for plot configuration
de_title = "DE"
de_xlabel = "CKA Similarity"
de_ylabel = "MSE"
de_xlim = (0.6, 1.1)
de_xticks = [0.6, 0.7, 0.8, 0.9, 1.0, 1.1]
de_ylim = (0.09, 0.13)
de_yticks = [0.09, 0.10, 0.11, 0.12, 0.13]

pjm_title = "PJM"
pjm_xlabel = "CKA Similarity"
pjm_ylabel = "MSE"
pjm_xlim = (0.5, 1.0)
pjm_xticks = [0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
pjm_ylim = (0.40, 0.60)
pjm_yticks = [0.40, 0.45, 0.50, 0.55, 0.60]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create figure and axes
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(7, 10))

# DE plot
for x, y, color, label in zip(de_x, de_y, de_colors, de_labels):
    if label == "iTrm-All":
        ax1.scatter(
            x, y, label=label, facecolors="none", edgecolors=color, s=200, linewidths=4
        )
    else:
        ax1.scatter(x, y, label=label, color=color, s=200)  # Increase marker size
ax1.set_title(de_title)
ax1.set_xlabel(de_xlabel)
ax1.set_ylabel(de_ylabel)
ax1.set_xlim(de_xlim)  # Adjust x-axis range
ax1.set_xticks(de_xticks)
ax1.set_ylim(de_ylim)  # Adjust y-axis range
ax1.set_yticks(de_yticks)
ax1.grid(True, linestyle="--", linewidth=0.5, color="black")  # Add grid

# PJM plot
for x, y, color, label in zip(pjm_x, pjm_y, pjm_colors, pjm_labels):
    if label == "iTrm-All":
        ax2.scatter(
            x, y, label=label, facecolors="none", edgecolors=color, s=200, linewidths=4
        )
    else:
        ax2.scatter(x, y, label=label, color=color, s=200)  # Increase marker size
ax2.set_title(pjm_title)
ax2.set_xlabel(pjm_xlabel)
ax2.set_ylabel(pjm_ylabel)
ax2.set_xlim(pjm_xlim)  # Adjust x-axis range
ax2.set_xticks(pjm_xticks)
ax2.set_ylim(pjm_ylim)  # Adjust y-axis range
ax2.set_yticks(pjm_yticks)
ax2.grid(True, linestyle="--", linewidth=0.5, color="black")  # Add grid

legend_elements = [
    Line2D(
        [0],
        [0],
        marker="o",
        color="w",
        label="iTrm-All",
        markersize=10,
        markerfacecolor="none",
        markeredgewidth=4,
        markeredgecolor="#a0cf63",
    ),
    Line2D(
        [0],
        [0],
        marker="o",
        color="w",
        label="iTrm-En",
        markersize=10,
        markerfacecolor="#a0cf63",
    ),
    Line2D(
        [0],
        [0],
        marker="o",
        color="w",
        label="PatchTST",
        markersize=10,
        markerfacecolor="#56bcba",
    ),
    Line2D(
        [0],
        [0],
        marker="o",
        color="w",
        label="TiDE",
        markersize=10,
        markerfacecolor="#e69c55",
    ),
    Line2D(
        [0],
        [0],
        marker="o",
        color="w",
        label="TimeXer",
        markersize=10,
        markerfacecolor="#c43932",
    ),
]

# Create the legend using the custom handles
fig.legend(
    handles=legend_elements,
    loc="lower center",
    ncol=5,
    borderaxespad=0.05,
    frameon=False,
)

# Adjust the layout to make room for the legend
plt.subplots_adjust(bottom=0.1)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save plot
plt.tight_layout()
plt.savefig('scatters_9.pdf', bbox_inches='tight')
