import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# New sample data with different distribution characteristics
highway_speeds = np.random.uniform(60, 120, 1000)

# Traffic data: travel times for a specific route during rush hour (minutes)
rush_hour_travel_times = np.random.normal(45, 10, 1000)

# Define bins aligned for both histograms with a little space between bars
bin_width = 0.8  # Determines the space between bars; adjust as necessary for clear separation
bins = np.histogram(np.hstack((highway_speeds, rush_hour_travel_times)), bins=40)[1]

# Updated labels and titles
labels = ["Highway Speeds (km/h)", "Rush Hour Travel Times (minutes)"]
xlabel = "Value"
ylabel = "Frequency"
title = "Comparison of Highway Speeds and Rush Hour Travel Times"
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create figure and axis
fig, ax = plt.subplots(figsize=(6, 4))  # Adjust size if needed

# Plot histograms directly using plt.hist() with appropriate alignment
ax.hist(
    highway_speeds,
    bins=bins,
    alpha=0.7,
    label=labels[0],
    color="#ca3142",
    edgecolor="black",
)
ax.hist(
    rush_hour_travel_times,
    bins=bins,
    alpha=0.7,
    label=labels[1],
    color="#458ef7",
    edgecolor="black",
)

# Set labels
ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)

# Add title
ax.set_title(
    title
)  # Adjust title to reflect the data

# Add grid
ax.grid(color="#d3d3d3", linestyle="-", linewidth=1, zorder=0)

# Add legend at a new location
ax.legend(loc="upper right")

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout
plt.tight_layout()

# Save the plot
plt.savefig('hist_14.pdf', bbox_inches='tight')
