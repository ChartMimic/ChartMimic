# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

import matplotlib.gridspec as gridspec

# ===================
# Part 2: Data Preparation
# ===================
eye_movement_data2 = {
    "Effort": [20.4, 29.6, 20.4, 20.4, 9.3],
}

brainwave_data2 = {"Effort": [23.8, 14.3, 16.7, 38.1, 7.1]}

categories2 = ["Very Low", "Low", "Neutral", "High", "Very High"]
colors = ["#d95f02", "#fdae61", "white", "#a6d96a", "#1a9641"]
xlim = [-69, 69]
xticks = np.arange(-60, 61, 20)
labels = ["Eye Movement", "Brainwave"]
suptitle = "Survey Results"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
fig, axes = plt.subplots(2, 1, figsize=(6, 3), sharex=True)


def create_bar_chart(ax, results, category_names, title):
    labels = list(results.keys())
    data = np.array(list(results.values()))
    data_cum = data.cumsum(axis=1)
    middle_index = data.shape[1] // 2
    offsets = data[:, range(middle_index)].sum(axis=1) + data[:, middle_index] / 2

    # Color Mapping
    category_colors = plt.get_cmap("RdYlGn")(np.linspace(0.15, 0.85, data.shape[1]))

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
        for j, (start, width) in enumerate(zip(starts, widths)):
            # Calculate the center position of each bar segment for the text
            text_x = start + width / 2
            text_y = j  # y-coordinate is based on the bar's index (j)
            ax.text(
                text_x,
                text_y,
                f"{abs(width):.1f}%",
                va="center",
                ha="center",
                color="black",
                fontsize=8,
            )
    # Add Zero Reference Line
    ax.axvline(0, linestyle="-", color="black", alpha=0.25)
    # X Axis
    ax.set_xlim(xlim)
    ax.set_xticks(xticks)
    ax.xaxis.set_major_formatter(lambda x, pos: str(abs(int(x))))
    # Y Axis
    ax.invert_yaxis()
    ax.set_title(title)


create_bar_chart(axes[0], eye_movement_data2, categories2, labels[0])
create_bar_chart(axes[1], brainwave_data2, categories2, labels[1])

# Set the overall title
fig.suptitle(suptitle)

# Add legend for the last two subplots
handles, labels = axes[1].get_legend_handles_labels()
fig.legend(
    handles,
    labels,
    loc="lower center",
    ncol=len(categories2),
    bbox_to_anchor=(0.5, -0.1),
)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig("bar_93.pdf", bbox_inches="tight")
