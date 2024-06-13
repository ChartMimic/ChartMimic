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
categories = [
    "Internet Penetration",
    "Smartphone Usage",
    "Research Investment",
    "Patents Filed",
]
internet_penetration = [585, 920, 760, 686]  # Example data in percentage
smartphone_usage = [900, 350, 718, 634]  # Example data in percentage
research_investment = [1500, 1400, 800, 450]  # Example data in numbers of patents
labels = ["Internet Penetration (%)", "Smartphone Usage (%)", "Research Investment (% of GDP)"]
xticks = np.arange(0, 3500, 250)

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Stacked Bar Chart
fig, ax = plt.subplots(figsize=(8, 5))
bar_width = 0.5
y_pos = range(len(categories))

ax.barh(
    y_pos,
    internet_penetration,
    bar_width,
    color="#d66555",
    edgecolor="#2a3b4d",
    hatch="*",
    label=labels[0]
)
ax.barh(
    y_pos,
    smartphone_usage,
    bar_width,
    left=internet_penetration,
    color="#88a27d",
    edgecolor="#2a3b4d",
    hatch="+",
    label=labels[1]
)
ax.barh(
    y_pos,
    research_investment,
    bar_width,
    left=[i + j for i, j in zip(internet_penetration, smartphone_usage)],
    color="#a1b5ce",
    edgecolor="#2a3b4d",
    hatch="/",
    label=labels[2],
)

# Labels and Legend
ax.set_xticks(xticks)
ax.set_yticks(y_pos)
ax.grid(axis="x", color="gray", linestyle="--")
ax.set_axisbelow(True)
ax.set_yticklabels(categories)
ax.legend(loc="upper center", bbox_to_anchor=(0.5, 1.2), ncols=3)

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig("bar_61.pdf", bbox_inches="tight")
