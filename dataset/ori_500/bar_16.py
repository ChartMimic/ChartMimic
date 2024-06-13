# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

# ===================
# Part 2: Data Preparation
# ===================
# Data for the plots
roles = ["human", "gpt4", "gpt4-cot"]
counts_s1 = np.array([[100, 200, 500], [150, 300, 350], [200, 400, 200]])
counts_s2 = np.array([[150, 250, 400], [100, 350, 350], [250, 300, 250]])

# Colors for the bars
colors = ["skyblue", "gold", "lightcoral"]
width = 0.3

# Variables for plot configuration
xlim_value = (0, 800)
xlabel_value = "Count"
ylabel_value = "Role"
xticks_value = [0, 100, 200, 300, 400, 500, 600, 700, 800]
yticks_value = roles
title_s1 = "s1"
title_s2 = "s2"
legend_labels = ["O", "T", "P"]
fig_title = "Resonance Preference Plot for rich_context"
fontsize_title = 16

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create subplots with shared x-axis
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6), sharex=True)


# Function to plot stacked bars
def plot_stacked_bars(ax, counts, roles, colors):
    bottom = np.zeros(len(roles))
    for i in range(counts.shape[1]):
        ax.barh(
            roles, counts[:, i], height=width, zorder=5, left=bottom, color=colors[i]
        )
        bottom += counts[:, i]


# Plot for s1
plot_stacked_bars(ax1, counts_s1, roles, colors)
ax1.set_title(title_s1, y=1.2)
ax1.set_xlabel(xlabel_value)
ax1.set_ylabel(ylabel_value)
ax1.invert_yaxis()  # Invert y-axis to match the picture
ax1.grid(True, alpha=0.7)  # Add grid lines
ax1.set_xlim(*xlim_value)
ax1.tick_params(axis="y", which="both", length=0)
ax1.tick_params(axis="x", which="both", color="gray")

# Plot for s2
plot_stacked_bars(ax2, counts_s2, roles, colors)
ax2.set_title(title_s2)
ax2.set_xlabel(xlabel_value)
ax2.set_ylabel(ylabel_value)
ax2.set_xlim(*xlim_value)
ax2.invert_yaxis()  # Invert y-axis to match the picture
ax2.grid(True, alpha=0.7)  # Add grid lines
ax2.tick_params(axis="y", which="both", length=0)
ax2.tick_params(axis="x", which="both", color="gray")

# Legend
ax1.legend(
    legend_labels,
    bbox_to_anchor=(0.5, 1.2),
    loc="upper center",
    ncol=3,
    frameon=False,
)

# Set x-axis ticks after all plots
ax1.set_xticks(xticks_value)
ax2.set_xticks(xticks_value)
ax1.tick_params(axis="x", which="both", bottom=True, top=False, labelbottom=True)

# Title for the whole figure
fig.suptitle(fig_title, fontsize=fontsize_title)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout
plt.tight_layout()
plt.savefig("bar_16.pdf", bbox_inches="tight")
