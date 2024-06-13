# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

import matplotlib.patches as mpatches

# ===================
# Part 2: Data Preparation
# ===================
# Random data to simulate the boxplot values
data_ST_CVRP = np.random.normal(30, 10, 100)
data_ST_VRPTW = np.random.normal(40, 10, 100)
data_ST_All = np.random.normal(30, 15, 100)
data_Ours = np.random.normal(5, 2, 100)

data = [data_ST_CVRP, data_ST_VRPTW, data_ST_All, data_Ours]

# Labels and Plot Types
legend_labels = ["ST_CVRP", "ST_VRPTW", "ST_All", "Ours"]

# Axes Limits and Labels
xticklabels = ["ST_CVRP", "ST_VRPTW", "ST_All", "Ours"]
ylabel_value = "Performance Gap (%)"
ylim_values = [-10, 70]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create the boxplot
fig, ax = plt.subplots(
    figsize=(8, 6)
)  # Adjusting figure size to match original image dimensions
bp = ax.boxplot(data, patch_artist=True, notch=False, showfliers=False)

# Customizing the boxplot colors
colors = ["#6f94e7", "#9467bd", "#ff7f0e", "#d62728"]
for patch, color in zip(bp["boxes"], colors):
    patch.set_facecolor(color)

# Customizing the boxplot median lines
for median in bp["medians"]:
    median.set(color="black", linewidth=1)

legend_patches = [
    mpatches.Patch(color=color, label=label)
    for color, label in zip(colors, legend_labels)
]
ax.legend(handles=legend_patches, loc="upper right")

# Setting the x-axis labels
ax.set_xticklabels(xticklabels)

# Setting the y-axis label
ax.set_ylabel(ylabel_value)

# Setting the y-axis limits
ax.set_ylim(ylim_values)

# Adding grid lines
ax.yaxis.grid(True, which="major", color="grey", alpha=0.5)

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig("box_3.pdf", bbox_inches="tight")
