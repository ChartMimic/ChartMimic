# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data points representing pollution emission levels in four regions
x = np.arange(4)  # X-axis points represent different regions
y1 = np.array([-190, -150, -180, -160])  # Pollution levels for 2020
y2 = np.array([-180, -140, -170, -150])  # Pollution levels for 2021
labels = ["2020 Emissions", "2021 Emissions"]
xticklabels = ["Region 1", "Region 2", "Region 3", "Region 4"]
title = "Annual Pollution Emission Reductions"
ylim1 = [-220, 0]
ylim2 = [-220, 0]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
fig, ax1 = plt.subplots(figsize=(10, 5))
width = 0.4  # Width of the bars

# Plotting data for the year 2020
ax1.bar(
    x,
    y1,
    color="#d87769",
    hatch="/",
    width=width,
    label=labels[0],
    edgecolor="black",
)

# Create a second y-axis sharing the same x-axis
ax2 = ax1.twinx()
ax2.bar(
    x + width,
    y2,
    color="#7da1c7",
    hatch="\\",
    width=width,
    label=labels[1],
    edgecolor="black",
)

# Set the x-ticks to be in the middle of the two bars and add labels for the regions
ax1.set_xticks(x + width / 2)
ax1.set_xticklabels(["Region 1", "Region 2", "Region 3", "Region 4"])

# Adding legends to the plot
ax1.legend(loc="lower left")
ax2.legend(loc="lower right")

# Labeling y-axes
ax1.set_ylabel(labels[0], color="#d26252")
ax2.set_ylabel(labels[1], color="#3f81bb")

# Setting colors for y-axis
ax1.tick_params(axis="y", colors="#d26252")
ax2.tick_params(axis="y", colors="#3f81bb")

# Setting the limits for y-axes
ax1.set_ylim(ylim1)
ax2.set_ylim(ylim2)

# Title for the chart
plt.title(title)

# ===================
# Part 4: Saving Output
# ===================
# Layout adjustment to prevent clipping
plt.tight_layout()

# Saving the plot as a PDF
plt.savefig("bar_78.pdf", bbox_inches="tight")
