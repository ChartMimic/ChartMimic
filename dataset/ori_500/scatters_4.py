# ===================
# Part 1: Importing Libraries
# ===================

import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)

# ===================
# Part 2: Data Preparation
# ===================
clusters = {
    "cluster_1": np.array([[-1.29, 0.27], [-0.04, -1.17], [0.52, -0.17], [0.77, 0.82], [2.16, 1.34], [-0.37, -0.24], [1.1, 0.66], [0.64, -1.62], [-0.02, -0.74], [0.28, -0.1]]),
    "cluster_2": np.array([[5.91, 5.32], [5.79, 4.53], [4.06, 4.59], [4.98, 5.38], [7.26, 4.96], [4.04, 4.65], [4.54, 5.48], [3.46, 5.06], [5.16, 5.23], [4.4, 4.76], [3.58, 4.51], [4.46, 5.42], [3.84, 5.78], [6.49, 2.93], [5.43, 5.68]]),
    "cluster_3": np.array([[-5.64, 4.6], [-5.13, 4.7], [-5.31, 3.32], [-3.85, 6.08], [-5.81, 3.53], [-4.48, 4.42], [-4.86, 4.68], [-4.31, 5.69], [-5.73, 3.62], [-6.58, 5.61], [-6.19, 4.49], [-5.6, 4.95], [-6.94, 5.19], [-4.48, 5.09], [-5.31, 5.1], [-4.6, 2.23], [-3.04, 5.39], [-5.65, 4.61], [-4.51, 4.88], [-7.03, 7.06]]),
    "cluster_4": np.array([[4.89, -3.98], [4.31, -3.46], [5.29, -4.39], [3.95, -3.79], [5.69, -3.7], [4.37, -5.48], [7.3, -6.06], [4.86, -3.86], [5.1, -4.42], [4.6, -4.63], [3.69, -3.34], [4.88, -5.68], [5.67, -5.46], [3.67, -6.35], [5.69, -5.16]]),
    "cluster_5": np.array([[-5.13, -3.92], [-6.13, -5.73], [-5.38, -4.91], [-5.04, -5.29], [-5.06, -5.11], [-5.72, -5.81], [-4.73, -5.89], [-6.16, -5.31], [-5.16, -2.74], [-5.7, -4.06]]),
    "cluster_6": np.array([[0.75, 8.81], [0.77, 8.82], [-2.66, 10.61], [-1.76, 10.45], [-0.68, 11.66], [1.07, 9.55], [-0.69, 8.79], [-0.44, 9.72], [-0.36, 10.16], [0.58, 10.35], [-0.76, 8.56], [1.36, 9.31], [-0.65, 9.48], [-1.84, 9.52], [-0.48, 10.62], [0.7, 10.], [0.93, 10.34], [-0.02, 10.16], [-0.19, 9.61], [-0.27, 8.87], [0.28, 9.01], [0.84, 9.75], [0.05, 10.49], [0.64, 8.43], [-0.21, 10.88]]),
}

# Colors for each cluster (replace with actual colors)
colors = {
    "cluster_1": "red",
    "cluster_2": "blue",
    "cluster_3": "green",
    "cluster_4": "purple",
    "cluster_5": "orange",
    "cluster_6": "yellow",
}

# Variables for plot configuration
xlim = None
ylim = None
xlabel = None
ylabel = None
xticks = None
yticks = None
xtickslabel = None
ytickslabel = None
title = None
axhline = None
axvline = None

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create the scatter plot
plt.figure(figsize=(5, 5))
for cluster, data in clusters.items():
    plt.scatter(data[:, 0], data[:, 1], c=colors[cluster], alpha=0.5)

# Remove axes and grid
plt.axis("off")

# ===================
# Part 4: Saving Output
# ===================
# Show the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig('scatters_4.pdf', bbox_inches='tight')
