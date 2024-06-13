# ===================
# Part 1: Importing Libraries
# ===================
import numpy as np; np.random.seed(0)

import matplotlib.pyplot as plt


# ===================
# Part 2: Data Preparation
# ===================
# Define the vector field function
def vector_field(X, Y):
    # Placeholder function for the vector field
    # Replace with the actual function based on the provided image
    U = -Y
    V = X
    return U, V


# Create a finer grid of points
x = np.linspace(-2.0, 2.0, 20)
y = np.linspace(-2.0, 2.0, 20)
X, Y = np.meshgrid(x, y)

# Compute the vector field
U, V = vector_field(X, Y)
xlabel = "x"
ylabel = "y"
title = "Magnetic Field $\\vec{B}$ in Tesla units"
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create the plot
fig, ax = plt.subplots(figsize=(6, 5))
# Use a more contrasting color scheme
colors = np.sqrt(U**2 + V**2)
ax.quiver(X, Y, U, V, colors, cmap="viridis")

# Add several streamlines to the vector field plot
# strm = ax.streamplot(X, Y, U, V, color='black', linewidth=0.5)

# Set labels and title
ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)
ax.set_title(title)

# Show grid
ax.grid(True, linestyle="--", alpha=0.7)

# Adjust the aspect ratio
ax.set_aspect("equal")

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout
plt.tight_layout()

# Display the plot
plt.savefig('quiver_5.pdf', bbox_inches='tight')
