# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

from scipy.stats import gaussian_kde

# ===================
# Part 2: Data Preparation
# ===================
# Sample data for the line plot
y1 = np.random.normal(0, 1, 100)
y2 = np.random.normal(0, 2, 100)
y3 = np.random.normal(0, 1.5, 100)

kde1 = gaussian_kde(y1)
kde2 = gaussian_kde(y2)
kde3 = gaussian_kde(y3)

x_range = np.linspace(-5, 5, 50)
labels = ["Proposed", "FOD-Net", "SS3T"]
title = "Model"
xlabel = "ACC"
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create a figure with specific size to match the original image's dimensions
fig, (ax1, ax2) = plt.subplots(
    2, 1, figsize=(8, 4), gridspec_kw={"height_ratios": [3, 2]}
)

# Line plot
ax1.fill_between(x_range, kde1(x_range), color="skyblue", alpha=0.4)
ax1.fill_between(x_range, kde2(x_range), color="sandybrown", alpha=0.5)
ax1.fill_between(x_range, kde3(x_range), color="olivedrab", alpha=0.3)
ax1.plot(x_range, kde1(x_range), label=labels[0], color="blue")
ax1.plot(x_range, kde2(x_range), label=labels[1], color="orange")
ax1.plot(x_range, kde3(x_range), label=labels[2], color="green")
ax1.legend(title=title, loc="upper left")
ax1.set_xticks([])
ax1.set_yticks([])

# Box plot
box = ax2.boxplot(
    [y1, y2, y3], vert=False, patch_artist=True, medianprops={"color": "black"}
)
colors = ["skyblue", "sandybrown", "olivedrab"]
for patch, color in zip(box["boxes"], colors):
    patch.set_facecolor(color)

ax2.set_xlabel(xlabel)
ax2.set_yticks([])
ax2.set_xlim(-6, 6)

# ===================
# Part 4: Saving Output
# ===================
# Show the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig("CB_21.pdf", bbox_inches="tight")
