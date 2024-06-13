import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================

categories = ["ROI", "Risk Exposure", "Asset Allocation"]
values = [0.45, 0.33, 0.25]

# Data for heatmap representing financial metrics correlations
data = np.array(
    [[0.5, -0.2, 0.4, 0.3], [-0.1, 0.6, -0.3, 0.2], [0.4, -0.1, 0.2, 0.1]]
)
rows = ["ROI", "Risk Exposure", "Asset Allocation"]
columns = ["Q1", "Q2", "Q3", "Q4"]

ylabel = "Correlation"
ylim = [0, 0.6]
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create the bar plot on the left
# Set the figure size to match the original image's dimensions
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
bars = plt.bar(categories, values, color="#376686")
plt.ylabel(ylabel)
plt.ylim(ylim)
# Create the heatmap on the right
plt.subplot(1, 2, 2)
heatmap = plt.imshow(
    data, cmap="coolwarm", interpolation="nearest", vmin=-1.0, vmax=1.0
)
plt.xticks(np.arange(len(columns)), columns, rotation=30, ha="right")
plt.yticks(np.arange(len(rows)), rows)
plt.colorbar(heatmap)

# Annotate the heatmap with text
for i in range(len(rows)):
    for j in range(len(columns)):
        plt.text(j, i, f"{data[i, j]:.2f}", ha="center", va="center", color="black")

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout to prevent overlap
plt.tight_layout()

plt.savefig('multidiff_15.pdf', bbox_inches='tight')
