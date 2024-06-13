import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Updated data
clusters = [50, 500]
personalized_ads = [82.5, 81.8]
contextual_ads = [79.2, 84.7]
random_sampling = 78.9

labels = ["Personalized Ads", "Contextual Ads"]
xlabel = "Number of Clusters"
ylabel = "Click-Through Rate (%)"
title = "Click-Through Rate by Number of Clusters"
axlabels = "Random Sampling"

ylim = [75, 88]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plotting
fig, ax = plt.subplots(
    figsize=(6.61, 5.23)
)  # Adjusted to match the original image's dimensions
bar_width = 0.35
index = np.arange(len(clusters))

bar1 = ax.bar(index, personalized_ads, bar_width, label=labels[0], color="#5e74a0")
bar2 = ax.bar(
    index + bar_width, contextual_ads, bar_width, label=labels[1], color="#c38c6a"
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
plt.savefig('bar_36.pdf', bbox_inches='tight')
