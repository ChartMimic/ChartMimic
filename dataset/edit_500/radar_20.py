import numpy as np; np.random.seed(0)

import matplotlib.pyplot as plt
from math import pi

# ===================
# Part 2: Data Preparation
# ===================
# Define the data for the radar chart
categories = [
    "Accuracy",
    "Speed",
    "Battery Life",
    "Durability",
    "Portability",
    "Design",
    "Customer Support",
    "Price",
]
values_a = [9, 7, 8, 6, 7, 8, 9, 7]  # Values for Dell
values_b = [8, 8, 7, 7, 8, 7, 8, 8.5]  # Values for HP
values_c = [7, 7, 8, 9, 6, 8, 7, 8]  # Values for Lenovo
suptitle = "Laptop Brand Comparison"
yticks = [2, 4, 6, 8, 10]
ytickslabel = ["2", "4", "6", "8", "10"]
labels = ["Dell", "HP", "Lenovo"]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Initialize figure
fig, axs = plt.subplots(1, 3, figsize=(18, 6), subplot_kw=dict(polar=True))
plt.suptitle(suptitle, fontsize=19)

# Number of variables and angle calculation
N = len(categories)
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]


# Function to create radar chart
def create_radar_chart(ax, angles, values, color, brand_name):
    values += values[:1]
    ax.plot(angles, values, linewidth=2, linestyle="solid", label=brand_name)
    ax.fill(angles, values, color=color, alpha=0.25)

    # Add data point markers
    ax.scatter(angles[:-1], values[:-1], color=color, s=50, zorder=5)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, color="navy")
    ax.tick_params(pad=15)  # Adjust the distance of the label from the axis
    ax.set_rlabel_position(30)
    ax.set_yticks(yticks)
    ax.set_yticklabels(ytickslabel, color="darkblue")
    ax.set_ylim(0, 10)


# Create radar charts for each brand
create_radar_chart(axs[0], angles, values_a, "gold", labels[0])
create_radar_chart(axs[1], angles, values_b, "silver", labels[1])
create_radar_chart(axs[2], angles, values_c, "green", labels[2])

# Set a common legend
fig.legend(loc="lower center", bbox_to_anchor=(0.5, 0), ncol=3)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save the figure
plt.tight_layout(
    rect=[0, 0.1, 1, 0.95]
)  # Adjust the padding to make room for the suptitle
plt.savefig('radar_20.pdf', bbox_inches='tight')
