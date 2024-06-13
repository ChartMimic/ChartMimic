# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)

import squarify
from matplotlib.gridspec import GridSpec

# ===================
# Part 2: Data Preparation
# ===================
# Treemap data for educational resources allocation by region
sizes_treemap = [40, 25, 15, 10, 5, 5]
labels_treemap = [
    "North\n40%",
    "South\n25%",
    "East\n15%",
    "West\n10%",
    "Central\n5%",
    "Others\n5%",
]
colors_treemap = ["#8dd3c7", "#ffffb3", "#bebada", "#fb8072", "#80b1d3", "#fdb462"]

# Pie chart data for literacy rates in regions
sizes_pie = [35, 25, 20, 15, 5]
labels_pie = ["North", "South", "East", "West", "Central"]
colors_pie = plt.cm.Set3(np.linspace(0, 1, len(sizes_pie)))
explode_pie = (0.1, 0, 0, 0, 0)  # Highlight the first slice

title = "Literacy Rate by Region"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create figure and set GridSpec
fig = plt.figure(figsize=(10, 5))
gs = GridSpec(1, 2, figure=fig)

# Create treemap subplot
ax1 = fig.add_subplot(gs[0, 0])
squarify.plot(
    sizes=sizes_treemap,
    label=labels_treemap,
    color=colors_treemap,
    alpha=0.7,
    text_kwargs={"fontsize": 14},
)
ax1.axis("off")  # Disable the axes

# Create pie chart subplot
ax2 = fig.add_subplot(gs[0, 1])
wedges, texts, autotexts = ax2.pie(
    sizes_pie,
    explode=explode_pie,
    labels=labels_pie,
    colors=colors_pie,
    autopct="%1.1f%%",
    shadow=True,
    startangle=90,
)
ax2.set_title(title)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save the figure
plt.tight_layout()
plt.savefig('multidiff_1.pdf', bbox_inches='tight')
