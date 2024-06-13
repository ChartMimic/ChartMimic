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
# Define parameters for three Gaussian distributions
distributions = {
    "teenagers": {"mean": [30, 1.0], "cov": [[5, 0.8], [0.5, 0.5]]},
    "children": {"mean": [35, 0.8], "cov": [[6, 0.3], [0.1, 0.3]]},
    "adults": {"mean": [40, 0.9], "cov": [[4, 0.6], [0.3, 0.5]]},
}
keys = ["teenagers", "children", "adults"]
# Generate samples
samples = {
    species: np.random.multivariate_normal(dist["mean"], dist["cov"], 100)
    for species, dist in distributions.items()
}

xlabel = "Relative Cluster Size"
ylabel = "Average Norm of Difference Vectors"
title = "Species"
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create the plotting grid
fig = plt.figure(figsize=(10, 8))
grid = plt.GridSpec(4, 4, hspace=0, wspace=0)

# Main scatter plot
main_ax = fig.add_subplot(grid[1:, :-1])
colors = {keys[0]: "r", keys[1]: "g", keys[2]: "b"}
for species, color in colors.items():
    subset = samples[species]
    main_ax.scatter(subset[:, 0], subset[:, 1], c=color, label=species, alpha=0.6)
main_ax.set_xlabel(xlabel)
main_ax.set_ylabel(ylabel)

# Top density plot
top_ax = fig.add_subplot(grid[0, :-1], sharex=main_ax)
all_samples = np.concatenate([samples[species] for species in samples], axis=0)
x_min, x_max = all_samples[:, 0].min(), all_samples[:, 0].max()
xs = np.linspace(x_min, x_max, 200)
for species, color in colors.items():
    density = gaussian_kde(samples[species][:, 0])
    top_ax.fill_between(xs, density(xs), alpha=0.6, color=color)

# Right density plot
right_ax = fig.add_subplot(grid[1:, -1], sharey=main_ax)
y_min, y_max = all_samples[:, 1].min(), all_samples[:, 1].max()
ys = np.linspace(y_min, y_max, 200)
for species, color in colors.items():
    density = gaussian_kde(samples[species][:, 1])
    right_ax.fill_betweenx(ys, density(ys), alpha=0.6, color=color)

# Hide the spines
top_ax.spines["top"].set_visible(False)
top_ax.spines["right"].set_visible(False)
top_ax.spines["left"].set_visible(False)
right_ax.spines["top"].set_visible(False)
right_ax.spines["right"].set_visible(False)
right_ax.spines["bottom"].set_visible(False)

# Remove the labels from the top and right axes
top_ax.tick_params(axis="x", which="both", top=False, bottom=False, labelbottom=False)
right_ax.tick_params(axis="y", which="both", left=False, right=False, labelleft=False)

# Remove all ticks from the right axis
top_ax.set_yticks([])
right_ax.set_xticks([])

main_ax.legend(title=title)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig("CB_6.pdf", bbox_inches="tight")
