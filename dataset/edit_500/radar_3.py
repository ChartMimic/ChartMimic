import numpy as np; np.random.seed(0)

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# ===================
# Part 2: Data Preparation
# ===================
# Data for PC1 and PC2
values_speed = [55.2, 62.8, 70.5, 68.3, 73.0, 75.2, 79.3, 82.1, 84.5, 88.8]
values_fuel_efficiency = [30.1, 28.4, 26.8, 27.2, 25.9, 24.3, 23.7, 22.1, 20.8, 19.5]
num_vars = len(values_speed)
labels = ["Average Speed (km/h)", "Fuel Efficiency (mpg)"]
ticks = [20, 40, 60, 80, 100]
tickslabel = ["20 km/h", "40 km/h", "60 km/h", "80 km/h", "100 km/h"]
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Compute angle for each axis
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# The plot is circular, so we need to "complete the loop" and append the start to the end.
values_speed += values_speed[:1]
values_fuel_efficiency += values_fuel_efficiency[:1]
angles += angles[:1]

# Draw the radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
ax.fill(angles, values_speed, color="black", alpha=0.1)
ax.plot(angles, values_speed, color="black", linewidth=2, label=labels[0])
ax.scatter(angles[:-1], values_speed[:-1], color="black", s=50)
ax.fill(angles, values_fuel_efficiency, color="red", alpha=0.1)
ax.plot(angles, values_fuel_efficiency, color="red", linewidth=2, label=labels[1])
ax.scatter(angles[:-1], values_fuel_efficiency[:-1], color="red", s=50)

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
