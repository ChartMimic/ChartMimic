# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Data
energy_sources = [
    "Anthracite",
    "Charcoal",
    "Wood",
    "Syngas",
    "Butane",
    "Propane",
    "Liquefied Natural Gas",
    "Compressed Natural Gas",
    "Fuel Cells",
    "Electricity",
    "Biodiesel",
    "Ethanol",
    "Methane",
    "Peat",
    "Waste",
    "Biofuel",
    "Hydrogen",
    "Wave",
    "Tidal",
    "Nuclear",
    "Geothermal",
    "Hydropower",
    "Wind",
    "Solar",
    "Biomass",
    "Natural Gas",
    "Oil",
    "Coal",
]
emission_change = [
    15,
    10,
    7,
    5,
    4,
    3,
    2.5,
    2,
    1,
    0.5,
    -1,
    -1.5,
    -2,
    -2.5,
    -3,
    -3,
    -3.5,
    -4,
    -5,
    -5,
    -7,
    -8,
    -10,
    -15,
    -18,
    -20,
    -22.5,
    -25,
]

# Extracted variables
xlim_values = (-1, len(energy_sources))
ylim_values = (-30, 20)
ylabel_text = "Emission Change (%)"
title_text = "Carbon Emission Changes by Energy Source"
legend_labels = ["Reduction > 5%", "5% <= Reduction <= 0%", "Increase"]
yticks_values = [-30, -20, -10, 0, 10, 20]

# Colors based on delta accuracy
colors = [
    "#346c98" if x < 0 else "#bb8b39" if 0 <= x <= 1 else "#41886c"
    for x in emission_change
]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plot
fig, ax = plt.subplots(figsize=(8, 5))  # Convert mm to inches for figsize
bars = ax.bar(energy_sources, emission_change, color=colors)

# Labels and Title
ax.set_xlim(*xlim_values)
ax.set_xticks([])
ax.set_ylim(*ylim_values)
ax.set_yticks(yticks_values)
ax.set_ylabel(ylabel_text)
ax.set_title(title_text)

# Add text labels
for bar, task in zip(bars, energy_sources):
    y = bar.get_height()
    if y < 0:
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            0.2,
            task,
            rotation=90,
            ha="center",
            va="bottom",
        )
    else:
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            -0.2,
            task,
            rotation=90,
            ha="center",
            va="top",
        )

# Legend
blue_patch = plt.Rectangle((0, 0), 1, 1, fc="blue", edgecolor="none")
orange_patch = plt.Rectangle((0, 0), 1, 1, fc="orange", edgecolor="none")
green_patch = plt.Rectangle((0, 0), 1, 1, fc="green", edgecolor="none")
ax.legend(
    [blue_patch, orange_patch, green_patch],
    legend_labels,
    loc="lower center",
    bbox_to_anchor=(0.5, -0.1),
    ncol=3,
    frameon=False,
)

plt.tick_params(axis="both", which="both", length=0)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout
plt.tight_layout()
plt.savefig('bar_42.pdf', bbox_inches='tight')
