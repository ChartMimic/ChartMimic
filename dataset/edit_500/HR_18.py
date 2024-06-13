import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)

from matplotlib.collections import PatchCollection
from matplotlib.patches import Rectangle

# ===================
# Part 2: Data Preparation
# ===================
# Number of data points
n = 7

# Dummy data for demonstration
x = np.arange(0, n, 1)
y = np.random.rand(n) * 3.0 + 5.0  # Simulated values for average speed (e.g., in m/s)

# Dummy errors (above and below) representing measurement uncertainty
xerr = np.random.rand(2, n) * 0.5 + 0.1  # Variation due to environmental conditions
yerr = np.random.rand(2, n) * 0.5 + 0.2  # Measurement errors in average speed

# Updated titles and labels for sports domain
title = "Uncertainty in Average Speed of Athletes"
xlabel = "Athlete Sample Number"
ylabel = "Average Speed (m/s)"
color = "#4a5dd6"

def make_error_boxes(
    ax, xdata, ydata, xerror, yerror, facecolor="r", edgecolor="none", alpha=0.5
):
    # Loop over data points; create box from errors at each point
    errorboxes = [
        Rectangle((x - xe[0], y - ye[0]), xe.sum(), ye.sum())
        for x, y, xe, ye in zip(xdata, ydata, xerror.T, yerror.T)
    ]

    # Create patch collection with specified colour/alpha
    pc = PatchCollection(
        errorboxes, facecolor=facecolor, alpha=alpha, edgecolor=edgecolor
    )

    # Add collection to axes
    ax.add_collection(pc)

    # Plot errorbars
    artists = ax.errorbar(
        xdata, ydata, xerr=xerror, yerr=yerror, fmt="none", ecolor="k"
    )

    return artists


# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create figure and axes
fig, ax = plt.subplots(figsize=(7, 5))

# Call function to create error boxes
_ = make_error_boxes(ax, x, y, xerr, yerr,facecolor=color)

# Set titles and labels
ax.set_title(title)
ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig('HR_18.pdf', bbox_inches='tight')
