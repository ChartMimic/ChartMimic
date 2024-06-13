# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Data for plotting
efficiency = [
    15,
    20,
    25,
    30,
    35,
    40,
    45,
    50,
]  # Renewable energy efficiency values in percentage
carbon_reduction = [
    5,
    45,
    23,
    42,
    23,
    10,
    2,
    0,
]  # Corresponding carbon reduction percentages
energy_sources = [
    "Solar",
    "Wind",
    "Hydro",
    "Geothermal",
    "Biomass",
    "Nuclear",
    "Tidal",
    "Wave",
]
colors = [
    "yellow",
    "blue",
    "aqua",
    "brown",
    "green",
    "orange",
    "purple",
    "red",
]  # Colors representing different energy sources
markers = ["o", "o", "o", "o", "o", "o", "o", "x"]  # Different marker for 'Wave'
xlabel = "Efficiency (%)"
ylabel = "Carbon Reduction (%)"
legend_title = "Energy Source"
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create figure and axis
fig, ax = plt.subplots(figsize=(8, 4))

# Plot each point with corresponding color and marker
for i, (eff, carbon, color, marker) in enumerate(
    zip(efficiency, carbon_reduction, colors, markers)
):
    ax.scatter(eff, carbon, color=color, marker=marker, label=energy_sources[i])

# Set labels and title
ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)

# Create legend
legend = ax.legend(title=legend_title, bbox_to_anchor=(1.05, 1), loc="upper left")

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout to make room for the legend
plt.tight_layout()
plt.savefig('scatters_16.pdf', bbox_inches='tight')
