# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data
tasks = ["snarks", "navigate", "question_selection", "object_counting"]
scores_step1 = [0.65, 0.7, 0.68, 0.66]
scores_step1_APE = [0.67, 0.72, 0.7, 0.68]
scores_step2 = [0.75, 0.78, 0.76, 0.76]
scores_step2_APE = [0.77, 0.72, 0.7, 0.76]
scores_best = [0.75, 0.71, 0.71, 0.61]
scores_iterative_best = [0.73, 0.73, 0.76, 0.74]
scores_sum_best = [0.77, 0.72, 0.7, 0.68]
trend = [0.7, 0.75, 0.73, 0.71]
title = "Comparison of APO & APO-APEs (GPT-3 5-Turbo)"
labels = [
    "APO-step1",
    "APO-step1-APE",
    "APO-step2",
    "APO-step2-APE",
    "APO-best",
    "Iterative-APE-best",
    "APO-Sum-best",
    "APO-trend",
]
x_label = "Tasks"
y_label = "Scores"
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Set figure size to match the original image's dimensions
plt.figure(figsize=(10, 4))

# Bar width
barWidth = 0.1

# Set position of bar on X axis
r1 = np.arange(len(scores_step1))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
r4 = [x + barWidth for x in r3]
r5 = [x + barWidth for x in r4]
r6 = [x + barWidth for x in r5]
r7 = [x + barWidth for x in r6]

# Make the plot
plt.bar(
    r1,
    scores_step1,
    color="#b7cdde",
    width=barWidth,
    edgecolor="white",
    label=labels[0],
)
plt.bar(
    r2,
    scores_step1_APE,
    color="#b7cdde",
    width=barWidth,
    edgecolor="white",
    label=labels[1],
    hatch="\\",
)
plt.bar(
    r3,
    scores_step2,
    color="#81aac8",
    width=barWidth,
    edgecolor="white",
    label=labels[2],
)
plt.bar(
    r4,
    scores_step2_APE,
    color="#81aac8",
    width=barWidth,
    edgecolor="white",
    label=labels[3],
    hatch="\\",
)
plt.bar(
    r5,
    scores_best,
    color="#5584af",
    width=barWidth,
    edgecolor="white",
    label=labels[4],
)
plt.bar(
    r6,
    scores_iterative_best,
    color="#666666",
    width=barWidth,
    edgecolor="white",
    label=labels[5],
)
plt.bar(
    r7,
    scores_sum_best,
    color="#4a8f74",
    width=barWidth,
    edgecolor="white",
    label=labels[6],
)

# Add trend line
plt.plot(
    tasks,
    trend,
    color="gray",
    marker="o",
    linestyle="--",
    linewidth=2,
    markersize=6,
    label=labels[7],
)

# Add xticks on the middle of the group bars
plt.xlabel(x_label)
plt.ylabel(y_label)
plt.xticks([r + barWidth * 3 for r in range(len(scores_step1))], tasks)
plt.ylim(0.3, 0.9)
plt.yticks([0.4, 0.5, 0.6, 0.7, 0.8, 0.9])

# Create legend & Show graphic
plt.title(title)
plt.legend(loc="upper center", ncol=4)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig("CB_13.pdf", bbox_inches="tight")
