# ===================
# Part 1: Importing Libraries
# ===================
import numpy as np; np.random.seed(0)

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# ===================
# Part 2: Data Preparation
# ===================
# Data for PC1 and PC2
values_pc1 = [0.8, 0.7, 0.6, 0.85, 0.9, 0.75, 0.7, 0.65, 0.8, 0.9]
values_pc2 = [0.6, 0.55, 0.5, 0.45, 0.4, 0.35, 0.3, 0.25, 0.2, 0.15]
num_vars = len(values_pc1)
labels = ["Loadings PC1", "Loadings PC2"]
ticks=[0.2, 0.4, 0.6, 0.8, 1.0]
tickslabel=["0.2", "0.4", "0.6", "0.8", "1.0"]


# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Compute angle for each axis
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# The plot is circular, so we need to "complete the loop" and append the start to the end.
values_pc1 += values_pc1[:1]
values_pc2 += values_pc2[:1]
angles += angles[:1]

# Draw the radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
ax.fill(angles, values_pc1, color="black", alpha=0.1)
ax.plot(angles, values_pc1, color="black", linewidth=2, label=labels[0])
ax.scatter(angles[:-1], values_pc1[:-1], color="black", s=50)
ax.fill(angles, values_pc2, color="red", alpha=0.1)
ax.plot(angles, values_pc2, color="red", linewidth=2, label=labels[1])
ax.scatter(angles[:-1], values_pc2[:-1], color="red", s=50)

# Add labels to the plot
ax.set_yticklabels([])
grid_angles = np.linspace(0, 2 * np.pi, 8, endpoint=False)
ax.set_xticks(grid_angles)
angle_labels = [f"{i*45}°" for i in range(8)]
ax.set_xticklabels(angle_labels)

# Add grid lines and labels for the concentric circles
ax.set_rgrids(
    ticks,
    labels=tickslabel,
    angle=30,
    color="black",
    size=10,
)

# Create legend handles manually
legend_elements = [
    Line2D(
        [0],
        [0],
        color="black",
        linewidth=2,
        marker="o",
        markersize=8,
        label=labels[0],
    ),
    Line2D(
        [0],
        [0],
        color="red",
        linewidth=2,
        marker="o",
        markersize=8,
        label=labels[1],
    ),
]

# Add legend and title
ax.legend(
    handles=legend_elements, loc="upper right", bbox_to_anchor=(1.1, 1.1), frameon=False
)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save the plot
plt.tight_layout()
plt.savefig('radar_3.pdf', bbox_inches='tight')
