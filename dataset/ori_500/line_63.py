# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data for the plot
weeks = np.arange(1, 29)
data1 = np.clip(np.sin(weeks * 0.1) + np.random.normal(0, 0.1, len(weeks)), 0, 1)
data2 = np.clip(np.cos(weeks * 0.1) + np.random.normal(0, 0.1, len(weeks)), 0, 1)
data3 = np.clip(
    np.sin(weeks * 0.15) + np.random.normal(0, 0.1, len(weeks)), 0, 1
)  # Additional data series

# Axes Limits and Labels
xlabel_value = "Weeks"
ylabel_value = "Normalized Value"

# Labels
label_1 = "Data Series 1"
label_2 = "Data Series 3"
label_legend = ["Data Series 1", "Data Series 2 with Gradient", "Data Series 3"]

# Titles
title = "Dynamic Data Presentation Across Weeks"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create a figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the data series 1
ax.plot(weeks, data1, label=label_1, color="deepskyblue", linewidth=3)

# Plot the data series 2 with a gradient color
for i in range(len(weeks) - 1):
    ax.plot(
        weeks[i : i + 2],
        data2[i : i + 2],
        linestyle="-",
        linewidth=3,
        color=plt.cm.viridis(i / len(weeks)),
    )

# Plot the data series 3
ax.plot(
    weeks, data3, label=label_2, color="magenta", linestyle="--", linewidth=3
)

# Customize the plot with labels, title, and legend
ax.set_title(title, fontsize=18)
ax.set_xlabel(xlabel_value, fontsize=14)
ax.set_ylabel(ylabel_value, fontsize=14)

# Add a legend to the plot
custom_lines = [
    plt.Line2D([0], [0], color="deepskyblue", lw=4),
    plt.Line2D([0], [0], color="green", lw=4),
    plt.Line2D([0], [0], color="magenta", lw=4, linestyle="--"),
]
ax.legend(
    custom_lines,
    label_legend,
    fontsize=12,
)

# Add a grid to the plot
ax.set_facecolor("floralwhite")
ax.grid(True, which="both", linestyle=":", linewidth=0.75, color="gray")

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout for better spacing and display
plt.tight_layout()

# Show the plot
plt.savefig('line_63.pdf', bbox_inches='tight')
