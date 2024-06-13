# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Sample data
ratios = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
pna_performance = np.array([0.6, 0.65, 0.7, 0.75, 0.8, 0.82, 0.85, 0.83, 0.82, 0.8])
gin_performance = np.array([0.5, 0.52, 0.55, 0.57, 0.6, 0.62, 0.63, 0.65, 0.64, 0.63])
pna_std = np.array([0.05] * 10)
gin_std = np.array([0.08] * 10)

# Axes Limits and Labels
xlabel_value = "Ratio r"
xlim_values = [0.05, 1.05]
xticks_values = np.arange(0.1, 1.05, 0.1)

ylabel_value = "Performance"
yticks_values_1 = np.arange(0.5, 0.82, 0.1)
ylim_values_1 = [0.42, 0.9]
yticks_values_2 = np.arange(0.4, 0.82, 0.1)
ylim_values_2 = 0.35, 0.9
yticks_values_3 = np.arange(0.4, 0.82, 0.1)
ylim_values_3 = [0.35, 0.9]

# Labels
labels = ["PNA + ours", "GIN + ours"]

# Titles
titles = ["SPMotif-0.5", "SPMotif-0.7", "SPMotif-0.9"]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plot settings
fig, axs = plt.subplots(1, 3, figsize=(15, 5))
colors = ["#9467bd", "#ff7f0e"]
markers = ["s", "s"]  # Square and circle markers

for i, ax in enumerate(axs):
    ax.plot(
        ratios, pna_performance, label=labels[0], color=colors[0], marker=markers[0]
    )
    ax.fill_between(
        ratios,
        pna_performance - pna_std,
        pna_performance + pna_std,
        color=colors[0],
        alpha=0.2,
    )
    ax.plot(
        ratios, gin_performance, label=labels[1], color=colors[1], marker=markers[1]
    )
    ax.fill_between(
        ratios,
        gin_performance - gin_std,
        gin_performance + gin_std,
        color=colors[1],
        alpha=0.2,
    )
    ax.set_xticks(xticks_values)
    ax.set_xlim(xlim_values)
    ax.set_title(titles[i])
    ax.set_xlabel(xlabel_value)
    ax.grid(True)

# Adjust subplot layout
plt.subplots_adjust(wspace=0.3)

axs[0].set_yticks(yticks_values_1)
axs[0].set_ylim(ylim_values_1)
axs[1].set_yticks(yticks_values_2)
axs[1].set_ylim(ylim_values_2)
axs[2].set_yticks(yticks_values_3)
axs[2].set_ylim(ylim_values_3)

# Move legend inside the plot area
axs[0].legend(loc="upper left")
axs[1].legend(loc="lower right")
axs[2].legend(loc="lower left")

# Adjust y-axis label to match reference picture
axs[0].set_ylabel(ylabel_value)
axs[1].set_ylabel(ylabel_value)
axs[2].set_ylabel(ylabel_value)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig('line_36.pdf', bbox_inches='tight')
