# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

import matplotlib.colors as mcolors

# ===================
# Part 2: Data Preparation
# ===================
# Data for environmental factors affecting plant growth
categories = [
    "Sunlight",
    "Water Quality",
    "Soil pH",
    "Fertilizer",
    "Temperature",
    "Pesticides",
    "CO2 Levels",
    "Plant Variety",
    "Planting Density",
    "Watering Frequency",
]
values = [0.18, 0.15, 0.12, 0.09, 0.06, 0.03, -0.06, -0.03, -0.02, -0.03]
errors = [0.05, 0.04, 0.03, 0.03, 0.02, 0.02, 0.02, 0.02, 0.01, 0.01]

min_val = min(values) - 0.1
max_val = max(values) + 0.1


# Normalizing function to convert values to a 0-1 range for color scaling
def normalize(value, min_val, max_val):
    return (value - min_val) / (max_val - min_val)


# Determine color based on normalized value
def get_color(value):
    norm_value = normalize(value, min_val, max_val)
    green_base = np.array(mcolors.to_rgb("#6a8347"))
    # Create a color that ranges from very light green to the base green
    return mcolors.to_hex((1 - green_base) * (1 - norm_value) + green_base)


colors = [get_color(value) for value in values]

# Axes Limits and Labels
ylabel_value = "Environmental Factors"
xlabel_value = "Impact on Plant Growth (Δ to control)"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 8))

# Horizontal bar chart
bars = ax.barh(
    categories, values, xerr=errors, color=colors, capsize=3, edgecolor="none"
)
ax.set_ylabel(ylabel_value)
ax.set_xlabel(xlabel_value)

# Set y-axis limits and x-axis limits
ax.set_xlim(min_val, max_val)  # Adjust limits to encompass errors

# Remove top and right spines for a cleaner look
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# Customize grid lines
ax.xaxis.grid(True, linestyle="--", which="major", color="gray", alpha=0.6)
ax.set_axisbelow(True)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout to prevent clipping of ylabel
plt.tight_layout()
plt.savefig("errorbar_28.pdf", bbox_inches="tight")
