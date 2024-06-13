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


# Create a grid of points
x = np.linspace(-1.0, 1.0, 10)
y = np.linspace(-1.0, 1.0, 10)
X, Y = np.meshgrid(x, y)

# Compute the vector field
U, V = vector_field(X, Y)
xlabel = "x"
ylabel = "y"
title = "Vector Field: -F + ρ∇FF (Small ρ)"
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create the plot
fig, ax = plt.subplots(figsize=(5, 4))
ax.quiver(X, Y, U, V, color="#3171ad")

# Set labels and title
ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)
ax.set_title(title)

# Show grid
ax.grid(True, linestyle="--", alpha=0.5)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and display the plot
plt.tight_layout()
plt.savefig('quiver_4.pdf', bbox_inches='tight')
