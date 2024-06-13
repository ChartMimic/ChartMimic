# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

import matplotlib.patches as mpatches

# ===================
# Part 2: Data Preparation
# ===================
# Data
models = [
    "Deep Ens.",
    "Dropout",
    "Laplace",
    "SNGP",
    "HET-XL",
    "Baseline",
    "GP",
    "Shallow Ens.",
    "DUQ",
    "Corr. Pred.",
]
log_probabilities = [
    -0.5,
    -0.394,
    -0.443,
    -0.531,
    -0.539,
    -0.541,
    -0.543,
    -0.552,
    -0.590,
    -0.819,
]
errors = [0.05] * 8 + [0.09] + [0.3]  # Assuming constant error for all but the last bar
legendtitle = ["Distributional", "Deterministic"]
ylabel = "Log Probability ↑"


# ===================
# Part 3: Plot Configuration and Rendering
# ===================
colors = ["#58a65d"] * 5 + ["#9ba0a6"] + ["#58a65d"] * 2 + ["#f2bf42"] * 2
# Plot
fig, ax = plt.subplots(figsize=(6, 4))
bars = ax.bar(
    models,
    log_probabilities,
    yerr=errors,
    color=colors,
    capsize=10,
    error_kw={
        "ecolor": "gray",
    },
)

# Annotate bars with log probability values
for bar, log_prob, error, model in zip(bars, log_probabilities, errors, models):
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() - error - 0.1,
        f"{log_prob:.3f}",
        ha="center",
        va="bottom",
    )
    # Add model name on the bar
    ax.text(
        bar.get_x() + bar.get_width() / 2, 0, model, ha="center", va="top", rotation=90
    )

# Legend
ax.legend(legendtitle, loc="lower left")
ax.set_xticks([])
plt.tick_params(axis="x", which="both", length=0)
# Labels and grid
ax.set_ylabel(ylabel)
ax.set_ylim(-2.00, 0.00)

ax.yaxis.grid(True)
ax.set_axisbelow(True)

# Create patches for the legend
patch1 = mpatches.Patch(color="#58a65d", label=legendtitle[0])
patch2 = mpatches.Patch(color="#f2bf42", label=legendtitle[1])

# Add legend
ax.legend(handles=[patch1, patch2], loc="lower left", frameon=False)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout to match the original image's dimensions
plt.tight_layout()
plt.savefig("errorbar_1.pdf", bbox_inches="tight")
