# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

# ===================
# Part 2: Data Preparation
# ===================
# Data for the plot with new trends
decomposition_IO_norm = np.array([0, 20, 40, 60, 80])
coco_10k = np.array([0.60, 0.70, 0.72, 0.73, 0.74]) + np.array(
    [0.018, 0.004, 0.01, 0.022, 0.019]
)  # Small noise
laion_10k = np.array([0.58, 0.67, 0.70, 0.71, 0.73]) + np.array(
    [-0.01, 0.01, -0.002, -0.001, 0.004]
)
coco_5k = np.array([0.56, 0.66, 0.67, 0.68, 0.68])  # Changed last point to non-None
laion_5k = np.array([0.55, 0.61, 0.64, 0.65, 0.66])  # Continuation of the trend
clip = np.linspace(0.75, 0.75, len(decomposition_IO_norm))  # Make clip a full line

# Extracted variables
fill_label_coco_10k = "coco (10k)"
fill_label_laion_10k = "laion (10k)"
fill_label_coco_5k = "coco (5k)"
fill_label_laion_5k = "laion (5k)"
plot_label_clip = "clip"
title_text = "Dynamic Effect of Vocab on Zero Shot Accuracy"
xlabel_text = "Decomposition IO Norm"
ylabel_text = "Accuracy"
xlim_values = (min(decomposition_IO_norm), max(decomposition_IO_norm))
ylim_values = (0.53, 0.76)
xticks_values = decomposition_IO_norm
yticks_values = [0.53, 0.55, 0.60, 0.65, 0.70, 0.75, 0.76]
legend_title = "Dataset"
legend_loc = "upper center"
legend_bbox_to_anchor = (0.5, 1.12)
legend_ncol = 5

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create the plot with a different visualization style
plt.figure(figsize=(10, 6))
plt.fill_between(
    decomposition_IO_norm, coco_10k, color="red", alpha=0.3, label=fill_label_coco_10k
)
plt.fill_between(
    decomposition_IO_norm,
    laion_10k,
    color="green",
    alpha=0.3,
    label=fill_label_laion_10k,
)
plt.fill_between(
    decomposition_IO_norm, coco_5k, color="blue", alpha=0.3, label=fill_label_coco_5k
)
plt.fill_between(
    decomposition_IO_norm,
    laion_5k,
    color="orange",
    alpha=0.3,
    label=fill_label_laion_5k,
)
plt.plot(
    decomposition_IO_norm,
    clip,
    color="black",
    linestyle="--",
    linewidth=2,
    label=plot_label_clip,
)

# Add a title and labels with enhanced formatting
plt.title(title_text, fontsize=14, y=1.1)
plt.xlabel(xlabel_text, fontsize=12)
plt.ylabel(ylabel_text, fontsize=12)
plt.xticks(xticks_values)
plt.yticks(yticks_values)
plt.gca().tick_params(axis="both", which="both", length=0)

# Setting the limits explicitly to prevent cut-offs
plt.xlim(*xlim_values)
plt.ylim(*ylim_values)

# Adding a legend with a title
plt.legend(
    title=legend_title,
    frameon=False,
    reverse=True,
    framealpha=0.8,
    loc=legend_loc,
    bbox_to_anchor=legend_bbox_to_anchor,
    ncol=legend_ncol,
)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout to ensure no clipping
plt.tight_layout()
plt.savefig("area_3.pdf", bbox_inches="tight")
