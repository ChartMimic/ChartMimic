# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Create some data
y = np.linspace(0, 20, 100)
x1 = np.exp(-0.5 * (y - 5) ** 2)
x2 = 0.75 * np.exp(-0.2 * (y - 8) ** 2)

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create the figure and axis
fig, ax = plt.subplots(figsize=(8, 4))  # Adjusted to match the dimensions in pixels

# Plot the data
# ax.fill_between(x1, y, color="gray", edgecolor="#929292" ,alpha=0.5)
ax.fill_between(
    x2, y, color="pink", edgecolor="#be6373", alpha=0.5
)  # Adjusted to taper off the pink area

# Add the dashed vertical line at the peak of the gray area
# Add the red horizontal line at the bottom
# ax.axhline(0, color='red', linewidth=2)

# Customize the plot to match the picture
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(True)
ax.spines["bottom"].set_visible(False)
ax.tick_params(left=False, labelleft=False, bottom=False, labelbottom=False)

ax.set_ylim(1, 15)

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig("density_2.pdf", bbox_inches="tight")
