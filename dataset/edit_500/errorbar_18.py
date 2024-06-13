import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Regions for environmental data
regions = ["North", "East", "West", "South", "Central"]

# Annual Traffic Accident Rates (hypothetical data)
accident_rates = [2300, 1500, 2800, 1900, 1700]  # Approximate values
accident_rates_errors = [200, 180, 250, 210, 190]  # Error estimates

# Public Transport Usage Rate (% of population using public transport)
transport_usage = [45, 30, 55, 40, 35]  # Approximate percentages
transport_usage_errors = [5, 4, 6, 5, 4]  # Error estimates

# Bicycle Lane Coverage (% of total road length)
bicycle_lane_coverage = [12, 20, 15, 10, 18]  # Approximate percentages
bicycle_lane_coverage_errors = [2, 3, 2, 1, 2]  # Error estimates

titles =["Annual Traffic Accident Rates","Public Transport Usage Rate","Bicycle Lane Coverage"]
xlabels=["Number of Accidents","% of Population","% of Road Length"]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create a subplot for each category
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(6, 9))
# Colors for bars, each plot can have its own color map or shared
colors = plt.get_cmap("Pastel2")(np.linspace(0.2, 0.8, 5))


def add_bars_with_annotations(ax, data, errors, colors):
    bars = ax.barh(regions, data, xerr=errors, color=colors, capsize=0)
    for i, bar in enumerate(bars):
        width = bar.get_width()
        label_x_pos = bar.get_width() + errors[i] * 0.2
        ax.text(
            label_x_pos, bar.get_y() + bar.get_height() / 2, f"{width}", va="bottom"
        )


# Plot Carbon Dioxide Emissions on the first subplot
ax1.barh(
    regions,
    accident_rates,
    xerr=accident_rates_errors,
    edgecolor="black",
    color=colors,
    capsize=0,
)
add_bars_with_annotations(ax1, accident_rates, accident_rates_errors, colors)
ax1.set_title(titles[0])
ax1.set_xlabel(xlabels[0])
ax1.xaxis.grid(True, linestyle="--")
ax1.spines["right"].set_visible(False)
ax1.spines["top"].set_visible(False)

# Plot Forest Coverage Rate on the second subplot
ax2.barh(
    regions,
    transport_usage,
    xerr=transport_usage_errors,
    edgecolor="black",
    color=colors,
    capsize=0,
)
add_bars_with_annotations(ax2, transport_usage, transport_usage_errors, colors)
ax2.set_title(titles[1])
ax2.set_xlabel(xlabels[1])
ax2.xaxis.grid(True, linestyle="--")
ax2.spines["right"].set_visible(False)
ax2.spines["top"].set_visible(False)

# Plot Renewable Energy Usage on the third subplot
ax3.barh(
    regions,
    bicycle_lane_coverage,
    xerr=bicycle_lane_coverage_errors,
    edgecolor="black",
    color=colors,
    capsize=0,
)
add_bars_with_annotations(ax3, bicycle_lane_coverage, bicycle_lane_coverage_errors, colors)
ax3.set_title(titles[2])
ax3.set_xlabel(xlabels[2])
ax3.xaxis.grid(True, linestyle="--")
ax3.spines["right"].set_visible(False)
ax3.spines["top"].set_visible(False)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save the figure
plt.tight_layout()
plt.savefig('errorbar_18.pdf', bbox_inches='tight')
