# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
models = ["Netflix", "Hulu", "Amazon Prime", "Disney+", "HBO Max", "Apple TV+"]
high_satisfaction = [30, 40, 35, 50, 45, 40]
medium_satisfaction = [50, 60, 55, 70, 50, 65]
low_satisfaction = [75, 70, 75, 90, 65, 80]

very_low_satisfaction = [15, 20, 25, 30, 35, 25]

# Bar positions
x = np.arange(len(models))
width = 0.15  # Adjusted width for spacing
labels = ["High Satisfaction", "Medium Satisfaction", "Low Satisfaction", "Very Low Satisfaction"]
ylabel = "User Satisfaction (%)"
title = "User Satisfaction Across Streaming Platforms"
ylim = [0, 100]


# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plotting
fig, ax = plt.subplots(
    figsize=(7, 5)
)  # Adjusted to match the image dimensions (504x360)

ax.bar(x - width * 2, high_satisfaction, width, label=labels[0], color="#c0e4b8")  # Lighter green
ax.bar(
    x - width,
    medium_satisfaction,
    width,
    label=labels[1],
    color="#97ccf6",
)  # Lighter blue
ax.bar(
    x, low_satisfaction, width, label=labels[2], color="#e48b88"
)  # Lighter red
ax.bar(
    x + width,
    very_low_satisfaction,
    width,
    label=labels[3],
    hatch="/",
    color="#cac4e1",
)  # Lighter purple

# Labels and Title
ax.set_ylabel(ylabel)
ax.set_title(title)
ax.set_xticks(x)
ax.set_xticklabels(models)
ax.set_ylim(ylim)  # Adjusted y-axis limit

# Move legend inside the plot area
ax.legend(loc="upper left")

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig('bar_38.pdf', bbox_inches='tight')
