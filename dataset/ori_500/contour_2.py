# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Create a grid of x and z values
x = np.linspace(0, 1, 100)
z = np.linspace(0, 1, 100)
X, Z = np.meshgrid(x, z)


# Adjust the lambda function to reflect the 3 different regions in the image
# Assuming that the regions are peaks and valleys, we might use a combination of Gaussian functions
def lambda_function(X, Z):
    # Parameters for the Gaussians might need to be fitted to the image
    # Here, we use arbitrary values just to illustrate the process
    return (
        np.exp(-((X - 0.2) ** 2 + (Z - 0.5) ** 2) / 0.01)
        + np.exp(-((X - 0.5) ** 2 + (Z - 0.1) ** 2) / 0.02)
        + np.exp(-((X - 0.8) ** 2 + (Z - 0.8) ** 2) / 0.08)
    )


# Calculate the function values on the grid
Z_values = lambda_function(X, Z)
xlabel = "$x_1$"
ylabel = "$x_2$"
title = "λ(x, z)"
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create the contour plot
plt.figure(figsize=(8, 6))

# Using a discrete colormap instead of 'viridis'
n_colors = 10  # Number of discrete colors in the colormap
discrete_cmap = plt.cm.get_cmap("summer", n_colors)

contour = plt.contourf(X, Z, Z_values, levels=n_colors, cmap=discrete_cmap)

# Add a color bar
cbar = plt.colorbar(
    contour, ticks=np.linspace(Z_values.min(), Z_values.max(), n_colors)
)

# Label the axes
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.title(title)

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()

# Show the plot
plt.savefig("contour_2.pdf", bbox_inches="tight")
