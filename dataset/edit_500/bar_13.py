# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data
models = ["SolarBoost", "WindStream", "HydroFlow", "GeoThermal"]
energy_types = ["Solar", "Wind", "Hydro", "Geothermal", "Bioenergy"]
improvements = {
    "Solar": [5, 1.5, 1.3, 3.5],
    "Wind": [2.5, 2.3, -2.2, 2.8],
    "Hydro": [4.4, 0.8, -1, 1.3],
    "Geothermal": [4.0, 1.5, -2, 1.3],
    "Bioenergy": [4.4, -0.7, -3.9, 1.3],
}

# Colors for each energy type
colors = ["#8171d7", "#af4b3d", "#d07035", "#d6a741", "#639b48"]

xlabel = "Model"
ylabel = "Efficiency Improvement [%]"
legendtitle = "Energy Type"
title = "Energy Efficiency Improvement by Model and Energy Type"


# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Bar width
bar_width = 0.15

# Positions of the bars on the x-axis
r = np.arange(len(models))

for i, language in enumerate(energy_types):
    # Plot bars
    bars = plt.bar(
        r,
        improvements[language],
        color=colors[i],
        hatch="//",
        width=bar_width,
        edgecolor="white",
        label=language,
    )
    # Add text labels
    for bar, val in zip(bars, improvements[language]):
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height + (0.1 if val > 0 else -0.4),
            str(val),
            ha="center",
        )

    # Move the position for the next set of bars
    r = [x + bar_width for x in r]
# Add xticks on the middle of the group bars
plt.xlabel(xlabel)
plt.xticks([r + bar_width*2 for r in range(len(models))], models)

# Add ylabel
plt.ylabel(ylabel)

plt.gca().grid(color="gray", linewidth=0.5)
plt.gca().set_axisbelow(True)

# Create legend & Show graphic
plt.legend(
    title=legendtitle, bbox_to_anchor=(0.5, 1), loc="upper center", ncol=3
)
plt.title(title)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig('bar_13.pdf', bbox_inches='tight')
