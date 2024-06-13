# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data for the bar chart
models = [
    "Engstrom (M1)",
    "Zhang (M2)",
    "Rice (M3)",
    "Rade (M4)",
    "Hendrycks (M5)",
    "Addep. (M6)",
    "Carmon (M7)",
]
robust_error = [44.15, 44.05, 41.55, 40.90, 40.65, 39.45, 36.70]

# Data for the heatmap
rnfs = np.array(
    [
        [0.00, 6.20, 4.90, 4.25, 5.40, 3.65, 3.25],
        [6.65, 0.00, 5.15, 2.80, 5.25, 2.85, 2.50],
        [7.75, 7.70, 0.00, 5.35, 6.30, 4.80, 4.15],
        [7.85, 5.90, 6.25, 0.00, 5.45, 3.85, 2.95],
        [9.15, 8.75, 7.25, 5.75, 0.00, 5.25, 4.95],
        [8.65, 7.40, 6.95, 5.25, 6.45, 0.00, 4.00],
        [10.90, 9.90, 9.15, 7.15, 8.95, 6.85, 0.00],
    ]
)
ax1title="Robust Error (%)"
ax2title="RNFs (%)"
ax1xlim=[0, 50]

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
