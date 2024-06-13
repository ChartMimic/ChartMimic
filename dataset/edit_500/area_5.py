
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0); np.random.seed(0)

# ===================
# Part 2: Data Preparation
# ===================
year = [1950, 1960, 1970, 1980, 1990, 2000, 2010, 2018]
population_by_continent = {
    "africa": [75, 74, 72, 60, 45, 40, 37, 34],      # Forest cover decreasing
    "americas": [85, 80, 75, 70, 65, 60, 55, 50],    # Forest cover decreasing
    "asia": [66, 63, 56, 50, 46, 40, 38, 37],        # Forest cover decreasing
    "europe": [40, 38, 36, 34, 32, 30, 28, 26],      # Forest cover decreasing
    "oceania": [20, 28, 30, 24, 15, 20, 18, 16],     # Forest cover decreasing
}

# Extracted variables
legend_labels = ["AF rate", "AM rate", "AS rate", "EU rate", "OC rate"]
xlim_values = (1950, 2018)
ylim_values = (0, 300)
xlabel_value = "Year"
ylabel_value = "Forest Cover (millions of hectares)"
title_value = "Global Forest Cover Decline by Region"
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
    colors =colors,
)
ax.legend(
    loc=legend_loc, reverse=legend_reverse, frameon=legend_frameon, ncol=legend_ncol, bbox_to_anchor=legend_bbox_to_anchor
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
plt.savefig('area_5.pdf', bbox_inches='tight')
