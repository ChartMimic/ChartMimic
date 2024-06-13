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
clusters = [100, 1000]
uniform = [49.98, 49.63]
clusterclip = [51.05, 50.74]
random_sampling = 48.9

labels = ["Uniform", "ClusterClip"]
xlabel = "Number of Clusters"
ylabel = "MMLU"
title = "MMLU by Number of Clusters"
axlabels = "Random Sampling"

ylim = [47, 53]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plotting
fig, ax = plt.subplots(
    figsize=(6.61, 5.23)
)  # Adjusted to match the original image's dimensions
bar_width = 0.35
index = np.arange(len(clusters))

bar1 = ax.bar(index, uniform, bar_width, label=labels[0], color="#5e74a0")
bar2 = ax.bar(
    index + bar_width, clusterclip, bar_width, label=labels[1], color="#c38c6a"
)

# Adding the text on the bars
for rect in bar1 + bar2:
    height = rect.get_height()
    ax.text(
        rect.get_x() + rect.get_width() / 2.0,
        height,
        "%.2f" % height,
        ha="center",
        va="bottom",
    )

# Random Sampling Line
ax.axhline(y=random_sampling, color="green", linestyle="--", label=axlabels)

# Labels, title and legend
ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)
# ax.set_title('MMLU by Number of Clusters')
ax.set_ylim(ylim)
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(clusters)
ax.legend(loc="upper right")  # Changed legend position
grid_color = "#d2d2d2"
ax.yaxis.grid(True)
ax.set_axisbelow(True)
# Set border color
for spine in ax.spines.values():
    spine.set_edgecolor(grid_color)

plt.tick_params(axis="both", which="both", length=0)

# ===================
# Part 4: Saving Output
# ===================
# Adjusting layout
plt.tight_layout()
plt.savefig("bar_36.pdf", bbox_inches="tight")
