# ===================
# Part 1: Importing Libraries
# ===================

import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)
import matplotlib.colors as mcolors

# ===================
# Part 2: Data Preparation
# ===================
# Sample data to mimic the trends in the provided image

tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
baCE = [95.29, 87.87, 86.27, 86.72, 82.27, 70.4, 72.85, 66.21, 63.02, 61.23]
lwf = [75.43, 76.59, 71.73, 67.03, 65.22, 62.11, 62.82, 54.94, 53.72, 47.44]
ewc = [42.34, 49.74, 48.15, 41.11, 47.92, 34.53, 36.8, 33.88, 36.82, 34.41]
seq = [20.15, 19.82, 18., 16.35, 17.43, 17.38, 17.9, 17.31, 15.17, 14.7]
# Labels and plot types
line_label_baCE = "BaCE"
line_label_lwf = "LWF"
line_label_ewc = "EWC"
line_label_seq = "SEQ"

# Plot configuration
xlim_values = [1, 10]
ylim_values = [0, 100]
xlabel_value = "Task"
ylabel_value = "Average Accuracy (%)"
xticks_values = np.arange(1, 11, 1)
yticks_values = np.arange(0, 101, 10)
xtickslabel_values = None  # Not explicitly set in the code
ytickslabel_values = None  # Not explicitly set in the code
title_value = None  # Not explicitly set in the code
axhiline_values = None  # Not explicitly set in the code
axvline_values = None  # Not explicitly set in the code

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create a figure and axis
plt.figure(figsize=(12, 6))
plt.plot(
    tasks,
    baCE,
    marker="s",
    markersize=10,
    color="#2171b5",
    clip_on=False,
    zorder=10,
    mfc="w",
    mew=2,
    label=line_label_baCE,
    linewidth=2.5,
    linestyle="--",
)
plt.plot(
    tasks,
    lwf,
    marker="v",
    markersize=10,
    color="#6baed6",
    clip_on=False,
    zorder=10,
    mfc="w",
    mew=2,
    label=line_label_lwf,
    linewidth=2.5,
    linestyle="-.",
)
plt.plot(
    tasks,
    ewc,
    marker="D",
    markersize=10,
    color="#42cc46",
    clip_on=False,
    zorder=10,
    mfc="w",
    mew=2,
    label=line_label_ewc,
    linewidth=2.5,
    linestyle=":",
)
plt.plot(
    tasks,
    seq,
    marker="o",
    markersize=10,
    color="#9dfa9f",
    clip_on=False,
    zorder=10,
    mfc="w",
    mew=2,
    label=line_label_seq,
    linewidth=2.5,
)

# Customize the plot with labels, title, and legend
plt.yticks(yticks_values)
plt.ylim(ylim_values)  # Adjusted y-axis limit

# Customize the x-axis ticks
plt.xticks(xticks_values)  # Ticks from 1 to 20, interval of 1
plt.xlim(xlim_values)  # Slightly beyond 1 and 20 for a margin

# Add a grid to the plot
plt.xlabel(xlabel_value, fontsize=16)
plt.ylabel(ylabel_value, fontsize=16)
plt.tick_params(axis="x", which="both", length=0)
# Add a title to the plot
plt.legend(
    frameon=False,
    fontsize=12,
    loc="upper right",
    borderpad=1,
    ncol=4,
    bbox_to_anchor=(1, 1.1),
)

# Add a grid to the plot
plt.grid(True, linestyle="-", linewidth=0.5, axis="y")

# Set the background color of the plot
ax = plt.gca()
ax.set_facecolor(
    mcolors.LinearSegmentedColormap.from_list("custom", ["#e6f7ff", "#ffffff"])(0.8)
)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout for better spacing and display
plt.tight_layout()

# Show the plot
plt.savefig('line_64.pdf', bbox_inches='tight')
