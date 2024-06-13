import numpy as np; np.random.seed(0)

import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Data for the radar chart
labels = np.array(
    [
        "[1] Solar Panel\nInstallation",
        "[2] Wind Turbine\nSetup",
        "[3] Hydro Power\nConstruction",
        "[4] Geothermal Plant\nDevelopment",
        "[5] Energy Storage\nSolutions",
        "[6] Smart Grid\nImplementation",
        "[7] Electric Vehicle\nInfrastructure",
        "[8] Biomass Energy\nProduction",
        "[9] Energy Efficiency\nImprovements",
        "[10] Renewable Energy\nPolicy",
    ]
)
baseline_values = np.array([80, 70, 60, 50, 80, 70, 42, 35, 50, 85])
retrosyn2_values = np.array([75, 65, 55, 85, 65, 55, 55, 45, 95, 90])
yticks = [10, 20, 30, 40, 50, 60, 70, 80, 90]
ytickslabel = ["10", "20", "30", "40", "50", "60", "70", "80", "90"]
ylim = [0, 100]
labels2 = ["Baseline", "GreenTech Initiative"]
rgrids = [30, 40, 50, 60, 70, 80, 90]


# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Size of the figure

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Number of variables
num_vars = len(labels)

# Compute angle for each axis
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# The plot is circular, so we need to "complete the loop" and append the start to the end.
baseline_values = np.concatenate((baseline_values, [baseline_values[0]]))
retrosyn2_values = np.concatenate((retrosyn2_values, [retrosyn2_values[0]]))
angles += angles[:1]

# Draw one axe per variable and add labels
plt.xticks(angles[:-1], [], color="black", size=8, ha="right")
for angle, label in zip(angles[:-1], labels):  # Remove the appended first element
    if (
        angle < np.pi / 2 or angle > 3 * np.pi / 2
    ):  # If the text is at the bottom or right side of the chart
        ax.text(
            angle,
            110,
            label,
            horizontalalignment="left",
            size=8,
            verticalalignment="bottom",
        )
    else:  # If the text is at the top or left side of the chart
        ax.text(
            angle,
            110,
            label,
            horizontalalignment="right",
            size=8,
            verticalalignment="bottom",
        )

# Draw ylabels
ax.set_rlabel_position(0)
plt.yticks(
    yticks,
    ytickslabel,
    color="grey",
    size=8,
)
plt.ylim(ylim)

# Plot data
ax.plot(
    angles,
    baseline_values,
    linewidth=1,
    linestyle="solid",
    label=labels2[0],
    color="blue",
)
ax.fill(angles, baseline_values, "blue", alpha=0.1)

ax.plot(
    angles,
    retrosyn2_values,
    linewidth=1,
    linestyle="solid",
    label=labels2[1],
    color="orange",
)
ax.fill(angles, retrosyn2_values, "orange", alpha=0.1)

# Add legend
plt.legend(loc="upper right", bbox_to_anchor=(0.1, 0.1))

# Adjust gridlines
ax.set_rgrids(
    rgrids,
    labels=rgrids,
    angle=0,
    color="black",
)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout for better fit and save the plot
plt.tight_layout()
plt.savefig('radar_5.pdf', bbox_inches='tight')
