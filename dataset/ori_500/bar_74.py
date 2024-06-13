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
categories = ["λ=0.06", "λ=0.08", "λ=0.1"]
values1 = [39.4, 35.18, 34.06]
values2 = [32.84, 20.84, 30.84]
values3 = [19.66, 28.0, 24.27]
values4 = [26.82, 30, 34.06]
values5 = [22, 22, 22]

values1minus = [-17, -19, -16]
values2minus = [-9, -12, -14]
values3minus = [-11, -14, -20]
values4minus = [-20, -30, -35]
values5minus = [0, 0, 0]

values = [values1, values2, values3, values4, values5]
values_minus = [values1minus, values2minus, values3minus, values4minus, values5minus]
labels = ["E16.6", "L26.8", "D19.7", "L22.2", "L22.2"]
colors = ["#f6c3cb", "#fbe5c8", "#55b0aa", "#6f94e7", "#e6e6f9"]
xlabel = "Series Labels"
yticks = np.arange(-40, 41, 10)
ylabel = "Reward Values"
legendtitle = "Categories"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Set up the figure size
plt.figure(figsize=(10, 5))

# Set up the bar width
barWidth = 0.2

# Set up positions for the bars
positions = np.arange(len(labels))

# Creating bars for each category
for i, category in enumerate(categories):
    pos = [x + barWidth * i for x in positions]  # shift each bar by `barWidth * i`
    plt.bar(
        pos,
        [v[i] for v in values],
        color=colors[i],
        width=barWidth,
        edgecolor="black",
        label=category,
    )
    plt.bar(
        pos,
        [v[i] for v in values_minus],
        color=colors[i],
        width=barWidth,
        edgecolor="black",
        alpha=0.5,
    )

    # Add text on top and bottom of the bars
    for idx, val in enumerate(pos):
        plt.text(
            val,
            values[idx][i] - 1,
            f"{values[idx][i]}",
            ha="center",
            va="top",
            rotation=-90,
        )
        plt.text(
            val,
            values_minus[idx][i] + 1,
            f"{-values_minus[idx][i]}",
            ha="center",
            va="bottom",
            rotation=-90,
        )

# Adding axis labels and ticks
plt.xlabel(xlabel)
plt.xticks([r + barWidth * 1.0 for r in range(len(labels))], labels)
plt.yticks(yticks)

# Add a legend and display the plot
plt.ylabel(ylabel)
plt.legend(title=legendtitle)

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig("bar_74.pdf", bbox_inches="tight")
