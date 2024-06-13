# ===================
# Part 1: Importing Libraries
# ===================
import colorsys
import numpy as np; np.random.seed(0)

import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
models = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio"]
percentages = [0.0, 0.71, 4.64, 4.64, 31.79, 73.93, 82.5]
percentages2 = [2.0, 3.55, 5.64, 12.64, 18.79, 20.93, 30.5]

# Sorting the data in descending order while keeping track of the cities order
sorted_data = sorted(zip(percentages, models), reverse=True)
sorted_percentages, sorted_models = zip(*sorted_data)

xlabel = "City"
ylabel1 = "Housing Price Increase (%)"
ylabel2 = "Living Cost Increase (%)"
title = "Cost of Living Comparison in Major US Cities"


# Generate random colors with lower saturation
def hsl_to_rgb(h, s, l):
    return colorsys.hls_to_rgb(h, l, s)


# Randomly generate colors
colors = [hsl_to_rgb(hue, 0.5, 0.6) for hue in np.linspace(0, 1, len(models) + 1)[:-1]]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create figure and bar chart with the sorted data
fig, axes = plt.subplots(2, 1, figsize=(12, 8), sharex=True)
bars = axes[0].bar(sorted_models, sorted_percentages, color=colors)
bars2 = axes[1].bar(sorted_models, percentages2, color=colors)
# Randomly decide where to put the text based on the value of the bar
for bar in bars:
    yval = bar.get_height()
    text_y = (
        yval - 5 if yval > 10 else yval + 1
    )  # Slight modification to avoid negative values
    axes[0].text(
        bar.get_x() + bar.get_width() / 2,
        text_y,
        f"{yval}%",
        ha="center",
        va="top" if text_y < yval else "bottom",
    )

# Set chart title and labels
plt.xlabel(xlabel)
axes[0].set_ylabel(ylabel1)
axes[1].set_ylabel(ylabel2)

# Randomly set y-axis range to a bit higher than the max value
axes[0].set_ylim(0, np.max(sorted_percentages) + 10)
axes[1].set_ylim(0, np.max(percentages2) + 10)

# Randomize the gridlines and ticks
axes[1].grid(axis="y", linestyle="--", alpha=0.7)
# Hide the top and right spines
axes[0].spines["top"].set_visible(False)
axes[0].spines["right"].set_visible(False)
axes[1].spines["top"].set_visible(False)
axes[1].spines["right"].set_visible(False)
# Randomize tick rotation
plt.xticks(rotation=45)
fig.suptitle(title)

# ===================
# Part 4: Saving Output
# ===================
# Apply tight layout
plt.tight_layout()
plt.savefig('bar_90.pdf', bbox_inches='tight')
