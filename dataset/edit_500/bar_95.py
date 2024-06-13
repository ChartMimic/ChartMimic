import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)

# ===================
# Part 2: Data Preparation
# ===================
# Data
models = ["XCalibur AI", "OmegaNet 2.0", "NeuroStream", "QuantumLeap AI", "Sentient Core"]
improvements = {"Healthcare": [4.5], "Finance": [1.2], "Education": [3.4], "Retail": [2.8], "Manufacturing": [0.7]}
improvements2 = {"Healthcare": [2.1], "Finance": [-0.5], "Education": [4.1], "Retail": [1.9], "Manufacturing": [-1.3]}
title = "AI Model Performance Improvement by Sector"
legendtitle = "Sector"
ylabel = "Improvement [%]"
ylims = [[-2, 5], [-5, 5]]
xlabel = "AI Model"
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
ax[1].set_ylim(ylims[1])
ax[0].set_ylim(ylims[0])
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
plt.savefig('bar_95.pdf', bbox_inches='tight')
