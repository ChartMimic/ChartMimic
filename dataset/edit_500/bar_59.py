# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)

import matplotlib.colors as mcolors

# ===================
# Part 2: Data Preparation
# ===================
# Set the seed for reproducibility

# Data
categories = [
    "Speed Limit Compliance",
    "Fuel Efficiency",
    "Lane Discipline",
    "Traffic Signal Obedience",
    "Parking Efficiency",
    "Carpool Participation",
    "Accident Response Time",
]
differences = [ 42 ,49 , 24  , 7, -30 ,57 ,-22]
title = "Relative Difference in Autonomous vs. Human Driving Focus on Performance Metrics"
xlabel = "Difference (%)"
ylabel = "Performance Metric"
xlim = [-80, 80]
xticks = range(-80, 81, 20)
cbarlabels = ["Negative Differences", "Positive Differences"]
colors = [
    (
        plt.cm.Reds(np.array(i) / min(differences))
        if i < 0
        else plt.cm.Greens(np.array(i) / max(differences))
    )
    for i in differences
]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create figure and plot
fig, ax = plt.subplots(figsize=(10, 5))
ax.barh(categories, differences, color=colors)

# Set title and labels
ax.set_title(title)
ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)

# Set x-axis limits and labels
ax.set_xlim(xlim)
ax.set_xticks(xticks)
ax.xaxis.grid(True)

# Create colorbars
cbar1 = plt.colorbar(
    plt.cm.ScalarMappable(norm=mcolors.Normalize(0, 80), cmap="Reds"),
    ax=ax,
    orientation="vertical",
    pad=0.01,
    aspect=20,
)
cbar2 = plt.colorbar(
    plt.cm.ScalarMappable(norm=mcolors.Normalize(0, 80), cmap="Greens"),
    ax=ax,
    orientation="vertical",
    pad=0.01,
    aspect=20,
)
cbar1.set_label(cbarlabels[0])
cbar2.set_label(cbarlabels[1])

# ===================
# Part 4: Saving Output
# ===================
# Show plot with tight layout
plt.tight_layout()

# Save the figure
plt.savefig('bar_59.pdf', bbox_inches='tight')
