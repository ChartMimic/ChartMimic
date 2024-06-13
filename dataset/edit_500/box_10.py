import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Updated sample data for the boxplots
data = {
    "Commute Time": np.random.uniform(10, 15, 20),
    "Work Hours": np.random.uniform(6, 10, 20),
    "Leisure Time": np.random.uniform(2, 6, 20),
    "Sleep Duration": np.random.uniform(5, 9, 20),
}
xlabel = "Time (hours)"
title = "Daily Time Distribution"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create a figure and axis with the specified size
fig, ax = plt.subplots(figsize=(9, 5))

# Create the boxplots with specific colors
boxprops = dict(linestyle="-", linewidth=2, color="darkblue")
flierprops = dict(marker="D", color="red", markerfacecolor="red", markersize=5)
medianprops = dict(linestyle="-", linewidth=2, color="green")

# Boxplot with vertical orientation
bp = ax.boxplot(
    data.values(),
    vert=False,
    patch_artist=True,
    boxprops=boxprops,
    flierprops=flierprops,
    medianprops=medianprops,
)

colors = ["lightblue", "lightgreen", "lightyellow", "lightgray"]
for patch, color in zip(bp["boxes"], colors):
    patch.set_facecolor(color)
    # Scatter plot for data points
    for j, key in enumerate(data.keys()):
        x = data[key]
        y = np.random.normal(j + 1, 0.02, size=len(x))
        plt.plot(x, y, "k.", alpha=0.4, color="#4e8a84")

# Set the x-axis labels with data keys
ax.set_yticklabels(data.keys(), ha="right")

# Set the y-axis label
ax.set_xlabel(xlabel)
ax.xaxis.grid(False)
ax.xaxis.grid(True)

# Set the title of the plot
ax.set_title(title)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig('box_10.pdf', bbox_inches='tight')
