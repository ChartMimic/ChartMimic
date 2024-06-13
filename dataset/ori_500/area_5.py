# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

# ===================
# Part 2: Data Preparation
# ===================
year = [1950, 1960, 1970, 1980, 1990, 2000, 2010, 2018]
population_by_continent = {
    "africa": [228, 284, 365, 477, 631, 814, 1044, 1275],
    "americas": [943, 606, 540, 727, 840, 425, 519, 619],
    "asia": [1394, 1686, 2120, 1625, 1202, 1714, 2169, 2560],
    "europe": [220, 253, 276, 295, 310, 303, 294, 293],
    "oceania": [200, 300, 340, 360, 280, 260, 320, 280],
}

# Extracted variables
legend_labels = list(population_by_continent.keys())
xlim_values = (1950, 2018)
ylim_values = (0, 6000)
xlabel_value = "Year"
ylabel_value = "Number of people (millions)"
title_value = "World population"
legend_loc = "upper center"
legend_reverse = False
legend_frameon = False
legend_ncol = 5
legend_bbox_to_anchor = (0.5, 1.08)
title_y_position = 1.08
colors = ["#b2e7aa", "#fae18f", "#d75949", "#f0906d", "#a1a8d6"]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
fig, ax = plt.subplots(figsize=(8, 6))
ax.stackplot(
    year,
    population_by_continent.values(),
    labels=legend_labels,
    alpha=0.8,
    colors=colors,
)
ax.legend(
    loc=legend_loc,
    reverse=legend_reverse,
    frameon=legend_frameon,
    ncol=legend_ncol,
    bbox_to_anchor=legend_bbox_to_anchor,
)
ax.set_xlim(*xlim_values)
ax.set_ylim(*ylim_values)
ax.set_title(title_value, y=title_y_position)
ax.set_xlabel(xlabel_value)
ax.set_ylabel(ylabel_value)
ax.tick_params(axis="both", which="both", length=0)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig("area_5.pdf", bbox_inches="tight")
