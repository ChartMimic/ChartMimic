# ===================
# Part 1: Importing Libraries
# ===================

import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Data to plot
labels = ["Psychological", "Others", "Market", "Satisfactory", "Social"]
sizes = [35.4, 10.3, 24.7, 17.2, 12.4]
colors = ["#1a78b1", "#379f39", "#aec8e6", "#fe7e28", "#ffba7e"]

# Plot configuration
legend_labels = labels
legend_loc = "upper center"
legend_bbox_to_anchor = (0.5, 1.05)
legend_ncol = 5
legend_frameon = False

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plot
plt.figure(
    figsize=(8, 6)
)  # Adjust the figure size to match the original image's dimensions
plt.pie(sizes, colors=colors, autopct="%1.1f%%", shadow=False, startangle=140)
plt.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

# Add legend
plt.legend(
    legend_labels, loc=legend_loc, bbox_to_anchor=legend_bbox_to_anchor, frameon=legend_frameon, ncol=legend_ncol
)

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig('pie_6.pdf', bbox_inches='tight')

