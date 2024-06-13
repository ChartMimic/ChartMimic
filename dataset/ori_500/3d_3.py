# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data for plotting
K = np.array(
    [
        [1, 2, 3, 4, 5, 6],
        [1, 2, 3, 4, 5, 6],
        [1, 2, 3, 4, 5, 6],
        [1, 2, 3, 4, 5, 6],
        [1, 2, 3, 4, 5, 6],
        [1, 2, 3, 4, 5, 6],
    ]
)
tau = np.array(
    [
        [1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
        [1.1, 1.1, 1.1, 1.1, 1.1, 1.1],
        [1.3, 1.3, 1.3, 1.3, 1.3, 1.3],
        [1.5, 1.5, 1.5, 1.5, 1.5, 1.5],
        [1.8, 1.8, 1.8, 1.8, 1.8, 1.8],
        [2.0, 2.0, 2.0, 2.0, 2.0, 2.0],
    ]
)
accuracy = np.array(
    [
        [82, 84, 86, 88, 90, 89],
        [83, 85, 87, 89, 91, 87],
        [84, 86, 88, 90, 92, 88],
        [85, 87, 89, 91, 93, 89],
        [86, 88, 90, 92, 94, 87],
        [87, 89, 91, 93, 95, 88],
    ]
)

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plotting
fig = plt.figure(
    figsize=(10, 6)
)  # Adjusting figure size to match original image's dimensions
ax = fig.add_subplot(111, projection="3d")

# Plot a 3D surface
surf = ax.plot_surface(K, tau, accuracy, cmap="magma", edgecolor="black")

# Labels and title
ax.set_xlabel("K")
ax.set_ylabel("tau")
ax.set_zlabel("Accuracy (%)")
ax.set_title("CIFAR10 Spiking ResNet18\nT = 6", y=1.00)
ax.set_box_aspect(aspect=None, zoom=0.9)

# ===================
# Part 4: Saving Output
# ===================
# Saving the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig("3d_3.pdf", bbox_inches="tight")
