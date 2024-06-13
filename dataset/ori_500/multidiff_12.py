# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Set the figure size and create a gridspec with different widths
plt.figure(figsize=(10, 4))
gs = gridspec.GridSpec(1, 3, width_ratios=[1, 1, 2])

# Data for bar plots
categories = ["Cartesian", "Retinotopic"]
vgg16_acc = [0.551, 0.538]
resnet101_acc = [0.744, 0.762]
vgg16_bottom = [0.043, 0.195]
resnet101_bottom = [0.394, 0.477]

# Data for line plot
angles = np.arange(0, 181, 15)
vgg16_cartesian = [
    0.58,
    0.45,
    0.32,
    0.33,
    0.38,
    0.35,
    0.30,
    0.35,
    0.29,
    0.24,
    0.26,
    0.20,
    0.21,
]
vgg16_retinotopic = [
    0.60,
    0.58,
    0.55,
    0.50,
    0.53,
    0.56,
    0.45,
    0.48,
    0.5,
    0.51,
    0.49,
    0.45,
    0.52,
]
resnet101_cartesian = [
    0.78,
    0.75,
    0.70,
    0.65,
    0.69,
    0.72,
    0.74,
    0.69,
    0.65,
    0.70,
    0.64,
    0.63,
    0.62,
]
resnet101_polar = [
    0.82,
    0.79,
    0.76,
    0.68,
    0.70,
    0.75,
    0.74,
    0.71,
    0.69,
    0.72,
    0.74,
    0.75,
    0.81,
]
titles =["(A) VGG 16", "(B) Resnet 101", "(C) Rotation invariance"]
ax1ylabel="Accuracy"
ax3labels=["VGG16 Cartesian", "Resnet101 Cartesian", "VGG16 Retinotopic", "Resnet101 Polar"]
ax3xlabel="Rotation angle (°)"
ax3xticks=[0, 90, 180]
ax3vlines=[0, 90, 180]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Bar plot for VGG 16
ax1 = plt.subplot(gs[0])
ax1.bar(categories, vgg16_acc, color=["#c99796", "#f8d48b"])
ax1.bar(categories, vgg16_bottom, color=["#983530", "#f2a93c"])
ax1.set_title(titles[0])
ax1.set_ylabel(ax1ylabel)
ax1.set_ylim(0, 1)
for i, v in enumerate(vgg16_acc):
    ax1.text(i, v - 0.045, str(v), color="black", ha="center")
for i, v in enumerate(vgg16_bottom):
    ax1.text(i, v - 0.045, str(v), color="black", ha="center")

# Bar plot for Resnet 101
ax2 = plt.subplot(gs[1])
ax2.bar(categories, resnet101_acc, color=["#a4b4eb", "#d9e1ed"])
ax2.bar(categories, resnet101_bottom, color=["#4a68da", "#b4c4dc"])
ax2.set_title(titles[1])
ax2.set_ylim(0, 1)
for i, v in enumerate(resnet101_acc):
    ax2.text(i, v - 0.045, str(v), color="black", ha="center")
for i, v in enumerate(resnet101_bottom):
    ax2.text(i, v - 0.045, str(v), color="black", ha="center")

# Remove y-axis labels for the second plot
ax2.set_yticklabels([])

# Line plot for rotation invariance - with double the width
ax3 = plt.subplot(gs[2])
ax3.plot(
    angles,
    vgg16_cartesian,
    "r-x",
    label=ax3labels[0],
    color="#983530",
    markersize=4,
)
ax3.plot(
    angles,
    resnet101_cartesian,
    "b-o",
    label=ax3labels[1],
    color="#4a68da",
    markersize=4,
)
ax3.plot(
    angles,
    vgg16_retinotopic,
    "y-x",
    label=ax3labels[2],
    color="#f2a93c",
    markersize=4,
)
ax3.plot(
    angles,
    resnet101_polar,
    "c-o",
    label=ax3labels[3],
    color="#b4c4dc",
    markersize=4,
)
ax3.set_title(titles[2])
ax3.set_xlabel(ax3xlabel)
ax3.set_xticks(ax3xticks)
ax3.legend(loc="upper right", bbox_to_anchor=(0.95, 1.0), fontsize=6, frameon=False)
ax3.vlines(ax3vlines, 0, 1, colors="k", linestyles="dashed", linewidth=0.5)
ax3.set_yticklabels([])

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and show plot
plt.tight_layout()
plt.savefig('multidiff_12.pdf', bbox_inches='tight')
