import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data
entities = ["Carbon Capture", "Geothermal", "Biomass", "Wave"]
protocols = [
    "Cost Efficiency",
    "Energy Output Efficiency",
    "Maintenance Costs",
    "Environmental Impact",
    "Regulatory Compliance",
    "Safety Standards",
]
# Simulated mean scores for different protocols (more distinctive values)
efficiency_means = np.array(
    [
        [80, 65, 85, 50, 75, 80],  # Carbon Capture
        [65, 85, 60, 80, 55, 75],  # Geothermal
        [75, 70, 90, 65, 85, 70],  # Biomass
        [50, 80, 55, 95, 80, 60],  # Wave
    ]
)

# Simulated standard deviations for scores (made more dramatic)
efficiency_std = np.array(
    [
        [6, 9, 7, 5, 6, 4],  # Carbon Capture
        [9, 5, 8, 6, 10, 3],  # Geothermal
        [7, 8, 5, 9, 7, 5],  # Biomass
        [8, 6, 9, 4, 8, 7],  # Wave
    ]
)
xlabel = "Energy Assessment Entity"
ylabel = "Efficiency and Cost Scores (%)"
ylim = [40, 105]
legendtitle = "Evaluation Protocol"


# ===================
# Part 3: Plot Configuration and Rendering
# ===================
fig, ax = plt.subplots(figsize=(10, 5))
# Subdued color palette
colors = ["#92c6ff", "#97f0aa", "#ff9f9a", "#d0bbff", "#ffb480", "#99e6e6"]

# Bar width and positions
bar_width = 0.12

# Positions of the bar groups
r = np.arange(len(entities))

# Drawing bars for different protocols
for i in range(len(protocols)):
    ax.bar(
        r + i * bar_width,
        efficiency_means[:, i],
        yerr=efficiency_std[:, i],
        width=bar_width,
        label=protocols[i],
        capsize=0,
        color=colors[i],
        edgecolor="black",
    )

# Set x-axis labels and axis properties
ax.set_xlabel(xlabel)
ax.set_xticks(r + bar_width * (len(protocols) / 2))
ax.set_xticklabels(entities)
ax.set_ylabel(ylabel)
ax.set_ylim(ylim)  # Adjust y-axis to better fit extended range

# Customize the legend
ax.legend(
    loc="lower center", bbox_to_anchor=(0.5, -0.4), title=legendtitle, ncol=3
)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig('errorbar_23.pdf', bbox_inches='tight')
