# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Sample data with modified distributions
correctly_classified = np.random.exponential(scale=0.8, size=1000)
misclassified = np.random.normal(loc=2.0, scale=0.5, size=1000)

# Labels and Plot Types
hist_label = ["Baguette", "Youtiao"]

# Axes Limits and Labels
xlabel_value = "Distance to Threshold"
ylabel_value = "Frequency"
title = "Baking Accuracy Analysis"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Set the figure size
plt.figure(figsize=(5, 4))

# Plot histograms with stacked bars, modified colors, and alpha for transparency
plt.hist(
    [correctly_classified, misclassified],
    bins=50,
    stacked=True,
    label=hist_label,
    color=["#6495ED", "#FFA07A"],
    alpha=0.6,
)

# Add labels, title, and modify the style of the labels
plt.xlabel(xlabel_value, color="#333333")
plt.ylabel(ylabel_value, color="#333333")
plt.title(title)

# Modify the legend style and position to lower center
plt.legend(frameon=True, loc="lower center", ncol=2, bbox_to_anchor=(0.5, -0.4))

# Adjust x-axis range and add some space at the beginning of the x-axis
plt.xlim(left=plt.xlim()[0] + 0.1, right=3)  # Adjusted right xlim

# Add grid with lighter color and set behind the histograms
plt.grid(color="grey", linestyle="--", linewidth=0.5, alpha=0.7)
plt.gca().set_axisbelow(True)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save the plot
plt.tight_layout()
plt.savefig("hist_16.pdf", bbox_inches="tight")
