# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data (assuming correlation coefficients are provided in a 2D array)
data = np.array(
    [
        [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
        [0.19, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
        [0.19, 0.62, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
        [0.26, 0.53, 0.52, np.nan, np.nan, np.nan, np.nan, np.nan],
        [0.16, 0.39, 0.50, 0.39, np.nan, np.nan, np.nan, np.nan],
        [0.03, 0.24, 0.24, 0.34, 0.20, np.nan, np.nan, np.nan],
        [-0.03, 0.10, -0.03, 0.06, -0.10, 0.06, np.nan, np.nan],
        [0.07, 0.28, 0.26, 0.26, 0.20, 0.21, 0.05, np.nan],
    ]
)

metrics = [
    "LexRank",
    "ROUGE",
    "BERTScore",
    "SimCSE",
    "PMI",
    "GPT-3.5",
    "CrossAttn",
    "PPL",
]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
fig, ax = plt.subplots(
    figsize=(8, 6)
)  # Adjusted to match the original image's dimensions

# Create heatmap
cax = ax.matshow(data, cmap="Blues")

# Add color bar
plt.colorbar(cax)

# Set axis labels
ax.set_xticks(np.arange(len(metrics)))
ax.set_yticks(np.arange(len(metrics)))
ax.set_xticklabels(metrics)
ax.set_yticklabels(metrics)

# Rotate the tick labels bottom and rotated to 90
ax.xaxis.set_ticks_position("bottom")
ax.xaxis.set_tick_params(rotation=90)

# Loop over data dimensions and create text annotations
for i in range(len(metrics)):
    for j in range(len(metrics)):
        if not np.isnan(data[i, j]):
            if data[i, j] > 0.25:
                text = ax.text(
                    j, i, f"{data[i, j]:.2f}", ha="center", va="center", color="white"
                )
            else:
                text = ax.text(
                    j, i, f"{data[i, j]:.2f}", ha="center", va="center", color="black"
                )

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["bottom"].set_visible(False)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig("heatmap_8.pdf", bbox_inches="tight")
