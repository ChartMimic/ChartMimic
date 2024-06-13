# ===================
# Part 1: Importing Libraries
# ===================
import numpy as np

np.random.seed(0)

import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Define the data and category names as provided by the user
category_names = [
    "Strongly disagree",
    "Disagree",
    "Neither agree nor disagree",
    "Agree",
    "Strongly agree",
]
results = {
    "Question 1": [10, 15, 17, 32, 26],
    "Question 2": [26, 22, 29, 10, 13],
    "Question 3": [35, 37, 15, 12, 19],
    "Question 4": [32, 11, 9, 15, 33],
    "Question 5": [21, 29, 13, 14, 40],
}
ylim = [-90, 90]
yticks = np.arange(-90, 91, 20)
xlabel = "Responses"
axhline = 0


# ===================
# Part 3: Plot Configuration and Rendering
# ===================
def create_vertical_bar_chart(results, category_names):
    fig, ax = plt.subplots(figsize=(10, 6))

    labels = list(results.keys())
    data = np.array(list(results.values()))
    data_cum = data.cumsum(axis=1)
    middle_index = data.shape[1] // 2
    offsets = data[:, range(middle_index)].sum(axis=1) + data[:, middle_index] / 2

    # Color Mapping
    category_colors = plt.get_cmap("Pastel1")(np.linspace(0.15, 0.85, data.shape[1]))

    # Plot Bars
    for i, (colname, color) in enumerate(zip(category_names, category_colors)):
        heights = data[:, i]
        bottoms = data_cum[:, i] - heights - offsets
        rects = ax.bar(
            labels,
            heights,
            bottom=bottoms,
            width=0.5,
            label=colname,
            color=color,
            edgecolor="black",
        )
        for j, (bottom, height) in enumerate(zip(bottoms, heights)):
            # Calculate the center position of each bar segment for the text
            text_x = bottom + height / 2
            text_y = j  # y-coordinate is based on the bar's index (j)
            ax.text(
                text_y,
                text_x,
                f"{abs(height):.1f}%",
                va="center",
                ha="center",
                color="black",
                fontsize=8,
            )
    # Add Zero Reference Line
    ax.axhline(axhline, linestyle="--", color="black", alpha=0.25)

    # X Axis
    ax.set_ylim(ylim)
    ax.set_yticks(yticks)
    ax.yaxis.set_major_formatter(lambda y, pos: str(abs(int(y))))

    # Y Axis
    ax.set_xlabel(xlabel)

    # Remove spines
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    # Legend
    ax.legend(
        ncol=len(category_names) // 2,
        bbox_to_anchor=(0.5, 1.1),
        loc="upper center",
        frameon=False,
    )

    return fig, ax


fig, ax = create_vertical_bar_chart(results, category_names)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig("bar_79.pdf", bbox_inches="tight")
