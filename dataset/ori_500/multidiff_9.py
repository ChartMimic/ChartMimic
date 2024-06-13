# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)

import matplotlib.lines as mlines

# ===================
# Part 2: Data Preparation
# ===================
# Data for the first plot (bar plot with white circles)
debaters = [
    "bo32",
    "bo4c8",
    "c16",
    "bo16",
    "bo32",
    "bo4c8",
    "c16",
    "bo16",
    "bo32",
    "bo4c8",
    "c16",
    "bo16",
    "bo32",
    "bo4c8",
    "c16",
    "bo16",
]
n_categories = len(debaters)
elo_correct = np.random.uniform(0, 400, n_categories)
elo_incorrect = elo_correct - np.random.uniform(50, 200, n_categories)
sorted_indices = np.argsort((elo_correct + elo_incorrect) / 2)
categories = np.array(debaters)[sorted_indices]
elo_correct = elo_correct[sorted_indices]
elo_incorrect = elo_incorrect[sorted_indices]

# Colors and assignments for the first plot
colors = ["#0069a6", "#d98322", "#18936a", "#ce5318"]
assignments = ["GPT-3.5-Turbo", "Claude 1.3", "Claude 2.1", "GPT-4-Turbo"]

# Data for the second plot (error bar plot with legend)
for i in range(len(assignments)):
    aggregate_elo = np.random.randint(-250, 250, size=5)
    correct_rating = np.random.randint(0, 300, size=5)
    error = np.random.randint(10, 15, size=5)

# Data for the third plot (scatter plot with trend line and correct text)
aggregate_elos = [
    np.linspace(180, 200, 5) - 150 * i + np.random.randint(-20, 20, 5)
    for i in range(len(assignments))
]
judge_accuracys = [
    np.linspace(80, 85, 5) - 10 * i + np.random.randint(-20, 20, 5)
    for i in range(len(assignments))
]
scatterlabels =["Correct", "Incorrect"]
xlabels=["Elo Rating", "Aggregate Elo Rating", "Aggregate Elo Rating"]
ylabels=["Debater", "Correct Rating - Incorrect Rating", "Judge Accuracy (%)"]

ax2textlabel= "Judge: GPT-4-Turbo"
title="Debaters"
text_j=200
text_i=38
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Adjusting figure size to match the original image's dimensions
fig, axs = plt.subplots(1, 3, figsize=(10, 4))

# First plot (bar plot with white circles)
axs[0].grid(axis="x", zorder=0)
# Plotting the lines first
for i in range(n_categories):
    color = colors[i // 4]
    axs[0].plot(
        [elo_incorrect[i], elo_correct[i]], [i, i], color=color, lw=6, zorder=1
    )  # Black line for visibility
# Plotting the points
# set the layer of the white circles to be above the lines
axs[0].scatter(
    elo_correct, range(n_categories), color="black", label=scatterlabels[0], zorder=2, s=80
)  # Black dots for 'Correct'
axs[0].scatter(
    elo_incorrect,
    range(n_categories),
    color="white",
    edgecolors="black",
    label=scatterlabels[1],
    zorder=2,
    s=80,
)  # White dots for 'Incorrect'
axs[0].legend(loc="lower right", title="Assignment")
axs[0].set_xlabel(xlabels[0])
axs[0].set_ylabel(ylabels[0])
axs[0].set_yticks(range(n_categories))
axs[0].set_yticklabels(debaters[::-1])

# Second plot (error bar plot with legend)
for i in range(len(assignments)):
    axs[1].errorbar(
        aggregate_elo,
        correct_rating,
        yerr=error,
        xerr=error + 10,
        fmt="o",
        capsize=3,
        color=colors[i],
    )
axs[1].set_xlabel(xlabels[1])
axs[1].set_ylabel(ylabels[1])
axs[1].grid()

# Third plot (scatter plot with trend line and correct text)
for i in range(len(assignments)):
    aggregate_elo = aggregate_elos[i]
    judge_accuracy = judge_accuracys[i]
    error = np.random.randint(5, 10, size=5)
    axs[2].errorbar(
        aggregate_elo,
        judge_accuracy,
        yerr=error,
        xerr=error + 10,
        fmt="o",
        capsize=3,
        color=colors[i],
    )
# Plotting the trend line
axs[2].plot(
    np.linspace(-300, 200, 5), np.linspace(40, 85, 5), color="black", lw=2, ls="-"
)
axs[2].set_xlabel(xlabels[2])
axs[2].set_ylabel(ylabels[2])
# set box edge color
axs[2].text(
    text_j,
    text_i,
    ax2textlabel,
    fontsize=8,
    color="black",
    ha="right",
    va="bottom",
    bbox=dict(facecolor="white", edgecolor="black"),
)
axs[2].grid()

# add legend to the whole figure and set colormaps
legend_handles = [
    mlines.Line2D(
        [], [], color=color, marker="s", linestyle="None", markersize=10, label=label
    )
    for label, color in zip(assignments, colors)
]
fig.legend(
    handles=legend_handles,
    loc="upper center",
    title=title,
    ncol=len(assignments),
    bbox_to_anchor=(0.5, 1.15),
    facecolor="white",
)

# ===================
# Part 4: Saving Output
# ===================
# Show plot
plt.tight_layout()
plt.savefig('multidiff_9.pdf', bbox_inches='tight')
