# ===================
# Part 1: Importing Libraries
# ===================
import numpy as np; np.random.seed(0)

import matplotlib.pyplot as plt
from math import pi

# ===================
# Part 2: Data Preparation
# ===================
# Define the data for each line
labels = np.array(
    [
        "line",
        "heatmap",
        "line_num",
        "candlestick",
        "3D-bar",
        "rose",
        "multi-axes",
        "bubble",
        "radar",
        "area",
        "pie",
        "funnel",
        "histogram",
        "bar_num",
        "box",
        "treemap",
    ]
)
num_vars = len(labels)

values1 = np.array([3, 3.5, 4.2, 4, 4.8, 5, 4, 3.2, 4, 4.3, 3.6, 3.8, 4.4, 4.2, 3.6, 4])
values2 = np.array(
    [3.5, 3.2, 3.6, 3.5, 3.7, 3.1, 3.4, 4, 4.5, 3.7, 4, 2.8, 3, 4, 2.9, 3]
)
values3 = np.array(
    [2, 2.4, 2.3, 2.4, 2.5, 2.4, 2.3, 2.2, 1.4, 2.5, 1.3, 1.4, 2.2, 2.3, 1.4, 1.5]
)
labels2=["QWen-VL", "SPHINX-V2", "ChartLlama"]
yticks=[1, 2, 3, 4, 5]
ytickslabel=["1", "2", "3", "4", "5"]
ylim=[0, 5]
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plot
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Compute angle for each axis
angles = [n / float(num_vars) * 2 * pi for n in range(num_vars)]
values1 = np.concatenate((values1, [values1[0]]))
values2 = np.concatenate((values2, [values2[0]]))
values3 = np.concatenate((values3, [values3[0]]))
angles += angles[:1]

# Draw one axe per variable and add labels
plt.xticks(angles[:-1], labels)

# Draw ylabels
ax.set_rlabel_position(0)
plt.yticks(yticks, ytickslabel, color="black", size=7)
plt.ylim(ylim)

# Plot data
ax.plot(
    angles,
    values1,
    linewidth=1,
    linestyle="solid",
    label=labels2[0],
    color="#971d2b",
    marker="o",
)
ax.fill(angles, values1, "#971d2b", alpha=0.1)

ax.plot(
    angles,
    values2,
    linewidth=1,
    linestyle="dashed",
    label=labels2[1],
    color="#6f98c3",
    marker="s",
)
ax.fill(angles, values2, "#6f98c3", alpha=0.1)

ax.plot(
    angles,
    values3,
    linewidth=1,
    linestyle="dotted",
    label=labels2[2],
    color="#f4c17d",
    marker="D",
)
ax.fill(angles, values3, "#f4c17d", alpha=0.1)

# Add legend
plt.legend(loc="lower left", bbox_to_anchor=(-0.15, -0.1))

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout for better fit and save the plot
plt.tight_layout()
plt.savefig('radar_7.pdf', bbox_inches='tight')
