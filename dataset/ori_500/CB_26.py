# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

from scipy.stats import gaussian_kde

# ===================
# Part 2: Data Preparation
# ===================
# Set the figure size to match the original image's dimensions
plt.figure(figsize=(7, 5))

# Generate random data to simulate the plot
data_seac = np.random.gamma(2.0, 0.5, 100)
data_ctco = np.random.gamma(2.0, 0.5, 100) + 0.5

# Combine data into a list
data = [data_seac, data_ctco]

# Create positions for each box plot
positions = [0, 1]
xticks = ["SEAC", "CTCO"]
xlabel = "Algorithms"
ylabel = "Time Cost (Seconds)"
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Calculate the kernel density estimate and plot the density plot for each dataset
colors = ["seagreen", "darkorange"]
for i, d in enumerate(data):
    # Calculate KDE
    kde = gaussian_kde(d)
    # Create an array of values covering the entire range of data for KDE
    kde_x = np.linspace(min(d), max(d), 300)
    kde_y = kde(kde_x)
    # Scale KDE values to match the position of the boxplot
    kde_y_scaled = kde_y / kde_y.max() * 0.1  # Scale factor can be adjusted
    # Plot filled density plot to the left of the boxplot
    offset = 0.2
    plt.fill_betweenx(
        kde_x,
        positions[i] - kde_y_scaled - offset,
        positions[i] - offset,
        alpha=0.5,
        color=colors[i],
        edgecolor="black",
    )

# Create box plots inside the violin plots
for i, d in enumerate(data):
    plt.boxplot(
        d,
        positions=[positions[i]],
        widths=0.05,
        patch_artist=True,
        medianprops=dict(color="black"),
        boxprops=dict(facecolor="none", color="black"),
    )

# Add scatter plot for individual data points with grey color
for i, d in enumerate(data):
    x = np.random.normal(positions[i], 0.04, size=len(d))
    plt.scatter(
        x,
        d,
        alpha=0.3,
        color=colors[i],
    )

# Set the x-axis labels and add title
plt.xticks([0, 1], xticks)
plt.xlabel(xlabel)

# Set the y-axis label
plt.ylabel(ylabel)

# Adjust the y-axis limits
plt.ylim(-1, 4)

# ===================
# Part 4: Saving Output
# ===================
# Show the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig("CB_26.pdf", bbox_inches="tight")
