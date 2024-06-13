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
counts_s3 = np.array([[100, 270, 430], [150, 350, 300], [270, 300, 230]])

# Colors for the bars
colors = ["#7cb7ef", "#829be6", "#f2d18b"]
colors2 = ["#97e4a0", "#eea092", "#a093d7"]
width = 0.3
legendtitle = ["O1", "T1", "P1"]
titles = ["s1", "s2", "s3"]
ylabel = "Role"
xlabel = "Count"
xticks = [0, 100, 200, 300, 400, 500, 600, 700, 800]
suptitle = "Resonance Preference Plot for rich_context"


# Function to plot stacked bars
def plot_stacked_bars(ax, counts, roles, colors):
    bottom = np.zeros(len(roles))
    for i in range(counts.shape[1]):
        ax.barh(roles, counts[:, i], height=width, left=bottom, color=colors[i])
        bottom += counts[:, i]


# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create subplots with shared x-axis
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 6), sharex=True)

# Plot for s1
plot_stacked_bars(ax1, counts_s1, roles, colors)
ax1.set_title(titles[0])
ax1.set_ylabel(ylabel)
ax1.invert_yaxis()  # Invert y-axis to match the picture
ax1.grid(True, alpha=0.7)  # Add grid lines

# Plot for s2
plot_stacked_bars(ax2, counts_s2, roles, colors)
ax2.set_title(titles[1])
ax2.set_ylabel(ylabel)
ax2.invert_yaxis()  # Invert y-axis to match the picture
ax2.grid(True, alpha=0.7)  # Add grid lines

# Plot for s3
plot_stacked_bars(ax3, counts_s3, roles, colors2)
ax3.set_title(titles[2])
ax3.set_xlabel(xlabel)
ax3.set_ylabel(ylabel)
ax3.invert_yaxis()  # Invert y-axis to match the picture
ax3.grid(True, alpha=0.7)  # Add grid lines

# Legend
ax1.legend(legendtitle, bbox_to_anchor=(1.05, 1), loc="upper left")
ax2.legend(legendtitle, bbox_to_anchor=[1.05, 1], loc="upper left")
ax3.legend(legendtitle, bbox_to_anchor=[1.05, 1], loc="upper left")

# Set x-axis ticks after all plots
ax1.set_xticks(xticks)
ax2.set_xticks(xticks)
ax3.set_xticks(xticks)
ax1.tick_params(axis="x", which="both", bottom=True, top=False, labelbottom=True)

# Title for the whole figure
fig.suptitle(suptitle)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout
plt.tight_layout()
plt.savefig("bar_92.pdf", bbox_inches="tight")
