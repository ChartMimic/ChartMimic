# ===================
# Part 1: Importing Libraries
# ===================

import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# New example data for the double layer donut chart
vals1 = [250, 150, 100, 300]
vals2 = [200, 100, 150, 250]
vals3 = [700]  # This will be the white center

# Define labels and colors
labels = ["E-commerce", "Education", "Entertainment", "Technology"]
colors1 = ["#FFD700", "#FF8C00", "#1E90FF", "#32CD32"]
colors2 = ["#F0E68C", "#FFA07A", "#87CEFA", "#98FB98"]

# Variables for plot configuration
title_text = "Market Share by Sector - External vs. Internal"
legend_labels = labels
legend_bbox_to_anchor = (1, 1)
legend_frameon = False

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
fig, ax = plt.subplots(figsize=(8, 6))

# Outer donut chart
wedges1, texts1, autotexts1 = ax.pie(
    vals1,
    labels=labels,
    radius=1.2,
    colors=colors1,
    autopct="%1.1f%%",
    pctdistance=0.9,
    wedgeprops=dict(width=0.3, edgecolor="w"),
)

# Inner donut chart
wedges2, texts2, autotexts2 = ax.pie(
    vals2,
    radius=0.9,
    colors=colors2,
    autopct="%1.1f%%",
    pctdistance=0.75,
    wedgeprops=dict(width=0.3, edgecolor="w"),
)

# White center circle for the 'hole'
ax.pie(vals3, radius=0.6, colors="w", wedgeprops=dict(width=0.3, edgecolor="w"))

# Equal aspect ratio ensures that pie chart is drawn as a circle
ax.axis("equal")

# Title for the donut chart
ax.set_title(title_text)

# Show the plot with a legend
plt.legend(legend_labels, bbox_to_anchor=legend_bbox_to_anchor, frameon=legend_frameon)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig('pie_15.pdf', bbox_inches='tight')
