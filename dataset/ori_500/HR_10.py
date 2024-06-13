# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
start_r = 1
end_r = 10
num_points = 2000
ellipse_ratio = 1.2
# Generate theta values
theta = np.linspace(0, 20 * np.pi, num_points)  # Increase the range for more loops

# Exponential function for r to make the spiral more compact
r = start_r + (end_r - start_r) * (theta / max(theta)) ** 2
# Convert to Cartesian coordinates with scaling for the ellipse
x = r * np.cos(theta) * ellipse_ratio
y = r * np.sin(theta)
label = "SINDy"
title = "Compact Spiral with Elliptical Hollow Center"


# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plot
plt.figure(figsize=(8, 8))
plt.plot(x, y, label=label)
plt.plot(x[0], y[0], "ko")
plt.title(title)
plt.axis("equal")  # Ensure the aspect ratio is equal
plt.gca().set_aspect("equal", adjustable="box")  # Adjust aspect ratio
plt.legend()

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig("HR_10.pdf", bbox_inches="tight")
