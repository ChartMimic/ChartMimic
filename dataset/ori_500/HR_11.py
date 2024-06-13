# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data
flops_per_byte = [0.1, 10]
flops = [2e10, 2e12]

# Points
points_x = [2, 3, 4, 5, 6, 7]
points_y = [3e11, 2.5e11, 2e11, 2.5e11, 3e11, 3.5e11]
labels = [
    "explicit, random",
    "explicit, block size 10",
    "explicit, block size 100",
    "implicit, random",
    "implicit, block size 10",
    "implicit, block size 100",
]
colors = ["blue", "orange", "green", "cyan", "darkorange", "olive"]
markers = ["o", "o", "o", "v", "^", "s"]
axlines = [
    [[10, 20], [2e12, 2e12]],
    [[6, 20], [1.2e12, 1.2e12]],
    [[1, 20], [2e11, 2e11]],
]
x_fill = [0.1, 10, 20, 20]  # x goes from 0.1 to 20 and back to 0.1
y_fill_top = [
    2e10,
    2e12,
    2e12,
    2e12,
]  # y follows the line segment, then the horizontal line, and back to the start
y_fill_bottom = [
    1e10,
    1e10,
    1e10,
    1e10,
]  # y is constant at 1e10 for the bottom boundary
xlabel = "Flops/byte"
ylabel = "Flops/s"
xlim = [0.1, 2e1]
ylim = [1e10, 1e12 * 3]
textlabels = ["DAXPY memory bandwidth", "peak", "w/o FMA", "w/o vectorization"]
textposition = [[0.2, 1e11], [19, 2.1e12], [19, 1e12 * 1.3], [19, 2.1e11]]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create figure and axis
fig, ax = plt.subplots(figsize=(8, 7))

# Plot the roofline model
ax.plot(flops_per_byte, flops, color="black")
ax.plot(axlines[0][0], axlines[0][1], color="black", linestyle="-")
ax.plot(axlines[1][0], axlines[1][1], color="black", linestyle="-")
ax.plot(axlines[2][0], axlines[2][1], color="black", linestyle="-")

ax.fill_between(x_fill, y_fill_top, y_fill_bottom, color="lightblue", alpha=0.3)

# Add text annotations
ax.text(
    textposition[0][0],
    textposition[0][1],
    textlabels[0],
    rotation=40,
    verticalalignment="center",
)
ax.text(
    textposition[1][0],
    textposition[1][1],
    textlabels[1],
    rotation=0,
    va="bottom",
    ha="right",
)
ax.text(
    textposition[2][0],
    textposition[2][1],
    textlabels[2],
    rotation=0,
    va="bottom",
    ha="right",
)
ax.text(
    textposition[3][0],
    textposition[3][1],
    textlabels[3],
    rotation=0,
    va="bottom",
    ha="right",
)

# Plot the points
for x, y, label, color, marker in zip(points_x, points_y, labels, colors, markers):
    ax.plot(x, y, label=label, color=color, marker=marker, linestyle="-", markersize=10)

# Set scale to log
ax.set_xscale("log")
ax.set_yscale("log")

# Set labels
ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)

# Set limits
ax.set_xlim(xlim)
ax.set_ylim(ylim)
ax.grid(True)

# Add legend
ax.legend()

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig("HR_11.pdf", bbox_inches="tight")
