# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data for plotting
decomposition_IO_norm = [1, 12, 28, 93]
accuracy_laion = [0.225, 0.275, 0.325, 0.375]
accuracy_CLIP = [0.385, 0.385, 0.385, 0.385]

# Axes Limits and Labels
xlabel_value = "Decomposition IO Norm"
xlim_values = [-5, 95]
xticks_values = np.arange(0, 81, 20)

ylabel_value = "Accuracy"
ylim_values = [0.200, 0.400]
yticks_values = np.arange(0.200, 0.376, 0.025)

# Labels
label_laion="laion"
label_CLIP="CLIP"
label_deepjscc_w_ofdm = "DEEPJSCC w/ ofdm"
label_ours = "OURS"

# Titles
title_1 = "CIFAR100 States Zero Shot Accuracy"
title_2 = "Dictionary"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create the figure and the line that we will manipulate
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(
    decomposition_IO_norm,
    accuracy_laion,
    marker="o",
    color="orange",
    linewidth=2,
    markersize=6,
    markerfacecolor="orange",
    label=label_laion,
)

# Extend the CLIP line visually by adding extra points
extended_x = [-5] + decomposition_IO_norm + [95]  # Extend x-axis data points
extended_y = [0.385] * (len(accuracy_CLIP) + 2)  # Extend y-axis data points to match
ax.plot(
    extended_x, extended_y, linestyle="--", color="#202020", label=label_CLIP
)  # Plot the extended line

# Set x,y-axis to only display specific ticks and extend y-axis to leave space at top
plt.yticks(yticks_values, fontsize=12)
plt.ylim(ylim_values)  # Adjusted y-axis limit
plt.xticks(xticks_values, fontsize=12)
plt.xlim(xlim_values)  # Adjusted x-axis limit

# Set the title and labels
ax.set_title(title_1, fontsize=20)
ax.set_xlabel(xlabel_value, fontsize=16)
ax.set_ylabel(ylabel_value, fontsize=16)

# Remove tick lines outside the plotting area
ax.tick_params(
    axis="both", which="both", length=0, color="#d2d2d2"
)  # Remove tick marks and set their color

# Add a legend with a title
ax.legend(
    title=title_2,
    loc="lower right",
    fontsize=12,
    title_fontsize=12,
    edgecolor="#fdfdfd",
)

# Change the plot background color
ax.set_facecolor("#f5f5f5")

# Show grid with lighter color
ax.grid(True, color="#fcfcfc", linewidth=1.5)

# Change the axis colors
ax = plt.gca()
ax.spines["bottom"].set_color("#ffffff")
ax.spines["top"].set_color("#ffffff")  # Optional: hide or set color
ax.spines["left"].set_color("#ffffff")
ax.spines["right"].set_color("#ffffff")  # Optional: hide or set color

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and show plot
plt.tight_layout()
plt.savefig('line_32.pdf', bbox_inches='tight')
