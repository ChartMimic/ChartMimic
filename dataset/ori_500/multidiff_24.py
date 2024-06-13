# ===================
# Part 1: Importing Libraries
# ===================
import numpy as np; np.random.seed(0)

import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from matplotlib.lines import Line2D

# ===================
# Part 2: Data Preparation
# ===================
# Create a figure and a GridSpec layout
fig = plt.figure(figsize=(10, 5))
gs = GridSpec(1, 2, figure=fig)

# ------- Pie Chart Data for Arts Education Programs -------
categories = ["Performing Arts", "Visual Arts", "Music", "Dance", "Literature"]
sizes = [30, 25, 20, 15, 10]  # Percentages of each program
colors = ["#ff9999", "#66b3ff", "#99ff99", "#ffcc99", "#c2c2f0"]
explode = (0.1, 0, 0, 0, 0)  # Highlight Performing Arts

# ------- Radar Chart Data for Student Performance in Arts Education -------
labels = np.array(
    ["Creativity", "Technique", "Expression", "Collaboration", "Dedication"]
)
num_vars = len(labels)
values = np.array([0.9, 0.85, 0.75, 0.80, 0.90])
values = np.concatenate((values, [values[0]]))
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

title_1 = "Distribution of Arts Education Programs"
title_2 = "Student Performance in Arts Education"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create the pie chart in the left panel
ax1 = fig.add_subplot(gs[0, 0])
wedges, texts, autotexts = ax1.pie(
    sizes,
    labels=categories,
    colors=colors,
    autopct="%1.1f%%",
    startangle=140,
    explode=explode,
)
ax1.set_title(title_1)
ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

# Create the radar chart in the right panel
ax2 = fig.add_subplot(gs[0, 1], polar=True)
ax2.fill(angles, values, color="blue", alpha=0.25)
ax2.plot(angles, values, color="blue", linewidth=1)
ax2.set_xticks(angles[:-1])
ax2.set_xticklabels(labels)
ax2.set_title(title_2)

# ===================
# Part 4: Saving Output
# ===================
# Display the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig('multidiff_24.pdf', bbox_inches='tight')
