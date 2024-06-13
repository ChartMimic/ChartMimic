import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data setup
regions = ["Scandinavia", "Eastern Europe", "Southeast Asia", "South America"]
x = np.arange(len(regions))  # X-axis points

# Stress levels and work dissatisfaction scores in different regions
# These are fabricated values for demonstration
stress_levels_scores = np.array([-7.9, -6.8, -7.2, -7.0])  # Simulated negative values
work_dissatisfaction_scores = np.array([-8.1, -6.5, -7.3, -7.4])  # Simulated negative values

# Errors for both metrics
stress_levels_errors = np.array([0.3, 0.4, 0.2, 0.25])
work_dissatisfaction_errors = np.array([0.2, 0.35, 0.3, 0.25])

labels = ["Stress Levels", "Work Dissatisfaction"]
ylabels = ["Stress Levels Score", "Work Dissatisfaction Score"]

title = "Stress Levels and Work Dissatisfaction Across Regions"
ylims = [[-9, -6], [-9, -6]]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plotting setup
fig, ax1 = plt.subplots(figsize=(8, 5))

# Bar width and hatch patterns
width = 0.35
hatch_patterns = ["+", "x"]

# Colors for the bars
colors = ["#e18683", "#98bb93"]  # Greener and bluer shades

# Plot data on the left y-axis (air quality scores)
ax1.bar(
    x,
    stress_levels_scores,
    width,
    color=colors[0],
    hatch=hatch_patterns[0],
    label=labels[0],
    yerr=stress_levels_errors,
    capsize=5,
    edgecolor="black",
)

# Create a second y-axis sharing the same x-axis (water quality scores)
ax2 = ax1.twinx()
ax2.bar(
    x + width,
    work_dissatisfaction_scores,
    width,
    color=colors[1],
    hatch=hatch_patterns[1],
    label=labels[1],
    yerr=work_dissatisfaction_errors,
    capsize=5,
    edgecolor="black",
)

# Set the x-ticks to be in the middle of the two bars and add the labels
ax1.set_xticks(x + width / 2)
ax1.set_xticklabels(regions)

# Add a legend
ax1.legend(loc="lower left")
ax2.legend(loc="lower right")

# Set labels for y-axes
ax1.set_ylabel(ylabels[0], color=colors[0])
ax2.set_ylabel(ylabels[1], color=colors[1])

# Set colors for y-axes
ax1.tick_params(axis="y", colors=colors[0])
ax2.tick_params(axis="y", colors=colors[1])

# Set the limits for y-axes to fit the negative data
ax1.set_ylim(ylims[0])
ax2.set_ylim(ylims[0])

# Set title for the chart
plt.title(title)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig('errorbar_30.pdf', bbox_inches='tight')
