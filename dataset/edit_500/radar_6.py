import numpy as np; np.random.seed(0)

import matplotlib.pyplot as plt
from math import pi

# ===================
# Part 2: Data Preparation
# ===================
# Define the data for each line
values_predicted = [0.05, 0.12, 0.09, 0.14, 0.07, 0.10]
values_help = [0.10, 0.08, 0.11, 0.09, 0.13, 0.06]
values_rs = [0.07, 0.15, 0.05, 0.12, 0.10, 0.08]
values_rhpn = [0.12, 0.07, 0.14, 0.06, 0.11, 0.13]
xtickslabel = ["System_A", "System_B", "System_C", "System_D", "System_E", "System_F"]
y_ticks = [0.05, 0.10, 0.15]
labels = ["predicted_score", "helpful_score", "result_score", "rating_score"]
ylim = [0, 0.2]
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Set up the figure and polar axis
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

# Number of variables
num_vars = len(values_predicted)
# Compute angle for each axis
angles = [n / float(num_vars) * 2 * pi for n in range(num_vars)]
angles += angles[:1]  # Complete the loop

# Repeat the first value to close the circle
values_predicted += values_predicted[:1]
values_help += values_help[:1]
values_rs += values_rs[:1]
values_rhpn += values_rhpn[:1]

# Draw one axe per variable and add labels
plt.xticks(
    angles[:-1],
    xtickslabel,
    color="black",
    size=8,
)


# Draw ylabels
def add_custom_y_labels(ax, angles, labels, distance, size=7):
    for angle, label in zip(angles, labels):
        ax.text(
            angle,
            distance,
            label,
            horizontalalignment="center",
            size=size,
            verticalalignment="bottom",
        )


# Define the range of y-axis and y-labels

plt.yticks(y_ticks, [str(i) for i in y_ticks], color="black", size=7)
add_custom_y_labels(
    ax, angles[:-1], ["0.03"] * len(angles[:-1]), 0.03
)  # Add the 0.03 label at each axis
add_custom_y_labels(
    ax, angles[:-1], ["0.07"] * len(angles[:-1]), 0.07
)  # Add the 0.07 label at each axis

# Set y-axis limit
plt.ylim(ylim)

# Plot data and fill area for each line
ax.plot(
    angles,
    values_predicted,
    linewidth=1,
    linestyle="solid",
    label=labels[0],
    color="green",
    marker="v",
)
ax.fill(angles, values_predicted, "green", alpha=0.05)

ax.plot(
    angles,
    values_help,
    linewidth=1,
    linestyle="solid",
    label=labels[1],
    color="orange",
    marker="o",
)
ax.fill(angles, values_help, "orange", alpha=0.05)

ax.plot(
    angles,
    values_rs,
    linewidth=1,
    linestyle="solid",
    label=labels[2],
    color="blue",
    marker="x",
)
ax.fill(angles, values_rs, "blue", alpha=0.05)

ax.plot(
    angles,
    values_rhpn,
    linewidth=1,
    linestyle="solid",
    label=labels[3],
    color="red",
    marker="^",
)
ax.fill(angles, values_rhpn, "red", alpha=0.05)

# Add legend with a different style
plt.legend(loc="lower center", bbox_to_anchor=(0.5, -0.2), ncol=4)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout for better fit and save the plot
plt.tight_layout()
plt.savefig('radar_6.pdf', bbox_inches='tight')
