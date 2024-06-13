# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# ===================
# Part 2: Data Preparation
# ===================
# Sample data similar to the provided image
categories1 = [
    "Notre-Dame de Paris",
    "Demi-Gods and Semi-Devils",
    "The Count of Monte Cristo",
    "Game of Thrones",
    "Attack on Titan",
]
scores_0 = [0.6, 0.4, 0.3, 0.5, 0.2]
scores_20 = [0.7, 0.5, 0.35, 0.45, 0.25]
scores_40 = [0.4, 0.3, 0.25, 0.35, 0.15]

categories2 = [
    "Notre-Dame de Paris",
    "Demi-Gods and Semi-Devils",
    "The Count of Monte Cristo",
]
scores_0_2 = [
    0.6,
    0.4,
    0.3,
]
scores_20_2 = [
    0.7,
    0.5,
    0.35,
]
scores_40_2 = [
    0.4,
    0.3,
    0.25,
]

scores_0_3 = [
    0.2,
    0.4,
    0.3,
]
scores_20_3 = [
    0.3,
    0.2,
    0.35,
]
scores_40_3 = [0.4, 0.5, 0.25]

scores_0_4 = [
    0.7,
    0.8,
    0.3,
]
scores_20_4 = [
    0.9,
    1,
    0.35,
]
scores_40_4 = [0.4, 0.6, 0.25]

labels = ["Score at Time 0", "Score at Time 20", "Score at Time 40"]

title2 = "1st Experiment"
title3 = "2nd Experiment"
title4 = "3rd Experiment"

# Adjust the position of the bars on the x-axis to prevent overlap
bar_height = 0.15
bar_height2 = 0.1
ind = [i * (bar_height * len(categories1)) for i in range(len(scores_0))]
ind2 = [i * (bar_height2 * len(categories1)) for i in range(len(scores_0_2))]
ind3 = [i * (bar_height2 * len(categories1)) for i in range(len(scores_0_3))]
ind4 = [i * (bar_height2 * len(categories1)) for i in range(len(scores_0_4))]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
fig = plt.figure(tight_layout=True, figsize=(10, 6))
gs = gridspec.GridSpec(2, 3)
ax1 = fig.add_subplot(gs[0, :])
ax2 = fig.add_subplot(gs[1, 0])
ax3 = fig.add_subplot(gs[1, 1])
ax4 = fig.add_subplot(gs[1, 2])

# Creating the bar plot with adjusted positions to prevent overlap
ax1.barh(
    [pos - bar_height for pos in ind],
    scores_0,
    color="#9dcec9",
    height=bar_height,
    label=labels[0]
)
ax1.barh(
    [pos + bar_height * 0 for pos in ind],
    scores_20,
    color="#f5c085",
    height=bar_height,
    label=labels[1]
)
ax1.barh(
    [pos + bar_height * 1 for pos in ind],
    scores_40,
    color="#ea8675",
    height=bar_height,
    label=labels[2]
)
ax1.set_yticks([pos + bar_height * 0 for pos in ind], categories1)

ax2.barh(
    [pos - bar_height2 for pos in ind2],
    scores_0_2,
    color="#9dcec9",
    height=bar_height2,
    label=labels[0]
)
ax2.barh(
    [pos + bar_height2 * 0 for pos in ind2],
    scores_20_2,
    color="#f5c085",
    height=bar_height2,
    label=labels[1]
)
ax2.barh(
    [pos + bar_height2 * 1 for pos in ind2],
    scores_40_2,
    color="#ea8675",
    height=bar_height2,
    label=labels[2]
)
ax2.set_yticks([pos + bar_height2 * 0 for pos in ind2], categories2)
ax2.set_title(title2)

ax3.barh(
    [pos - bar_height2 * 1 for pos in ind3],
    scores_0_3,
    color="#9dcec9",
    height=bar_height2,
    label=labels[0]
)
ax3.barh(
    [pos + bar_height2 * 0 for pos in ind3],
    scores_20_3,
    color="#f5c085",
    height=bar_height2,
    label=labels[1]
)
ax3.barh(
    [pos + bar_height2 * 1 for pos in ind3],
    scores_40_3,
    color="#ea8675",
    height=bar_height2,
    label=labels[2]
)
ax3.set_yticks([])
ax3.set_title(title3)

ax4.barh(
    [pos - bar_height2 * 1 for pos in ind4],
    scores_0_4,
    color="#9dcec9",
    height=bar_height2,
    label=labels[0],
)
ax4.barh(
    [pos + bar_height2 * 0 for pos in ind4],
    scores_20_4,
    color="#f5c085",
    height=bar_height2,
    label=labels[1]
)
ax4.barh(
    [pos + bar_height2 * 1 for pos in ind4],
    scores_40_4,
    color="#ea8675",
    height=bar_height2,
    label=labels[2]
)
ax4.set_yticks([])
ax4.set_title(title4)

# Adding legend
ax1.legend(loc="upper center", bbox_to_anchor=(0.5, 1.2), ncols=3)

# ===================
# Part 4: Saving Output
# ===================
# Display the plot with enough space
plt.tight_layout()
plt.savefig("bar_84.pdf", bbox_inches="tight")
