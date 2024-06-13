# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Sample data to approximate the distribution in the image
data = np.random.gamma(shape=2.0, scale=1.0, size=10000)
data = data[data < 30]  # Limiting the data to match the x-axis in the image
xlabel = "Number of Repetition"
ylabel = "Number of Clusters"
binslist = [30, 30]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Set the figure size to match the original image's dimensions
plt.figure(figsize=(4, 3))

# Show grid with some transparency
plt.grid(True, linestyle="-", linewidth=0.5, color="#000000", alpha=0.1)

# Create the histogram
plt.hist(data, bins=binslist[0], color="#dca684")

# Create the histogram with histtype='step' for edge-only bars
plt.hist(
    data,
    bins=binslist[1],
    color="#dca684",
    edgecolor="#d1885c",
    histtype="step",
    linewidth=1.2,
)

# Set the title and labels to match the image
plt.xlabel(xlabel)
plt.ylabel(ylabel)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout
plt.tight_layout()

# Display the plot
plt.savefig("hist_5.pdf", bbox_inches="tight")
