# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
red = np.array([[10.0, 20.0], [10.0, 30.0], [-50.0, -40.0]])
blue = np.array([[20.0, 30.0], [40.0, 70.0], [-40.0, -30.0]])
orange = np.array([[30.0, 40.0], [80.0, 90.0], [-20.0, -10.0]])
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(projection="3d")

ax.plot(red[0], red[1], red[2], color="red")
ax.plot(blue[0], blue[1], blue[2], color="blue")
ax.plot(orange[0], orange[1], orange[2], color="orange")

ax.set_xlabel("Temperature (℃)")
ax.set_ylabel("Time (s)")
ax.set_zlabel("Depth (m)")

ax.set_xticks([10, 15, 20, 25, 30, 35, 40])
ax.set_yticks([10, 30, 50, 70, 90])
ax.set_zticks([-50, -40, -30, -20])

ax.set_box_aspect(aspect=None, zoom=0.8)

# ===================
# Part 4: Saving Output
# ===================
# ===================
plt.tight_layout()
plt.savefig("3d_9.pdf", bbox_inches="tight")
