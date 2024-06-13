# ===================
# Part 1: Importing Libraries
# ===================
import numpy as np

np.random.seed(0)

import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Define the categories and scores
categories = ["LLAMA-Default", "LLAMA-HAG", "Vicuna-Default", "Vicuna-HAG"]
num_scores = 4
score_range = (-3.5, -0.5)
scores_3 = np.random.uniform(score_range[0], score_range[1], num_scores).tolist()
scores_5 = np.random.uniform(score_range[0], score_range[1], num_scores).tolist()
scores_7 = np.random.uniform(score_range[0], score_range[1], num_scores).tolist()
scores_10 = np.random.uniform(score_range[0], score_range[1], num_scores).tolist()

# The x locations for the groups
ind = np.arange(len(scores_3))

# The width of the bars
bar_width = 0.2

# Labels and Plot Types
label_3_Constraint_Words = "3 Constraint Words"
label_5_Constraint_Words = "5 Constraint Words"
label_7_Constraint_Words = "7 Constraint Words"
label_10_Constraint_Words = "10 Constraint Words"

# Axes Limits and Labels
xlabel_value = "Score"
ax_title = "Scores by group and constraint word count"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create the figure and axes objects
fig, ax = plt.subplots(figsize=(10, 6))

# Plotting data
bars_3 = ax.barh(
    ind - bar_width * 1.5,
    scores_3,
    bar_width,
    label=label_3_Constraint_Words,
    color="salmon",
)
bars_5 = ax.barh(
    ind - bar_width * 0.5,
    scores_5,
    bar_width,
    label=label_5_Constraint_Words,
    color="skyblue",
)
bars_7 = ax.barh(
    ind + bar_width * 0.5,
    scores_7,
    bar_width,
    label=label_7_Constraint_Words,
    color="coral",
)
bars_10 = ax.barh(
    ind + bar_width * 1.5,
    scores_10,
    bar_width,
    label=label_10_Constraint_Words,
    color="lightblue",
)

# Adding text inside the bars
for i, (score_3, score_5, score_7, score_10) in enumerate(
    zip(scores_3, scores_5, scores_7, scores_10)
):
    ax.text(
        score_3,
        i - bar_width * 1.5,
        f"{score_3:.1f}",
        va="center",
        ha="right",
        color="black",
    )
    ax.text(
        score_5,
        i - bar_width * 0.5,
        f"{score_5:.1f}",
        va="center",
        ha="right",
        color="black",
    )
    ax.text(
        score_7,
        i + bar_width * 0.5,
        f"{score_7:.1f}",
        va="center",
        ha="right",
        color="black",
    )
    ax.text(
        score_10,
        i + bar_width * 1.5,
        f"{score_10:.1f}",
        va="center",
        ha="right",
        color="black",
    )

# Adding labels, title, and custom x-axis tick labels, etc.
ax.set_xlabel(xlabel_value)
ax.set_title(ax_title)
ax.set_yticks(ind)
ax.set_yticklabels(categories)
ax.legend()

# Invert y-axis to have the first entry at the top
plt.gca().invert_yaxis()

# Show grid lines for x-axis
ax.xaxis.grid(True)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig("bar_65.pdf", bbox_inches="tight")
