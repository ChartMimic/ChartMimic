# ===================
# Part 1: Importing Libraries
# ===================
import numpy as np

np.random.seed(0)

import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# raw data
# data for the first person
ap1 = np.array(
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

# data for the second person
ap2 = np.array(
    [
        [
            0.509,
            0.428,
            0.424,
            0.486,
            0.593,
            0.537,
            0.55,
            0.523,
            0.492,
            0.445,
            0.48,
            0.628,
            0.661,
            0.637,
            0.395,
            0.327,
            0.361,
        ],
        [
            0.217,
            0.317,
            0.28,
            0.351,
            0.118,
            0.092,
            0.138,
            0.225,
            0.2,
            0.143,
            0.167,
            0.108,
            0.008,
            -0.013,
            0.31,
            0.413,
            0.335,
        ],
        [
            0.67,
            0.726,
            0.198,
            -0.227,
            0.724,
            0.199,
            -0.229,
            0.896,
            1.135,
            1.189,
            1.31,
            1.112,
            0.924,
            0.797,
            1.115,
            0.958,
            0.797,
        ],
    ]
)

# ===================
# Part 3: Plot Configuration and Rendering
# ===================

# data for the first person
xp = ap1[0]
yp = ap2[1]
zp = ap2[2]

# data for the second person
xp2 = ap2[0]
yp2 = ap2[1]
zp2 = ap2[2]

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

# second person
ax.scatter3D(xp2, yp2, zp2, color="blue", label="Predictions")
#
# left leg
ax.plot(xp2[0:4], yp2[0:4], zp2[0:4], ls="-", color="blue")
# right leg
ax.plot(
    np.hstack((xp2[0], xp2[4:7])),
    np.hstack((yp2[0], yp2[4:7])),
    np.hstack((zp2[0], zp2[4:7])),
    ls="-",
    color="blue",
)
# spine
ax.plot(
    np.hstack((xp2[0], xp2[7:11])),
    np.hstack((yp2[0], yp2[7:11])),
    np.hstack((zp2[0], zp2[7:11])),
    ls="-",
    color="blue",
)
# right arm
ax.plot(
    np.hstack((xp2[8], xp2[11:14])),
    np.hstack((yp2[8], yp2[11:14])),
    np.hstack((zp2[8], zp2[11:14])),
    ls="-",
    color="blue",
)
# left arm
ax.plot(
    np.hstack((xp2[8], xp2[14:])),
    np.hstack((yp2[8], yp2[14:])),
    np.hstack((zp2[8], zp2[14:])),
    ls="-",
    color="blue",
)

plt.legend()

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig("3d_1.pdf", bbox_inches="tight")
