# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
x = np.arange(1, 6)
categories = ["A", "B", "C", "D", "E", "F"]  # Expanded categories

# Generate cumulative data with non-linear trends for two runs each
y_data = {
    "Category A": [
        np.square(np.arange(1, 6)) * 2 + 20,
        np.square(np.arange(1, 6)) * 2 + 30,
    ],
    "Category B": [np.exp(np.arange(1, 6) * 0.5), np.exp(np.arange(1, 6) * 0.5) + 10],
    "Category C": [
        np.square(np.arange(1, 6) - 3) + 40,
        np.square(np.arange(1, 6) - 3) + 50,
    ],
    "Category D": [
        np.log(np.arange(1, 6) * 5) * 10 + 40,
        np.log(np.arange(1, 6) * 5) * 10 + 50,
    ],
    "Category E": [
        np.cos(np.arange(1, 6)) * 15 + 50,
        np.cos(np.arange(1, 6)) * 15 + 60,
    ],
    "Category F": [np.arange(1, 6) ** 1.5 * 10, np.arange(1, 6) ** 1.5 * 12],
}
# Axes Limits and Labels
xlabel_value = "Growth Phase"
xticklabels = ["Phase 1", "Phase 2", "Phase 3", "Phase 4", "Phase 5"]

ylabel_value = "Cumulative Value"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create figure and subplots
fig, axs = plt.subplots(2, 3, figsize=(9, 6), facecolor="beige")
axs = axs.flatten()  # Flatten the array to make indexing easier

# Enhanced color palette
colors = [
    ["#8034a0", "#20b2aa"],
    ["#dd5145", "#f08080"],
    ["#faa74b", "#8034a0"],
    ["#67a9cf", "#dd5145"],
    ["#20b2aa", "#67a9cf"],
    ["#f08080", "#faa74b"],
]
for i, category in enumerate(categories):
    for run in range(2):
        y = y_data[f"Category {category}"][run]
        axs[i].plot(
            x,
            y,
            "-o",
            label=f"Run {run+1}",
            color=colors[i][run],
            markersize=10,
            linewidth=3,
        )
    axs[i].set_xticks(x)
    axs[i].set_xticklabels(
        xticklabels, rotation=45
    )
    axs[i].set_title(f"Category {category} Growth", fontsize=14)
    axs[i].set_xlabel(xlabel_value, fontsize=10)
    axs[i].set_ylabel(ylabel_value, fontsize=10)
    axs[i].grid(True, linestyle="--", color="gray", alpha=0.5)
    axs[i].set_facecolor("lavenderblush")
    axs[i].legend(loc="upper left", fontsize=9)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig('line_80.pdf', bbox_inches='tight')
