import numpy as np; np.random.seed(0)

import matplotlib.pyplot as plt
from math import pi

# ===================
# Part 2: Data Preparation
# ===================
# Define the data for the radar chart
categories = [
    "quantum_computing",
    "artificial_intelligence",
    "blockchain",
    "cybersecurity",
    "biotechnology",
    "nanotechnology",
    "robotics",
    "augmented_reality",
    "virtual_reality",
    "internet_of_things",
    "5G_technology",
    "autonomous_vehicles",
    "cloud_computing",
    "edge_computing",
    "fintech",
]
N = len(categories)

# Values for each algorithm
QuantumFlow = [80, 85, 78, 90, 88, 84, 82, 75, 80, 85, 90, 88, 85, 84, 82]
AIDeepDive = [45, 50, 48, 52, 50, 49, 51, 48, 47, 50, 52, 50, 49, 48, 47]
BlockSafe = [68, 70, 65, 72, 70, 68, 69, 65, 64, 68, 72, 70, 68, 67, 66]

labels=["QuantumFlow", "AIDeepDive", "BlockSafe"]
title="Advanced Tech Performance Comparison\n(speed-up ratio: 4)"
yticks=[20, 40, 60, 80, 100]
ylim=[0, 100]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Initialize the spider plot
fig, ax = plt.subplots(figsize=(5, 5), subplot_kw=dict(polar=True))

# We need to repeat the first value to close the circular graph:
QuantumFlow += QuantumFlow[:1]
AIDeepDive += AIDeepDive[:1]
BlockSafe += BlockSafe[:1]

# Calculate angle for each category
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]

# Draw one axe per variable and add labels
plt.xticks(angles[:-1], categories)

# Draw ylabels
ax.set_rlabel_position(0)
plt.yticks(yticks, color="grey", size=10)
plt.ylim(ylim)

# Plot data
ax.plot(
    angles, QuantumFlow, linewidth=3, linestyle="solid", label=labels[0], color="#ee9f9b"
)
ax.plot(angles, AIDeepDive, linewidth=3, linestyle="solid", label=labels[1], color="#549e3f")
ax.plot(
    angles, BlockSafe, linewidth=3, linestyle="solid", label=labels[2], color="#3c76af"
)

# Add a title and a legend
plt.title(title, size=15, color="black", y=1.1)
plt.legend(loc="upper left", bbox_to_anchor=(0.9, 1.3))

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout for better fit and save the plot
plt.tight_layout()
plt.savefig('radar_10.pdf', bbox_inches='tight')
