import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)

import matplotlib.lines as mlines

# ===================
# Part 2: Data Preparation
# ===================
import numpy as np
import matplotlib.pyplot as plt

# Data for simulated athlete performance categories
athletes = [
    "Usain Bolt",
    "Michael Phelps",
    "Simone Biles",
    "Serena Williams",
    "Cristiano Ronaldo",
    "LeBron James",
    "Lionel Messi",
    "Roger Federer",
    "Tom Brady",
    "Rafael Nadal",
    "Tiger Woods",
    "Megan Rapinoe",
    "Naomi Osaka",
    "Stephen Curry",
    "Novak Djokovic",
    "Kevin Durant",
]
n_categories = len(athletes)
performance_correct = np.random.uniform(200, 800, n_categories)
performance_incorrect = performance_correct - np.random.uniform(50, 200, n_categories)
sorted_indices = np.argsort((performance_correct + performance_incorrect) / 2)
categories = np.array(athletes)[sorted_indices]
performance_correct = performance_correct[sorted_indices]
performance_incorrect = performance_incorrect[sorted_indices]

# Colors and assignments for the first plot
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"]
assignments = ["Nike", "Adidas", "Puma", "Reebok"]

# Data for the second plot (error bar plot with legend)
for i in range(len(assignments)):
    aggregate_performance = np.random.randint(-150, 150, size=5)
    correct_score = np.random.randint(50, 300, size=5)
    error = np.random.randint(5, 25, size=5)

# Data for the third plot (scatter plot with trend line and correct text)
aggregate_scores = [
    np.linspace(600, 800, 5) - 100 * i + np.random.randint(-30, 30, 5)
    for i in range(len(assignments))
]
judge_ratings = [
    np.linspace(70, 90, 5) - 10 * i + np.random.randint(-15, 15, 5)
    for i in range(len(assignments))
]
scatterlabels = ["Correct Score", "Incorrect Score"]
xlabels = ["Performance Rating", "Aggregate Performance Rating", "Aggregate Performance Rating"]
ylabels = ["Athlete", "Correct Score - Incorrect Score", "Judge Rating (%)"]

ax2textlabel = "Judge: Elite Coach"
title = "Athletes"
text_j = 650
text_i = 25
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
        [performance_incorrect[i], performance_correct[i]], [i, i], color=color, lw=6, zorder=1
    )  # Black line for visibility
# Plotting the points
# set the layer of the white circles to be above the lines
axs[0].scatter(
    performance_correct, range(n_categories), color="black", label=scatterlabels[0], zorder=2, s=80
)  # Black dots for 'Correct'
axs[0].scatter(
    performance_incorrect,
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
axs[0].set_yticklabels(athletes[::-1])

# Second plot (error bar plot with legend)
for i in range(len(assignments)):
    axs[1].errorbar(
        aggregate_performance,
        correct_score,
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
    aggregate_elo = aggregate_scores[i]
    judge_accuracy = judge_ratings[i]
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
    np.linspace(250, 750, 5), np.linspace(40, 85, 5), color="black", lw=2, ls="-"
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
