# ===================
# Part 1: Importing Libraries
# ===================
import numpy as np; np.random.seed(0)

import matplotlib.pyplot as plt
from math import pi

# ===================
# Part 2: Data Preparation
# ===================
# Define the data for the radar chart
categories = [
    "bg",
    "de",
    "el",
    "en",
    "es",
    "fr",
    "hi",
    "ru",
    "th",
    "tr",
    "ur",
    "vi",
    "zh",
    "ar",
    "sw",
]
N = len(categories)

# Values for each algorithm
DeeBERT = [70, 75, 80, 85, 90, 85, 70, 65, 70, 75, 80, 85, 90, 95, 60]
PABEE = [35, 47, 45, 38, 35, 39, 43, 36, 35, 37, 45, 48, 38, 39, 45]
CascadeL = [66, 55, 67, 64, 68, 59, 55, 65, 62, 58, 67, 65, 58, 65, 54]

labels=["DeeBERT", "PABEE", "CascadeL"]
title="XNLI\n(speed-up ratio: 4)"
yticks=[20, 40, 60, 80]
ylim=[0, 100]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Initialize the spider plot
fig, ax = plt.subplots(figsize=(5, 5), subplot_kw=dict(polar=True))

# We need to repeat the first value to close the circular graph:
DeeBERT += DeeBERT[:1]
PABEE += PABEE[:1]
CascadeL += CascadeL[:1]

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
    angles, DeeBERT, linewidth=3, linestyle="solid", label=labels[0], color="#ee9f9b"
)
ax.plot(angles, PABEE, linewidth=3, linestyle="solid", label=labels[1], color="#549e3f")
ax.plot(
    angles, CascadeL, linewidth=3, linestyle="solid", label=labels[2], color="#3c76af"
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
