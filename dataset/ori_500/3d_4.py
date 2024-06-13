# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Define the data for the surface plots (assuming some function f(m, n))
m = np.linspace(-100, 100, 200)  # Increased resolution
n = np.linspace(-100, 100, 200)  # Increased resolution
m, n = np.meshgrid(m, n)
z1 = 0.01 * (m**2 + n**2)  # Adjust the function to create a concave shape
z2 = 0.01 * (m**2 + n**2)
z3 = np.sqrt(m**2 + n**2)
z4 = np.log(m**2 + n**2 + 1)

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create a figure with specified size to match the original image's dimensions
fig = plt.figure(figsize=(15, 10))

# Plot the first subplot
ax1 = fig.add_subplot(
    141, projection="3d", facecolor="white"
)  # Set background to white
surf1 = ax1.plot_surface(m, n, z1, cmap="viridis")
ax1.set_title("Origin", fontsize=12, y=-0.1)
ax1.set_xlabel("m", fontsize=12)  # Increased font size
ax1.set_ylabel("n", fontsize=12)  # Increased font size
ax1.set_zlabel("FREEDOM", fontsize=12)  # Increased font size

# Plot the second subplot
ax2 = fig.add_subplot(142, projection="3d", facecolor="white")
surf2 = ax2.plot_surface(m, n, z2, cmap="viridis")
ax2.set_title("MG (ours)", fontsize=14, y=-0.1)
ax2.set_xlabel("m", fontsize=12)
ax2.set_ylabel("n", fontsize=12)
ax2.set_zlabel("FREEDOM", fontsize=12, y=-0.3, rotation=0)

# Plot the third subplot
ax3 = fig.add_subplot(143, projection="3d", facecolor="white")
surf3 = ax3.plot_surface(m, n, z3, cmap="viridis")
ax3.set_title("Origin", fontsize=14, y=-0.1)
ax3.set_xlabel("m", fontsize=12)
ax3.set_ylabel("n", fontsize=12)
ax3.set_zlabel("BM3", fontsize=12, rotation=90)

# Plot the fourth subplot
ax4 = fig.add_subplot(144, projection="3d", facecolor="white")
surf4 = ax4.plot_surface(m, n, z4, cmap="viridis")
ax4.set_title("MG (ours)", fontsize=14, y=-0.1)
ax4.set_xlabel("m", fontsize=12)
ax4.set_ylabel("n", fontsize=12)
ax4.set_zlabel("BM3", fontsize=12, rotation=90, x=-100)

# Zoom all the subplots
ax1.set_box_aspect(aspect=None, zoom=0.83)
ax2.set_box_aspect(aspect=None, zoom=0.83)
ax3.set_box_aspect(aspect=None, zoom=0.83)
ax4.set_box_aspect(aspect=None, zoom=0.83)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and spacing
plt.tight_layout()

# Show the plot
plt.savefig("3d_4.pdf", bbox_inches="tight")
