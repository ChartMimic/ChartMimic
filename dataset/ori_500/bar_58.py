# ===================
# Part 1: Importing Libraries
# ===================
import numpy as np

np.random.seed(0)

import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
category_names = ["Excellent", "Good", "Moderate", "Poor", "Very Poor"]
results = {
    "New York": [10, 15, 17, 32, 26],
    "Los Angeles": [26, 22, 29, 10, 13],
    "Chicago": [35, 37, 7, 2, 19],
    "Houston": [32, 11, 9, 15, 33],
    "Phoenix": [21, 29, 5, 5, 40],
    "Philadelphia": [8, 19, 5, 30, 38],
}
xlim = [-90, 90]
xticks = np.arange(-90, 91, 10)
xvline = 0

def create_bar_chart(results, category_names):
    fig, ax = plt.subplots(figsize=(10, 6))

    labels = list(results.keys())
    data = np.array(list(results.values()))
    data_cum = data.cumsum(axis=1)
    middle_index = data.shape[1] // 2
    offsets = data[:, range(middle_index)].sum(axis=1) + data[:, middle_index] / 2

    # Color Mapping
    category_colors = plt.get_cmap("coolwarm_r")(np.linspace(0.15, 0.85, data.shape[1]))

    # Plot Bars
    for i, (colname, color) in enumerate(zip(category_names, category_colors)):
        widths = data[:, i]
        starts = data_cum[:, i] - widths - offsets
        rects = ax.barh(
            labels,
            widths,
            left=starts,
            height=0.5,
            label=colname,
            color=color,
            edgecolor="black",
        )

    # Add Zero Reference Line
    ax.axvline(xvline, linestyle="--", color="black", alpha=0.25)

    # X Axis
    ax.set_xlim(xlim)
    ax.set_xticks(xticks)
    ax.xaxis.set_major_formatter(lambda x, pos: str(abs(int(x))))

    # Y Axis
    ax.invert_yaxis()

    # Remove spines
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)
    ax.spines["left"].set_visible(False)

    # Legend
    ax.legend(ncol=len(category_names), bbox_to_anchor=(0.5, 1.1), loc="upper center")

    # Set Background Color
    fig.set_facecolor("#FFFFFF")

    return fig, ax


# ===================
# Part 3: Plot Configuration and Rendering
# ===================
fig, ax = create_bar_chart(results, category_names)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig("bar_58.pdf", bbox_inches="tight")
