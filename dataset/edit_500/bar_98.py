# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data
labels = [
    "Beijing",
    "Shanghai",
    "Guangzhou",
    "Shenzhen",
    "Chengdu",
    "Hangzhou",
    "Wuhan",
    "Xi'an",
    "Chongqing",
]
non_aggregation = np.random.rand(9) * 1000
aggregation = np.random.rand(9) * 1000

datalabels = ["Summer", "Winter"]
ylabel = "Electricity Usage (MWh)"
title = "Seasonal Electricity Usage Comparison by City"
ylim = [0, 1200]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

legendtitle = "Methods"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plotting
fig, ax = plt.subplots(figsize=(10, 6))  # Adjust the size accordingly
rects1 = ax.bar(
    x - width / 2,
    non_aggregation,
    width,
    label=datalabels[0],
    color="#69b3a2",
    hatch="/",
)
rects2 = ax.bar(
    x + width / 2, aggregation, width, label=datalabels[1], color="#d98763", hatch="\\"
)

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel(ylabel)
ax.set_title(title)
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=0)
ax.set_ylim(ylim)
ax.set_xlim(-1, len(labels))

# Adding the values on top of the bars
for rect in rects1 + rects2:
    height = rect.get_height()
    ax.annotate(
        f"{height:.1f}",
        xy=(rect.get_x() + rect.get_width() / 2, height),
        xytext=(0, 3),  # 3 points vertical offset
        textcoords="offset points",
        ha="center",
        va="bottom",
    )

# Custom grid
ax.grid(axis="y", color="gray", linestyle="--", linewidth=0.7, alpha=0.7)
ax.set_axisbelow(True)

# Hide the ticks
ax.tick_params(axis="both", which="both", length=0)

# Hide the right and top spines
ax.spines["right"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.legend(title=legendtitle)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig('bar_98.pdf', bbox_inches='tight')
