# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Data for the plots
models = ["SolarMax", "WindFlow", "HydroBoost", "EnergyNet", "EcoModel"]
solar_values = [15.2, 20.4, 3.0, 12.1, 2.5]
wind_values = [3.5, 3.2, 4.5, 5.3, 3.4]
hydro_values = [6.9, -1.3, -0.2, 5.5, -0.4]

title1 = "Solar Energy"
axvline1 = 0
title2 = "Wind Energy"
axvline2 = 0
title3 = "Hydro Energy"
axvline3 = 0

xticks1 = [0, 5, 10, 15, 20]
xticks2 = [0, 5, 10]
xticks3 = [0, 5, 10, 15, 20]

xlabel = "Efficiency Improvement (%)"



# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Set the figure size to match the original image's dimensions
fig, axes = plt.subplots(1, 3, figsize=(10, 4))

# Plot for Beauty
axes[0].barh(models, solar_values, color="white", edgecolor="black")
axes[0].set_title(title1)
for i, v in enumerate(solar_values):
    axes[0].text(
        v - 0.5 if v < 0 else v + 0.5,
        i,
        f"{v}%",
        color="black",
        va="center",
        ha="right" if v < 0 else "left",
    )
axes[0].axvline(axvline1, color="black")

# Plot for MovieLens-1M
axes[1].barh(models, wind_values, color="white", edgecolor="black")
axes[1].set_title(title2)
for i, v in enumerate(wind_values):
    axes[1].text(
        v - 0.2 if v < 0 else v + 0.2,
        i,
        f"{v}%",
        color="black" if v > 0 else "red",
        va="center",
        ha="right" if v < 0 else "left",
    )
axes[1].axvline(axvline2, color="black")
axes[1].set_xticks(xticks1)

# Plot for Yelp
axes[2].barh(models, hydro_values, color="white", edgecolor="black")
axes[2].set_title(title3)
for i, v in enumerate(hydro_values):
    axes[2].text(
        v - 0.5 if v < 0 else v + 0.5,
        i,
        f"{v}%",
        color="black" if v > 0 else "red",
        va="center",
        ha="right" if v < 0 else "left",
    )
axes[2].axvline(axvline3, color="black")
axes[2].set_xticks(xticks2)

# Hide all axes except the bottom one
for ax in axes:
    for spine in ["left", "right", "top"]:
        ax.spines[spine].set_visible(False)

# Hide y-axis labels for axes[1] and axes[2]
axes[1].set_yticks([])
axes[1].set_yticklabels([])
axes[2].set_yticks([])
axes[2].set_yticklabels([])

# Add x-axis label for all axes
for ax in axes:
    ax.set_xlabel(xlabel)

plt.subplots_adjust(wspace=0.5)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig('bar_12.pdf', bbox_inches='tight')
