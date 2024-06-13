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
# Setting a seed for reproducibility

# Generating random data to represent the time to market (in days) for different fashion brands
data_brand_A = np.random.normal(80, 15, 100)  # Brand A
data_brand_B = np.random.normal(90, 5, 100)  # Brand B
data_brand_C = np.random.normal(85, 10, 100)  # Brand C
data_ours = np.random.normal(70, 5, 100)  # Our brand

# Packing the data into a list
data = [data_brand_A, data_brand_B, data_brand_C, data_ours]
legend_labels = ["Adidas", "Nike", "New Balance", "Our Brand"]
line_label = "Median Time to Market"
ylabel = "Time to Market (Days)"
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Creating a box plot
fig, ax1 = plt.subplots(figsize=(10, 6))
bp = ax1.boxplot(
    data, patch_artist=True, notch=False, showfliers=False, positions=[1, 2, 3, 4]
)

# Customizing the boxplot colors
colors = ["#17c3b2", "#ffcb77", "#fe6d73", "#00b4d8"]
for patch, color in zip(bp["boxes"], colors):
    patch.set_facecolor(color)
for median in bp["medians"]:
    median.set(color="black", zorder=2)

# Extracting medians for the line graph
medians = [np.median(d) for d in data]

# Creating the line graph on the same axes
ax1.plot(
    [1, 2, 3, 4],
    medians,
    "-*",
    color="black",
    label="Median Time to Market",
    ms=20,
    markerfacecolor="#d90368",
)

# Setting legend for the boxplot
legend_patches = [
    mpatches.Patch(color=color, label=label)
    for color, label in zip(colors, legend_labels)
]
ax1.legend(
    handles=legend_patches + [mpatches.Patch(color="#d90368", label=line_label)],
    loc="upper right",
)

# Setting labels for the x-axis
ax1.set_xticklabels(legend_labels)

# Setting the y-axis label
ax1.set_ylabel(ylabel)

# Setting y-axis limits and adding grid lines
ax1.set_ylim(40, 120)
ax1.yaxis.grid(True, which="major", linestyle="--", color="grey", alpha=0.5)

# Removing top and right spines for aesthetics
ax1.spines["top"].set_visible(False)
ax1.spines["right"].set_visible(False)

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig("CB_27.pdf", bbox_inches="tight")
