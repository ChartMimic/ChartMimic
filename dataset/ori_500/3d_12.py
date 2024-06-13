# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
x = np.array([-5.0, -3.75, -2.5, -1.25, 0.0, 1.25, 2.5, 3.75, 5.0])
y = np.array([-5.0, -3.75, -2.5, -1.25, 0.0, 1.25, 2.5, 3.75, 5.0])
z = np.array([-22.47, -18.95, -11.54, -2.77, 2.74, 3.3, 13.4, 17.45, 23.79])
z_fit = np.array([-22.8, -16.96, -11.12, -5.29, 0.55, 6.39, 12.22, 18.06, 23.9])

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection="3d")

ax.scatter(x, y, z, color="r", label="Discrete Points", marker="o")
ax.plot(x, y, z_fit, color="b", label="Fit Line")

ax.set_xlabel("Temperature (°C)")
ax.set_ylabel("Pressure (kPa)")
ax.set_zlabel("Volume (L)")
ax.legend()

ax.set_box_aspect(aspect=None, zoom=0.8)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig("3d_12.pdf", bbox_inches="tight")
