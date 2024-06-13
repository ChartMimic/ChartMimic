# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde
import numpy as np; np.random.seed(0)

import random

# ===================
# Part 2: Data Preparation
# ===================
# Sample data to mimic the picture provided
data = np.random.beta(a=[4, 30, 15, 28, 21], b=[10, 32, 43, 52, 25], size=(10, 5))
data_memory = np.random.beta(
    a=[7, 45, 62, 22, 72], b=[22, 61, 22, 53, 24], size=(40, 5)
)
xticklabels=["A2", "B1", "B2", "C1", "C2"]
legend_labels = ["Teacher-Style", "Standardize"]
# The scaling factor is used to ensure the violins do not overlap
scaling_factor = 1
violin_width = 0.5

# Adjust the offsets for 5 groups instead of 3
offsets = np.linspace(-3, 3, 5)

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Set the figure size
fig, ax = plt.subplots(
    figsize=(6, 6)
)  # Increased the figure width to accommodate additional groups

# Define the colors for each group
colors = ["#d48640", "#44739d"]
legend_colors = ["#44739d", "#d48640"]

# Plot the half-violins with an offset for 5 groups
for i in range(data.shape[1]):
    offset = offsets[i]

    # Plot data without memory
    kde_data = gaussian_kde(data[:, i])
    kde_x = np.linspace(0, 1, 300)
    kde_data_y = kde_data(kde_x)
    kde_data_y_scaled = kde_data_y / max(kde_data_y) * violin_width
    ax.fill_betweenx(
        kde_x,
        kde_data_y_scaled * scaling_factor + offset,
        offset,
        color=colors[0],
        edgecolor="black",
    )

    # Plot data with memory
    kde_data_memory = gaussian_kde(data_memory[:, i])
    kde_data_memory_y = kde_data_memory(kde_x)
    kde_data_memory_y_scaled = kde_data_memory_y / max(kde_data_memory_y) * violin_width
    ax.fill_betweenx(
        kde_x,
        offset,
        -kde_data_memory_y_scaled * scaling_factor + offset,
        color=colors[1],
        edgecolor="black",
    )

    # add yellow stars at the top of each violin plot
    ax.scatter(
        offset,
        random.uniform(0.2, 0.8),
        marker="*",
        color="yellow",
        s=260,
        zorder=3,
        edgecolor="black",
    )


# Set x and y axis labels, limits, and add x-axis tick labels for 5 groups
ax.set_xlim(
    min(offsets) - scaling_factor - violin_width,
    max(offsets) + scaling_factor + violin_width,
)
ax.set_xticks(offsets)  # Set x-ticks to the center of each group
ax.set_xticklabels(xticklabels)  # Label x-ticks accordingly

# Adjust the legend
handles = [
    plt.Rectangle((0, 0), 1, 1, color=color, edgecolor="black")
    for color in legend_colors
]

ax.legend(handles, legend_labels, loc="upper left", ncol=1)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save the plot
plt.tight_layout()
plt.savefig('violin_5.pdf', bbox_inches='tight')
