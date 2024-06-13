# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Define the Gaussian function
def gaussian(x, y, sigma=0.1, mu=0):
    return np.exp(-((x - mu) ** 2 + (y - mu) ** 2) / (2.0 * sigma**2))


# Create a grid of points
x = np.linspace(-1, 1, 100)
y = np.linspace(-1, 1, 100)
x, y = np.meshgrid(x, y)
z1 = -gaussian(x, y, sigma=0.4)
z2 = gaussian(x, y, sigma=0.3)

# Axes Limits and Labels
ax1_title = "f(x)"
xlim1_values = np.linspace(-1, 1, 9)
ylim1_values = np.linspace(-1, 1, 9)
ax2_title = "solution"
xlim2_values = np.linspace(-1, 1, 9)
ylim2_values = np.linspace(-1, 1, 9)


# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create the figure with specified size
fig = plt.figure(figsize=(10, 7))

# First subplot
ax1 = fig.add_subplot(121, projection="3d")
ax1.plot_surface(x, y, z1, cmap="jet")
ax1.set_title(ax1_title)
ax1.set_xticks(xlim1_values)
ax1.set_xticklabels(xlim1_values, rotation=45)
ax1.set_yticks(ylim1_values)
ax1.set_yticklabels(ylim1_values, rotation=0)

# Second subplot
ax2 = fig.add_subplot(122, projection="3d")
ax2.plot_surface(x, y, z2, cmap="jet")
ax2.set_title(ax2_title)
ax2.set_xticks(xlim2_values)
ax2.set_xticklabels(xlim2_values, rotation=45)
ax2.set_yticks(ylim2_values)
ax2.set_yticklabels(ylim2_values, rotation=0)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save the figure
plt.tight_layout()
plt.savefig("3d_2.pdf", bbox_inches="tight")
