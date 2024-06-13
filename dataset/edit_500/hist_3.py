import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Simulating data
camel_weights = np.random.exponential(scale=0.03, size=1000)
kangaroo_weights = np.random.exponential(scale=0.03, size=1000)

# Define the number of bins and bin edges for consistent bin width
bins = np.histogram(np.hstack((camel_weights, kangaroo_weights)), bins=25)[1]
labels =  ["Elephant", "Giraffe"]
xticks = [0.00, 0.05, 0.10, 0.15]
xlabel = "Animal Weight"
ylabel = "Count"
title = "Animal Weights Distribution"
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Set the figure size
plt.figure(figsize=(5, 4))

# Create the histograms without stacking
plt.hist(
    camel_weights,
    bins=bins,
    color="#85c23b",
    label=labels[0],
    edgecolor="white",
    linewidth=0.6,
    alpha=0.6,
    zorder=2,
)
plt.hist(
    kangaroo_weights,
    bins=bins,
    color="#e57476",
    label=labels[1],
    edgecolor="white",
    linewidth=0.6,
    alpha=0.6,
    zorder=3,
)

# Set the background color
plt.gca().set_facecolor("#f5f5f5")

# Set the scale of y-axis to logarithmic
plt.yscale("log")

# Set the x-axis ticks
plt.xticks(xticks)
plt.tick_params(axis="x", length=0)

# Add white grid lines and place them behind the bars (zorder=0)
plt.grid(color="white", linestyle="-", linewidth=1.5, zorder=0)

# Set the y-axis ticks and remove all line markings (spines)
plt.yticks([1, 10, 100])
plt.tick_params(axis="y", length=0)
for spine in plt.gca().spines.values():
    spine.set_visible(False)  # Remove all the spines

# remove small dash on y-axis
plt.tick_params(axis="y", which="minor", length=0)

# Set labels and title
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.title(title)

# Add legend with title
plt.legend(title="Class")

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout
plt.tight_layout()

# Show the plot
plt.savefig('hist_3.pdf', bbox_inches='tight')
