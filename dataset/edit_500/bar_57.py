# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
categories = [
    "Healthcare Spending",
    "Education Expenditure",
    "Defense Budget",
    "Technology Investment",
    "Public Infrastructure",
    "Renewable Energy",
    "Social Welfare",
][::-1]
us_data = [17.7, 6.0, 3.4, 8.5, 10.2, 12.1, 14.3][::-1]
eu_data = [7.0, 5.5, 2.0, 7.8, 9.0, 14.5, 12.7][::-1]
china_data = [5.3, 4.2, 1.9, 16.0, 13.5, 19.0, 9.8][::-1]
india_data = [3.5, 3.1, 2.4, 9.2, 8.7, 15.2, 8.5][::-1]
brazil_data = [8.4, 4.6, 1.5, 5.9, 7.5, 13.1, 10.1][::-1]
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
ax.set_xticks(np.arange(0, 80, 10))
ax.set_yticks(y_pos)
ax.grid(axis="x", color="gray", linestyle="--")
ax.set_axisbelow(True)
ax.set_yticklabels(categories)
ax.legend(loc="upper center", bbox_to_anchor=(0.5, 1.2), ncols=3)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig('bar_57.pdf', bbox_inches='tight')
