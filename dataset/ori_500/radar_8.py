# ===================
# Part 1: Importing Libraries
# ===================

import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)

# ===================
# Part 2: Data Preparation
# ===================
# Data for each method
labels = np.array(
    [
        "Long-horizon\nForecasting",
        "Imputation",
        "Anomaly\nDetection",
        "Short-horizon\nForecasting",
        "Classification",
    ]
)
stats_moment = np.array([80, 70, 40, 85, 75])
stats_gpt4ts = np.array([55, 80, 85, 80, 40])
stats_timesnet = np.array([70, 35, 80, 75, 80])

# Number of variables
num_vars = len(labels)

# Compute angle for each axis
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# The plot is made circular, so we need to "complete the loop" and append the start to the end.
stats_moment = np.concatenate((stats_moment, [stats_moment[0]]))
stats_gpt4ts = np.concatenate((stats_gpt4ts, [stats_gpt4ts[0]]))
stats_timesnet = np.concatenate((stats_timesnet, [stats_timesnet[0]]))
angles += angles[:1]

# Extracted variables
label_moment = "MOMENT"
label_gpt4ts = "GPT4TS"
label_timesnet = "TimesNet"
xlim_values = None  # Not specified in the code
ylim_values = (0, 100)
xlabel_value = None  # Not specified in the code
ylabel_value = None  # Not specified in the code
xticks_values = angles[:-1]
yticks_values = [20, 40, 60, 80]
xtickslabel_values = labels
ytickslabel_values = []  # Empty list as specified in plt.yticks
title_value = None  # Not specified in the code
axhline_value = None  # Not specified in the code
axvline_value = None  # Not specified in the code

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Size of the figure
fig, ax = plt.subplots(figsize=(5, 5), subplot_kw=dict(polar=True))

# Draw one axe per variable and add labels with increased padding
plt.xticks(xticks_values, xtickslabel_values)
ax.tick_params(pad=23)  # Increase the distance of the label from the axis

# Draw ylabels and set them to be dashed
ax.set_rlabel_position(0)
plt.yticks(yticks_values, ytickslabel_values, color="grey", size=7)
plt.ylim(ylim_values)

# Customizing the grid (set grid to be dashed)
ax.yaxis.grid(True, linestyle="--", color="grey", linewidth=0.5)

# Plot data
ax.plot(
    angles, stats_moment, color="red", linewidth=1, linestyle="solid", label=label_moment
)
ax.fill(angles, stats_moment, color="red", alpha=0.25)

ax.plot(
    angles, stats_gpt4ts, color="blue", linewidth=1, linestyle="dashed", label=label_gpt4ts
)
ax.fill(angles, stats_gpt4ts, color="blue", alpha=0.25)

ax.plot(
    angles,
    stats_timesnet,
    color="green",
    linewidth=1,
    linestyle="dotted",
    label=label_timesnet,
)
ax.fill(angles, stats_timesnet, color="green", alpha=0.25)

# Add legend
plt.legend(loc="lower center", bbox_to_anchor=(0.5, -0.3), ncol=3, frameon=False)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout for better fit
plt.tight_layout()

# Show the plot
plt.savefig('radar_8.pdf', bbox_inches='tight')
