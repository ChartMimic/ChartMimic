# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# initialise labels and a numpy array make sure you have
# N labels of N number of values in the array
xlabels = ["I", "II", "III", "IV", "V"]
playerA = np.array([28, 20, 10, 22, 28])
playerB = np.array([35, 26, 20, 25, 30])

# Labels and Plot Types
hat_graph_label = ["Player A", "Player B"]

# Axes Limits and Labels
xlabel_value = "Games"
ylabel_value = "Score"
ylim_values = [0, 60]
title = "Scores by number of game and players"


# ===================
# Part 3: Plot Configuration and Rendering
# ===================
def hat_graph(ax, xlabels, values, group_labels):
    def label_bars(heights, rects):
        """Attach a text label on top of each bar."""
        for height, rect in zip(heights, rects):
            ax.annotate(
                f"{height}",
                xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(0, 4),  # 4 points vertical offset.
                textcoords="offset points",
                ha="center",
                va="bottom",
            )

    values = np.asarray(values)
    x = np.arange(values.shape[1])
    ax.set_xticks(x, labels=xlabels)
    spacing = 0.3  # spacing between hat groups
    width = (1 - spacing) / values.shape[0]
    heights0 = values[0]
    for i, (heights, group_label) in enumerate(zip(values, group_labels)):
        style = (
            {"fill": False, "edgecolor": "black"}
            if i == 0
            else {"edgecolor": "black", "color": "#64a36c"}
        )
        rects = ax.bar(
            x - spacing / 2 + i * width,
            heights - heights0,
            width,
            bottom=heights0,
            label=group_label,
            **style,
        )
        label_bars(heights, rects)


fig, ax = plt.subplots(figsize=(7, 5))
hat_graph(ax, xlabels, [playerA, playerB], hat_graph_label)

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_xlabel(xlabel_value)
ax.set_ylabel(ylabel_value)
ax.set_ylim(ylim_values)
ax.set_title(title)
ax.legend()

# ===================
# Part 4: Saving Output
# ===================
fig.tight_layout()
plt.savefig("HR_19.pdf", bbox_inches="tight")
