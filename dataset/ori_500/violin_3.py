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
data_5_groups = np.random.beta(a=[2, 2, 1, 2, 2], b=[5, 2, 3, 2, 5], size=(100, 5))
data_memory_5_groups = np.random.beta(
    a=[2, 5, 2, 2, 2], b=[2, 1, 2, 5, 2], size=(100, 5)
)

data_3_groups = np.random.beta(a=[2, 2, 1], b=[5, 2, 3], size=(100, 3))
data_memory_3_groups = np.random.beta(a=[2, 5, 2], b=[2, 1, 2], size=(100, 3))
ylabel="Length Distribution"
ylim=[0, 1]
violin_width = 0.5
scaling_factor = 1
kde_x = np.linspace(0, 1, 300)

# Offsets for groups
offsets_5_groups = np.linspace(-3, 3, 5)
offsets_3_groups = np.linspace(-3, 3, 3)
labels=["Without Memory", "With Memory"]
titles=["Scoring Evaluation", "Pair Comparison"]
legend_labels = ["GPT-4V(Vision)", "Gemini"]
xticklabels=[ ["1", "2", "3", "4", "5"], ["Winner", "Losser Preference", "Tie"]]


# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))

# Define the colors for each group
colors_5_groups = ["#e4aa90", "#9cc39f"]
colors_3_groups = ["#e4aa90", "#9cc39f"]

# Function to plot half violins
def plot_half_violins(
    ax, data, data_memory, offsets, colors, labels, title, xticklabels
):
    # Plot the half-violins with an offset for groups
    for i in range(data.shape[1]):
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
        kde_data_memory_y_scaled = (
            kde_data_memory_y / max(kde_data_memory_y) * violin_width
        )
        ax.fill_betweenx(
            kde_x,
            offset,
            -kde_data_memory_y_scaled * scaling_factor + offset,
            color=colors[1],
            edgecolor="#9e8d8b",
        )

    # Set x and y axis labels, limits, and add x-axis tick labels for groups
    ax.set_xlim(
        min(offsets) - scaling_factor - violin_width,
        max(offsets) + scaling_factor + violin_width,
    )
    ax.set_ylim(ylim)  # Set y-axis limits to 0-1 for beta distribution
    ax.set_ylabel(ylabel)
    ax.set_xticks(offsets)  # Set x-ticks to the center of each group
    ax.set_xticklabels(xticklabels)  # Label x-ticks accordingly
    ax.title.set_text(title)


# Plot each set of violins
plot_half_violins(
    ax1,
    data_5_groups,
    data_memory_5_groups,
    offsets_5_groups,
    colors_5_groups,
    labels,
    titles[0],
    xticklabels[0],
)
plot_half_violins(
    ax2,
    data_3_groups,
    data_memory_3_groups,
    offsets_3_groups,
    colors_3_groups,
    labels,
    titles[1],
    xticklabels[1],
)

# Add a legend for the entire figure
handles = [
    plt.Line2D(
        [0], [0], marker="o", color="w", markerfacecolor="#9cc39f", markersize=10
    ),
    plt.Line2D(
        [0], [0], marker="o", color="w", markerfacecolor="#e4aa90", markersize=10
    ),
]

fig.legend(handles, legend_labels, loc="lower center", bbox_to_anchor=(0.5, -0.05), ncol=2)

# ===================
# Part 4: Saving Output
# ===================
# Tighten the layout and show the combined plot
plt.tight_layout()

# Display the plot
plt.savefig('violin_3.pdf', bbox_inches='tight')
