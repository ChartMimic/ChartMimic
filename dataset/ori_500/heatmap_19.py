# ===================
# Part 1: Importing Libraries
# ===================
import numpy as np

np.random.seed(0)

import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

# ===================
# Part 2: Data Preparation
# ===================
# Defining the colormap from white to blue
cmap = plt.cm.Blues

# Data for the two subplots
data1 = np.array(
    [
        [50.3, 12.0, 0.9, 7.0, 13.4, 16.3],
        [49.2, 11.2, 0.6, 7.8, 17.3, 13.9],
        [50.8, 12.3, 0.9, 6.2, 15.5, 14.3],
        [76.0, 2.1, 0.5, 4.1, 8.1, 9.2],
        [15.7, 28.1, 2.6, 14.5, 28.6, 10.5],
    ]
)

data2 = np.array(
    [
        [61.5, 2.0, 8.7, 14.9, 13.0, 4.0],
        [44.4, 10.0, 7.8, 22.9, 25.0, 2.0],
        [38.6, 2.2, 0.8, 55.3, 3.1, 1.0],
        [35.3, 2.2, 4.0, 32.5, 26.0, 0.8],
        [31.5, 4.3, 17.4, 2.5, 27.1, 17.3],
    ]
)

# X and Y labels
x_labels = ["Werewolf", "Seer", "Witch", "Hunter", "Villager", "Abstain"]
y_labels = ["Werewolf", "Seer", "Witch", "Hunter", "Villager"]

# Subplot titles
titles = ["(a) Role voting in the Werewolf game", "(b) Final state of roles"]

# Set up the colormap and norm (log scale)
norm = LogNorm(vmin=0.1, vmax=100)

# Axes Limits and Labels
xticks_values = range(len(x_labels))
yticks_values = range(len(y_labels))
colorbar_ticks = [0.1, 1, 10, 100]
yticklabels = ["0.1", "1", "10", "100"]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Set up the figure
fig, axes = plt.subplots(
    1, 2, figsize=(20, 8), gridspec_kw={"width_ratios": [1, 1], "wspace": 0.3}
)


# Function to create a subplot
def create_subplot(ax, data, title):
    # Create the scatter plot
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            # Calculate the color based on the original value
            color = cmap(norm(data[i, j]))

            # Draw the circle with a fixed size
            circle = plt.Circle((j, i), 0.4, color=color)  # Fixed size
            ax.add_artist(circle)

            # Determine text color based on the value
            text_color = "white" if data[i, j] > 25 else "black"

            # Add the text inside the circle
            ax.text(
                j, i, f"{data[i, j]:.1f}%", ha="center", va="center", color=text_color
            )

    # Set labels for x and y axes
    ax.set_xticks(range(len(x_labels)))
    ax.set_xticklabels(x_labels, ha="center")
    ax.set_yticks(range(len(y_labels)))
    ax.set_yticklabels(y_labels, va="center")

    # Adding the title for the subplot
    ax.set_title(title, fontsize=16)

    # Set the limits of the axes; they should be one more than your data range
    ax.set_xlim(-0.5, data.shape[1] - 0.5)
    ax.set_ylim(-0.5, data.shape[0] - 0.5)

    # Set the aspect of the plot to be equal and add a frame
    ax.set_aspect("equal")
    for spine in ax.spines.values():
        spine.set_visible(True)


# Create each subplot
create_subplot(axes[0], data1, titles[0])
create_subplot(axes[1], data2, titles[1])

# Create a colorbar on the far right side of the figure
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
cbar = fig.colorbar(
    sm,
    ax=axes,
    ticks=colorbar_ticks,
    orientation="vertical",
    fraction=0.015,
    pad=0.05,
)
cbar.ax.set_yticklabels(yticklabels)

# ===================
# Part 4: Saving Output
# ===================
# Show the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig("heatmap_19.pdf", bbox_inches="tight")
