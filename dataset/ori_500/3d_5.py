# ===================
# Part 1: Importing Libraries
# ===================
import numpy as np

np.random.seed(0)

import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Data
ap = np.array(
    [
        [
            0.009,
            -0.072,
            -0.076,
            -0.014,
            0.093,
            0.037,
            0.05,
            0.023,
            -0.008,
            -0.055,
            -0.02,
            0.128,
            0.161,
            0.137,
            -0.105,
            -0.173,
            -0.139,
        ],
        [
            0.017,
            0.117,
            0.08,
            0.151,
            -0.082,
            -0.108,
            -0.062,
            0.025,
            0.0,
            -0.057,
            -0.033,
            -0.092,
            -0.192,
            -0.213,
            0.11,
            0.213,
            0.135,
        ],
        [
            0.37,
            0.426,
            -0.102,
            -0.527,
            0.424,
            -0.101,
            -0.529,
            0.596,
            0.835,
            0.889,
            1.01,
            0.812,
            0.624,
            0.497,
            0.815,
            0.658,
            0.497,
        ],
    ]
)

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
xp = ap[0]
yp = ap[1]
zp = ap[2]
fig, ax = plt.subplots(figsize=(7, 7), subplot_kw={"projection": "3d"})

radius = 1
ax.set_xlim3d([0, radius])
ax.set_ylim3d([0, radius])
ax.set_zlim3d([0, radius * 1.5])
ax.view_init(elev=15.0, azim=70)
ax.dist = 7.5

# 3D scatter
ax.scatter3D(xp, yp, zp, color="darkorange", label="Targets")

# draw the body
# left leg
ax.plot(xp[0:4], yp[0:4], zp[0:4], ls="-", color="orange")
# right leg
ax.plot(
    np.hstack((xp[0], xp[4:7])),
    np.hstack((yp[0], yp[4:7])),
    np.hstack((zp[0], zp[4:7])),
    ls="-",
    color="orange",
)
# spine
ax.plot(
    np.hstack((xp[0], xp[7:11])),
    np.hstack((yp[0], yp[7:11])),
    np.hstack((zp[0], zp[7:11])),
    ls="-",
    color="orange",
)
# right arm
ax.plot(
    np.hstack((xp[8], xp[11:14])),
    np.hstack((yp[8], yp[11:14])),
    np.hstack((zp[8], zp[11:14])),
    ls="-",
    color="orange",
)
# left arm
ax.plot(
    np.hstack((xp[8], xp[14:])),
    np.hstack((yp[8], yp[14:])),
    np.hstack((zp[8], zp[14:])),
    ls="-",
    color="orange",
)

plt.legend()

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig("3d_5.pdf", bbox_inches="tight")
