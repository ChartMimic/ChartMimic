# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data to plot
sizes = [12, 28, 30, 40, 45, 55]
colors = plt.cm.Reds(np.linspace(0, 1, 6))  # Use colormap to color the slices
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1)  # add explode parameter to separate slices

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plot
fig, ax = plt.subplots(figsize=(5, 5))
ax.pie(
    sizes,
    colors=colors,
    autopct="%1.1f%%",
    startangle=140,
    wedgeprops=dict(edgecolor="w"),
    explode=explode,
)

# Set aspect ratio to be equal so that pie is drawn as a circle.
ax.axis("equal")

plt.title("Slice of a pie chart", fontsize=16)

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig('pie_5.pdf', bbox_inches='tight')
