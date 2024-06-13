# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data for the plot
weeks = np.arange(1, 29)
performance_data = np.sin(2 * np.pi * weeks / len(weeks)) + np.random.normal(
    0, 0.1, len(weeks)
)
efficiency_data = np.cos(3 * np.pi * weeks / len(weeks)) + np.random.normal(
    0, 0.1, len(weeks)
)


# Axes Limits and Labels
xlabel_value = "Weeks"

ylabel_value_1 = "Performance"
ylabel_value_2 = "Efficiency"
ylim_values = [-1.5, 1.5]

# Labels
label_1 = "Performance"
label_2 = "Efficiency"

# Titles
title = "Performance and Efficiency Over Weeks"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create a figure and axis
fig, ax1 = plt.subplots(figsize=(8, 6))

# Plot the data on the primary y-axis
color = "tab:blue"
ax1.set_xlabel(xlabel_value)
ax1.set_ylabel(ylabel_value_1, color=color)
ax1.plot(
    weeks, performance_data, label=label_1, color=color, marker="o", linestyle="-"
)
ax1.tick_params(axis="y", labelcolor=color)
ax1.set_ylim(ylim_values)

# Create a secondary y-axis and plot the data
ax2 = ax1.twinx()
color = "tab:red"
ax2.set_ylabel(ylabel_value_2, color=color)
ax2.plot(
    weeks, efficiency_data, label=label_2, color=color, marker="x", linestyle="--"
)
ax2.tick_params(axis="y", labelcolor=color)
ax2.set_ylim(ylim_values)

# Add a legend to the plot
ax1.legend(loc="upper left")
ax2.legend(loc="upper right")

# Customize the plot with a title, grid, and background color
ax1.set_facecolor("whitesmoke")
ax1.grid(True, which="both", linestyle="--", linewidth=0.5, alpha=0.7)

# Set the title
plt.title(title, fontsize=16)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout for better spacing and display
plt.tight_layout()
plt.savefig('line_60.pdf', bbox_inches='tight')
