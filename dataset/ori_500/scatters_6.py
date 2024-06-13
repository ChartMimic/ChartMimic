# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Generate sample data for the three clusters with adjusted positions and spread
x1 = np.random.normal(-2, 1, 100)
y1 = np.random.normal(2, 1, 100)

x2 = np.random.normal(-2, 1, 100)
y2 = np.random.normal(-2, 1, 100)

x3 = np.random.normal(2, 1, 100)
y3 = np.random.normal(0, 1, 100)

labels = ["Daytime Sunny", "Night Rainy", "PGST"]
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Set the figure size to match the original image's dimensions
plt.figure(figsize=(8, 8))

# Plot the data with adjusted colors
plt.scatter(x1, y1, c="orange", label=labels[0])
plt.scatter(x2, y2, c="blue", label=labels[1])
plt.scatter(x3, y3, c="green", label=labels[2])

# Add the legend with adjusted order of labels
plt.legend(labels, loc="upper right", frameon=True)

# Remove axis for clean look
plt.axis("off")

# ===================
# Part 4: Saving Output
# ===================
# Show the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig('scatters_6.pdf', bbox_inches='tight')
