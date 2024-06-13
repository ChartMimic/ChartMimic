# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.ticker as ticker
import numpy as np

np.random.seed(0)

# ===================
# Part 2: Data Preparation
# ===================
# Data
professions = [
    "Cleaning / laundry",
    "Crafting/knitting",
    "Baker",
    "Carpenter",
    "Making Bricks",
    "Gardening",
]
number_of_videos = [8062.5, 6285.0, 5314.5, 4824.0, 4372.5, 3822.0]
colors = [
    "lightskyblue",
    "turquoise",
    "lightgreen",
    "navajowhite",
    "lightsalmon",
    "lightcoral",
]

# Plot Configuration
xlabel = "Number of Videos"
xlim_values = (0, 9000)
ylim_values = (-0.5, 5.5)
title_text = "Number of Videos by Profession"
yticks_rotation = 45

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create horizontal bar chart
plt.figure(figsize=(12, 8))  # Adjust figure size to match original image's dimensions
plt.barh(
    professions, number_of_videos, color=colors, edgecolor="white"
)  # Change bar color to purple
plt.xlabel(xlabel)
plt.xlim(*xlim_values)
plt.ylim(*ylim_values)
plt.title(title_text)

basetick = [0, 1, 2, 3, 4, 5]
offsetticks = [-0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5]
plt.gca().yaxis.set_major_locator(ticker.FixedLocator(basetick))
plt.gca().yaxis.set_major_formatter(
    ticker.FuncFormatter(lambda x, _: f"{professions[x-1]}")
)
plt.gca().yaxis.set_minor_locator(ticker.FixedLocator(offsetticks))
plt.gca().grid(True, which="minor", axis="y", color="gray", linestyle="--")
plt.gca().grid(True, which="major", axis="x", color="gray", linestyle="--")
plt.gca().set_axisbelow(True)
plt.tick_params(axis="both", which="major", length=0)
plt.tick_params(axis="y", which="minor", color="gray", length=3)
plt.gca().spines["top"].set_visible(False)
plt.gca().spines["right"].set_visible(False)
plt.gca().spines["bottom"].set_visible(False)
plt.gca().spines["left"].set_visible(False)
plt.yticks(rotation=yticks_rotation)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig("bar_56.pdf", bbox_inches="tight")
