# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)

import matplotlib.gridspec as gridspec

# ===================
# Part 2: Data Preparation
# ===================
# Data for Picture in Picture bar plot
tech_sales_known = np.array(
    [15000, 12000, 9000, 7000, 5000, 3000, 2000, 1500, 1000, 800, 600]
)
tech_sales_unknown = np.array(
    [10000, 8000, 6000, 4000, 2000, 1500, 1000, 750, 500, 300, 100]
)
bins = np.linspace(0, 0.5, 11)

# Data for the heatmap
tech_ratings = np.array(
    [
        [90, 80, 70, 60, 50, 40],
        [88, 76, 65, 54, 43, 32],
        [85, 75, 65, 55, 45, 35],
        [95, 85, 75, 65, 55, 45],
        [99, 89, 79, 69, 59, 49],
    ]
)
x_labels = [
    "Product A",
    "Product B",
    "Product C",
    "Product D",
    "Product E",
    "Product F",
]
y_labels = ["Region 1", "Region 2", "Region 3", "Region 4", "Region 5"]
bar_labels=["Known Sales", "Unknown Sales"]
xlabels = ["Sale Probability","Technology Products" ]
ylabels = ["Number of Sales","Regions"]
cbarlabel="User Ratings"
insetaxes=[0.251, 0.5, 0.1, 0.2]
insetxlim=[0.25, 0.5]


# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create a figure with GridSpec
fig = plt.figure(figsize=(10, 5))
gs = gridspec.GridSpec(1, 2, width_ratios=[1, 1.5])

# Picture in Picture bar plot
ax0 = plt.subplot(gs[0])
ax0.bar(
    bins,
    tech_sales_known,
    width=0.04,
    color="#8ac926",
    align="center",
    label=bar_labels[0],
    edgecolor="black",
)
ax0.bar(
    bins,
    tech_sales_unknown,
    width=0.04,
    color="#1982c4",
    align="center",
    bottom=tech_sales_known,
    label=bar_labels[1],
    edgecolor="black",
)
ax0.set_xlabel(xlabels[0])
ax0.set_ylabel(ylabels[0])
ax0.legend(loc="upper right")
ax0.grid(True)

# Add inset
ax_inset = fig.add_axes(insetaxes)
ax_inset.bar(
    bins[5:],
    tech_sales_known[5:],
    width=0.04,
    color="#8ac926",
    align="center",
    edgecolor="black",
)
ax_inset.bar(
    bins[5:],
    tech_sales_unknown[5:],
    width=0.04,
    color="#1982c4",
    align="center",
    bottom=tech_sales_known[5:],
    edgecolor="black",
)
ax_inset.set_xlim(insetxlim)

# Heatmap plot
ax1 = plt.subplot(gs[1])
cmap = plt.cm.coolwarm_r
norm = plt.Normalize(vmin=tech_ratings.min(), vmax=tech_ratings.max())
heatmap = ax1.imshow(tech_ratings, cmap=cmap, norm=norm, aspect="auto")

# Add color bar
cbar = plt.colorbar(heatmap, ax=ax1, orientation="vertical", pad=0.1)
cbar.set_label(cbarlabel)

# Set x and y labels
ax1.set_xticks(np.arange(len(x_labels)))
ax1.set_yticks(np.arange(len(y_labels)))
ax1.set_xticklabels(x_labels, rotation=45)
ax1.set_yticklabels(y_labels)
ax1.set_xlabel(xlabels[1])
ax1.set_ylabel(ylabels[1])

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig('multidiff_25.pdf', bbox_inches='tight')
