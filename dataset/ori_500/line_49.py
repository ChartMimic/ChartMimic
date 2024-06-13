# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

# ===================
# Part 2: Data Preparation
# ===================
# Data preparation

times = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
growth = [1.18, 0.76, 0.61, 0.59, 0.45, 0.09, 0.23, 0.08, 0.06, 0.09, 0.05]
decay = [1.07, 0.41, 0.14, 0.07, 0.03, 0.08, -0.01, 0.02, -0.04, -0.13, 0.03]
oscillation = [0.09, 0.77, 1.14, -0.0, -0.75, -0.98, -0.13, 0.8, 1.0, 0.45, -0.63]

# Extracted variables
growth_label = "Growth"
decay_label = "Decay"
oscillation_label = "Oscillation"

xlim_values = (0, 10)
ylim_values_growth = (-0.2, 1.3)
ylim_values_decay = (-0.2, 1.3)
ylim_values_oscillation = (-1.2, 1.2)

yticks_growth = [-0.2, 0.3, 0.8, 1.3]
yticks_decay = [-0.2, 0.3, 0.8, 1.3]
yticks_oscillation = [-1.2, -1, 0, 1, 1.2]

xlabel_value = "Time"
ylabel_value = "Value"

title_growth = "Exponential Growth Over Time"
title_decay = "Exponential Decay Over Time"
title_oscillation = "Oscillatory Behavior Over Time"

legend_location = "upper center"
legend_bbox_to_anchor = (0.5, 1.15)
legend_frameon = False

grid_linestyle = "--"
grid_alpha = 0.5

tick_params_color = "gray"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create a 3-subplot layout
fig, axs = plt.subplots(3, 1, figsize=(6, 9))

# First subplot: Growth
axs[0].plot(
    times,
    growth,
    label=growth_label,
    color="green",
    clip_on=False,
    zorder=10,
    linestyle="-",
    marker="o",
)
axs[0].set_title(title_growth, y=1.1)
axs[0].set_xlim(*xlim_values)
axs[0].set_ylim(*ylim_values_growth)
axs[0].set_yticks(yticks_growth)
axs[0].set_ylabel(ylabel_value)
axs[0].legend(
    loc=legend_location, bbox_to_anchor=legend_bbox_to_anchor, frameon=legend_frameon
)
axs[0].grid(True, linestyle=grid_linestyle, alpha=grid_alpha)
axs[0].tick_params(axis="both", which="both", color=tick_params_color)

# Second subplot: Decay
axs[1].plot(
    times,
    decay,
    label=decay_label,
    color="red",
    clip_on=False,
    zorder=10,
    linestyle="-",
    marker="x",
)
axs[1].set_xlim(*xlim_values)
axs[1].set_ylim(*ylim_values_decay)
axs[1].set_yticks(yticks_decay)
axs[1].set_title(title_decay, y=1.1)
axs[1].set_ylabel(ylabel_value)
axs[1].legend(
    loc=legend_location, bbox_to_anchor=legend_bbox_to_anchor, frameon=legend_frameon
)
axs[1].grid(True, linestyle=grid_linestyle, alpha=grid_alpha)
axs[1].tick_params(axis="both", which="both", color=tick_params_color)

# Third subplot: Oscillation
axs[2].plot(
    times,
    oscillation,
    label=oscillation_label,
    clip_on=False,
    zorder=10,
    color="blue",
    linestyle="-",
    marker="s",
)
axs[2].set_title(title_oscillation, y=1.1)
axs[2].set_xlim(*xlim_values)
axs[2].set_ylim(*ylim_values_oscillation)
axs[2].set_yticks(yticks_oscillation)
axs[2].set_xlabel(xlabel_value)
axs[2].set_ylabel(ylabel_value)
axs[2].legend(
    loc=legend_location, bbox_to_anchor=legend_bbox_to_anchor, frameon=legend_frameon
)
axs[2].grid(True, linestyle=grid_linestyle, alpha=grid_alpha)
axs[2].tick_params(
    axis="both",
    which="both",
    color=tick_params_color,
)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout for better spacing and display
plt.tight_layout()

# Show the plot
plt.savefig("line_49.pdf", bbox_inches="tight")
