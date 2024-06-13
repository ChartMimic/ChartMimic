# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Generate distinct data sets for each subplot
N = np.array([10, 20, 30, 40, 50, 60])
datasets = {
    "Standard": np.power(10, -np.linspace(1, 6, len(N))),
    "Constrained": np.power(10, -np.linspace(6, 1, len(N))),
    "Innovative": np.power(10, -np.linspace(4, 2, len(N))) * 1.5,
    "Experimental": np.power(10, -np.linspace(2, 5, len(N))) * 2,  # New dataset
}

# Assign each dataset to a subplot
plot_order = ["Standard", "Constrained", "Innovative", "Experimental"]

# Axes Limits and Labels
xlabel_value = "N"

ylabel_value = "Precision"
ylim_values = [1e-14, 2]

# Text
text = "Peak Performance"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Set the figure size and define colors, markers, and linestyles
fig, axs = plt.subplots(2, 2, figsize=(12, 8))  # Use a 2x2 subplot grid
colors = ["deepskyblue", "magenta", "limegreen", "orange"]
markers = ["o", "s", "^", "d"]
linestyles = ["-", "--", ":", "-."]

# Plot data in each subplot
for i, (ax, key) in enumerate(zip(axs.flat, plot_order)):
    for j, data_key in enumerate(plot_order):
        if key == data_key:
            ax.loglog(
                N,
                datasets[data_key],
                linestyle=linestyles[j],
                marker=markers[j],
                color=colors[j],
                label=data_key,
                markersize=8,
            )
        else:
            ax.loglog(
                N,
                datasets[data_key],
                linestyle=linestyles[j],
                marker=markers[j],
                color=colors[j],
                label=data_key,
                markersize=8,
                alpha=0.8,
            )  # Faded other lines

    ax.set_xlabel(xlabel_value)
    ax.set_ylabel(ylabel_value)
    ax.set_ylim(ylim_values)  # Ensure y-axis ranges don't clip data
    ax.set_title(f"Graph Variation {i+1}")
    ax.legend()

    # Annotations to explain features, only on primary dataset for clarity
    if i == 0 or i == 3:
        ax.annotate(
            text,
            xy=(N[-2], datasets[key][-2]),
            xytext=(N[-4], datasets[key][-2] / 100),
            arrowprops=dict(arrowstyle="->", color="navy"),
            textcoords="data",
        )
    else:
        ax.annotate(
            text,
            xy=(N[-2], datasets[key][-2]),
            xytext=(N[-4], datasets[key][-2] * 10),
            arrowprops=dict(arrowstyle="->", color="navy"),
            textcoords="data",
        )

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout to prevent overlap and ensure clarity
plt.tight_layout()
plt.savefig('line_45.pdf', bbox_inches='tight')
