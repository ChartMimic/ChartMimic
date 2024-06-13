# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
weeks = np.arange(1, 29)
performance_data = np.sin(2 * np.pi * weeks / len(weeks)) + np.random.normal(
    0, 0.1, len(weeks)
)
efficiency_data = np.cos(3 * np.pi * weeks / len(weeks)) + np.random.normal(
    0, 0.1, len(weeks)
)

# Calculate the upper and lower bounds for the data
performance_upper = performance_data + 0.1
performance_lower = performance_data - 0.1
efficiency_upper = efficiency_data + 0.1
efficiency_lower = efficiency_data - 0.1


# Axes Limits and Labels
xlabel_value = "Weeks"
ylabel_value = "Values"

# Labels
labelPerformance="Performance"
label_Efficiency="Efficiency"

# Titles
title = "Performance and Efficiency Analysis"
title_2 = "Parallel (n=2, m=4)"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create a figure and axis
fig, ax = plt.subplots(figsize=(6, 4))

# Plot the performance data line and fill the confidence interval
ax.plot(
    weeks,
    performance_data,
    label=labelPerformance,
    color="deepskyblue",
    marker="o",
    linestyle="-",
)
ax.fill_between(
    weeks, performance_lower, performance_upper, color="deepskyblue", alpha=0.3
)

# Plot the efficiency data line and fill the confidence interval
ax.plot(
    weeks,
    efficiency_data,
    label=label_Efficiency,
    color="salmon",
    marker="x",
    linestyle="--",
)
ax.fill_between(weeks, efficiency_lower, efficiency_upper, color="salmon", alpha=0.3)

# Customize the plot with labels, title, and legend
ax.set_xlabel(xlabel_value)
ax.set_ylabel(ylabel_value)
ax.set_title(title, fontsize=16)
ax.legend()

# Add a grid to the plot
ax.grid(True, linestyle="--", linewidth=0.5, alpha=0.7)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout for better spacing and display
plt.tight_layout()
plt.savefig('line_61.pdf', bbox_inches='tight')
