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

# Sample data: a 5x6 grid, similar to the provided heatmap
data = np.array(
    [
        [50.3, 12.0, 0.9, 7.0, 13.4, 16.3],
        [49.2, 11.2, 0.6, 7.8, 17.3, 13.9],
        [50.8, 12.3, 0.9, 6.2, 15.5, 14.3],
        [76.0, 2.1, 0.5, 4.1, 8.1, 9.2],
        [15.7, 28.1, 2.6, 14.5, 28.6, 10.5],
    ]
)

# X and Y labels
xticklabels = ["Werewolf", "Seer", "Witch", "Hunter", "Villager", "Abstain"]
yticklabels = ["Werewolf", "Seer", "Witch", "Hunter", "Villager"]
x_label = "Votee"
y_label = "Voter"
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Set up the figure and axis
fig, ax = plt.subplots(figsize=(10, 8))

# Set up the colormap and norm (log scale)
norm = LogNorm(vmin=0.1, vmax=100)

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
        ax.text(j, i, f"{data[i, j]:.1f}%", ha="center", va="center", color=text_color)

# Set labels for x and y axes
ax.set_xticks(range(len(xticklabels)))
ax.set_xticklabels(xticklabels, ha="center")
ax.set_yticks(range(len(yticklabels)))
ax.set_yticklabels(yticklabels, va="center")

# Adding titles for the axes
ax.set_xlabel(x_label, fontsize=14)
ax.set_ylabel(y_label, fontsize=14)

# Set the limits of the axes; they should be one more than your data range
ax.set_xlim(-0.5, data.shape[1] - 0.5)
ax.set_ylim(-0.5, data.shape[0] - 0.5)

# Set the aspect of the plot to be equal and add a frame
ax.set_aspect("equal")
for spine in ax.spines.values():
    spine.set_visible(True)

# Create a colorbar
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
cbar = plt.colorbar(sm, ax=ax, ticks=[0.1, 1, 10, 100], orientation="vertical")
cbar.ax.set_yticklabels(["0.1", "1", "10", "100"])

# Add gridlines
plt.grid(True, which="both", color="gray", linestyle="--", linewidth=0.5)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout to fit the figure size
plt.tight_layout()

# Show the plot
plt.savefig("heatmap_21.pdf", bbox_inches="tight")
