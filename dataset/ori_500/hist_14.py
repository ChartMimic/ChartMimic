# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# New sample data with different distribution characteristics
center_data = np.random.uniform(0, 8, 1000)  # Use correct labels for the data
random_data = np.random.normal(4, 1.5, 1000)  # Means and standard deviations adjusted

# Define bins aligned for both histograms with a little space between bars
bin_width = (
    0.6  # Determines the space between bars; adjust as necessary for clear separation
)
bins = np.histogram(np.hstack((center_data, random_data)), bins=30)[1]
labels = ["Uniform data", "Normal data"]
xlabel = "Value"
ylabel = "Frequency"
title = "Comparison of Uniform and Normal Distributions"
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create figure and axis
fig, ax = plt.subplots(figsize=(6, 4))  # Adjust size if needed

# Plot histograms directly using plt.hist() with appropriate alignment
ax.hist(
    center_data,
    bins=bins,
    alpha=0.7,
    label=labels[0],
    color="#ca3142",
    edgecolor="black",
)
ax.hist(
    random_data,
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
ax.set_title(title)  # Adjust title to reflect the data

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
plt.savefig("hist_14.pdf", bbox_inches="tight")
