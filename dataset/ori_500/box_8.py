# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

from matplotlib.patches import Patch

# ===================
# Part 2: Data Preparation
# ===================
# Sample data for demonstration purposes
data1 = [
    np.random.normal(0.85, 0.05, 20),
    np.random.normal(0.84, 0.04, 20),
    np.random.normal(0.84, 0.03, 20),
]
data2 = [
    np.random.normal(0.87, 0.03, 20),
    np.random.normal(0.80, 0.02, 20),
    np.random.normal(0.86, 0.03, 20),
]
data3 = [
    np.random.normal(0.83, 0.04, 20),
    np.random.normal(0.78, 0.02, 20),
    np.random.normal(0.79, 0.02, 20),
]

# Combine data
data = [data1, data2, data3]
xticklabels = ["Only WSI\nModality", "Only CNV\nModality", "WSI+CNV\nModality"]
ylabel = "AUC"
xticks = [1, 3, 5]
ylim = [0.7, 1.0]
labels = ["Hospital 1", "Hospital 2", "Hospital 3"]


# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create a figure and axis with specific size
fig, ax = plt.subplots(figsize=(5, 5))  # Size in inches to match 360x288 pixels

# Plot boxplots with different colors and hatch patterns
colors = ["#b6d7e4", "#a6ec9a", "#f4b9c2"]  # Lighter shades of blue, green, and red
hatches = ["/", "\\", "o"]  # Diagonal, horizontal lines, and dots

for i, d in enumerate(data):
    bp = ax.boxplot(
        d,
        positions=np.array(range(len(d))) * 2 + (i + 1) * 0.5,
        widths=0.5,
        patch_artist=True,
    )
    for patch in bp["boxes"]:
        patch.set_facecolor(colors[i])
        patch.set_hatch(hatches[i])
        patch.set_edgecolor("black")  # Set edge color to black
        # Set outlier markers to black
    for flier in bp["fliers"]:
        flier.set(
            marker="o", color="black", markerfacecolor="black", markersize=2, alpha=0.5
        )

# Customizing the plot to match the given picture
ax.set_xticks(xticks)
ax.set_xticklabels(xticklabels)
ax.set_ylabel(ylabel)
ax.set_ylim(ylim)

# Adding legend manually to match the picture
legend_elements = [
    Patch(facecolor=colors[0], hatch=hatches[0], label=labels[0], edgecolor="black"),
    Patch(facecolor=colors[1], hatch=hatches[1], label=labels[1], edgecolor="black"),
    Patch(facecolor=colors[2], hatch=hatches[2], label=labels[2], edgecolor="black"),
]
ax.legend(handles=legend_elements, loc="upper left")

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig("box_8.pdf", bbox_inches="tight")
