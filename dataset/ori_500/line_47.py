# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Generate new data representing different types of performance metrics over time
time_points = np.linspace(0, 12, 100)  # Representing time in months
performance_standard = 0.5 * np.sin(2 * np.pi * time_points / 12) + 0.5
performance_innovation = 0.5 * np.cos(2 * np.pi * time_points / 12) + 0.5

# Calculate uncertainty bounds for visual emphasis
upper_bound_standard = performance_standard + 0.1
lower_bound_standard = performance_standard - 0.1
upper_bound_innovation = performance_innovation + 0.1
lower_bound_innovation = performance_innovation - 0.1

# Axes Limits and Labels
xlabel_value = "Time (Months)"
xlim_values = [5, 25]
xticks_values = np.arange(0, 13, 1)

ylabel_value = "Performance Index"
ylim_values = [0, 1.1]
yticks_values = np.linspace(0, 1, 6)

# Labels
label_1 = "Standard Performance"
label_2 = "Innovative Performance"

# Title
title = "Comparative Performance Analysis Over Time"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Set the figure size and create a single plot
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the standard performance with filled uncertainty
ax.fill_between(
    time_points,
    lower_bound_standard,
    upper_bound_standard,
    color="lightblue",
    alpha=0.3,
)
ax.plot(
    time_points,
    performance_standard,
    label=label_1,
    color="blue",
    linestyle="-",
    linewidth=2,
)

# Plot the innovative performance with filled uncertainty
ax.fill_between(
    time_points,
    lower_bound_innovation,
    upper_bound_innovation,
    color="lightcoral",
    alpha=0.3,
)
ax.plot(
    time_points,
    performance_innovation,
    label=label_2,
    color="red",
    linestyle="-",
    linewidth=2,
)

# Customize the axes and grid
ax.set_title(title)
ax.set_xlabel(xlabel_value, fontsize=14)
ax.set_ylabel(ylabel_value, fontsize=14)
ax.set_ylim(ylim_values)
ax.set_xticks(xticks_values)
ax.set_yticks(yticks_values)

# Add a legend to the plot
ax.legend(loc="upper right", frameon=True, fontsize=12)

# ===================
# Part 4: Saving Output
# ===================
# Enhance layout and display
plt.tight_layout()
plt.savefig('line_47.pdf', bbox_inches='tight')
