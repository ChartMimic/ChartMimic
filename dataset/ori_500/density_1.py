# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Generate data for the plot
x = np.linspace(8, 15, 1000)
y = [
    np.random.uniform(0.5, 1.5)
    * np.exp(-0.5 * (x - i) ** 2 / np.linspace(0.1, 0.5, 9)[index])
    for index, i in enumerate(np.linspace(9.5, 13, 9))
]
cbar_label = "Iteration"
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Set the figure size to match the original image's dimensions
fig, ax = plt.subplots(figsize=(10, 3))

# Create a colorbar
sm = plt.cm.ScalarMappable(cmap="coolwarm", norm=plt.Normalize(vmin=0, vmax=25))
cbar = plt.colorbar(sm, ax=ax, label=cbar_label)
cbar.set_label(cbar_label, rotation=270, labelpad=15)

for i in range(9):
    plt.fill_between(x, y[i], color=plt.cm.coolwarm(i / 9), alpha=0.9)
plt.ylim(0, 2)
# Remove the plot border
plt.gca().spines["top"].set_visible(False)
plt.gca().spines["right"].set_visible(False)
plt.gca().spines["bottom"].set_visible(True)
plt.gca().spines["left"].set_visible(False)
plt.gca().set_yticks([])

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig("density_1.pdf", bbox_inches="tight")
