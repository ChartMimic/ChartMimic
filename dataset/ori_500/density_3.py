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
# Generate a bimodal distribution for the data
data1 = np.random.normal(loc=-0.5, scale=0.2, size=500)
data2 = np.random.normal(loc=0.5, scale=0.2, size=500)
data = np.concatenate([data1, data2])
xs = np.linspace(-1.5, 1.5, 200)

# Axes Limits and Labels
xticks_values = [-1, -0.5, 0, 0.5, 1]
xticklabels = ["-1.0", "-0.5", "0.0", "0.5", "1.0"]
yticks_values = [0, 0.2, 0.4, 0.6, 0.8, 1.0]
yticklabels = ["0.0", "0.2", "0.4", "0.6", "0.8", "1.0"]
xlim_values = [-1.5, 1.5]
ylim_values = [0, 1.2]
title = "KDE Plot of Spearman Coefficient Distribution"
xlabel_value = "Spearman Coefficient"
ylabel_value = "Density"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Set the figure size to match the original image's dimensions
fig, ax = plt.subplots(figsize=(8, 4))

# Create the KDE plot with adjusted x-axis range
density = gaussian_kde(data)
density.covariance_factor = lambda: 0.5
density._compute_covariance()
plt.fill_between(xs, density(xs), color="#d1e4e5", edgecolor="teal")

ax.set_xticks(xticks_values)
ax.set_xticklabels(xticklabels)

ax.set_yticks(yticks_values)
ax.set_yticklabels(yticklabels)

plt.xlim(xlim_values)
plt.ylim(ylim_values)
# Set the title and labels
plt.title(title)
plt.xlabel(xlabel_value)
plt.ylabel(ylabel_value)

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig("density_3.pdf", bbox_inches="tight")
