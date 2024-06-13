# ===================
# Part 1: Importing Libraries
# ===================

import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)

# ===================
# Part 2: Data Preparation
# ===================
# Data for plotting
imbalance_ratios = ["120", "90", "60", "30", "1", "1/30", "1/60", "1/90", "1/120"]
ours_acc = [75, 80, 85, 90, 95, 90, 85, 84, 83]
acr_acc = [77, 82, 87, 92, 90, 87, 82, 79, 80]

# Variables for plot configuration
ours_label = "Ours"
acr_label = "ACR"
xlim_values = (0, len(imbalance_ratios) - 1)
ylim_values = (75, 95)
xlabel_text = "Imbalance Ratio of Unlabeled Data"
ylabel_text = "Top-1 Acc (%)"
xticks_values = np.arange(len(imbalance_ratios))
yticks_values = [75, 77.5, 80, 82.5, 85, 87.5, 90, 92.5, 95]
xtickslabel_fontsize = 16
ytickslabel_fontsize = 16
title_text = None  # No title in the provided code
axhline_value = None  # No axhline in the provided code
axvline_value = None  # No axvline in the provided code

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plotting the lines
plt.figure(figsize=(9, 6))  # Adjusting figure size
plt.plot(
    imbalance_ratios,
    ours_acc,
    marker="o",
    linestyle="--",
    linewidth=4,
    clip_on=False,
    zorder=10,
    color="#1f77b4",
    markersize=12,
    label=ours_label,
    mec="#4682b4",
    mfc="white",
    mew=4,
)  # Adjusted color and marker size
plt.plot(
    imbalance_ratios,
    acr_acc,
    marker="s",
    linestyle="-.",
    linewidth=4,
    clip_on=False,
    zorder=10,
    color="#2ca02c",
    markersize=12,
    label=acr_label,
    mec="#008b74",
    mfc="white",
    mew=4,
)  # Adjusted color, line style, and marker size

# Adding titles and labels with increased font size
plt.yticks(yticks_values, fontsize=ytickslabel_fontsize)
plt.xticks(xticks_values, fontsize=xtickslabel_fontsize)
plt.ylim(*ylim_values)
plt.xlim(*xlim_values)
plt.xlabel(xlabel_text, fontsize=xtickslabel_fontsize)
plt.ylabel(ylabel_text, fontsize=ytickslabel_fontsize)

# Adding legend with square markers
plt.legend(
    markerscale=1,
    fontsize=16,
    loc="lower center",
    bbox_to_anchor=(0.5, -0.25),
    ncol=2,
    frameon=False,
)

# Changing the background color to #f5f5f5
plt.gca().set_facecolor("#f5f5f5")

# Change the axis colors
ax = plt.gca()
ax.spines["bottom"].set_color("#f5f5f5")
ax.spines["top"].set_color("#f5f5f5")  # Optional: hide or set color
ax.spines["left"].set_color("#f5f5f5")
ax.spines["right"].set_color("#f5f5f5")  # Optional: hide or set color

plt.tick_params(axis="both", which="both", length=0)
# Adding grid
plt.grid(True, color="white")

# ===================
# Part 4: Saving Output
# ===================
# Adjusting layout to add more space on the right
plt.tight_layout()
plt.savefig('line_21.pdf', bbox_inches='tight')
