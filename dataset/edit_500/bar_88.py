# ===================
# Part 1: Importing Libraries
# ===================
import numpy as np; np.random.seed(0)

import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Define the categories and scores
categories = ["Internet Service", "Mobile Service", "TV Service", "Home Phone Service"]
num_scores = 4
score_range = (-6.5, -0.5)
scores_2021 = np.random.uniform(score_range[0], score_range[1], num_scores).tolist()
scores_2022 = np.random.uniform(score_range[0], score_range[1], num_scores).tolist()
scores_2023 = np.random.uniform(score_range[0], score_range[1], num_scores).tolist()
scores_2024 = np.random.uniform(score_range[0], score_range[1], num_scores).tolist()
labels = ["2021 Satisfaction Scores", "2022 Satisfaction Scores", "2023 Satisfaction Scores", "2024 Satisfaction Scores"]
title1 = "Customer Satisfaction Scores by Service and Year"
xlabel1 = "Score"
xticks1 = np.arange(-6.5, 0.1, 0.5)
xticks2 = np.arange(-6.5, 0.1, 0.5)
xlim1 = [-7, 0]
xlim2 = [-7, 0]
# The x locations for the groups
ind = np.arange(len(scores_2021))

# The width of the bars
bar_width = 0.2

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create the figure and axes objects
fig, ax = plt.subplots(2, 1, figsize=(10, 8))
bars_3 = ax[0].barh(
    ind,
    scores_2021, 
    bar_width * 2, 
    label=labels[0], 
    color="#F27970"
)

# Plotting data
bars_3 = ax[1].barh(
    ind - bar_width * 1.5,
    scores_2021,
    bar_width,
    label=labels[0],
    color="#F27970",
)
bars_5 = ax[1].barh(
    ind - bar_width * 0.5,
    scores_2022,
    bar_width,
    label=labels[1],
    color="#54B345",
)
bars_7 = ax[1].barh(
    ind + bar_width * 0.5,
    scores_2023,
    bar_width,
    label=labels[2],
    color="#C76DA2",
)
bars_10 = ax[1].barh(
    ind + bar_width * 1.5,
    scores_2024,
    bar_width,
    label=labels[3],
    color="#05B9E2",
)

# Adding text inside the bars
for i, (score_3, score_5, score_7, score_10) in enumerate(
    zip(scores_2021, scores_2022, scores_2023, scores_2024)
):
    ax[1].text(
        score_3,
        i - bar_width * 1.5,
        f"{score_3:.1f}",
        va="center",
        ha="right",
        color="black",
    )
    ax[1].text(
        score_5,
        i - bar_width * 0.5,
        f"{score_5:.1f}",
        va="center",
        ha="right",
        color="black",
    )
    ax[1].text(
        score_7,
        i + bar_width * 0.5,
        f"{score_7:.1f}",
        va="center",
        ha="right",
        color="black",
    )
    ax[1].text(
        score_10,
        i + bar_width * 1.5,
        f"{score_10:.1f}",
        va="center",
        ha="right",
        color="black",
    )

# Adding labels, title, and custom x-axis tick labels, etc.
ax[1].set_xlabel(xlabel1)
ax[0].set_xticks(xticks1)
ax[1].set_xticks(xticks2)
ax[0].set_xlim(xlim1)
ax[1].set_xlim(xlim2)
ax[0].set_title(title1)
ax[0].set_yticks(ind)
ax[0].set_yticklabels(categories)
ax[1].set_yticks(ind)
ax[1].set_yticklabels(categories)
ax[1].legend()

# Show grid lines for x-axis
ax[0].xaxis.grid(True)
ax[1].xaxis.grid(True)

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig('bar_88.pdf', bbox_inches='tight')
