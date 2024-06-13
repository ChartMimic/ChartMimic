# ===================
# Part 1: Importing Libraries
# ===================

import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Example data
categories = ["Fruits", "Proteins", "Vegetables", "Grains", "Dairy"]
sizes = [25, 35, 20, 10, 10]  # These values are for illustrative purposes
colors = ["#ff9999", "#66b3ff", "#99ff99", "#ffcc99", "#c2c2f0"]
explode = (0, 0, 0, 0, 0)  # Only "explode" the 1st slice (Fruits)

# Variables for plot configuration
title_text = "Nutritional Distribution"  # Title for the donut chart

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
fig, ax = plt.subplots(figsize=(6, 6))

# The pie function also handles donuts with the 'wedgeprops' argument
wedges, texts, autotexts = ax.pie(
    sizes,
    labels=categories,
    colors=colors,
    autopct="%1.1f%%",
    startangle=90,
    explode=explode,
    wedgeprops=dict(width=0.3, edgecolor="w"),
)

# Draw a circle at the center of pie to make it a donut
centre_circle = plt.Circle((0, 0), 0.70, fc="white")
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle
ax.axis("equal")

# Set title for the donut chart
ax.set_title(title_text)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig('pie_14.pdf', bbox_inches='tight')
