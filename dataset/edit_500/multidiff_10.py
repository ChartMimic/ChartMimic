import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Sample data for two heatmaps and one bar chart
num_attributes = 5

# Generate heatmap data for athlete performance correlations and comparisons
performance_comparison1 = np.random.rand(num_attributes, num_attributes) * 2 - 0.7 # Random values between -1 and 1
performance_comparison2 = np.random.rand(num_attributes, num_attributes) * 2 - 0.3  # Random values between -1 and 1

# Generate bar data for athlete performance metrics
performance_metrics = np.random.rand(num_attributes)  # Random values with a shift to mimic metrics

# Define attributes relevant to sports performance
attributes = ["Speed", "Stamina", "Strength", "Agility", "Flexibility"]

# Titles and labels for plots
heatmap_title = "Performance Attribute Correlation"
bar_xlabel = r"Performance Metric ($\tilde{I}_\infty$)"
bar_xticks = [0.00, 0.25, 0.50, 0.75, 1.00]
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create a figure with specific dimensions
fig = plt.figure(figsize=(8, 2))  # Adjust as needed

# Create a grid for subplots with adjusted width ratios
grid = plt.GridSpec(1, 3, width_ratios=[4, 4, 4], wspace=0.1)

# Create first heatmap subplot
heatmap_ax1 = plt.subplot(grid[0])
heatmap1 = heatmap_ax1.imshow(
    performance_comparison1, cmap="coolwarm", aspect="auto", vmin=-1, vmax=1.5
)
heatmap_ax1.set_xticks(np.arange(len(attributes)))
heatmap_ax1.set_yticks(np.arange(len(attributes)))
heatmap_ax1.set_xticklabels(attributes, rotation=45, ha="right")
heatmap_ax1.set_yticklabels(attributes)
heatmap_ax1.set_xlabel(heatmap_title)

# Create second heatmap subplot
heatmap_ax2 = plt.subplot(grid[1])
heatmap2 = heatmap_ax2.imshow(
    performance_comparison2, cmap="coolwarm", aspect="auto", vmin=-1, vmax=1.5
)
heatmap_ax2.set_xticks(np.arange(len(attributes)))
heatmap_ax2.set_yticks(np.arange(len(attributes)))
heatmap_ax2.set_xticklabels(attributes, rotation=45, ha="right")
heatmap_ax2.set_yticklabels([])
heatmap_ax2.set_xlabel(heatmap_title)
heatmap_ax2.yaxis.set_visible(False)

# Create an axes on the top side of ax_heatmap_top for the colorbar.
ax_colorbar = fig.add_axes(
    [
        heatmap_ax1.get_position().x0,
        heatmap_ax1.get_position().y1 + 0.05,
        heatmap_ax1.get_position().width * 2.1,
        0.05,
    ]
)
# Adding a colorbar at the very top of the heatmap
cbar = plt.colorbar(heatmap1, cax=ax_colorbar, orientation="horizontal")
cbar.ax.xaxis.set_ticks_position("top")

# Create bar chart subplot
bar_ax = plt.subplot(grid[2])
bar_ax.barh(attributes[::-1], performance_metrics, color=plt.cm.coolwarm(performance_metrics))
bar_ax.set_xlabel(bar_xlabel,fontsize=14)
bar_ax.set_xticks(bar_xticks)
bar_ax.yaxis.set_visible(False)
bar_ax.grid(True)
bar_ax.set_ylim(heatmap_ax1.get_ylim())

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save plot
plt.tight_layout()
plt.savefig('multidiff_10.pdf', bbox_inches='tight')
