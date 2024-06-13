# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data
models = ["Bactrian-X EN", "Lima-X DE", "Bactrian-X FR", "Lima-X IT", "Bactrian-X ES"]
improvements = {"EN": [3.5], "DE": [2.3], "FR": [4.4], "IT": [1.3], "ES": [-0.7]}

xlabel = "Model with Language"
ylabel = "Improvement [%]"
ylim = [-1.5, 5]
legendtitle = "Language"
title = "Model Performance Improvement by Language"

# Colors for each language
colors = ["#8171d7", "#af4b3d", "#d07035", "#d6a741", "#639b48"]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Bar width
bar_width = 0.75

# Positions of the bars on the x-axis
r = np.arange(len(models))

# Plotting the bars
for i, language in enumerate(improvements):
    bars = plt.bar(
        r[i],
        improvements[language],
        color=colors[i],
        width=bar_width,
        label=language,
        hatch="//",
        edgecolor="white",
    )
    # Add text labels
    for bar, val in zip(bars, improvements[language]):
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height + 0.1 if height > 0 else height - 0.4,
            f"{val:.1f}",
            ha="center",
        )

# Add xticks on the middle of the group bars
plt.xlabel(xlabel)
plt.xticks(r, models, rotation=45)

# Add ylabel
plt.ylabel(ylabel)
plt.ylim(ylim)

plt.gca().grid(color="gray", linewidth=0.5)
plt.gca().set_axisbelow(True)

# Create legend & Show graphic
plt.legend(title=legendtitle, loc="upper right")
plt.title(title)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig("bar_72.pdf", bbox_inches="tight")
