# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0); np.random.seed(0)

# ===================
# Part 2: Data Preparation
# ===================
# Data
speed_limits = [30, 40, 50, 60, 70]
Urban_Area = [-5, -7, -6, -8, -9]
Suburban_Area = [-4, -6, -5, -7, -8]
Highway_Area = [-6, -8, -7, -9, -10]
Rural_Area = [-3, -5, -4, -6, -7]

# X-axis positions for each group
x = np.arange(len(speed_limits))

# Labels and Titles
ylabel = "Accident Rate Change (%)"
xlabel = "Speed Limit (mph)"
title = "Impact of Speed Limits on Accident Rates"

# Legend labels
legend_labels = ["Urban Area", "Suburban Area", "Highway Area", "Rural Area"]

# Axis limits
ylim = (-11, 0)
# Axis tick labels
xticks = x
xticklabels = speed_limits

# Bar width
bar_width = 0.2

# Colors
colors = ["#f1c5c1", "#dc7870", "#b9d0e5", "#8ab1d2"]


# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Figure and axis
fig, ax = plt.subplots(figsize=(10, 7))

# Plotting bars
ax.bar(
    x - bar_width * 1.5,
    Urban_Area,
    width=bar_width,
    label=legend_labels[0],
    color=colors[0],
)
ax.bar(
    x - bar_width / 2, Suburban_Area, width=bar_width, label=legend_labels[1], color=colors[1]
)
ax.bar(
    x + bar_width / 2,
    Highway_Area,
    width=bar_width,
    label=legend_labels[2],
    color=colors[2],
)
ax.bar(
    x + bar_width * 1.5,
    Rural_Area,
    width=bar_width,
    label=legend_labels[3],
    color=colors[3],
)

# Adding labels and title
ax.set_ylim(ylim)
ax.set_ylabel(ylabel)
ax.set_xlabel(xlabel)
ax.set_title(title)

# Adding x-axis tick labels
ax.set_xticks(xticks)
ax.set_xticklabels(xticklabels)

plt.tick_params(axis="both", which="both", length=0)

# Adding legend
ax.legend(loc="lower center", bbox_to_anchor=(0.5, -0.15), frameon=False, ncol=4)

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig('bar_45.pdf', bbox_inches='tight')
