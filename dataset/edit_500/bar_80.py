# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Updated Data
groups = ["3", "5", "7", "10"]
car_sales_2020 = [150, 180, 200, 250]
car_sales_2021 = [170, 210, 230, 260]
bike_sales_2020 = [50, 60, 70, 90]
bike_sales_2021 = [60, 75, 85, 100]

n_groups = len(groups)
labels = ["Car Sales 2020", "Car Sales 2021", "Bike Sales 2020", "Bike Sales 2021"]
xlabel = "Month"
ylabel = "Sales (units)"
title = "Monthly Car and Bike Sales in 2020 and 2021"


# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create the plot
fig, ax = plt.subplots(figsize=(10, 5))

index = np.arange(n_groups)
bar_width = 0.2

opacity = 0.8

rects1 = ax.bar(
    index - 1.5 * bar_width,
    car_sales_2020,
    bar_width,
    alpha=opacity,
    color="#8ECFC9",
    label=labels[0],
)

rects2 = ax.bar(
    index - 0.5 * bar_width,
    car_sales_2021,
    bar_width,
    alpha=opacity,
    color="#FFBE7A",
    label=labels[1],
)

rects3 = ax.bar(
    index + 0.5 * bar_width,
    bike_sales_2020,
    bar_width,
    alpha=opacity,
    color="#82B0D2",
    label=labels[2],
)

rects4 = ax.bar(
    index + 1.5 * bar_width,
    bike_sales_2021,
    bar_width,
    alpha=opacity,
    color="#E7DAD2",
    hatch="+",
    label=labels[3],
)


ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)
ax.set_title(title)
ax.set_xticks(index)
ax.set_xticklabels(groups)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.yaxis.grid(True, linestyle="--")
plt.legend()

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig('bar_80.pdf', bbox_inches='tight')
