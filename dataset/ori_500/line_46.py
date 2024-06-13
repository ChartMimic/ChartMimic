# ===================
# Part 1: Importing Libraries
# ===================

import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)

# ===================
# Part 2: Data Preparation
# ===================
# New data for plotting, representing some scientific or business metrics

times = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0, 21.0, 22.0, 23.0, 24.0]
activity_standard = [0.0, 0.91, 0.95, 0.14, -0.73, -1.01, -0.27, 0.76, 1.17, 0.39, -0.61, -1.01, -0.55, 0.49, 0.82, 0.54, -0.23, -1.09, -0.83, 0.17, 1.09, 0.94, -0.01, -0.94, -0.77]
activity_innovative = [1.06, 0.46, -0.49, -1.0, -0.63, 0.26, 1.07, 0.74, -0.15, -0.74, -0.88, 0.0, 0.88, 1.07, 0.15, -0.72, -0.93, -0.3, 0.54, 1.05, 0.44, -0.48, -0.85, -0.49, 0.4]

# Extracted variables
line_label1 = "Standard Activity"
line_label2 = "Innovative Activity"
xlim_values = (0, 25)
ylim_values = (-1.5, 1.5)
xlabel_value = "Time (Hours)"
ylabel_value = "Activity Level"
yticks_values = [-1.5, -1.0, -0.5, 0, 0.5, 1, 1.5]
title1 = "Daytime Activity Monitoring"
title2 = "Nighttime Activity Monitoring"
legend_location = "lower center"
legend_bbox_to_anchor = (0.5, -0.2)
legend_frameon = False

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Set the figure size
fig, axs = plt.subplots(
    2, 1, figsize=(6, 10)
)  # Use a 1x2 subplot grid for horizontal layout

# Define new colors and markers for a fresh look
colors = ["dodgerblue", "crimson"]
linestyles = ["-", "--"]
labels = [line_label1, line_label2]

# First subplot with area fill
axs[0].plot(
    times, activity_standard, color=colors[0], linestyle=linestyles[0], label=labels[0]
)
axs[0].set_title(title1)
axs[0].set_xlabel(xlabel_value)
axs[0].set_ylabel(ylabel_value)
axs[0].set_xlim(xlim_values)
axs[0].set_ylim(ylim_values)
axs[0].set_yticks(yticks_values)
axs[0].legend(loc=legend_location, bbox_to_anchor=legend_bbox_to_anchor, frameon=legend_frameon)
axs[0].tick_params(axis="both", which="both", length=0)

# Second subplot with gradient fill emulation
axs[1].plot(
    times,
    activity_innovative,
    color=colors[1],
    linestyle=linestyles[1],
    label=labels[1],
)
axs[1].set_title(title2)
axs[1].set_xlabel(xlabel_value)
axs[1].set_ylabel(ylabel_value)
axs[1].set_ylim(ylim_values)
axs[1].set_xlim(xlim_values)
axs[1].set_yticks(yticks_values)
axs[1].legend(loc=legend_location, bbox_to_anchor=legend_bbox_to_anchor, frameon=legend_frameon)
axs[1].tick_params(axis="both", which="both", length=0)

# ===================
# Part 4: Saving Output
# ===================
# Enhance overall layout and visuals
plt.tight_layout()
plt.savefig('line_46.pdf', bbox_inches='tight')
