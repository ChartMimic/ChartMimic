import numpy as np; np.random.seed(0)

import matplotlib.pyplot as plt
from math import pi

# ===================
# Part 2: Data Preparation
# ===================
# Define the data for each model
values1 = [63.2, 55.4, 72.1, 78.9, 65.0, 59.7, 50.4]  # PublicTransit
values2 = [75.6, 68.9, 82.4, 71.1, 74.3, 80.7, 64.5]  # ElectricVehicles
values3 = [54.1, 78.5, 69.3, 64.7, 70.9, 69.2, 79.0]  # TrafficCongestion
xlabels = ["BikeSharing", "CarPooling", "SmartParking", "ElectricBuses", "UrbanLogistics", "RideHailing", "LastMileDelivery"]
yticks = [20, 40, 60, 80, 100]
title = "Urban Mobility Comparison"
labels = ["PublicTransit", "ElectricVehicles", "TrafficCongestion"]
ylim = [0, 100]
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Initialize the spider plot
fig, ax = plt.subplots(figsize=(8, 7), subplot_kw=dict(polar=True))

# Number of variables
num_vars = len(values1)

# Compute angle for each axis
angles = [n / float(num_vars) * 2 * pi for n in range(num_vars)]
angles += angles[:1]  # Complete the loop

# Repeat the first value to close the circle
values1 += values1[:1]
values2 += values2[:1]
values3 += values3[:1]


# Draw one axe per variable and add labels
plt.xticks(
    angles[:-1],
    xlabels,
    size=10,
)

# Draw ylabels
ax.set_rlabel_position(0)
plt.yticks(yticks, [], color="#bceced", size=7)
plt.ylim(ylim)

# Draw the inner circles with red color lines
for circle in ax.get_ygridlines():
    circle.set_color("#97ccf6")

# Plot each model
ax.plot(angles, values1, linewidth=1, linestyle="solid", label=labels[0], color="red")
ax.fill(angles, values1, "red", alpha=0.1)

ax.plot(angles, values2, linewidth=1, linestyle="solid", label=labels[1], color="blue")
ax.fill(angles, values2, "blue", alpha=0.1)

ax.plot(angles, values3, linewidth=1, linestyle="solid", label=labels[2], color="green")
ax.fill(angles, values3, "green", alpha=0.1)

# Add data labels
for i in range(num_vars):
    plt.text(
        angles[i],
        values1[i],
        str(values1[i]),
        horizontalalignment="center",
        size=8,
        color="black",
    )
    plt.text(
        angles[i],
        values2[i],
        str(values2[i]),
        horizontalalignment="center",
        size=8,
        color="black",
    )
    plt.text(
        angles[i],
        values3[i],
        str(values3[i]),
        horizontalalignment="center",
        size=8,
        color="black",
    )

# Add a legend and title
plt.legend(loc="lower center", bbox_to_anchor=(0.5, -0.1), ncol=3)
plt.title(title, position=(0.5, -0.15), ha="center")

# Adjust figure size to match original image's dimensions
fig.set_size_inches(8, 7)
ax.spines["polar"].set_color("#97ccf6")

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save the plot
plt.tight_layout()
plt.savefig('radar_2.pdf', bbox_inches='tight')
