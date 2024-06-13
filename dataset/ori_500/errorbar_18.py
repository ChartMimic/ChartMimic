# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Regions for environmental data
regions = ["Europe", "Asia", "North America", "South America", "Africa"]

# Annual Carbon Dioxide Emissions in millions of metric tons (hypothetical data)
co2_emissions = [3200, 10400, 5000, 1800, 1200]  # Approximate values
co2_emissions_errors = [600, 700, 600, 400, 300]  # Error estimates

# Forest Coverage Rate (% of land area covered by forests)
forest_coverage = [38, 25, 34, 52, 21]  # Approximate percentages
forest_coverage_errors = [6, 5, 7, 8, 7]  # Error estimates

# Renewable Energy Usage (% of total energy consumption)
renewable_energy = [34, 25, 28, 45, 18]  # Approximate percentages
renewable_energy_errors = [6, 6, 7, 8, 9]  # Error estimates

titles = [
    "Annual Carbon Dioxide Emissions",
    "Forest Coverage Rate",
    "Renewable Energy Usage",
]
xlabels = ["Millions of Metric Tons", "% of Land Area", "% of Total Energy Consumption"]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create a subplot for each category
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(6, 9))
# Colors for bars, each plot can have its own color map or shared
colors = plt.get_cmap("Pastel2")(np.linspace(0.2, 0.8, 5))


def add_bars_with_annotations(ax, data, errors, colors):
    bars = ax.barh(regions, data, xerr=errors, color=colors, capsize=0)
    for i, bar in enumerate(bars):
        width = bar.get_width()
        label_x_pos = bar.get_width() + errors[i] * 0.2
        ax.text(
            label_x_pos, bar.get_y() + bar.get_height() / 2, f"{width}", va="bottom"
        )


# Plot Carbon Dioxide Emissions on the first subplot
ax1.barh(
    regions,
    co2_emissions,
    xerr=co2_emissions_errors,
    edgecolor="black",
    color=colors,
    capsize=0,
)
add_bars_with_annotations(ax1, co2_emissions, co2_emissions_errors, colors)
ax1.set_title(titles[0])
ax1.set_xlabel(xlabels[0])
ax1.xaxis.grid(True, linestyle="--")
ax1.spines["right"].set_visible(False)
ax1.spines["top"].set_visible(False)

# Plot Forest Coverage Rate on the second subplot
ax2.barh(
    regions,
    forest_coverage,
    xerr=forest_coverage_errors,
    edgecolor="black",
    color=colors,
    capsize=0,
)
add_bars_with_annotations(ax2, forest_coverage, forest_coverage_errors, colors)
ax2.set_title(titles[1])
ax2.set_xlabel(xlabels[1])
ax2.xaxis.grid(True, linestyle="--")
ax2.spines["right"].set_visible(False)
ax2.spines["top"].set_visible(False)

# Plot Renewable Energy Usage on the third subplot
ax3.barh(
    regions,
    renewable_energy,
    xerr=renewable_energy_errors,
    edgecolor="black",
    color=colors,
    capsize=0,
)
add_bars_with_annotations(ax3, renewable_energy, renewable_energy_errors, colors)
ax3.set_title(titles[2])
ax3.set_xlabel(xlabels[2])
ax3.xaxis.grid(True, linestyle="--")
ax3.spines["right"].set_visible(False)
ax3.spines["top"].set_visible(False)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save the figure
plt.tight_layout()
plt.savefig("errorbar_18.pdf", bbox_inches="tight")
