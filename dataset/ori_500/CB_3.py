# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

from matplotlib.lines import Line2D

# ===================
# Part 2: Data Preparation
# ===================
# Fixing random state for reproducibility
# some random data
x = np.random.rand(100)

# linear relationship between x and y
y = 0.5 * x + np.random.rand(100) * 0.3

# add a line on ax
line_x = [0.2, 0.6, 0.7, 0.9, 1.0]
line_y = [0.25, 0.40, 0.50, 0.60, 0.75]
diagonal_line = [[0, 1], [0, 1]]

scatters_name = "Data points"
bin_edges_name = "Bin edges"
calibration_curve_name = "Calibration curve"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Draw the scatter plot and marginals.

# Start with a square Figure.
fig = plt.figure(figsize=(6, 6))
gs = fig.add_gridspec(
    2,
    1,
    height_ratios=(1, 4),
    left=0.1,
    right=0.9,
    bottom=0.1,
    top=0.9,
    wspace=0.0,
    hspace=0.0,
)
# Create the Axes.
ax = fig.add_subplot(gs[1, 0])
ax_histx = fig.add_subplot(gs[0, 0], sharex=ax)

# no labels
ax_histx.tick_params(axis="x", labelbottom=False)

# the scatter plot:
# add different colors to the scatter plot
sc = ax.scatter(x, y, c=x, cmap="autumn", s=50, edgecolor="black", alpha=0.7)

# # add a line on ax
ax.plot(
    line_x,
    line_y,
    color="black",
    linewidth=2,
    marker="o",
    markersize=6,
    label="Calibration curve",
)

# draw a diagonal line
ax.plot(diagonal_line[0], diagonal_line[1], color="black", linestyle="--")

# now determine nice limits by hand:
binwidth = 0.05
xymax = max(np.max(np.abs(x)), np.max(np.abs(y)))
lim = (int(xymax / binwidth) + 1) * binwidth
bins = np.arange(0, lim + binwidth, binwidth)
ax_histx.hist(x, bins=bins, color="#d6a3b3", edgecolor="black")

# remove the y-axis labels
ax_histx.set_yticks([])

# remove the top, left, and right spines
ax_histx.spines["top"].set_visible(False)
ax_histx.spines["left"].set_visible(False)
ax_histx.spines["right"].set_visible(False)

ax.set_xlabel("Predicted probability")
ax.set_ylabel("Fraction of positives")

ax.set_xticks([0.00, 0.25, 0.50, 0.75, 1.00])
ax.set_yticks([0.00, 0.25, 0.50, 0.75, 1.00])
ax.set_xlim(-0.05, 1.05)
ax.set_ylim(-0.05, 1.05)

# draw bin edges
for i in bins:
    ax.axvline(i, color="gray", linewidth=0.5, linestyle="--", zorder=0, alpha=0.5)

# Create an axes on the top side of ax_heatmap_top for the colorbar.
ax_colorbar = fig.add_axes(
    [ax.get_position().width * 1.15, 0.1, 0.05, ax.get_position().y1 * 0.86]
)
cbar = plt.colorbar(sc, cax=ax_colorbar, orientation="vertical")

# Create a Line2D instance for bin edges
bin_edge_line = Line2D([0], [0], color="gray", linewidth=0.5, linestyle="--")

# Create a Line2D instance for calibration curve
calibration_curve_line = Line2D(
    [0],
    [0],
    color="black",
    linewidth=2,
    marker="o",
    markersize=6,
)

# Update legend to include the new Line2D instances
ax.legend(
    handles=[sc, bin_edge_line, calibration_curve_line],
    labels=[scatters_name, bin_edges_name, calibration_curve_name],
    loc="upper left",
)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig("CB_3.pdf", bbox_inches="tight")
