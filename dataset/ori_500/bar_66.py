# ===================
# Part 1: Importing Libraries
# ===================
import colorsys
import numpy as np

np.random.seed(0)

import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Randomly generate new GDP growth rates with negative values to simulate a downturn
random_gdp_growth = {
    f"GDP_growth_{year}": -np.abs(np.random.rand(4).round(2))
    for year in [2018, 2019, 2020, 2021]
}


def hsl_to_rgb(h, s, l):
    return colorsys.hls_to_rgb(h, l, s)


# Random colors for each set of bars
colors = [
    hsl_to_rgb(hue, 0.5, 0.6) for hue in np.linspace(0, 1, 5)[:-1]
]  # Omitting the last value to avoid wrap-around duplication
countries = ["USA", "China", "Germany", "Brazil"]
ind = np.arange(4)
xlabel = "GDP Growth Rate (%)"
title = "Negative GDP Growth Rates by Country and Year"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create the figure and axes objects
fig, ax = plt.subplots(figsize=(10, 6))

# The width of the bars
bar_width = 0.2

# Define some hatch patterns to use for bars
hatch_patterns = ["/", "\\", "x", "o"]

# Plotting data with randomization
for i, (label, growth_rates) in enumerate(random_gdp_growth.items()):
    ax.barh(
        ind + bar_width * (i - 1.5),
        growth_rates,
        bar_width,
        label=label,
        color=colors[i],
        hatch=np.random.choice(hatch_patterns),
    )

# Adding labels, title, and custom y-axis tick labels, etc.
ax.set_xlabel(xlabel)
ax.set_title(title)
ax.set_yticks(ind)
ax.set_yticklabels(countries)

# Add random rotation to y-axis labels
for label in ax.get_yticklabels():
    label.set_rotation(np.random.randint(-30, 30))

# Adding legend
ax.legend(
    ncols=len(random_gdp_growth.keys()), loc="upper center", bbox_to_anchor=(0.5, 1.15)
)

# Invert y-axis to have the first entry at the top
plt.gca().invert_yaxis()

# Randomly decide whether to show grid lines for x-axis and set their properties
if np.random.rand() > 0.5:
    ax.xaxis.grid(
        True,
        linestyle=np.random.choice(["--", ":", "-."]),
        color=np.random.rand(
            3,
        ),
        alpha=0.7,
    )

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig("bar_66.pdf", bbox_inches="tight")
