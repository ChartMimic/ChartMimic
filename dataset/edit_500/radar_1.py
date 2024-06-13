import numpy as np; np.random.seed(0)

import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Data
categories = [
    "PublicTransit",
    "ElectricVehicles",
    "TrafficCongestion",
    "AirPollution",
    "BicycleUsage",
    "RoadSafety",
    "UrbanMobility",
    "Ridesharing",
    "PedestrianZones",
]
values1 = [45.2, 55.6, 70.3, 82.1, 63.5, 59.7, 76.4, 68.9, 50.3]
values2 = [68.4, 74.1, 80.6, 67.5, 54.2, 60.8, 72.3, 78.5, 49.7]
yticks = [20, 40, 60, 80, 100]
ylim = [0, 100]
labels = ["UrbanTransport-2024", "SmartMobility-2024"]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Size of the figure
fig, ax = plt.subplots(figsize=(8, 7), subplot_kw=dict(polar=True))

# Number of variables
num_vars = len(categories)
# Compute angle for each category
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# The plot is circular, so we need to "complete the loop" and append the start to the end.
values1 += values1[:1]
values2 += values2[:1]
angles += angles[:1]

margin = 0.1  # Adjust margin for labels
# Draw one axe per variable and add labels with a margin
labels = []
for angle, label in zip(angles[:-1], categories):
    x_offset = margin * np.cos(angle)
    y_offset = margin * np.sin(angle)
    labels.append(
        ax.text(
            angle + x_offset,
            100 + y_offset,
            label,
            color="black",
            size=10,
            horizontalalignment="center",
            verticalalignment="center",
        )
    )
plt.xticks(angles[:-1], [])

# Draw ylabels
ax.set_rlabel_position(0)
plt.yticks(yticks, [], color="#bceced", size=7)
plt.ylim(ylim)

# Plot data
ax.plot(
    angles,
    values2,
    linewidth=1,
    linestyle="solid",
    label=labels[0],
    color="#d1553e",
)
ax.fill(angles, values2, "#d1553e", alpha=0.2)

ax.plot(
    angles,
    values1,
    linewidth=1,
    linestyle="solid",
    label=labels[1],
    color="#4d88b9",
)
ax.fill(angles, values1, "#4d88b9", alpha=0.2)

# Add data labels
for angle, value in zip(angles, values1):
    ax.text(
        angle,
        value,
        str(value),
        color="black",
        size=10,
        horizontalalignment="center",
        verticalalignment="bottom",
    )
for angle, value in zip(angles, values2):
    ax.text(
        angle,
        value,
        str(value),
        color="black",
        size=10,
        horizontalalignment="center",
        verticalalignment="bottom",
    )

# Add legend
plt.legend(
    loc="lower center",
    ncol=2,
    bbox_to_anchor=(0.5, -0.15),
)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save the plot
plt.tight_layout()
plt.savefig('radar_1.pdf', bbox_inches='tight')
