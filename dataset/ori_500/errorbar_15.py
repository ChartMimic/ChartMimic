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
categories = ["Medium", "Medium-replay", "Medium-expert"]
methods = ["AUG", "TEstimation", "Qualification", "DiffStitch"]
performance = np.array([[60, 70, 80, 70], [80, 70, 75, 80], [70, 80, 75, 80]])
errors = np.array([[10, 10, 6, 6], [6, 10, 5, 4], [10, 4, 5, 4]])
ylim = [40, 90]
ylabel = "Performance"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Figure size 720x216 pixels
fig, axes = plt.subplots(1, 3, figsize=(10, 3))
# Colors
colors = ["#d66929", "#f7cc46", "blue", "darkblue"]

# Bar width
bar_width = 1

# Plotting bars
for i, ax in enumerate(axes):
    for j, method in enumerate(methods):
        ax.bar(
            j + bar_width * i,
            performance[i, j],
            width=bar_width,
            color=colors[j],
            yerr=errors[i, j],
            capsize=5,
            label=method if i == 0 else "",
        )

# Setting x-axis labels, y-axis limits, and titles
for i, ax in enumerate(axes):
    ax.set_xticks([])
    # ax.set_xticklabels(methods)
    ax.set_ylim(ylim)
    ax.set_xlabel(f"({chr(97+i)}) {categories[i]}")
    ax.set_ylabel(ylabel)
    ax.yaxis.grid(True)
    ax.set_axisbelow(True)

# Adding legend outside of the plot
fig.legend(loc="upper center", bbox_to_anchor=(0.5, 1.1), ncol=len(methods))

# ===================
# Part 4: Saving Output
# ===================
# Adjusting layout and saving the figure
plt.tight_layout()
plt.savefig("errorbar_15.pdf", bbox_inches="tight")
