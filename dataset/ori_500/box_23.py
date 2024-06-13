# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Sample data for the boxplots
data = {
    "Music Playtime": np.random.uniform(30, 90, 20),
    "Reading Duration": np.random.uniform(25, 75, 20),
    "Exercise Duration": np.random.uniform(20, 70, 20),
    "Gaming Duration": np.random.uniform(15, 65, 20),
}
ylabel = "Duration (minutes)"
title = "Daily Activity Durations"


# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create a figure and axis with the specified size
fig, ax = plt.subplots(figsize=(9, 5))

# Create the boxplots with specific colors
boxprops = dict(linestyle="-", linewidth=2, color="darkblue")
flierprops = dict(marker="D", color="red", markerfacecolor="red", markersize=5)
medianprops = dict(linestyle="-", linewidth=2, color="#ea3323")

# Boxplot with vertical orientation
bp = ax.boxplot(
    data.values(),
    vert=True,
    notch=True,
    patch_artist=True,
    boxprops=boxprops,
    flierprops=flierprops,
    medianprops=medianprops,
)

colors = ["#f4b6c2", "#f6d8ae", "#daedbd", "#ece2f0"]
for patch, color in zip(bp["boxes"], colors):
    patch.set_facecolor(color)

# Set the x-axis labels with data keys
ax.set_xticklabels(data.keys(), ha="center")

# Set the y-axis label
ax.set_ylabel(ylabel)

# Disable x-axis grid and enable y-axis grid for clarity
ax.xaxis.grid(False)
ax.yaxis.grid(True)

# Set the title of the plot
ax.set_title(title)

# Annotating medians inside the boxplots
for i, line in enumerate(bp["medians"]):
    x, y = line.get_xydata()[1]  # Top of the median line
    # Display the median value at the top of the median line
    ax.annotate(
        f"{y:.1f}", (x - 0.1, y), textcoords="offset points", xytext=(0, 5), ha="center"
    )

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig("box_23.pdf", bbox_inches="tight")
