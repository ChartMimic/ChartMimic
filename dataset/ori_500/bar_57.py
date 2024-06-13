# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Economic Data Example
categories = [
    "GDP Growth",
    "Unemployment Rate",
    "Inflation Rate",
    "NASDAQ",
    "Exchange Rate",
    "Real Estate Prices",
    "Corporate Profits",
][::-1]
us_data = [3.1, 5.3, 2.2, 13.8, 1.1, 4.5, 7.0][::-1]
eu_data = [2.4, 7.5, 1.7, 11.6, 0.9, 3.0, 6.5][::-1]
china_data = [6.5, 4.2, 2.5, 14.2, 6.5, 8.9, 9.4][::-1]
india_data = [7.1, 6.6, 4.0, 16.3, 3.3, 7.2, 10.5][::-1]
brazil_data = [1.2, 12.1, 3.8, 5.4, 2.2, 1.5, 3.6][::-1]
labels = ["US", "EU", "China", "India", "Brazil"]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Stacked Bar Chart
fig, ax = plt.subplots(
    figsize=(8, 5)
)  # Adjusted to match the original image's dimensions
bar_width = 0.5
y_pos = range(len(categories))

ax.barh(y_pos, us_data, bar_width, color="tomato", label=labels[0])
ax.barh(y_pos, eu_data, bar_width, left=us_data, color="wheat", label=labels[1])
ax.barh(
    y_pos,
    china_data,
    bar_width,
    left=[i + j for i, j in zip(us_data, eu_data)],
    color="#81acce",
    label=labels[2],
)
ax.barh(
    y_pos,
    india_data,
    bar_width,
    left=[i + j + k for i, j, k in zip(us_data, eu_data, china_data)],
    color="darkseagreen",
    label=labels[3],
)
ax.barh(
    y_pos,
    brazil_data,
    bar_width,
    left=[
        i + j + k + l for i, j, k, l in zip(us_data, eu_data, china_data, india_data)
    ],
    color="cornflowerblue",
    label=labels[4],
)

# Labels and Legend
ax.set_xticks(np.arange(0, 51, 5))
ax.set_yticks(y_pos)
ax.grid(axis="x", color="gray", linestyle="--")
ax.set_axisbelow(True)
ax.set_yticklabels(categories)
ax.legend(loc="upper center", bbox_to_anchor=(0.5, 1.2), ncols=3)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig("bar_57.pdf", bbox_inches="tight")
