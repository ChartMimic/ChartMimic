# ===================
# Part 1: Importing Libraries
# ===================
import numpy as np

np.random.seed(0)

import matplotlib.pyplot as plt
from math import pi

# ===================
# Part 2: Data Preparation
# ===================
# Define the data for the radar chart
labels = np.array(
    [
        "Qwen-VL-Max",
        "GPT4V-CoT",
        "Gemini Pro",
        "InternLM-XComposer2-VL",
        "GPT4V",
        "Gemini Pro-CoT",
    ]
)
num_vars = len(labels)

values = np.array(
    [
        [10, 15, 17, 12, 18, 10],
        [11, 21, 17, 13, 20, 13],
        [11, 26, 20, 14, 26, 14],
        [14, 29, 18, 16, 26, 15],
        [20, 33, 18, 19, 27, 23],
    ]
)

# Compute angle for each axis
angles = [n * 2 * pi / float(num_vars) for n in range(num_vars)]
perangles = 2 * pi / (float(num_vars) * (len(values) + 1))
angles += angles[:1]
xticks = [20, 30]
xtickslabel = ["20", "30"]
x_angles = [n + pi / 9 for n in angles[:-1]]
# Add legend
legend_labels = ["Level 1", "Level 2", "Level 3", "Level 4", "Level 5"]
# Set the start angle to degrees
offset = 11 * pi / 18

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plot
plt.figure(figsize=(6, 6))
ax = plt.subplot(projection="polar")

# Set the direction of the plot to clockwise
ax.set_theta_direction(-1)


ax.set_theta_offset(offset)

colors = ["#f8dbad", "#dbcce2", "#d2eac8", "#b8cce1", "#f1b7b0"]
for index, value in enumerate(values):
    for _index, _value in enumerate(value):
        theta1 = angles[_index] + perangles * index
        theta2 = angles[_index] + perangles * (index + 1)
        ax.bar(theta1, _value, perangles, color=colors[index])

# Add labels

ax.set_xticks(x_angles)
ax.set_xticklabels(labels, fontdict={"fontsize": 8})
ax.set_yticks(xticks)
ax.set_yticklabels(xtickslabel, color="grey")
ax.tick_params(axis="x", which="major", pad=15)

# Add a grid
ax.grid(alpha=0.3)

for i in range(len(legend_labels)):
    ax.bar(
        [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], color=colors[-i - 1], label=legend_labels[i]
    )
ax.legend(loc="upper right", bbox_to_anchor=(0.05, 0.2))

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig("HR_14.pdf", bbox_inches="tight")
