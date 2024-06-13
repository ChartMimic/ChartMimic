# ===================
# Part 1: Importing Libraries
# ===================

import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)

# ===================
# Part 2: Data Preparation
# ===================
weeks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
performance_data = [0.65, 0.64, 0.72, 0.83, 0.85, 0.73, 0.84, 0.79, 0.79, 0.79, 0.75, 0.78, 0.69, 0.61, 0.56, 0.5, 0.5, 0.36, 0.33, 0.23, 0.11, 0.25, 0.25, 0.16, 0.33, 0.16, 0.27, 0.3]
efficiency_data = [0.87, 0.85, 0.76, 0.73, 0.62, 0.51, 0.53, 0.5, 0.49, 0.44, 0.3, 0.26, 0.19, 0.15, 0.12, 0.3, 0.18, 0.21, 0.2, 0.34, 0.27, 0.4, 0.42, 0.55, 0.56, 0.58, 0.69, 0.75]
growth_data = [0.0, 0.27, 0.36, 0.48, 0.55, 0.63, 0.66, 0.66, 0.8, 0.81, 0.78, 0.92, 0.88, 0.95, 1.0, 1.0, 1.0, 0.98, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]

# Extracted variables
xlabel = "Weeks"
ylabel_performance = "Performance"
ylabel_efficiency = "Efficiency"
xlim = (0, 30)
ylim = (0, 1.2)
title = "Detailed Performance and Efficiency Analysis Over Weeks"
line_label_performance = "Performance"
line_label_efficiency = "Efficiency"
line_label_growth = "Growth"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create a figure and axis
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot the performance data on the primary y-axis
color = "tab:blue"
ax1.set_xlabel(xlabel)
ax1.set_ylabel(ylabel_performance, color=color)
(line1,) = ax1.plot(
    weeks,
    performance_data,
    color=color,
    marker="o",
    linestyle="-",
    clip_on=False,
    zorder=10,
    linewidth=2,
    label=line_label_performance,
)
ax1.tick_params(axis="y", labelcolor=color)
ax1.set_ylim(ylim)

# Create a secondary y-axis for the efficiency data
ax2 = ax1.twinx()
color = "tab:red"
ax2.set_ylabel(ylabel_efficiency, color=color)
(line2,) = ax2.plot(
    weeks,
    efficiency_data,
    color=color,
    marker="x",
    linestyle="--",
    clip_on=False,
    zorder=10,
    linewidth=2,
    label=line_label_efficiency,
)
ax2.tick_params(axis="y", labelcolor=color)
ax2.set_ylim(ylim)

# Add a legend to the plot
color = "tab:green"
(line3,) = ax1.plot(
    weeks,
    growth_data,
    color=color,
    marker="^",
    linestyle=":",
    linewidth=2,
    clip_on=False,
    zorder=10,
    label=line_label_growth,
)
# ax1.legend(loc='upper left')

# Customize the plot with a title, grid, and background color
fig.patch.set_facecolor("#f4f4f4")
ax1.set_facecolor("#e5f5f9")
ax2.set_facecolor("#f9e5e6")
ax1.set_xlim(xlim)
ax1.tick_params(axis="both", which="both", length=0)
ax2.tick_params(axis="both", which="both", length=0)
lines = [line1, line2, line3]
labels = [line.get_label() for line in lines]
fig.legend(
    lines, labels, loc="upper center", bbox_to_anchor=(0.5, 0.95), ncol=3, frameon=False
)
# Set the title and display the plot
plt.title(title, y=1.05)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout for better spacing and display
plt.tight_layout()
plt.savefig('line_62.pdf', bbox_inches='tight')
