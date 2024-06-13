import numpy as np; np.random.seed(0)

import matplotlib.pyplot as plt
from math import pi

# ===================
# Part 2: Data Preparation
# ===================
# Define the data for each brand
values1 = [15.2, 22.4, 18.7, 25.9, 20.8]  # Tesla
values2 = [30.1, 27.6, 22.8, 28.3, 32.5]  # BMW
values3 = [10.3, 12.9, 15.4, 11.7, 14.1]  # Audi
xtickslabel = ["Germany", "USA", "Japan", "South Korea", "France"]
yticks = [10, 15, 20, 25, 30, 35]
ytickslabel = ["10", "15", "20", "25", "30", "35"]
ylim = [0, 35]
labels = ["Tesla", "BMW", "Audi"]

# Number of variables
num_vars = len(values1)

# Compute angle for each axis
angles = [n / float(num_vars) * 2 * pi for n in range(num_vars)]
angles += angles[:1]  # Complete the loop

# Repeat the first value to close the circle
values1 += values1[:1]
values2 += values2[:1]
values3 += values3[:1]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Initialize the spider plot
fig, ax = plt.subplots(figsize=(8, 7), subplot_kw=dict(polar=True))

# Draw one axe per variable and add labels
plt.xticks(angles[:-1],xtickslabel, size=10)

# Draw ylabels
ax.set_rlabel_position(0)
plt.yticks(yticks, ytickslabel, color="grey", size=7)
plt.ylim(ylim)

# Plot each brand
ax.plot(
    angles, values1, linewidth=1, linestyle="solid", label=labels[0], color="darkorange"
)
ax.fill(angles, values1, "darkorange", alpha=0.1)

ax.plot(
    angles, values2, linewidth=1, linestyle="solid", label=labels[1], color="royalblue"
)
ax.fill(angles, values2, "royalblue", alpha=0.1)

ax.plot(
    angles, values3, linewidth=1, linestyle="solid", label=labels[2], color="forestgreen"
)
ax.fill(angles, values3, "forestgreen", alpha=0.1)

# Add data points labels
for i in range(num_vars):
    # For Apple values
    ax.annotate(
        f"{values1[i]}",
        xy=(angles[i], values1[i]),
        xytext=(5, 5),
        textcoords="offset points",
        ha="right",
        va="bottom",
        size=8,
        color="darkorange",
    )

    # For Samsung values
    ax.annotate(
        f"{values2[i]}",
        xy=(angles[i], values2[i]),
        xytext=(5, 5),
        textcoords="offset points",
        ha="right",
        va="bottom",
        size=8,
        color="royalblue",
    )

    # For Huawei values
    ax.annotate(
        f"{values3[i]}",
        xy=(angles[i], values3[i]),
        xytext=(5, 5),
        textcoords="offset points",
        ha="right",
        va="bottom",
        size=8,
        color="forestgreen",
    )

# Add a legend to the upper right
plt.legend(loc="upper right", bbox_to_anchor=(1.15, 1.15))

# ===================
# Part 4: Saving Output
# ===================
# Adjust figure size to match original image's dimensions
fig.set_size_inches(8, 7)

# Adjust layout
plt.tight_layout()

plt.savefig('radar_16.pdf', bbox_inches='tight')
