# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data

categories = ["Transport", "Tech", "Sports"]
values1 = [120, 150, 180]
values2 = [130, 140, 160]
values3 = [110, 135, 170]
values4 = [125, 155, 175]
values5 = [115, 145, 165]

values1minus = [-60, -50, -70]
values2minus = [-55, -45, -65]
values3minus = [-50, -55, -75]
values4minus = [-65, -60, -80]
values5minus = [-45, -50, -70]

values = [values1, values2, values3, values4, values5]
values_minus = [values1minus, values2minus, values3minus, values4minus, values5minus]
labels = ["Transport Q1", "Transport Q2", "Tech Q1", "Tech Q2", "Sports Q1"]
colors = ["#f6c3cb", "#fbe5c8", "#55b0aa", "#6f94e7", "#e6e6f9"]
xlabel = "Quarters"
yticks = np.arange(-80, 201, 20)
ylabel = "Performance Values"
legendtitle = "Sectors"

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
plt.savefig('bar_74.pdf', bbox_inches='tight')
