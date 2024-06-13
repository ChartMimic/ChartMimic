# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data for the plot
iterations = np.linspace(0, 200, 50)
base_data_1 = np.linspace(0.5, 0.2, 50) * (1 + np.random.normal(0, 0.05, 50))
ours_data_1 = np.linspace(0.4, 0.3, 50) * (1 + np.random.normal(0, 0.05, 50))

# Axes Limits and Labels
xlabel_value = "Training Iterations"

ylabel_value = "Metric Value"
ylim_values = [0.05, 0.9]

# Labels
label_Base_Model="Base Model"
label_Our_Model="Our Model"

# Titles
title = "Accuracy"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Customization options
color = "deepskyblue"
marker = "o"
style = "-"

# Create a figure and axis
fig, ax = plt.subplots(figsize=(5, 3))

# Plot the data
ax.plot(
    iterations,
    base_data_1,
    label=label_Base_Model,
    color=color,
    marker=marker,
    markersize=5,
    linestyle=style,
    linewidth=2,
)
ax.plot(
    iterations,
    ours_data_1,
    label=label_Our_Model,
    color=color,
    marker=marker,
    markersize=5,
    linestyle=style,
    linewidth=2,
    alpha=0.6,
)

# Enhance the plot with a title, labels, and legend
ax.set_title(title)
ax.set_xlabel(xlabel_value)
ax.set_ylabel(ylabel_value)

# Add a legend to the plot
ax.set_ylim(ylim_values)

# Show the plot
ax.legend(loc="upper right", frameon=True, shadow=True)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout for better spacing and display
plt.tight_layout()

# Save the plot
plt.savefig('line_59.pdf', bbox_inches='tight')
