# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data (estimated from the image)
means = [np.random.uniform(-15, 0, 3) for m in range(4)]
errors = [np.random.randint(1, 5, 3) for n in range(4)]

# Labels
labels = ["GPT-4", "Claude-2.1", "Claude-2", "GPT-3.5"]
x = np.arange(len(labels) - 1)  # Adjusted to have 3 bars instead of 4

label_s = [
    ["Claude-2.1", "Claude-2", "GPT-3.5"],
    ["GPT-4", "Claude-2", "GPT-3.5"],
    ["GPT-4", "Claude-2.1", "Claude-2"],
    ["GPT-4", "Claude-2.1", "GPT-3.5"],
]
title = "Sellers (valuation 60)"
xlabel = "Buyer (valuation 40)"
ylim = [-20, 0]
yticks = [-20, -10, 0]


# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plotting
fig, axs = plt.subplots(
    2, 2, figsize=(8, 5)
)  # Adjusted to match the original image's dimensions
# Define colors for each bar
colors = [
    ["sandybrown", "lightseagreen", "indianred"],
    ["dodgerblue", "lightseagreen", "indianred"],
    ["dodgerblue", "sandybrown", "lightseagreen"],
    ["dodgerblue", "sandybrown", "indianred"],
]


# Loop through each subplot to set properties
for i, ax in enumerate(axs.flat):
    ax.bar(
        x,
        means[i],
        yerr=errors[i],
        color=colors[i],
        edgecolor="white",
        label=label_s[i],
    )
    ax.set_xlabel(f"{labels[i]} {xlabel}")
    ax.set_xticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.set_ylim(ylim)
    ax.set_yticks(yticks)
    ax.set_facecolor("#eaeaf2")
    ax.yaxis.grid(color="white", linestyle="-", linewidth=1)
    ax.set_axisbelow(True)
    ax.tick_params(axis="both", length=0)

fig.legend(
    labels,
    loc="lower center",
    ncol=4,
    bbox_to_anchor=(0.5, -0.1),
    title=title,
    facecolor="#eaeaf2",
)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout
plt.tight_layout()
# Legend
plt.savefig("errorbar_12.pdf", bbox_inches="tight")
