# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Define a custom color palette
colors = ["#e74c3c", "#3498db", "#2ecc71", "#f39c12", "#9b59b6"]

# Data setup
decomposition_IO_norm = np.array([0, 20, 40, 60, 80])
coco_10k = np.array([0.60, 0.70, 0.72, 0.73, 0.74])
laion_10k = np.array([0.58, 0.67, 0.70, 0.71, 0.73])
coco_5k = np.array([0.56, 0.66, 0.67, 0.68, 0.70])
laion_5k = np.array([0.55, 0.61, 0.64, 0.65, 0.68])

# Axes Limits and Labels
xlabel_value = "Decomposition IO Norm"
xlim_values = [-5, 85]
ylabel_value = "Accuracy"
ylim_values = [0.53, 0.76]

# Labels
label_1 = "COCO (10k)"
label_2 = "LAION (10k)"
label_3 = "COCO (5k)"
label_4="LAION (5k)"

# Titles
title_1 = "COCO 10K"
title_2 = "LAION 10K"
title_3 = "COCO & LAION 5K"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create the 1x3 subplot configuration
fig, axs = plt.subplots(1, 3, figsize=(9, 3))

# Plot customization for a fancy look
marker_styles = ["o", "^", "s", "x"]
line_styles = ["-", "--", ":", "-."]

# First subplot for coco 10k
axs[0].plot(
    decomposition_IO_norm,
    coco_10k,
    label=label_1,
    color=colors[0],
    marker=marker_styles[0],
    linestyle=line_styles[0],
    markersize=10,
    linewidth=2,
)
axs[0].set_title(title_1, fontsize=14)
axs[0].set_xlabel(xlabel_value, fontsize=12)
axs[0].set_ylabel(ylabel_value, fontsize=12)

# Second subplot for laion 10k
axs[1].plot(
    decomposition_IO_norm,
    laion_10k,
    label=label_2,
    color=colors[1],
    marker=marker_styles[1],
    linestyle=line_styles[1],
    markersize=10,
    linewidth=2,
)
axs[1].set_title(title_2, fontsize=14)
axs[1].set_xlabel(xlabel_value, fontsize=12)
axs[1].set_ylabel(ylabel_value, fontsize=12)

# Third subplot for coco & laion 5k
axs[2].plot(
    decomposition_IO_norm,
    coco_5k,
    label=label_3,
    color=colors[2],
    marker=marker_styles[2],
    linestyle=line_styles[2],
    markersize=10,
    linewidth=2,
)
axs[2].plot(
    decomposition_IO_norm,
    laion_5k,
    label=label_4,
    color=colors[3],
    marker=marker_styles[3],
    linestyle=line_styles[3],
    markersize=10,
    linewidth=2,
)
axs[2].set_title(title_3, fontsize=14)
axs[2].set_xlabel(xlabel_value, fontsize=12)
axs[2].set_ylabel(ylabel_value, fontsize=12)

# Set global properties and customize each subplot individually
for ax in axs:
    ax.set_xticks(decomposition_IO_norm)
    ax.set_xlim(xlim_values)
    ax.set_ylim(ylim_values)
    ax.legend(loc="lower right", fontsize=10)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout to ensure no overlap and labels are clearly visible
plt.tight_layout()

# Show the plot
plt.savefig('line_56.pdf', bbox_inches='tight')
