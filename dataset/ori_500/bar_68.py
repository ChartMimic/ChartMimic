# ===================
# Part 1: Importing Libraries
# ===================
import numpy as np

np.random.seed(0)

import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Example transportation data
categories = [
    "Traffic Flow",
    "Accident Rate",
    "Public Transport Usage",
    "Road Condition",
]
layer_data = {
    "Cars": np.array([70, 50, 30, 80]),
    "Buses": np.array([30, 30, 40, 75]),
    "Bikes": np.array([15, 20, 20, 85]),
    "Pedestrians": np.array([50, 20, 20, 90]),
}

# Colors for each layer (from dark blue to light blue)
colors = ["#08306b", "#2171b5", "#6baed6", "#bdd7e7"]

title = "Stacked Bar Chart of Transportation Data"
xlabel = "Categories"
ylabel = "Values"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create the figure and axes objects
fig, ax = plt.subplots(figsize=(10, 6))

# Variables to store the bottom position for each stack
bottoms = np.array([0] * len(categories))

for i, (layer, values) in enumerate(layer_data.items()):
    bars = ax.bar(categories, values, bottom=bottoms, color=colors[i], label=layer)

    # Add data labels on each bar
    for bar, bottom in zip(bars, bottoms):
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bottom + height / 2,
            str(height),
            ha="center",
            va="center",
            color="white",
        )

    # Update the bottoms position
    bottoms += values

# Chart title and labels
plt.title("Stacked Bar Chart of Transportation Data")
plt.xlabel("Categories")
plt.ylabel("Values")

# Adding legend
plt.legend()

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
# Save the plot as PDF
plt.savefig("bar_68.pdf", bbox_inches="tight")
