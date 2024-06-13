# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)

import random

random.seed(42)

# ===================
# Part 2: Data Preparation
# ===================
# Data for bar chart
categories = ["c1355", "c1908", "c2670", "c3540"]
successful_adv_circuits = [40, 60, 50, 30]

# Data for boxplot
omla_kpa_data = [np.random.normal(0.45, 0.03, 100) for _ in categories]

success_threshold_upper = 0.50
success_threshold_lower = 0.35
ylabels=["# successful\n adv. circuits", "OMLA KPA"]
ax2hlineslabels=["Upper success threshold","Lower success threshold"]
ax2ylim=[0.30, 0.70]
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create figure and subplots and ax1, ax2 share the same x-axis
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6, 6), sharex=True)

# Bar chart
ax1.bar(
    categories,
    successful_adv_circuits,
    hatch="//",
    color="#b0c5de",
    edgecolor="black",
    width=0.6,
)
ax1.set_ylabel(ylabels[0])

# Boxplot chart
ax2.boxplot(omla_kpa_data, positions=range(len(categories)), widths=0.6)
ax2.hlines(
    success_threshold_upper,
    xmin=-0.5,
    xmax=len(categories) - 0.5,
    colors="red",
    linestyles="dashed",
    label=ax2hlineslabels[0],
)
ax2.hlines(
    success_threshold_lower,
    xmin=-0.5,
    xmax=len(categories) - 0.5,
    colors="red",
    linestyles="dashed",
    label=ax2hlineslabels[1],
)
ax2.fill_between(
    [-0.5, len(categories) - 0.5],
    success_threshold_lower,
    success_threshold_upper,
    color="grey",
    alpha=0.15,
)
ax2.set_ylabel(ylabels[1])
ax2.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"{x:.2f}"))
ax2.set_ylim(ax2ylim)
ax2.set_xticklabels(categories)
ax2.legend(loc="upper right")

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save plot
plt.tight_layout()
plt.savefig('multidiff_16.pdf', bbox_inches='tight')
