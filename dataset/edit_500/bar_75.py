# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)

# ===================
# Part 2: Data Preparation
# ===================
# Data for the bar charts
renewable_adoption = [68.2, 75.1, 83.5, 57.6]
non_renewable_adoption = [31.8, 24.9, 16.5, 42.4]
x = np.arange(len(renewable_adoption))  # x-coordinates for the bars
labels = ["Renewable Energy", "Non-Renewable Energy"]
title = "Energy Source Adoption Rates"
ylim1 = [-100, 100]
ylim2 = [-50, 50]
yticks1 = [0, 25, 50, 75, 100]
yticks2 = [-50, -25, 0, 25, 50]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Set the figure size to match the original image's dimensions
fig, ax1 = plt.subplots(figsize=(6, 4))

# Create the first subplot for 'renewable_adoption' using the left y-axis
ax1.bar(
    x,
    renewable_adoption,
    width=0.4,
    label=labels[0],
    color="#404346",
    align="center",
)
ax1.set_ylabel(labels[0], color="#404346")
ax1.tick_params(axis="y", labelcolor="#404346")

# Create the second y-axis for 'non_renewable_adoption'
ax2 = ax1.twinx()
ax2.bar(
    x,
    [-i for i in non_renewable_adoption],
    width=0.4,
    label=labels[1],
    color="#dc9dae",
    align="center",
)
ax2.set_ylabel(labels[1], color="#dc9dae")
ax2.tick_params(axis="y", labelcolor="#dc9dae")

# Title for the plot

ax1.set_title(title)

# Set x-axis labels (empty in this case as per original code)
ax1.set_xticks(x)
ax1.set_xticklabels([])

# Drawing a horizontal line at y=0
ax1.axhline(0, color="black", linewidth=0.8)

# Annotate bars with their values
for j in range(4):
    ax1.text(
        x[j],
        renewable_adoption[j] - 8,
        f"{renewable_adoption[j]}%",
        ha="center",
        color="white",
    )
    ax2.text(
        x[j],
        -non_renewable_adoption[j] - 5,
        f"{non_renewable_adoption[j]}%",
        ha="center",
        color="#dc9dae",
    )

ax1.set_ylim(ylim1)
ax1.set_yticks(yticks1)

ax2.set_ylim(ylim2)
ax2.set_yticks(yticks2)
ax2.set_yticklabels(yticks2)
# Add legend to the subplot
ax1.legend(loc="upper left", bbox_to_anchor=(0.0, 1.2))
ax1.grid(axis="y", linestyle="--")
ax1.set_axisbelow(True)
ax2.legend(loc="upper right", bbox_to_anchor=(1, 1.2))
ax2.grid(axis="y", linestyle="--")
ax2.set_axisbelow(True)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout
plt.tight_layout()
plt.savefig('bar_75.pdf', bbox_inches='tight')
