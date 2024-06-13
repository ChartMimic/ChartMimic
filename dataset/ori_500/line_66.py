# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data for the plot
iterations = np.array([0, 250, 500, 750, 1000, 1250, 1500, 1750, 2000])

# Simulated data for the models
data = {
    "model1": (
        np.linspace(0.1, 0.95, 9) + np.random.normal(0, 0.05, 9),
        np.linspace(0.2, 0.85, 9) + np.random.normal(0, 0.05, 9),
    ),
    "model2": (
        np.linspace(0.2, 0.9, 9) + np.random.normal(0, 0.05, 9),
        np.linspace(0.1, 0.88, 9) + np.random.normal(0, 0.05, 9),
    ),
    "model3": (
        np.linspace(0.15, 0.88, 9) + np.random.normal(0, 0.05, 9),
        np.linspace(0.2, 0.83, 9) + np.random.normal(0, 0.05, 9),
    ),
    "model4": (
        np.linspace(0.05, 0.8, 9) + np.random.normal(0, 0.05, 9),
        np.linspace(0.15, 0.78, 9) + np.random.normal(0, 0.05, 9),
    ),
}

# Axes Limits and Labels
xlabel_value = "Iterations"
xticks_values = np.arange(0, 2250, 250)

ylabel_value = "Success Rate"
ylim_values = [0, 1]

# Labels
label_1 = " Series 1"
label_2 = " Series 2"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create a figure and axis
plt.figure(figsize=(9, 7))

# Plot the data for each model
colors = ["#0a6ae1", "#d75faa"]
markers = ["o", "v"]

# Plot the data for each model
for i, (key, (series1, series2)) in enumerate(data.items()):
    ax = plt.subplot(2, 2, i + 1)
    ax.plot(
        iterations,
        series1,
        marker=markers[0],
        color=colors[0],
        markerfacecolor=colors[0],
        linewidth=2,
        markersize=5,
        label=f"{key}{label_1}",
    )
    ax.plot(
        iterations,
        series2,
        marker=markers[1],
        color=colors[1],
        markerfacecolor=colors[1],
        linewidth=2,
        markersize=5,
        label=f"{key}{label_2}",
    )
    ax.fill_between(
        iterations, series1 - 0.05, series1 + 0.05, color=colors[0], alpha=0.1
    )
    ax.fill_between(
        iterations, series2 - 0.03, series2 + 0.03, color=colors[1], alpha=0.1
    )
    ax.set_title(f"{key} Performance", fontsize=14)
    ax.set_xlabel(xlabel_value, fontsize=12)
    ax.set_ylabel(ylabel_value, fontsize=12)
    ax.set_ylim(ylim_values)
    ax.set_xticks(xticks_values)
    ax.legend()
    ax.grid(True, linestyle="--", linewidth=0.5)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout for better spacing and display
plt.tight_layout()

# Show the plot
plt.savefig('line_66.pdf', bbox_inches='tight')
