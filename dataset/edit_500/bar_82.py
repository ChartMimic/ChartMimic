# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np; np.random.seed(0)

# ===================
# Part 2: Data Preparation
# ===================
# Data
categories = ["Renewables", "EVs", "Smart Grids", "Storage", "Carbon Capture"]
categories2 = ["Renewables Adv", "EVs Adv", "Smart Grids Adv", "Storage Adv", "Carbon Capture Adv"]
values = [220, 208, 125, 302, 207]
values2 = [180, 230, 270, 129, 226]
title = "Probability of Improvement over Baseline Energy Technologies"
xlabel = "Probability of Improvement (%)"
# Create color map
colors = plt.get_cmap("PuBuGn")(np.linspace(0.15, 0.85, len(categories2)))

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
fig, axes = plt.subplots(
    2,
    1,
    figsize=(6, 6),
    layout="constrained",
)

# Create horizontal bar chart
axes[0].barh(categories, values, color=colors)
axes[1].barh(categories, values2, color=colors)
axes[0].set_title(title)

# Apply the xticks and labels
axes[0].set_yticklabels(categories, rotation=45)
axes[1].set_yticklabels(categories2, rotation=45)

# Adding title and labels
plt.xlabel(xlabel)

# ===================
# Part 4: Saving Output
# ===================
# Show plot with tight layout
plt.tight_layout()
plt.savefig('bar_82.pdf', bbox_inches='tight')
