# ===================
# Part 1: Importing Libraries
# ===================
import numpy as np

np.random.seed(0)

import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# ===================
# Part 2: Data Preparation
# ===================
# Define the increments and decrements for each step of the waterfall chart
increments = [350, 150, -50, -120, 200, -100, 75, -135, 50, 25, -300]

# Define the labels for each step
labels = [
    "Start",
    "Sale 1",
    "Sale 2",
    "Expense 1",
    "Expense 2",
    "Profit 1",
    "Loss 1",
    "Investment",
    "Profit 2",
    "Profit 3",
    "Final",
]

# Determine starting point and end point
start_value = 500
end_value = start_value + sum(increments)

# Calculate the bottom of each bar (cumulative)
bottoms = np.hstack(([start_value], np.cumsum(increments)[:-1])) + start_value

# Set the colors based on increment or decrement
colors = ["green" if x > 0 else "red" for x in increments]

# Axes Limits and Labels
ylabel_value = "Value"
title = "Waterfall Chart"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
fig, ax = plt.subplots(figsize=(8, 5))

# Plot bars
bars = ax.bar(labels, increments, bottom=bottoms, color=colors)

# Plot lines connecting the tops of each bar
for i in range(len(increments) - 1):  # Exclude the last increment
    start_top = bottoms[i] + increments[i]
    end_top = bottoms[i + 1] + increments[i + 1]
    ax.plot([i, i + 1], [start_top, end_top], color="k", linestyle="--")

# Annotate bars with value labels
for i, bar in enumerate(bars):
    height = bar.get_height()
    ax.annotate(
        f"{height}",
        xy=(bar.get_x() + bar.get_width() / 2, bar.get_y() + height),
        xytext=(
            0,
            3 if height > 0 else -12,
        ),  # 3 points vertical offset or -12 if negative
        textcoords="offset points",
        ha="center",
        va="bottom",
    )

# Set the y-axis label and title
ax.set_ylabel(ylabel_value)
ax.set_title(title)

# Format y-axis as currency
formatter = FuncFormatter(lambda y, _: f"${int(y)}")
ax.yaxis.set_major_formatter(formatter)

# Remove x-axis line and ticks
ax.spines["bottom"].set_visible(False)
ax.xaxis.set_ticks([])

# Set grid
ax.grid(True, axis="y", linestyle="--", linewidth=0.7, alpha=0.7)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig("HR_23.pdf", bbox_inches="tight")
