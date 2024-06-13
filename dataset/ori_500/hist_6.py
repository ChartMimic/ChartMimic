# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Sample data (replace with your actual data)
correctly_classified = np.random.exponential(scale=1.0, size=1000)
misclassified = np.random.exponential(scale=0.5, size=1000)
labels = ["Correctly classified", "Misclassified"]
xlabel = "Distance to threshold"
bins = 50


# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Set the figure size to match the original image's dimensions
plt.figure(figsize=(5, 3))

# Plot histograms with stacked bars
plt.hist(
    [correctly_classified, misclassified],
    bins=bins,
    stacked=True,
    label=labels,
    color=["#3b75af", "#ef8636"],
)

# Add labels and title
plt.xlabel(xlabel)
plt.legend()

# Adjust x-axis range to match the reference picture and add a little space at the beginning of the x-axis
plt.xlim(left=plt.xlim()[0] + 0.1, right=5)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save the plot
plt.tight_layout()
plt.savefig("hist_6.pdf", bbox_inches="tight")
