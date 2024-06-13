# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================

# Data for bar plot
categories = ["Sentiment", "Toxicity", "News"]
values = [0.35, 0.2, 0.3]

# Data for heatmap
data = np.array(
    [[-0.4, 0.14, 0.22, 0.13], [-0.13, -0.029, 0.17, 0.12], [-0.24, 0.052, 0.31, 0.17]]
)
rows = ["Sentiment", "Toxicity", "News"]
columns = ["Unchanged Correct", "Unfixed Mistake", "New Correct", "New Mistake"]
ylabel="Correlation"
ylim=[0, 0.4]
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create the bar plot on the left
# Set the figure size to match the original image's dimensions
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
bars = plt.bar(categories, values, color="#376686")
plt.ylabel(ylabel)
plt.ylim(ylim)
# Create the heatmap on the right
plt.subplot(1, 2, 2)
heatmap = plt.imshow(
    data, cmap="coolwarm", interpolation="nearest", vmin=-1.0, vmax=1.0
)
plt.xticks(np.arange(len(columns)), columns, rotation=30, ha="right")
plt.yticks(np.arange(len(rows)), rows)
plt.colorbar(heatmap)

# Annotate the heatmap with text
for i in range(len(rows)):
    for j in range(len(columns)):
        plt.text(j, i, f"{data[i, j]:.2f}", ha="center", va="center", color="black")

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout to prevent overlap
plt.tight_layout()

plt.savefig('multidiff_15.pdf', bbox_inches='tight')
