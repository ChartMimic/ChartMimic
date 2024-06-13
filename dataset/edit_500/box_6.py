import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
data_solar_efficiency = [
    np.random.normal(22, 2, 50),
    np.random.normal(20, 2, 50),
    np.random.normal(18, 2, 50),
]
data_wind_efficiency = [
    np.random.normal(20, 2, 50),
    np.random.normal(23, 2, 50),
    np.random.normal(19, 2, 50),
]
data_hydro_efficiency = [
    np.random.normal(24, 2, 50),
    np.random.normal(21, 2, 50),
    np.random.normal(17, 2, 50),
]

# Positions of the boxplots
positions_solar = [1, 5, 9]
positions_wind = [2, 6, 10]
positions_hydro = [3, 7, 11]

xticklabels = ["Morning", "Afternoon", "Evening"]
xticks = [2, 6, 10]
xlabel = "Time of Day"
ylabel = "Energy Efficiency (%)"
legend_labels = ["Solar (25%-75%)", "Wind (25%-75%)", "Hydro (25%-75%)"]
ylim = [10, 30]
legendtitle = "Energy Source"


# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create figure and axes
fig, ax = plt.subplots(figsize=(8, 6))

# Plotting the boxplots
bp_gmml = ax.boxplot(
    data_solar_efficiency,
    positions=positions_solar,
    widths=1,
    patch_artist=True,
    boxprops=dict(facecolor="#ab5b4e"),
    medianprops=dict(color="black"),
    showfliers=False,
)
bp_gml = ax.boxplot(
    data_wind_efficiency,
    positions=positions_wind,
    widths=1,
    patch_artist=True,
    boxprops=dict(facecolor="#54addb"),
    medianprops=dict(color="black"),
    showfliers=False,
)
bp_ao = ax.boxplot(
    data_hydro_efficiency,
    positions=positions_hydro,
    widths=1,
    patch_artist=True,
    boxprops=dict(facecolor="#a6edd1"),
    medianprops=dict(color="black"),
    showfliers=False,
)

# Customizing the axes
ax.set_xticks(xticks)
ax.set_xticklabels(xticklabels)
ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)
ax.set_ylim(ylim)
ax.yaxis.grid(True, linestyle="--", linewidth=0.5)
ax.xaxis.grid(True, linestyle="--", linewidth=0.5)

# Adding legend

ax.legend(
    [bp_gmml["boxes"][0], bp_gml["boxes"][0], bp_ao["boxes"][0]],
    legend_labels,
    loc="lower left",
    title=legendtitle
)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig('box_6.pdf', bbox_inches='tight')
