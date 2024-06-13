# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)

# ===================
# Part 2: Data Preparation
# ===================
# Enhanced seaborn style for a fancier look
iterations = np.linspace(0, 200, 200)

# Simulated data based on the previous setup
base_data = np.linspace(0.5, 0.2, 200) * (1 + np.random.normal(0, 0.05, 200))
ours_data = np.linspace(0.4, 0.3, 200) * (1 + np.random.normal(0, 0.05, 200))

# Axes Limits and Labels
xlabel_value = "Training Iterations"
ylabel_value = "Metric Value"
ylim_values = [0.15, 0.76]

# Labels
labels = ["Base Model", "Our Model"]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create a 1x2 subplot layout
fig, axs = plt.subplots(1, 2, figsize=(10, 4))

colors = ["#0072B2", "#D55E00"]  # Blue and orange colors for the lines

# Plot the data in each subplot
for i, ax in enumerate(axs.flat):
    ax.plot(
        iterations,
        base_data * (1 + 0.1 * np.random.randn(1)),
        label=labels[0],
        color=colors[0],
        marker="o",
        markersize=3,
        linewidth=2,
    )
    ax.plot(
        iterations,
        ours_data * (1 + 0.1 * np.random.randn(1)),
        label=labels[1],
        color=colors[1],
        marker="x",
        markersize=3,
        linewidth=2,
    )
    ax.set_title(f"Metric {i+1}")
    ax.set_xlabel(xlabel_value)
    ax.set_ylabel(ylabel_value)
    ax.set_ylim(ylim_values)  # Ensure consistent y-axis limits
    ax.legend(loc="upper right", frameon=True)  # Add a legend

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout for better spacing and display
plt.tight_layout()

# Show the plot
plt.savefig('line_58.pdf', bbox_inches='tight')
