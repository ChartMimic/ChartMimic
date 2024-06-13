import numpy as np; np.random.seed(0); np.random.seed(0)

import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Example education data
categories = [
    "Student Enrollment",
    "Graduation Rate",
    "Average Test Scores",
    "Teacher Satisfaction",
]
layer_data = {
    "High School": np.array([80, 78, 75, 200, ]),
    "University": np.array([70, 85, 70, 150, ]),
    "Primary School": np.array([ 90, 75, 85, 300,]),
    "Secondary School": np.array([85, 80, 80, 250, ]),
}
title = "Stacked Bar Chart of Education Data"
xlabel = "Categories"
ylabel = "Values"

# Colors for each layer (from dark blue to light blue)
colors = ["#08306b", "#2171b5", "#6baed6", "#bdd7e7"]

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
plt.title(title)
plt.xlabel(xlabel)
plt.ylabel(ylabel)

# Adding legend
plt.legend()

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
# Save the plot as PDF
plt.savefig('bar_68.pdf', bbox_inches='tight')
