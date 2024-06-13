# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data (estimated from the image)
models = ["CL-7b", "CL-13b", "CL-34b", "DS-6.7b", "DS-33b", "SC"]
correct = [20, 30, 25, 60, 55, 40]
counterfeit_passing = [30, 40, 35, 50, 60, 50]
counterfeit_failing = [10, 15, 12, 20, 30, 15]
counterfeit_confused = [15, 30, 25, 30, 35, 40]

# Bar positions
x = np.arange(len(models))
width = 0.15  # Adjusted width for spacing
labels = ["Correct", "Counterfeit (Test-Passing)", "Counterfeit (Test-Failing)", "Counterfeit (Test-Failing), Confused"]
ylabel = "Accuracy"
title = "LeetCode, DS-6.7b"
ylim = [0, 100]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plotting
fig, ax = plt.subplots(
    figsize=(7, 5)
)  # Adjusted to match the image dimensions (504x360)

ax.bar(x - width * 2, correct, width, label=labels[0], color="#c0e4b8")  # Lighter green
ax.bar(
    x - width,
    counterfeit_passing,
    width,
    label=labels[1],
    color="#97ccf6",
)  # Lighter blue
ax.bar(
    x, counterfeit_failing, width, label=labels[2], color="#e48b88"
)  # Lighter red
ax.bar(
    x + width,
    counterfeit_confused,
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
plt.savefig("bar_38.pdf", bbox_inches="tight")
