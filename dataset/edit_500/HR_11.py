import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data
flops_per_byte = [0.2, 12]
flops = [1e9, 1.5e12]

# Points
points_x = [1.5, 2.5, 3.5, 4.5, 5.5, 6.5]
points_y = [1.2e11, 1.4e11, 1.6e11, 1.8e11, 2.0e11, 2.2e11]
labels = [
    "simulation, low",
    "simulation, medium",
    "simulation, high",
    "analysis, low",
    "analysis, medium",
    "analysis, high",
]
colors = ["magenta", "navy", "teal", "orange", "green", "purple"]
markers = ["s", "s", "s", "d", "o", "v"]
axlines = [
    [[11.7, 15], [1.5e12, 1.5e12]],
    [[9.5, 15], [1e12, 1e12]],
    [[4.5, 15], [2.5e11, 2.5e11]],
]
x_fill = [0.2, 12, 15, 15]  # x goes from 0.2 to 15 and back to 0.2
y_fill_top = [
    1e9,
    1.5e12,
    1.5e12,
    1.5e12,
]  # y follows the line segment, then the horizontal line, and back to the start
y_fill_bottom = [
    5e8,
    5e8,
    5e8,
    5e8,
]  # y is constant at 5e8 for the bottom boundary
xlabel = "Compute Intensity (Flops/byte)"
ylabel = "Performance (Flops/s)"
xlim = [0.2, 1.5e1]
ylim = [5e8, 1.5e12 * 1.5]
textlabels = ["Memory Bound", "Peak Performance", "No FMA", "No Vectorization"]
textposition = [[0.3, 5e9], [14, 1.6e12], [14, 1e12], [14, 3e11]]
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
ax.text(textposition[0][0], textposition[0][1], textlabels[0], rotation=40, verticalalignment="center")
ax.text(textposition[1][0],textposition[1][1],textlabels[1], rotation=0, va="bottom", ha="right")
ax.text(textposition[2][0],textposition[2][1], textlabels[2], rotation=0, va="bottom", ha="right")
ax.text(textposition[3][0], textposition[3][1],textlabels[3], rotation=0, va="bottom", ha="right")

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
plt.savefig('HR_11.pdf', bbox_inches='tight')
