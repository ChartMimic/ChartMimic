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
    "Sillage",
    "Longevity",
    "Creativity",
    "Versatility",
    "Projection",
    "Value",
    "Popularity",
    "Packaging",
]
values1 = [8, 6, 7, 5, 6, 7, 8, 9]  # Values for Chanel
values2 = [7, 7.5, 8, 6, 7, 5, 8.5, 7]  # Values for Dior
values3 = [5, 7, 6.5, 8, 7, 6, 7, 7.5]  # Values for Gucci

# Number of variables
N = len(categories)

# Compute angle for each category
angles = [n / float(N) * 2 * pi for n in range(N)]
values1 += values1[:1]
values2 += values2[:1]
values3 += values3[:1]
angles += angles[:1]

# Extracted variables
xticks = angles[:-1]
xtickslabel = categories
yticks = [1, 3, 5, 7, 9]
ytickslabel = ["1", "3", "5", "7", "9"]
ylim = (0, 10)
line_label1 = "Chanel"
line_label2 = "Dior"
line_label3 = "Gucci"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Initialize the spider plot
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

# Draw one axe per variable and add labels
plt.xticks(xticks, xtickslabel, color="navy", size=8)
ax.tick_params(pad=15)  # Adjust the distance of the label from the axis

# Draw ylabels
ax.set_rlabel_position(30)
plt.yticks(yticks, ytickslabel, color="darkblue", size=7)
plt.ylim(ylim)

# Plot data
ax.plot(angles, values1, linewidth=2, linestyle="dashed", label=line_label1, color="gold")
ax.fill(angles, values1, color="yellow", alpha=0.25)

ax.plot(angles, values2, linewidth=2, linestyle="dashed", label=line_label2, color="silver")
ax.fill(angles, values2, color="lightgrey", alpha=0.25)

ax.plot(angles, values3, linewidth=2, linestyle="solid", label=line_label3, color="green")
ax.fill(angles, values3, color="lightgreen", alpha=0.25)

# Add legend
plt.legend(loc="upper right", bbox_to_anchor=(1.2, 1.2), ncol=3, frameon=False)

# Set the background color inside the radar chart to white
ax.set_facecolor("white")

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout for better fit
plt.tight_layout()

plt.savefig('radar_19.pdf', bbox_inches='tight')
