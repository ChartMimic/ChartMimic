# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Categories and values for different countries
categories = ["Germany", "China", "USA", "India", "Brazil"][::-1]
energy_consumption = [-4000, -6000, -5500, -3000, -2000][
    ::-1
]  # Total energy consumption in Petajoules
consumption_error = [400, 550, 400, 550, 400][
    ::-1
]  # Error values for energy consumption

renewable_energy = [20, 25, 18, 15, 10][
    ::-1
]  # Renewable energy usage as percentage of total
renewable_error = [3, 3.5, 4, 2.5, 3.8][::-1]  # Error values for renewable energy usage
xlabels = ["Energy Consumption (Petajoules)", "Renewable Energy Usage (%)"]
titles = ["Total Energy Consumption by Country", "Renewable Energy Usage by Country"]
xlims = [[-6500, 0], [0, 30]]


# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create horizontal bar chart with subplots
fig, axes = plt.subplots(1, 2, figsize=(10, 6), sharey=True)  # Adjust figure size

# Setting colors for the bars
neg_colors = ["#c5b3d6"] * 5
pos_colors = ["#76d7c4"] * 5

# Plotting bars for negative values (Energy Consumption)
bars = axes[0].barh(
    categories,
    energy_consumption,
    color=neg_colors,
    edgecolor="white",
    height=0.5,
    xerr=consumption_error,
    capsize=0,
)
axes[0].set_xlabel(xlabels[0])
axes[0].set_title(titles[0])
axes[0].invert_yaxis()
axes[0].set_xlim(xlims[0])
axes[0].xaxis.grid(True)
axes[0].spines["top"].set_visible(False)
axes[0].spines["right"].set_visible(False)

# Plotting bars for positive values (Renewable Energy Usage)
bars2 = axes[1].barh(
    categories,
    renewable_energy,
    color=pos_colors,
    edgecolor="white",
    height=0.5,
    xerr=renewable_error,
    capsize=0,
)
axes[1].set_xlabel(xlabels[1])
axes[1].set_title(titles[1])
axes[1].invert_yaxis()
axes[1].set_xlim(xlims[1])
axes[1].xaxis.grid(True)
axes[1].spines["top"].set_visible(False)
axes[1].spines["right"].set_visible(False)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig("errorbar_21.pdf", bbox_inches="tight")
