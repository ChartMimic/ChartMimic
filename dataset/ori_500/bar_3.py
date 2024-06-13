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
# Data for each subplot
datasets = ["LIVE", "CSIQ", "TID2013", "LIVE-M"]
models = ["w/o DaQRN", "w/o CPRN", "w/o QCN", "Full model"]
colors = ["#5377ca", "#e08a57", "#91c4df", "#d1bc73"]
PLCC_data = {
    "LIVE": [0.964, 0.968, 0.966, 0.972],
    "CSIQ": [0.940, 0.945, 0.950, 0.965],
    "TID2013": [0.905, 0.895, 0.900, 0.910],
    "LIVE-M": [0.942, 0.946, 0.950, 0.952],
}
SROCC_data = {
    "LIVE": [0.966, 0.970, 0.968, 0.970],
    "CSIQ": [0.945, 0.950, 0.955, 0.971],
    "TID2013": [0.890, 0.900, 0.905, 0.915],
    "LIVE-M": [0.946, 0.950, 0.954, 0.954],
}
lims = [(0.960, 0.978), (0.930, 0.975), (0.885, 0.920), (0.940, 0.956)]
label = ["PICC", "SROCC"]
ylabel = "Metric Values"
title = "Models"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create subplots
fig, axs = plt.subplots(1, 4, figsize=(10, 3))

# Plot each subplot
for i, dataset in enumerate(datasets):
    x = [3, 6]  # the label locations
    width = 0.5  # the width of the bars
    for j in range(len(PLCC_data)):
        # PLCC bars
        axs[i].bar(
            x[0] + (j - 1.5) * width,
            PLCC_data[dataset][j],
            width,
            label=label[0],
            color=colors[j],
            edgecolor="white",
        )
        # SROCC bars
        axs[i].bar(
            x[1] + (j - 1.5) * width,
            SROCC_data[dataset][j],
            width,
            label=label[1],
            color=colors[j],
            edgecolor="white",
        )

    # Add some text for labels, title and custom x-axis tick labels, etc.
    axs[i].set_ylabel(ylabel)
    axs[i].set_ylim(lims[i][0], lims[i][1])
    axs[i].set_title(dataset)
    axs[i].set_xticks(x)
    axs[i].set_xticklabels(label)

# Add legend
legend_handles = [
    mpatches.Patch(color=color, label=label) for color, label in zip(colors, models)
]
# Create legend
fig.legend(
    handles=legend_handles,
    loc="upper center",
    title=title,
    ncol=4,
    bbox_to_anchor=(0.5, 1.15),
)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save the figure
plt.tight_layout()
plt.savefig("bar_3.pdf", bbox_inches="tight")
