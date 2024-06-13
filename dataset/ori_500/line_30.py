# ===================
# Part 1: Importing Libraries
# ===================

import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)

# ===================
# Part 2: Data Preparation
# ===================
# Data
layers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
outside_code_diff = [
    0.0050,
    0.0051,
    0.0050,
    0.0052,
    0.0051,
    0.0051,
    0.0052,
    0.0051,
    0.0052,
    0.0053,
    0.0052,
]
inside_code_diff = [
    0.0036,
    0.0038,
    0.0037,
    0.0039,
    0.0040,
    0.0041,
    0.0040,
    0.0041,
    0.0039,
    0.0037,
    0.0038,
]

# Extracted variables
outside_label = "outside-code-diff"
inside_label = "inside-code-diff"
xlim_values = [2, 12]
ylim_values = [0.0030, 0.0055]
xlabel_value = "Layer"
ylabel_value = ""
xticks_values = layers
yticks_values = np.arange(0.0030, 0.0056, 0.0005)
xtickslabel_values = []
ytickslabel_values = [str(i) for i in yticks_values]
title_value = "Android"
legend_location = "lower center"
legend_bbox_to_anchor = (0.5, -0.3)
legend_ncol = 2
legend_frameon = False

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plot
fig, ax = plt.subplots(
    figsize=(6, 4)
)  # Adjusted to match the original image's dimensions

# Plot lines
ax.plot(
    layers,
    outside_code_diff,
    marker="o",
    clip_on=False,
    zorder=10,
    color="#1f77b4",
    label=outside_label,
    markersize=6,
    mec="white",
)
ax.plot(
    layers,
    inside_code_diff,
    marker="o",
    clip_on=False,
    zorder=10,
    color="#ff7f0e",
    label=inside_label,
    markersize=6,
    mec="white",
)

# Set x,y-axis to only display specific ticks and extend y-axis to leave space at top
plt.yticks(yticks_values, fontsize=10)
plt.ylim(ylim_values)  # Adjusted y-axis limit
plt.xlim(xlim_values)

# Title and labels
ax.set_title(title_value)
ax.set_xlabel(xlabel_value)
ax.tick_params(axis="both", which="both", length=0)

# Legend
ax.legend(loc=legend_location, bbox_to_anchor=legend_bbox_to_anchor, ncol=legend_ncol, frameon=legend_frameon)

# ===================
# Part 4: Saving Output
# ===================
# Show plot
plt.tight_layout()
plt.savefig('line_30.pdf', bbox_inches='tight')
