# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data reflecting energy statistics for various countries, scaled for better visualization
categories = ["Germany", "Canada", "Australia", "Japan"][::-1]
total_energy_consumption = (
    np.array([3450, 2750, 2300, 2900][::-1]) / 10
)  # in Petajoules, scaled down
renewable_energy_ratio = np.array(
    [400, 500, 750, 620][::-1]
)  # percentage of total energy
electricity_production = (
    np.array([6000, 7000, 5500, 6400][::-1]) / 10
)  # in Terawatt-hours, scaled down
electricity_consumption = np.array(
    [580, 690, 530, 630][::-1]
)  # in Terawatt-hours, scaled down

categories2 = ["USA", "UK", "France", "Italy"][::-1]
total_energy_consumption2 = (
    np.array([2300, 1950, 2500, 1750][::-1]) / 10
)  # in Petajoules, scaled down
renewable_energy_ratio2 = np.array(
    [550, 450, 530, 690][::-1]
)  # percentage of total energy
electricity_production2 = (
    np.array([4000, 2000, 5700, 3200][::-1]) / 10
)  # in Terawatt-hours, scaled down
electricity_consumption2 = (
    np.array([3900, 880, 5600, 3100][::-1]) / 10
)  # in Terawatt-hours, scaled down

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Stacked Bar Chart in subplots
fig, axs = plt.subplots(2, 1, figsize=(8, 8), sharex=True)  # 2 rows, 1 column
bar_width = 0.8
y_pos = range(len(categories))
y_pos2 = range(len(categories2))

colors = ["tomato", "wheat", "#81acce", "darkseagreen"]
labels = [
    "Total Energy Consumption (10^2 PJ)",
    "Renewable Energy Ratio (%)",
    "Electricity Production (10^1 TWh)",
    "Electricity Consumption (10^1 TWh)",
]
data_ratios = [
    total_energy_consumption,
    renewable_energy_ratio,
    electricity_production,
    electricity_consumption,
]
data_ratios2 = [
    total_energy_consumption2,
    renewable_energy_ratio2,
    electricity_production2,
    electricity_consumption2,
]

axs[0].invert_yaxis()  # labels read top-to-bottom
axs[0].set_yticks(y_pos)
axs[0].set_yticklabels(categories)
axs[0].grid(axis="x", color="gray", linestyle="--", linewidth=0.5)
axs[0].set_axisbelow(True)

axs[1].invert_yaxis()  # labels read top-to-bottom
axs[1].set_yticks(y_pos2)
axs[1].set_yticklabels(categories2)
axs[1].grid(axis="x", color="gray", linestyle="--", linewidth=0.5)
axs[1].set_axisbelow(True)

# Plot each ratio on separate subplots
for idx, data_ratio in enumerate(data_ratios[:3]):
    lefts = np.zeros(len(categories))
    for data, color, label in zip(data_ratios, colors, labels):
        axs[0].barh(
            y_pos,
            data,
            bar_width,
            left=lefts,
            color=color,
            label=label if idx == 0 else "",
        )
        lefts += data

for idx, data_ratio in enumerate(data_ratios2[:3]):
    lefts = np.zeros(len(categories2))
    for data, color, label in zip(
        data_ratios2, colors, labels
    ):  # Use data_ratios2 here
        axs[1].barh(
            y_pos2,
            data,
            bar_width,
            left=lefts,
            color=color,
            label=label if idx == 0 else "",
        )
        lefts += data
fig.legend(labels, loc="upper center", bbox_to_anchor=(0.5, 1.1), ncol=2)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save the figure
plt.tight_layout()
plt.savefig("bar_85.pdf", bbox_inches="tight")
