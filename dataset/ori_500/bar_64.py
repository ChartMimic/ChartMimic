# ===================
# Part 1: Importing Libraries
# ===================
import numpy as np

np.random.seed(0)

import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Environmental data for air quality metrics
regions = ["North", "South", "East", "West"]
CO2_levels = np.array([60, 85, 50, 95]) + np.random.rand(4) * 10  # CO2 levels in ppm
PM_levels = (
    np.array([35, 45, 30, 50]) + np.random.rand(4) * 5
)  # Particulate matter in µg/m3
SO2_levels = np.array([20, 25, 15, 10]) + np.random.rand(4) * 3  # SO2 levels in µg/m3
NO2_levels = np.array([30, 35, 25, 40]) + np.random.rand(4) * 5  # NO2 levels in µg/m3

labels = ["CO2 (ppm)", "PM (µg/m3)", "SO2 (µg/m3)", "NO2 (µg/m3)"]
xlabel = "Concentration"
ylabel = "Regions"
title = "Air Quality Metrics by Region"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Size of the plot
plt.figure(figsize=(10, 7))

# Adjust the position of the bars on the x-axis to prevent overlap
bar_height = 0.3
indices = np.arange(len(CO2_levels)) * 1.5  # Increase space between groups

# Define some hatch patterns and colors to use for bars
hatch_patterns = ["/", "\\", "|", "-", "+", "*"]
colors = ["#66c4d5", "#eca198", "#5886c7", "#a791e8"]

# Plot bars for each air quality metric
for i, level in enumerate([CO2_levels, PM_levels, SO2_levels, NO2_levels]):
    bars = plt.barh(
        [pos + bar_height * i for pos in indices],
        level,
        color=colors[i],
        height=bar_height,
        hatch=hatch_patterns[i],
        label=f'{labels[i]}',
    )

    # Add text annotations to the right of the bars
    for bar in bars:
        plt.text(
            bar.get_width(),  # X position
            bar.get_y() + bar.get_height() / 2,  # Y position
            f"{bar.get_width():.2f}",  # Text to display
            va="center",
        )

# X and Y axis Labels and limits
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.xlim(
    0,
    max(np.max(CO2_levels), np.max(PM_levels), np.max(SO2_levels), np.max(NO2_levels))
    + 10,
)

# Title of the plot
plt.title(title)

# Adding legend
plt.legend()

# Setting the labels for y-axis with adjusted positions
plt.yticks([pos + bar_height * 1.5 for pos in indices], regions)

# Adding grids
plt.grid(True, linestyle="--", which="both", axis="x", color="grey", alpha=0.7)

# ===================
# Part 4: Saving Output
# ===================
# Display the plot with enough space
plt.tight_layout()

# Save the plot as a PDF file
plt.savefig("bar_64.pdf", bbox_inches="tight")
