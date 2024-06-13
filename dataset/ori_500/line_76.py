# ===================
# Part 1: Importing Libraries
# ===================

import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)

# ===================
# Part 2: Data Preparation
# ===================
# Setting up the data
models = ["Model X", "Model Y", "Model Z"]
configurations = ["Config A", "Config B", "Config C"]
data = {
    "Model X": {
        "Config A": [83.19, 86.67, 81.32, 87.16, 82.89, 81.83, 85.87, 80.2, 88.29, 80.05],
        "Config B": [81.78, 77.7, 82.35, 84.62, 77.49, 80.76, 80.92, 80.72, 77.23, 84.53],
        "Config C": [89.47, 93.46, 91.99, 87.97, 93.14, 88.97, 93.81, 90.81, 93.82, 91.93],
    },
    "Model Y": {
        "Config A": [67.25, 65.01, 69.56, 66.44, 64.24, 66.06, 60.19, 63.02, 66.6, 62.9],
        "Config B": [71.18, 69.29, 66.35, 67.98, 70.7, 70.91, 70.74, 71.53, 71.52, 69.31],
        "Config C": [63.97, 58.68, 59.36, 63.92, 63.06, 62.04, 56., 64.19, 62.14, 64.99],
    },
    "Model Z": {
        "Config A": [71.49, 78.68, 71.62, 76.16, 71.24, 78.48, 78.07, 75.69, 74.07, 70.69],
        "Config B": [81.97, 79.54, 82.22, 83.66, 84.76, 83.56, 75.12, 78.6, 82.3, 76.72],
        "Config C": [70.21, 65.54, 67., 65.19, 72.94, 67.24, 68.45, 74.28, 72.04, 65.32],
    },
}

# Extracted variables
line_labels = [f"{config} - {model}" for model in models for config in configurations]
ylims = [(75, 95), (55, 75), (65, 85)]
yticks = [np.arange(75, 96, 2.5), np.arange(55, 76, 2.5), np.arange(65, 86, 2.5)]
titles = [f"Performance of {model}" for model in models]
xlabel = "Iteration"
ylabel = "Score"
xlim = (0, 9)
xticks = None  # Not explicitly set in the code
xtickslabel = None  # Not explicitly set in the code
ytickslabel = None  # Not explicitly set in the code
axhiline = None  # Not used in the code
axvline = None  # Not used in the code

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Prepare figure and axes
fig, axs = plt.subplots(3, 1, figsize=(8, 12), sharex=True)

# Color and marker setup
colors = ["red", "green", "blue"]
markers = ["o", "s", "^"]

# Plotting
for idx, (model, ylim, ytick, title) in enumerate(zip(models, ylims, yticks, titles)):
    ax = axs[idx]
    ax.set_ylim(ylim)
    ax.set_yticks(ytick)
    ax.set_title(title, y=1.1)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_xlim(xlim)
    ax.tick_params(axis="both", which="both", color="gray")
    for config, color, marker, line_label in zip(configurations, colors, markers, line_labels):
        scores = data[model][config]
        ax.plot(
            scores,
            marker=marker,
            color=color,
            clip_on=False,
            zorder=10,
            label=line_label,
            linestyle="-",
            markersize=8,
        )
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, 1.1), ncol=3, frameon=False)
    ax.grid(True)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig('line_76.pdf', bbox_inches='tight')
