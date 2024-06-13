# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

from matplotlib.colors import LinearSegmentedColormap

# ===================
# Part 2: Data Preparation
# ===================
# Generating non-linear data with complex trends

ratios = np.array([0.1, 0.19, 0.28, 0.37, 0.46, 0.55, 0.64, 0.73, 0.82, 0.91, 1.0])
pna_performance = np.array([1.5, 1.72, 2.31, 3.53, 9.1, -5.41, -1.03, -0.15, 0.36, 0.75, 1.01])
gin_performance = np.array([0.04, 0.08, 0.18, 0.47, 0.84, 1.39, 1.59, 1.89, 1.93, 1.86, 2.26])
pna_std = np.array([0.13, 0.15, 0.15, 0.14, 0.11, 0.08, 0.06, 0.05, 0.05, 0.07, 0.1])
gin_std = np.array([0.14, 0.12, 0.09, 0.07, 0.05, 0.05, 0.07, 0.09, 0.12, 0.14, 0.15])

# Extracted variables
line_label1 = "PNA + ours"
line_label2 = "GIN + ours"
xlim_values = (0.1, 1.0)
ylim_values = (-80, 30)
xlabel_value = "Ratio r"
ylabel_value = "Performance"
xticks_values = np.arange(0.1, 1.1, 0.1)
yticks_values = [-80, -60, -40, -20, 0, 20, 30]
title_value = "Dynamic Performance Trends"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create a gradient background
cmap = LinearSegmentedColormap.from_list("mycmap", ["lightblue", "lightgreen"])

# Plot settings
fig, ax = plt.subplots(figsize=(10, 5))

# Using the complex and colorful styles
ax.set_facecolor(cmap(0.5))  # Use the middle of the colormap for background
ax.plot(
    ratios,
    pna_performance,
    label=line_label1,
    clip_on=False,
    zorder=1,
    color="magenta",
    marker="o",
    linestyle="-",
    markersize=5,
)
ax.fill_between(
    ratios,
    pna_performance - pna_std,
    pna_performance + pna_std,
    color="magenta",
    alpha=0.3,
)
ax.plot(
    ratios,
    gin_performance,
    label=line_label2,
    clip_on=False,
    zorder=1,
    color="gold",
    marker="^",
    linestyle="-",
    markersize=5,
)
ax.fill_between(
    ratios,
    gin_performance - gin_std,
    gin_performance + gin_std,
    color="gold",
    alpha=0.3,
)

# Enhancing plot details
ax.set_xticks(xticks_values)
ax.set_xlim(*xlim_values)
ax.set_ylim(*ylim_values)
ax.set_yticks(yticks_values)
ax.set_xlabel(xlabel_value, fontsize=14)
ax.set_ylabel(ylabel_value, fontsize=14)
ax.legend(loc="upper right", bbox_to_anchor=(1, 1.1), ncol=3, frameon=False)
ax.grid(True, linestyle=":", color="grey")
ax.tick_params(axis="both", which="both", length=2, color="grey")

# Adding visual improvements
for spine in ax.spines.values():
    spine.set_visible(False)

plt.title(title_value, fontsize=16, y=1.1)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig("line_72.pdf", bbox_inches="tight")
