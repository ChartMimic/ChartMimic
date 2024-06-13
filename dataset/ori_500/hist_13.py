# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Generate bimodal data for camel weights
camel_peak1 = np.random.normal(loc=0.035, scale=0.004, size=200)
camel_peak2 = np.random.normal(loc=0.065, scale=0.004, size=200)
camel_weights = np.concatenate([camel_peak1, camel_peak2])

# Generate bimodal data for kangaroo weights
kangaroo_peak1 = np.random.normal(loc=0.03, scale=0.005, size=500)
kangaroo_peak2 = np.random.normal(loc=0.08, scale=0.005, size=500)
kangaroo_weights = np.concatenate([kangaroo_peak1, kangaroo_peak2])
labels = ["Camels", "Kangaroos"]
xticks = np.arange(0.00, 0.1, 0.02)
yticks = [1, 10, 100]
xlabel = "Animal Weight (Tons)"
ylabel = "Frequency"
title = "Desert Animals in the Wild"
legendtitle = "Species"


# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Set the figure size
plt.figure(figsize=(5, 5))

# Define the number of bins and bin edges for consistent bin width
bins = np.histogram(np.hstack((camel_weights, kangaroo_weights)), bins=15)[1]

# Create the histograms without stacking
# New colors using hex codes
plt.hist(
    camel_weights,
    bins=bins,
    color="#1f77b4",
    label=labels[0],
    edgecolor="white",
    linewidth=0.6,
    alpha=0.6,
    zorder=2,
)
plt.hist(
    kangaroo_weights,
    bins=bins,
    color="#ff7f0e",
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
plt.xticks(xticks)  # Adjusted to show more ticks
plt.tick_params(axis="x", length=0)

# Add white grid lines and place them behind the bars (zorder=0)
plt.grid(color="white", linestyle="-", linewidth=1.5, zorder=0)

# Set the y-axis ticks and remove all line markings (spines)
plt.yticks(yticks)  # Adjusted to show additional y-axis tick
plt.tick_params(axis="y", length=0)

# Remove spine lines
for spine in plt.gca().spines.values():
    spine.set_visible(False)

# remove small dash on y-axis
plt.tick_params(axis="y", which="minor", length=0)

# Set labels and title
plt.xlabel(xlabel)  # Adjusted label
plt.ylabel(ylabel)  # Adjusted label
plt.title(title)  # Adjusted title

# Move legend to the bottom center of the plot
plt.legend(
    title=legendtitle, loc="upper center", bbox_to_anchor=(0.5, -0.15), ncol=2
)  # Adjust legend position and make it span 2 columns

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout to make room for the legend
plt.tight_layout()  # We might need to adjust this to account for the new legend position

plt.savefig("hist_13.pdf", bbox_inches="tight")
