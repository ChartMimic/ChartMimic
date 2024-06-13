# ===================
# Part 1: Importing Libraries
# ===================

import numpy as np; np.random.seed(0)

import matplotlib.pyplot as plt
from math import pi

# ===================
# Part 2: Data Preparation
# ===================
# Define the data for the radar chart
categories = [
    "Memory",
    "Understanding",
    "Interference",
    "Questioning",
    "Reasoning",
    "Reflection",
    "Paraphrasing",
]
values1 = [6, 5, 4, 3, 4, 5, 7.3]  # Values for Yi-6B
values2 = [8.8, 7, 3.4, 7.6, 6, 8, 9.4]  # Values for Yi-34B

# Number of variables
N = len(categories)

# Compute angle for each category
angles = [n / float(N) * 2 * pi for n in range(N)]
values1 += values1[:1]
values2 += values2[:1]
angles += angles[:1]

# Extracted variables
line_label1 = "Yi-6B"
line_label2 = "Yi-34B"
xticks = angles[:-1]
xtickslabel = categories
yticks = [0, 2, 4, 6, 8, 10]
ytickslabel = ["0", "2", "4", "6", "8", "10"]
ylim = (0, 10)
legend_loc = "lower center"
legend_bbox_to_anchor = (0.5, 1.2)
legend_ncol = 2
legend_frameon = False

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Initialize the spider plot
fig, ax = plt.subplots(figsize=(4, 4), subplot_kw=dict(polar=True))

# Draw one axe per variable and add labels with increased padding
plt.xticks(xticks, xtickslabel, color="black", size=10)
ax.tick_params(pad=20)  # Increase the distance of the label from the axis

# Draw ylabels
ax.set_rlabel_position(0)
plt.yticks(yticks, ytickslabel, color="black", size=7)
plt.ylim(ylim)

# Plot data
ax.plot(angles, values1, linewidth=1, linestyle="solid", label=line_label1, color="#4ca730")
ax.fill(angles, values1, "green", alpha=0.2)

ax.plot(
    angles, values2, linewidth=1, linestyle="solid", label=line_label2, color="#81cbac"
)
ax.fill(angles, values2, "lightgreen", alpha=0.2)

# Add legend
plt.legend(loc=legend_loc, bbox_to_anchor=legend_bbox_to_anchor, ncol=legend_ncol, frameon=legend_frameon)

# Set the background color inside the radar chart to white
ax.set_facecolor("white")

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout for better fit
plt.tight_layout()

# Show the plot
plt.savefig('radar_11.pdf', bbox_inches='tight')
