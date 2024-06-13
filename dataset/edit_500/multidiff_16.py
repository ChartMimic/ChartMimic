import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)

import random

random.seed(42)

# ===================
# Part 2: Data Preparation
# ===================
# Data for bar chart
categories = ["Mutual Funds", "ETFs", "Bonds", "Stocks"]
successful_investments = [75, 68, 65, 90]

# Data for boxplot representing KPI for different investment products
kpi_data = [np.random.normal(0.55, 0.05, 100) for _ in categories]

# Threshold values for success evaluation
success_threshold_upper = 0.60
success_threshold_lower = 0.50

# Labels and limits
ylabels = ["# Successful Investments", "KPI Values"]
ax2hlineslabels = ["Upper Success Threshold", "Lower Success Threshold"]
ax2ylim = [0.35, 0.75]
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create figure and subplots and ax1, ax2 share the same x-axis
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6, 6), sharex=True)

# Bar chart
ax1.bar(
    categories,
    successful_investments,
    hatch="//",
    color="#b0c5de",
    edgecolor="black",
    width=0.6,
)
ax1.set_ylabel(ylabels[0])

# Boxplot chart
ax2.boxplot(kpi_data, positions=range(len(categories)), widths=0.6)
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
