# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Recalculating parabola parameters and points with error ellipses for denser points
k = 0.4
h = -0.5  # Assuming h from the given x-coordinate of the vertex
a = 4  # Adjusted manually to fit the given shape description
y_values = np.linspace(0, 3, 400)
x_values = a * (y_values - k) ** 2 + h

# Increasing the number of points for density
points_y = np.linspace(0.5, 2.5, 20)  # More points for higher density
points_x = a * (points_y - k) ** 2 + h - 0.15  # Offset to the left

# Labels and Plot Types
label_1 = "Monte Carlo"
label_2 = "± 3-σ of Prediction"
label_3 = "Mean-Taylor"
ylim_values = [0, 3]
ellipse_sizes = np.linspace(0, 2, len(points_y))

# Axes Limits and Labels
xlabel_value = "x(m)"
ylabel_value = "y(m)"
title = "Denser Points with Perfectly Circular Error Ellipses"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Adjusting the size of the error ellipses to make them larger and more clearly elliptical, with black borders
plt.figure(figsize=(8, 6))
plt.plot(x_values, y_values, label=label_1, color="red")

# Making error ellipses perfectly circular
ellipse_sizes = ellipse_sizes

for i, (px, py, size) in enumerate(zip(points_x, points_y, ellipse_sizes)):
    if i == 0:  # Only for the first ellipse add label
        ellipse = plt.matplotlib.patches.Ellipse(
            (px, py),
            width=size,
            height=size / 4,
            edgecolor="black",
            facecolor="none",
            label=label_2,
        )
    else:
        ellipse = plt.matplotlib.patches.Ellipse(
            (px, py), width=size, height=size / 4, edgecolor="black", facecolor="none"
        )
    plt.gca().add_patch(ellipse)

plt.scatter(points_x, points_y, color="blue", label=label_3, zorder=5)
plt.xlabel(xlabel_value)
plt.ylabel(ylabel_value)
plt.title(title)
plt.ylim(ylim_values)
plt.grid(True, color="white")
plt.gca().set_facecolor("#eaeaf2")
plt.gca().set_axisbelow(True)
# Adjusting the legend to include the representative ellipse
plt.legend(facecolor="#eaeaf2")
for spine in plt.gca().spines.values():
    spine.set_visible(False)
plt.gca().tick_params(axis="both", length=0)  # Hide tick marks

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig("HR_4.pdf", bbox_inches="tight")
