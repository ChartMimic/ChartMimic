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
# Sample data
data1 = np.random.normal(loc=8, scale=0.8, size=1000)
data2 = np.random.normal(loc=12, scale=0.8, size=1000)

# Compute density for each dataset
density1 = gaussian_kde(data1)
density2 = gaussian_kde(data2)
xs = np.linspace(5, 15, 300)
ys1 = density1(xs)
ys2 = density2(xs)
labels = ["Gucci", "Chanel"]
xlabel = "Density"
ylabel = "Value"
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create the figure and axis
fig, ax = plt.subplots(figsize=(9, 6))

# Fill between x for density regions
plt.fill_betweenx(xs, ys1, color="blue", alpha=0.2, label=labels[0])
plt.fill_betweenx(xs, ys2, color="green", alpha=0.2, label=labels[1])

# Set labels and title (if any)
ax.set_ylim(5, 15)
ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)

# Show grid
plt.grid(True, linestyle="--")

# Add legend
plt.legend()

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig("density_5.pdf", bbox_inches="tight")
