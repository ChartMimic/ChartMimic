import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Sample data (replace with your actual data)
correctly_classified = np.random.beta(a=2.0, b=5.0, size=1000)
misclassified = np.random.beta(a=1.0, b=4.0, size=1000)
labels = ["High Probability", "Low Probability"]
xlabel = "Probability of Outcome"
bins = 10

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
plt.xlim(left=plt.xlim()[0], right=3)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save the plot
plt.tight_layout()
plt.savefig('hist_6.pdf', bbox_inches='tight')
