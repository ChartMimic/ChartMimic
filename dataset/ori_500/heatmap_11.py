# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data for the heatmap (randomly generated to match the color pattern)
data = np.array(
    [
        [0.8, 1.0, 0.4, 0.2, 0.1],
        [0.6, 0.7, 0.5, 0.3, 0.2],
        [0.4, 0.5, 0.6, 0.7, 0.8],
        [0.2, 0.3, 0.4, 0.5, 0.6],
        [0.1, 0.2, 0.3, 0.4, 0.5],
    ]
)

# Players' names for the axes
players = ["D. Fox", "T. Haliburton", "M. Harkless", "H. Barnes", "C. Metu"]
xlabel = "Players"
ylabel = "Players"
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create the heatmap
fig, ax = plt.subplots(figsize=(8, 6))  # Adjusting figure size
cax = ax.matshow(data, cmap="plasma")

# Set the ticks and labels
ax.set_xticks(np.arange(len(players)))
ax.set_yticks(np.arange(len(players)))

# Adjust the tick label alignment to ensure the x-axis labels appear only at the bottom
ax.tick_params(
    axis="x", which="both", bottom=True, top=False, labelbottom=True, labeltop=False
)
ax.tick_params(axis="y", which="both", right=False, left=False, labelleft=True)

# Set the labels for the x-axis and rotate them for better readability
ax.set_xticklabels(players, rotation=45)

# Set the labels for the y-axis
ax.set_yticklabels(players)

# Add colorbar with the correct range
cbar = plt.colorbar(cax, ticks=[0, 0.2, 0.4, 0.6, 0.8, 1])
cbar.ax.set_yticklabels(
    ["0", "0.2", "0.4", "0.6", "0.8", "1"]
)  # Set the colorbar labels

# Add labels for the axes
plt.xlabel(xlabel)
plt.ylabel(ylabel)

# ===================
# Part 4: Saving Output
# ===================
# Adjust the layout to add more space around the heatmap
plt.tight_layout()

# Show the plot
plt.savefig("heatmap_11.pdf", bbox_inches="tight")
