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
labels = [
    "CometKiwi",
    "LaBSE",
    "IF",
    "Max",
    "STARE",
    "Ppl",
    "ALTI+",
    "Wass Combo",
    "IF",
    "Max",
    "STARE",
    "IF",
    "Max",
    "STARE",
]
non_aggregation = [35.15, 26.86, 0, 0, 0, 58.99, 66.19, 48.38, 0, 0, 0, 0, 0, 0]
aggregation = [
    0,
    0,
    19.08,
    22.09,
    20.67,
    0,
    0,
    0,
    36.63,
    62.94,
    42.50,
    23.90,
    26.38,
    17.06,
]

x = np.arange(len(labels))  # the label locations
width = 0.7  # the width of the bars

line_y_1 = 18
line_y_2 = 28
line_x_1 = 4.5
line_x_2 = 10.5

# Labels and Plot Types
label_Non_Aggregation = "Non-Aggregation"
label_Aggregation = "Aggregation"
legend_title = "Aggregation"

# Axes Limits and Labels
ylabel_value = "FPR@90TPR"
title_value = "FPR@90TPR on Guerreiro et al. 2022"
ylim_values = [0, 80]
xlim_values = [-0.6, 14]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plotting
fig, ax = plt.subplots(
    figsize=(10, 5)
)  # Adjust the size to match the original image's dimensions
rects1 = ax.bar(x, non_aggregation, width, label=label_Non_Aggregation, color="#81b4a2")
rects2 = ax.bar(x, aggregation, width, label=label_Aggregation, color="#dd997b")

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel(ylabel_value)
ax.set_title(title_value)
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=45, ha="center")
ax.set_ylim(ylim_values)
ax.set_xlim(xlim_values)

# Adding the values on top of the bars
for rect in rects1:
    if rect.get_height() > 0:
        height = rect.get_height()
        ax.annotate(
            "{}".format(height),
            xy=(rect.get_x() + rect.get_width() / 2, height),
            xytext=(0, 3),  # 3 points vertical offset
            textcoords="offset points",
            ha="center",
            va="bottom",
        )
for rect in rects2:
    if rect.get_height() > 0:
        height = rect.get_height()
        ax.annotate(
            "{}".format(height),
            xy=(rect.get_x() + rect.get_width() / 2, height),
            xytext=(0, 3),  # 3 points vertical offset
            textcoords="offset points",
            ha="center",
            va="bottom",
        )

# Reference lines
ax.axhline(y=line_y_1, color="red", linestyle="--")
ax.axhline(y=line_y_2, color="gray", linestyle="--")
ax.axvline(x=line_x_1, color="gray", linestyle="--")
ax.axvline(x=line_x_2, color="gray", linestyle="--")

# Hide the ticks
ax.tick_params(axis="both", which="both", length=0)

# Hide the right and top spines
ax.spines["right"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.legend(title=legend_title)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig("bar_4.pdf", bbox_inches="tight")
