# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Sample data to mimic the picture provided
data = np.random.beta(a=[2, 2, 1], b=[5, 2, 3], size=(100, 3))
data_memory = np.random.beta(a=[2, 5, 2], b=[2, 1, 2], size=(100, 3))

categories = ["Efficiency", "Comfort", "Safety"]
violin_width = 0.02

# Axes Limits and Labels
ylabel_value = "Score"
labels = ["Without Memory", "With Memory"]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Set the figure size
fig, ax = plt.subplots(
    figsize=(6, 6)
)  # Use the subplots function to create a figure and single axes

# Define the categories and the colors for each group
colors = ["#f0b7b0", "#b8cce1"]

# The scaling factor is used to ensure the violins do not overlap
scaling_factor = 1

# Define offset to separate the half violin plots in the single Axes object
offsets = [-0.05, 0, 0.05]

# Plot the half-violins with an offset
for i, category in enumerate(categories):
    offset = offsets[i]

    # Plot data without memory
    kde_data = gaussian_kde(data[:, i])
    kde_x = np.linspace(0, 1, 300)
    kde_data_y = kde_data(kde_x)
    kde_data_y_scaled = kde_data_y / max(kde_data_y) * violin_width
    ax.fill_betweenx(
        kde_x,
        kde_data_y_scaled * scaling_factor + offset,
        offset,
        color=colors[0],
        edgecolor="#9e8d8b",
    )

    # Plot data with memory
    kde_data_memory = gaussian_kde(data_memory[:, i])
    kde_data_memory_y = kde_data_memory(kde_x)
    kde_data_memory_y_scaled = kde_data_memory_y / max(kde_data_memory_y) * violin_width
    ax.fill_betweenx(
        kde_x,
        offset,
        -kde_data_memory_y_scaled * scaling_factor + offset,
        color=colors[1],
        edgecolor="#9e8d8b",
    )
    ax.text(
        offset, -0.1, category, ha="center", va="top"
    )  # Add the category label below the violin plot

# Set x and y axis labels and limits
ax.set_xlim(
    min(offsets) - scaling_factor * violin_width - 0.01,
    max(offsets) + scaling_factor * violin_width + 0.01,
)
y_margin = 0.01  # Adding 5% margin at top and bottom of the y-axis
y_min, y_max = ax.get_ylim()
ax.set_ylim(y_min - y_margin, y_max + y_margin)
ax.set_ylabel(ylabel_value)
ax.set_xticks([])  # Remove x-ticks as they are not meaningful here

# Adjust the legend
handles = [
    plt.Rectangle((0, 0), 1, 1, color=color, edgecolor="#9e8d8b") for color in colors
]
ax.legend(handles, labels, loc="lower left", bbox_to_anchor=(0.6, -0.2), ncol=1)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout for better fit and save the plot
plt.tight_layout()
plt.savefig('violin_2.pdf', bbox_inches='tight')
