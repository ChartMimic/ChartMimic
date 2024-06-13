# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Sample data similar to the provided image
categories = [
    "Notre-Dame de Paris",
    "Demi-Gods and Semi-Devils",
    "The Count of Monte Cristo",
    "Game of Thrones",
    "Attack on Titan",
]
scores_0 = [0.6, 0.4, 0.3, 0.5, 0.2]
scores_20 = [0.7, 0.5, 0.35, 0.45, 0.25]
scores_40 = [0.4, 0.3, 0.25, 0.35, 0.15]
scores_60 = [0.6, 0.5, 0.4, 0.55, 0.3]
labels = ["Time 0", "Time 20", "Time 40", "Time 60"]
xlabel = "Scores"
ylabel = "Categories"
title = "Scores by Category Over Time"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Size of the plot
plt.figure(figsize=(10, 8))

# Adjust the position of the bars on the x-axis to prevent overlap
bar_height = 0.15
ind = [i * (bar_height * len(categories)) for i in range(len(scores_0))]

# Creating the bar plot with adjusted positions to prevent overlap
plt.barh(
    [pos + bar_height * 0 for pos in ind],
    scores_0,
    color="navy",
    height=bar_height,
    label=labels[0],
)
plt.barh(
    [pos + bar_height * 1 for pos in ind],
    scores_20,
    color="blue",
    height=bar_height,
    label=labels[1],
)
plt.barh(
    [pos + bar_height * 2 for pos in ind],
    scores_40,
    color="royalblue",
    height=bar_height,
    label=labels[2],
)
plt.barh(
    [pos + bar_height * 3 for pos in ind],
    scores_60,
    color="lightblue",
    height=bar_height,
    label=labels[3],
)

# X and Y axis Labels
plt.xlabel(xlabel)
plt.ylabel(ylabel)

# Title of the plot
plt.title(title)

# Adding legend
plt.legend()

# Setting the labels for y-axis with adjusted positions
plt.yticks([pos + bar_height * 1.5 for pos in ind], categories)

# ===================
# Part 4: Saving Output
# ===================
# Display the plot with enough space
plt.tight_layout()

plt.savefig("bar_63.pdf", bbox_inches="tight")
