# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

import matplotlib.colors as mcolors

# ===================
# Part 2: Data Preparation
# ===================
# Sample data for demonstration purposes
center = np.random.randint(0, 12, 9)
center2 = np.random.randint(0, 80, 9)
center3 = np.random.randint(0, 150, 9)
data = [
    np.random.normal(center[i], std, 100)
    for (i, std) in enumerate(np.random.choice(range(1, 10), 9, replace=False))
]
data2 = [
    np.random.normal(center2[i], std, 100)
    for (i, std) in enumerate(np.random.choice(range(1, 51), 9, replace=False))
]
data3 = [
    np.random.normal(center3[i], std, 100)
    for (i, std) in enumerate(np.random.choice(range(1, 51), 9, replace=False))
]

titles = ["Linear travel times", "Exponential travel times", "Sigmoidal travel times"]
ylabel = "Full-information Gap (%)"
xticklabels = [
    "D-avg",
    "PTO-kNN",
    "PTO-OLS",
    "PTO-F",
    "SAA",
    "SAA-kNN",
    "CSAA",
    "RSAA",
    "P-NN",
]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create figure and subplots
fig, axs = plt.subplots(1, 3, figsize=(25, 8))

# Create a colormap with only one color
cmap = mcolors.LinearSegmentedColormap.from_list("mycmap", ["blue", "#b24743"])

# Get 10 colors from the colormap
colors = cmap(np.linspace(0, 1, 9))

# Linear travel times subplot
bplot = axs[0].boxplot(data, patch_artist=True)
axs[0].set_title(titles[0])
axs[0].set_ylabel(ylabel)
axs[0].set_xticklabels(
    xticklabels,
    rotation=45,
)

for patch, color in zip(bplot["boxes"], colors):
    patch.set_facecolor(color)

# Exponential travel times subplot
bplot1 = axs[1].boxplot(data2, patch_artist=True)
axs[1].set_title(titles[1])
axs[1].set_xticklabels(
    xticklabels,
    rotation=45,
)
for patch, color in zip(bplot1["boxes"], colors):
    patch.set_facecolor(color)

# Sigmoidal travel times subplot
bplot2 = axs[2].boxplot(data3, patch_artist=True)
axs[2].set_title(titles[2])
axs[2].set_xticklabels(
    xticklabels,
    rotation=45,
)
for patch, color in zip(bplot2["boxes"], colors):
    patch.set_facecolor(color)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save the figure
plt.tight_layout()
plt.savefig("box_7.pdf", bbox_inches="tight")
