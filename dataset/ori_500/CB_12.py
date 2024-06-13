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
# Sample data for demonstration purposes
benign_data = np.random.beta(a=2, b=10, size=1000)
badnets_data = np.random.beta(a=7, b=5, size=1000)

# Compute KDE for both datasets
kde_benign = gaussian_kde(benign_data)
kde_badnets = gaussian_kde(badnets_data)

# Create an array of values for plotting KDE
x_eval = np.linspace(
    min(np.concatenate([benign_data, badnets_data])),
    max(np.concatenate([benign_data, badnets_data])),
    1000,
)
labels = ["Benign", "BadNets", "Benign KDE", "BadNets KDE"]
p_text = "T-test p-value = 0.0000"
x_label = "Avg. Top-5 Persistence of 1D Diagram"
y_label = "Density"
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Set the figure size to match the original image's dimensions
plt.figure(figsize=(8, 6))

# Plot histograms
plt.hist(
    badnets_data, density=True, bins=30, color="salmon", alpha=0.8, label=labels[0]
)
plt.hist(
    benign_data, density=True, bins=30, color="#bad7b5", alpha=0.8, label=labels[1]
)

# Plot KDEs
plt.plot(
    x_eval,
    kde_badnets(x_eval),
    linestyle="dashed",
    color="darkred",
    label=labels[2],
)
plt.plot(
    x_eval,
    kde_benign(x_eval),
    linestyle="dashed",
    color="darkgreen",
    label=labels[3],
)

# Add legend
plt.legend()

# Add T-test p-value text
plt.text(0.25, 2.5, p_text, fontsize=10)

# Set labels and title
plt.xlabel(x_label)
plt.ylabel(y_label)

# ===================
# Part 4: Saving Output
# ===================
# Show the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig("CB_12.pdf", bbox_inches="tight")
