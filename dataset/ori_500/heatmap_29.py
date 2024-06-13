# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import matplotlib.colors as colors

# ===================
# Part 2: Data Preparation
# ===================
# Data
data = [[23, 35, 75, 55], [28, 34, 0, 0], [36, 53, 5, 38], [17, 79, 4, 42]]
yticklabels = ["Low", "Medium", "High"]
title = "Degree of acceptance of a product"


# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# with blue and green colors
colors_list = ["#0099ff", "#33cc33"]
cmap = colors.ListedColormap(colors_list)
plt.figure(figsize=(5, 4))
# Plot the heatmap with custom colors and annotations
plt.imshow(data, cmap=cmap, vmin=0, vmax=100, extent=[0, 4, 0, 4])
for i in range(4):
    for j in range(4):
        plt.annotate(
            str(data[i][j]),
            xy=(j + 0.5, i + 0.5),
            ha="center",
            va="center",
            color="white",
        )

# Add colorbar
cbar = plt.colorbar(ticks=[0, 50, 100])
cbar.ax.set_yticklabels(yticklabels)

# Set plot title and axis labels
plt.title(title)
plt.xticks([])
plt.yticks([])

# ===================
# Part 4: Saving Output
# ===================
# Display the plot
plt.tight_layout()
plt.savefig("heatmap_29.pdf", bbox_inches="tight")
