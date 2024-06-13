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
improvements2 = {"EN": [-1], "DE": [0.3], "FR": [3.4], "IT": [-3.3], "ES": [-2.7]}

title = "Model Performance Improvement by Language"
legendtitle = "Language"
ylabel = "Improvement [%]"
ylims = [[-2, 5], [-5, 5]]
xlabel = "Model with Language"

# Colors for each language
colors = ["#8171d7", "#af4b3d", "#d07035", "#d6a741", "#639b48"]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Figure and axis
fig, ax = plt.subplots(2, 1, figsize=(10, 6))

# Bar width
bar_width = 0.75

# Positions of the bars on the x-axis
r = np.arange(len(models))

# Plotting the bars
for i, language in enumerate(improvements):
    bars = ax[0].bar(
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
        ax[0].text(
            bar.get_x() + bar.get_width() / 2,
            height + 0.1 if height > 0 else height - 0.4,
            f"{val:.1f}",
            ha="center",
        )
for i, language in enumerate(improvements2):
    bars2 = ax[1].bar(
        r[i],
        improvements2[language],
        color=colors[i],
        width=bar_width,
        label=language,
        hatch="//",
        edgecolor="white",
    )
    # Add text labels
    for bar, val in zip(bars2, improvements2[language]):
        height = bar.get_height()
        ax[1].text(
            bar.get_x() + bar.get_width() / 2,
            height + 0.1 if height > 0 else height - 0.4,
            f"{val:.1f}",
            ha="center",
        )

ax[0].axhline(0, color="black")
ax[1].axhline(0, color="black")
# Add xticks on the middle of the group bars
plt.xticks(r, models, rotation=45)

# Add ylabel
plt.ylabel(ylabel)
ax[0].set_ylim(ylims[0])
ax[1].set_ylim(ylims[1])
plt.gca().grid(color="gray", linewidth=0.5)
plt.gca().set_axisbelow(True)

# Create legend & Show graphic
ax[0].legend(title=legendtitle, loc="upper right")
ax[0].set_title(title)
ax[1].set_xlabel(xlabel)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig("bar_95.pdf", bbox_inches="tight")
