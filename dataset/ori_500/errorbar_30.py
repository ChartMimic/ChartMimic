# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data setup
cities = ["City A", "City B", "City C", "City D"]
x = np.arange(len(cities))  # X-axis points

# Environmental impact scores for two metrics in different cities
# These are fabricated values for demonstration
air_quality_scores = np.array([-1.8, -2.2, -1.5, -2.0])  # Simulated negative values
water_quality_scores = np.array([-2.5, -2.0, -2.3, -1.8])  # Simulated negative values

# Errors for both metrics
air_quality_errors = np.array([0.2, 0.3, 0.25, 0.2])
water_quality_errors = np.array([0.3, 0.25, 0.3, 0.25])

labels = ["Air Quality", "Water Quality"]
ylabels = ["Air Quality Score", "Water Quality Score"]

title = "Environmental Impact Scores Across Cities"
ylims = [[-3, 0], [-3, 0]]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plotting setup
fig, ax1 = plt.subplots(figsize=(8, 5))

# Bar width and hatch patterns
width = 0.35
hatch_patterns = ["+", "x"]

# Colors for the bars
colors = ["#e18683", "#98bb93"]  # Greener and bluer shades

# Plot data on the left y-axis (air quality scores)
ax1.bar(
    x,
    air_quality_scores,
    width,
    color=colors[0],
    hatch=hatch_patterns[0],
    label=labels[0],
    yerr=air_quality_errors,
    capsize=5,
    edgecolor="black",
)

# Create a second y-axis sharing the same x-axis (water quality scores)
ax2 = ax1.twinx()
ax2.bar(
    x + width,
    water_quality_scores,
    width,
    color=colors[1],
    hatch=hatch_patterns[1],
    label=labels[1],
    yerr=water_quality_errors,
    capsize=5,
    edgecolor="black",
)

# Set the x-ticks to be in the middle of the two bars and add the labels
ax1.set_xticks(x + width / 2)
ax1.set_xticklabels(cities)

# Add a legend
ax1.legend(loc="lower left")
ax2.legend(loc="lower right")

# Set labels for y-axes
ax1.set_ylabel(ylabels[0], color=colors[0])
ax2.set_ylabel(ylabels[1], color=colors[1])

# Set colors for y-axes
ax1.tick_params(axis="y", colors=colors[0])
ax2.tick_params(axis="y", colors=colors[1])

# Set the limits for y-axes to fit the negative data
ax1.set_ylim(ylims[0])
ax2.set_ylim(ylims[0])

# Set title for the chart
plt.title(title)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig("errorbar_30.pdf", bbox_inches="tight")
