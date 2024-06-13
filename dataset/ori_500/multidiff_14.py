# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Sample data for the line plot
x = np.array([0, 10000, 20000, 30000, 40000, 50000])
y = np.array([-8, -8.5, -9, -9.2, -9.5, -10])
error = np.array([0.2, 0.3, 0.25, 0.3, 0.4, 0.35])

# Sample data for the box plot
data = [np.random.normal(7, 1, 100) for _ in range(5)]
positions = [0, 10000, 20000, 30000, 40000]
# Add scatter data points
scatters_data = np.random.normal(2, 0.5, len(positions))

titles=["(a) Token rarity", "(b) Length = 20"]
xlabels=["GPT2Tokenizer rank", "# of documents"]
ylabels=["Loss", "Loss"]
xtickslabels=[["0", "10k", "20k", "30k", "40k", "50k"], ["0", "10k", "20k", "30k", "40k"]]
yticks=[np.arange(-8, -11, -0.5), np.arange(0, 10, 2)]
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create figure and axes
fig, axs = plt.subplots(2, 1, figsize=(5, 6))

# Line plot
axs[0].errorbar(
    x,
    y,
    yerr=error,
    fmt="o-",
    ecolor="lightgray",
    markersize=8,
    linewidth=1,
    color="black",
)
axs[0].fill_between(x, y - error, y + error, color="lightgray", alpha=0.5)
axs[0].set_title(titles[0])
axs[0].set_xlabel(xlabels[0])
# axs[0].set_ylabel('Loss')
axs[0].grid(True)
axs[0].set_xticks(x)
axs[0].set_xticklabels(xtickslabels[0])
axs[0].set_yticks(yticks[0])

# Box plot
# set all linewidth to 1
axs[1].boxplot(
    data,
    positions=positions,
    widths=5000,
    showfliers=False,
    boxprops=dict(color="grey", linewidth=2),
    medianprops=dict(color="grey", linewidth=2),
    whiskerprops=dict(color="grey", linewidth=2),
    capprops=dict(color="grey", linewidth=2),
)
axs[1].set_title(titles[1])
axs[1].set_xlabel(xlabels[1])
axs[1].set_ylabel(ylabels[1])
axs[1].yaxis.grid(True)
axs[1].set_xticks(positions)
axs[1].set_xticklabels(xtickslabels[1])
axs[1].set_yticks(yticks[1])

axs[1].scatter(positions, scatters_data, marker="^", color="gray", s=100, zorder=3)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout
plt.tight_layout()

plt.savefig('multidiff_14.pdf', bbox_inches='tight')
