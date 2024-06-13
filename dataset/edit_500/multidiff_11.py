import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data for the bar chart
# Updated data for sports models (e.g., athlete performance models)
models = [
    "Bolt (M1)",
    "Phelps (M2)",
    "Biles (M3)",
    "Williams (M4)",
    "Ronaldo (M5)",
    "James (M6)",
    "Federer (M7)",
]
robust_error = [15.35, 14.80, 13.55, 12.95, 12.50, 11.75, 10.60]

# Updated data for the heatmap representing comparative performance metrics
rnfs = np.array(
    [
        [0.00, 2.25, 1.75, 1.60, 2.10, 1.15, 1.00],
        [2.35, 0.00, 1.55, 1.25, 2.30, 1.20, 1.05],
        [2.50, 2.40, 0.00, 1.70, 1.85, 1.50, 1.35],
        [2.60, 2.00, 2.35, 0.00, 1.90, 1.25, 1.10],
        [2.90, 2.75, 2.15, 1.95, 0.00, 1.70, 1.45],
        [2.85, 2.50, 2.25, 1.75, 1.95, 0.00, 1.30],
        [3.20, 3.10, 2.75, 2.15, 2.80, 2.00, 0.00],
    ]
).T

# Titles and labels for plots
ax1title = "Robust Performance Error (%)"
ax2title = "Relative Performance Fluctuation (RNFs) (%)"
ax1xlim = [0, 20]

# Placeholder to show where heatmaps and other plots would be plotted. Actual plotting code is not included.
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create figure and axes
fig, (ax1, ax2) = plt.subplots(
    1, 2, figsize=(10, 6), gridspec_kw={"width_ratios": [1, 1.25]}
)

# Bar chart
y_pos = np.arange(len(models))
ax1.barh(y_pos, robust_error, color="#4a895c")
ax1.set_yticks(y_pos)
ax1.set_yticklabels(models, fontsize=10)
ax1.invert_yaxis()  # labels read top-to-bottom
ax1.set_title(ax1title, fontsize=12)
ax1.set_xlim(ax1xlim)
for i, v in enumerate(robust_error):
    ax1.text(v - 8.0, i, "{:.2f}".format(v), color="white", va="center")

# Heatmap
im = ax2.imshow(rnfs, cmap="summer", aspect="auto")

# We want to show all ticks...
ax2.set_xticks(np.arange(len(models)))
# ax2.set_yticks(np.arange(len(models)))
# ... and label them with the respective list entries
ax2.set_xticklabels(models, fontsize=10)
ax2.yaxis.set_visible(False)

# Rotate the tick labels and set their alignment.
plt.setp(ax2.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

# Loop over data dimensions and create text annotations.
for i in range(len(models)):
    for j in range(len(models)):
        text = ax2.text(
            j, i, "{:.2f}".format(rnfs[i, j]), ha="center", va="center", color="black"
        )

ax2.set_title(ax2title, fontsize=12)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save the figure
plt.tight_layout()
plt.savefig('multidiff_11.pdf', bbox_inches='tight')
