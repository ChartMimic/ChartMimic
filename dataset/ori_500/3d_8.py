# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)
# ===================
# Part 2: Data Preparation
# ===================

red = np.array(
    [
        [15, 17, 16, 15, 14, 16, 14, 19, 20, 14],
        [26, 21, 21, 29, 11, 12, 10, 27, 26, 27],
        [-40, -42, -45, -42, -49, -44, -49, -41, -45, -46],
    ]
)
blue = np.array(
    [
        [23, 28, 25, 26, 20, 26, 26, 26, 29, 27],
        [51, 53, 61, 42, 60, 60, 46, 44, 49, 51],
        [-34, -36, -30, -39, -38, -38, -33, -37, -35, -38],
    ]
)
orange = np.array(
    [
        [32, 31, 37, 31, 32, 34, 38, 31, 38, 31],
        [99, 84, 99, 88, 92, 71, 78, 74, 79, 74],
        [-27, -26, -29, -23, -24, -27, -25, -29, -24, -21],
    ]
)
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(projection="3d")

ax.scatter(red[0], red[1], red[2], marker="o", color="red", depthshade=False)
ax.scatter(blue[0], blue[1], blue[2], marker="^", color="blue", depthshade=False)
ax.scatter(
    orange[0], orange[1], orange[2], marker="s", color="orange", depthshade=False
)
ax.set_xlabel("Age")
ax.set_ylabel("Income")
ax.set_zlabel("Debt")

ax.set_xticks([10, 15, 20, 25, 30, 35, 40])
ax.set_yticks([10, 30, 50, 70, 90])
ax.set_zticks([-50, -40, -30, -20])

ax.set_box_aspect(aspect=None, zoom=0.8)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig("3d_8.pdf", bbox_inches="tight")
