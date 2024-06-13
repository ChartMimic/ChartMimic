# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

# ===================
# Part 2: Data Preparation
# ===================
# Sample data for the plot; replace with actual data.
methods = ["CoT", "ToT", "Self-refine", "MAD+judge", "SPP", "DefInt"]
colors = [
    "black",
    "green",
    "red",
    "orange",
    "purple",
    "brown",
]  # Colors for each method.

# Data for the subplots; each list within diversity_data and accuracy_data corresponds to a subplot.
diversity_data = [[1.2, 2.1, 1.7, 1.9, 1.6, 1.3], [3.8, 5.1, 5.7, 4.9, 4.6, 4.3]]

accuracy_data = [[50, 45, 25, 65, 40, 70], [30, 40, 90, 85, 80, 82]]

# Sizes for the scatter points, shared across both subplots.
scatter_sizes = [50, 100, 100, 175, 300, 300]

# Legend labels for the subplots.
ax1_legend_names = ["1.0", "2.5", "10.0", "25.0"]
ax2_legend_names = ["2.0e+04", "1.0e+05", "4.0e+05", "1.6e+06"]
ax1_legend_title = "Token cost($)"
ax2_legend_title = "TFLOPS"
xlabel = "Diversity"
ylabel = "Accuracy (%)"
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create 2x1 grid of subplots with a specified figure size.
fig, axs = plt.subplots(2, 1, figsize=(6, 6))

# Populate the subplots with scatter points and add text labels.
for idx, ax in enumerate(axs):
    for method, div, acc, size, color in zip(
        methods, diversity_data[idx], accuracy_data[idx], scatter_sizes, colors
    ):
        ax.scatter(div, acc, s=size, color=color, alpha=0.5)  # Plot the scatter points.
        ax.text(
            div, acc + 5, method, fontsize=9
        )  # Add text labels above scatter points.

    ax.set_xlabel(xlabel)  # X-axis label.
    ax.set_ylabel(ylabel)  # Y-axis label.

# Adjust the x and y limits and ticks for the subplots.
axs[0].set_xlim(1.0, 2.6)
axs[0].set_ylim(10, 90)
axs[0].set_xticks([1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4])
axs[0].set_yticks([10, 30, 50, 70, 90])
axs[1].set_xlim(3.5, 6.5)
axs[1].set_ylim(20, 100)
axs[1].set_xticks([4.0, 4.5, 5.0, 5.5, 6.0])
axs[1].set_yticks([20, 40, 60, 80, 100])


size_legend_handles = [50, 100, 175, 250]  # Sizes for the legend handles.

# Create custom legend handles for the first subplot.
ax1_legend_handles = [
    mlines.Line2D(
        [],
        [],
        color="#8080f7",
        marker="o",
        linestyle="None",
        markersize=(size**0.5) * 0.8,
        label=name,
    )  # Adjust marker size here.
    for size, name in zip(size_legend_handles, ax1_legend_names)
]

# Create custom legend handles for the second subplot.
ax2_legend_handles = [
    mlines.Line2D(
        [],
        [],
        color="#8080f7",
        marker="o",
        linestyle="None",
        markersize=(size**0.5) * 0.8,
        label=name,
    )  # Adjust marker size here.
    for size, name in zip(size_legend_handles, ax2_legend_names)
]

# Add legends to the subplots.
axs[0].legend(
    handles=ax1_legend_handles,
    loc="lower right",
    title=ax1_legend_title,
    labelspacing=2.0,
    edgecolor="black",
)
axs[1].legend(
    handles=ax2_legend_handles,
    loc="lower right",
    title=ax2_legend_title,
    labelspacing=2.0,
    edgecolor="black",
)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig('scatters_3.pdf', bbox_inches='tight')
