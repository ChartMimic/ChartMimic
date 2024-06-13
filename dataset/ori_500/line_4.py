# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data for plotting
resolutions = ["224", "128", "64", "32"]  # Update for categorical x-axis
resolutions_int = [224, 128, 64, 32]
serial_imagenet1k = [75, 65, 50, 35]
serial_imagenet_cp = [40, 30, 20, 0]
parallel_imagenet1k = [80, 70, 55, 40]
parallel_imagenet_cp = [50, 40, 30, 10]

# Axes Limits and Labels
xticks_values = range(len(resolutions))
ylabel_value = "Top-1 Acc. (%)"

# Labels
label_1 = "ImageNet-1k"
label_2 = "ImageNet-C/P (Fog)"

# Titles
title_1 = "Serial (n=8, m=1)"
title_2 = "Parallel (n=2, m=4)"

# Texts
text_1 = "39.1%"
text_2 = "22.9%"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create figure and axes
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 4))

# Plotting for Serial
ax1.set_xticks(xticks_values)  # Setting categorical x-axis
ax1.plot(
    resolutions,
    serial_imagenet1k,
    marker="o",
    color="#f5a45f",
    label=label_1,
    linewidth=4,
    markersize=8,
)
ax1.plot(
    resolutions,
    serial_imagenet_cp,
    marker="o",
    linestyle="--",
    color="#f5a45f",
    label=label_2,
    linewidth=4,
    markersize=8,
)
ax1.set_title(title_1, fontsize=16)
ax1.set_ylabel(ylabel_value, fontsize=16)  # Adjusted font size
ax1.legend(loc="lower left", fontsize=14)
ax1.set_xticklabels(resolutions, fontsize=12)  # Adjust font size for x-axis labels
ax1.grid(True, which="both", ls="--", color="grey", linewidth=1, axis="y", alpha=0.5)
ax1.annotate(
    "",
    xy=(0, serial_imagenet_cp[0]),
    xytext=(0, serial_imagenet1k[0]),
    arrowprops=dict(color="red", shrink=0.05, width=1.5, headwidth=8),
    annotation_clip=False,
)
ax1.text(
    0.1,
    (serial_imagenet1k[0] + serial_imagenet_cp[0]) / 2,
    text_1,
    ha="left",
    va="center",
    fontsize=14,
    color="black",
)

# Plotting for Parallel
ax2.plot(
    resolutions,
    parallel_imagenet1k,
    marker="o",
    color="#3ebcec",
    label=label_1,
    linewidth=4,
    markersize=8,
)
ax2.plot(
    resolutions,
    parallel_imagenet_cp,
    marker="o",
    linestyle="--",
    color="#3ebcec",
    label=label_2,
    linewidth=4,
    markersize=8,
)
ax2.set_title(title_2, fontsize=16)  # Adjusted font size
ax2.legend(loc="lower left", fontsize=14)
ax2.set_xticklabels(
    resolutions, fontsize=12
)  # Ensure x-axis labels are set for both axes
ax2.grid(True, which="both", ls="--", color="grey", linewidth=1, axis="y", alpha=0.5)
ax2.annotate(
    "",
    xy=(0, parallel_imagenet_cp[0]),
    xytext=(0, parallel_imagenet1k[0]),
    arrowprops=dict(color="red", shrink=0.05, width=1.5, headwidth=8),
    annotation_clip=False,
)
ax2.text(
    0.1,
    (parallel_imagenet1k[0] + parallel_imagenet_cp[0]) / 2,
    text_2,
    ha="left",
    va="center",
    fontsize=14,
    color="black",
)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and add common annotation for resolution
plt.tight_layout()
plt.savefig('line_4.pdf', bbox_inches='tight')
