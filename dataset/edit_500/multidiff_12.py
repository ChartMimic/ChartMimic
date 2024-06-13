import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Set the figure size and create a gridspec with different widths

import numpy as np
import matplotlib.pyplot as plt

# Categories for different investment strategies
categories = ["Growth Investing", "Value Investing"]
strategy1_acc = [0.68, 0.75]
strategy2_acc = [0.72, 0.78]
strategy1_bottom = [0.15, 0.22]
strategy2_bottom = [0.18, 0.25]

# Data for line plot representing performance under different market conditions
angles = np.arange(0, 181, 15)
strategy1_growth = [
    0.65, 0.62, 0.60, 0.58, 0.56, 0.57, 0.60, 0.63, 0.66, 0.69, 0.68, 0.70, 0.72
]
strategy1_value = [
    0.70, 0.68, 0.65, 0.63, 0.62, 0.61, 0.63, 0.66, 0.69, 0.72, 0.74, 0.77, 0.79
]
strategy2_growth = [
    0.68, 0.66, 0.64, 0.62, 0.61, 0.60, 0.62, 0.65, 0.67, 0.70, 0.72, 0.74, 0.76
]
strategy2_value = [
    0.75, 0.73, 0.71, 0.69, 0.68, 0.67, 0.68, 0.71, 0.73, 0.76, 0.78, 0.80, 0.82
]

titles = ["(A) Strategy 1", "(B) Strategy 2", "(C) Performance in Different Market Conditions"]
ax1ylabel = "Performance Index"
ax3labels = ["Strategy 1 Growth", "Strategy 2 Growth", "Strategy 1 Value", "Strategy 2 Value"]
ax3xlabel = "Market Conditions Severity (°)"
ax3xticks = [0, 90, 180]
ax3vlines = [0, 90, 180]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Bar plot for VGG 16
plt.figure(figsize=(10, 4))
gs = gridspec.GridSpec(1, 3, width_ratios=[1, 1, 2])

ax1 = plt.subplot(gs[0])
ax1.bar(categories, strategy1_acc, color=["#c99796", "#f8d48b"])
ax1.bar(categories, strategy1_bottom, color=["#983530", "#f2a93c"])
ax1.set_title(titles[0])
ax1.set_ylabel(ax1ylabel)
ax1.set_ylim(0, 1)
for i, v in enumerate(strategy1_acc):
    ax1.text(i, v - 0.045, str(v), color="black", ha="center")
for i, v in enumerate(strategy1_bottom):
    ax1.text(i, v - 0.045, str(v), color="black", ha="center")

# Bar plot for Resnet 101
ax2 = plt.subplot(gs[1])
ax2.bar(categories, strategy2_acc, color=["#a4b4eb", "#d9e1ed"])
ax2.bar(categories, strategy2_bottom, color=["#4a68da", "#b4c4dc"])
ax2.set_title(titles[1])
ax2.set_ylim(0, 1)
for i, v in enumerate(strategy2_acc):
    ax2.text(i, v - 0.045, str(v), color="black", ha="center")
for i, v in enumerate(strategy2_bottom):
    ax2.text(i, v - 0.045, str(v), color="black", ha="center")

# Remove y-axis labels for the second plot
ax2.set_yticklabels([])

# Line plot for rotation invariance - with double the width
ax3 = plt.subplot(gs[2])
ax3.plot(
    angles,
    strategy1_growth,
    "r-x",
    label=ax3labels[0],
    color="#983530",
    markersize=4,
)
ax3.plot(
    angles,
    strategy2_growth,
    "b-o",
    label=ax3labels[1],
    color="#4a68da",
    markersize=4,
)
ax3.plot(
    angles,
    strategy1_value,
    "y-x",
    label=ax3labels[2],
    color="#f2a93c",
    markersize=4,
)
ax3.plot(
    angles,
    strategy2_value,
    "c-o",
    label=ax3labels[3],
    color="#b4c4dc",
    markersize=4,
)
ax3.set_title(titles[2])
ax3.set_xlabel(ax3xlabel)
ax3.set_xticks(ax3xticks)
ax3.legend(loc="upper right", bbox_to_anchor=(0.95, 1.0), fontsize=6, frameon=False)
ax3.vlines(ax3vlines, 0, 1, colors="k", linestyles="dashed", linewidth=0.5)
ax3.set_yticklabels([])

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and show plot
plt.tight_layout()
plt.savefig('multidiff_12.pdf', bbox_inches='tight')
