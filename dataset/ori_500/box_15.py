# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Sample data for demonstration purposes
center = np.random.randint(0, 12, 5)
data = [np.random.normal(center[std - 1], std, 100) for std in range(1, 6)]
xticklabels = ["w/o att", "w/o DP", "1xQ", "20xQ", "200xQ"]
ylabel = "Z-Score"
xhline = 5
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create a figure with the specified dimensions
fig, ax = plt.subplots(figsize=(8, 5))

medianprops = dict(linestyle="-", linewidth=1, color="black")
# Boxplot with custom colors
box = ax.boxplot(data, patch_artist=True, medianprops=medianprops)
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"]
for patch, color in zip(box["boxes"], colors):
    patch.set_facecolor(color)

# Add threshold line
ax.axhline(xhline, color="r", linestyle="--", label="threshold")

# Set x-axis labels
ax.set_xticklabels(xticklabels)

# Set y-axis label
ax.set_ylabel(ylabel)

# Add legend for the threshold line
ax.legend(loc="upper right", frameon=False)

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig("box_15.pdf", bbox_inches="tight")
