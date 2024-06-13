# ===================
# Part 1: Importing Libraries
# ===================

import numpy as np; np.random.seed(0)
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Data
categories = [
    "Storage",
    "Material",
    "Labeling",
    "Nutrition",
    "Purity",
    "Allergen",
    "Pollution",
    "Compliance",
    "Recall",
]
values1 = [65, 70, 88, 76, 92, 89, 87, 95, 92]  # MUJI
values2 = [80, 85, 64, 69, 67, 96, 95, 82, 80]  # Nestle

# Number of variables
num_vars = len(categories)

# Compute angle for each category
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# The plot is circular, so we need to "complete the loop" and append the start to the end.
values1 += values1[:1]
values2 += values2[:1]
angles += angles[:1]

# Extracted variables
line_label1 = 'MUJI'
line_label2 = 'Nestle'
xticks_labels = categories
yticks_values = [20, 40, 60, 80]
yticks_labels = []
ylim_values = (0, 100)
title_text = "MUJI vs Nestle in Food Safety"
title_size = 14
title_color = "black"
title_y = 1.1
legend_loc = "lower center"
legend_ncol = 2
legend_bbox_to_anchor = (0.5, -0.2)
legend_fontsize = "small"
legend_frameon = False

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Size of the figure
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Draw one axe per variable and add labels, aligned vertically
plt.xticks(angles[:-1], xticks_labels, color="black", size=10, ha="center")

# Draw ylabels
ax.set_rlabel_position(0)
plt.yticks(yticks_values, yticks_labels, color="grey", size=7)
plt.ylim(ylim_values)

# Plot data with markers and new colors
ax.plot(
    angles,
    values2,
    linewidth=1,
    linestyle="solid",
    marker="o",
    label=line_label2,
    color="#ff6347",
)
ax.fill(angles, values2, "#ff6347", alpha=0.2)

ax.plot(
    angles,
    values1,
    linewidth=1,
    linestyle="solid",
    marker="s",
    label=line_label1,
    color="#556b2f",
)
ax.fill(angles, values1, "#556b2f", alpha=0.2)

# Add a title to the radar chart
plt.title(title_text, size=title_size, color=title_color, y=title_y)

# Add legend
plt.legend(
    loc=legend_loc,
    ncol=legend_ncol,
    bbox_to_anchor=legend_bbox_to_anchor,
    fontsize=legend_fontsize,
    frameon=legend_frameon,
)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save the plot
plt.tight_layout()
plt.savefig('radar_15.pdf', bbox_inches='tight')
