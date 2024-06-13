# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)

from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize

# ===================
# Part 2: Data Preparation
# ===================
heatmap_top_data = np.random.rand(12, 12) * 1.5 - 0.7
heatmap_bottom_data = np.random.rand(12, 12) * 1.5 - 0.7
bar_data_top = heatmap_top_data.mean(axis=0)
bar_data_bottom = heatmap_bottom_data.mean(axis=0)

# Attributes for y-axis
attributes = [
    "PaleSkin",
    "OvalFace",
    "Smiling",
    "BrownHair",
    "Attractive",
    "Male",
    "BigLips",
    "PointyNose",
    "White",
    "BigNose",
    "NoBeard",
    "HeavyMakeup",
]
heatmap_xlabel="sensitive attribute"
bar_xlabel="$I_{\infty}$(Y,Z)"
bar_xticks=[-0.5, 0, 0.5]
bar_xlim=[-0.5, 0.5]

# Normalize the bar data to match heatmap's vmin and vmax
norm = Normalize(vmin=-0.5, vmax=1.0)
cmap = plt.get_cmap("coolwarm")

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create figure and axes
fig = plt.figure(figsize=(8, 8))

# Heatmap top
ax_heatmap_top = fig.add_subplot(2, 2, 1)
cax_top = ax_heatmap_top.imshow(
    heatmap_top_data, cmap=cmap, aspect="auto", vmin=-0.5, vmax=1.5
)
ax_heatmap_top.set_yticks(np.arange(len(attributes)))
ax_heatmap_top.set_yticklabels(attributes)
ax_heatmap_top.set_xticks([])

# Create an axes on the top side of ax_heatmap_top for the colorbar.
ax_colorbar = fig.add_axes(
    [
        ax_heatmap_top.get_position().x0 + 0.05,
        ax_heatmap_top.get_position().y1 + 0.15,
        ax_heatmap_top.get_position().width,
        0.02,
    ]
)
ax_colorbar.xaxis.set_ticks_position("top")
ax_colorbar.xaxis.set_label_position("top")

# Adding a colorbar at the very top of the heatmap
plt.colorbar(cax_top, cax=ax_colorbar, orientation="horizontal")

# Heatmap bottom
ax_heatmap_bottom = fig.add_subplot(2, 2, 3)
cax_bottom = ax_heatmap_bottom.imshow(
    heatmap_bottom_data, cmap=cmap, aspect="auto", vmin=-0.5, vmax=1.5
)
ax_heatmap_bottom.set_yticks(np.arange(len(attributes)))
ax_heatmap_bottom.set_yticklabels(attributes)
ax_heatmap_bottom.set_xticks(np.arange(len(attributes)))
ax_heatmap_bottom.set_xticklabels(attributes, rotation=45, ha="right")
ax_heatmap_bottom.set_xlabel(heatmap_xlabel)

# Bar plot top
ax_bar_top = fig.add_subplot(2, 2, 2)
colors_top = [cmap(norm(value)) for value in bar_data_top]
ax_bar_top.barh(np.arange(len(attributes)), bar_data_top, color=colors_top)
ax_bar_top.set_yticks([])
ax_bar_top.set_xticks([])
ax_bar_top.set_xlim(bar_xlim)
ax_bar_top.set_ylim(ax_heatmap_top.get_ylim())

# Bar plot bottom
ax_bar_bottom = fig.add_subplot(2, 2, 4)
colors_bottom = [cmap(norm(value)) for value in bar_data_bottom]
ax_bar_bottom.barh(np.arange(len(attributes)), bar_data_bottom, color=colors_bottom)
ax_bar_bottom.set_yticks([])
ax_bar_bottom.set_xticks(bar_xticks)
ax_bar_bottom.set_xlim(bar_xlim)
ax_bar_bottom.set_xlabel(bar_xlabel)
ax_bar_bottom.set_ylim(ax_heatmap_bottom.get_ylim())

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save plot
plt.tight_layout()  # leave some space at the top for the colorbar
plt.savefig('multidiff_13.pdf', bbox_inches='tight')
