# ===================
# Part 1: Importing Libraries
# ===================
import numpy as np; np.random.seed(0)

import matplotlib.pyplot as plt
from math import pi

# ===================
# Part 2: Data Preparation
# ===================
# Define the data for each model
values1 = [76.1, 50.8, 66.1, 85.0, 80.9, 52.8, 50.2]  # TinyLaMA
values2 = [86.4, 66.4, 78.7, 71.9, 74.9, 86.9, 59.3]  # StableLM
values3 = [56.5, 85.8, 59.7, 64.1, 69.9, 69.9, 79.2]  # Phi-2
xlabels =["SQA-I", "TextVQA", "MM-Vet", "GQA", "VQAv2", "LLaVA-W", "POPE"]
yticks=[20, 40, 60, 80]
title="POPE"
labels=["TinyLaMA", "StableLM", "Phi-2"]
ylim=[0, 90]

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
