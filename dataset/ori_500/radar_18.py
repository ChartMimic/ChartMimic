# ===================
# Part 1: Importing Libraries
# ===================

import numpy as np; np.random.seed(0)

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# ===================
# Part 2: Data Preparation
# ===================
# Data for Disney and Universal Studios
values_disney = [0.8, 0.7, 0.6, 0.85, 0.9, 0.75, 0.7, 0.65, 0.8, 0.9]
values_universal = [0.6, 0.55, 0.5, 0.45, 0.4, 0.35, 0.3, 0.25, 0.34, 0.55]
labels = [
    "Thrill Rides",
    "Family Rides",
    "Shows",
    "Food Quality",
    "Staff",
    "Cleanliness",
    "Wait Times",
    "Ticket Price",
    "Souvenirs",
    "Parking",
]
num_vars = len(labels)

# Compute angle for each axis
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# The plot is circular, so we need to "complete the loop" and append the start to the end.
values_disney += values_disney[:1]
values_universal += values_universal[:1]
angles += angles[:1]

# Extracted variables
disney_label = "Disney"
universal_label = "Universal Studios"
xticks = angles[:-1]
xticklabels = labels
yticklabels = []
rgrids = [0.2, 0.4, 0.6, 0.8, 1.0]
rgrid_labels = ["0.2", "0.4", "0.6", "0.8", "1.0"]
title_text = "Amusement Park Comparison: Disney vs Universal Studios"
title_size = 18
title_color = "navy"
title_y = 1.1

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Draw the radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
ax.fill(angles, values_disney, color="darkorange", alpha=0.7)
ax.plot(angles, values_disney, color="darkorange", linewidth=2, label=disney_label)
ax.scatter(
    angles[:-1], values_disney[:-1], color="darkorange", s=75, zorder=5, marker="^"
)
ax.fill(angles, values_universal, color="purple", alpha=0.7)
ax.plot(
    angles, values_universal, color="purple", linewidth=2, label=universal_label
)
ax.scatter(
    angles[:-1], values_universal[:-1], color="purple", s=75, zorder=5, marker="o"
)

# Add labels to the plot
ax.set_xticks(xticks)
ax.set_xticklabels(xticklabels, size=13)

# Add grid lines and labels for the concentric circles
ax.set_yticklabels(yticklabels)
ax.set_rgrids(
    rgrids,
    labels=rgrid_labels,
    angle=225,
    color="gray",
    size=12,
)

# Create legend handles manually
legend_elements = [
    Line2D(
        [0],
        [0],
        color="darkorange",
        linewidth=2,
        marker="^",
        markersize=10,
        label=disney_label,
    ),
    Line2D(
        [0],
        [0],
        color="purple",
        linewidth=2,
        marker="o",
        markersize=10,
        label=universal_label,
    ),
]

# Add legend and title
ax.set_title(
    title_text,
    size=title_size,
    color=title_color,
    y=title_y,
)
ax.legend(
    handles=legend_elements,
    loc="lower center",
    bbox_to_anchor=(0.5, -0.2),
    frameon=False,
    ncol=2,
)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save the plot
plt.tight_layout()
plt.savefig('radar_18.pdf', bbox_inches='tight')
