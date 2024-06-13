# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Updated data
n_aug = ["0", "0.125", "0.25", "0.5", "1", "2", "4", "8"]
content = np.array([2, 4, 6, 8, 6, 5, 3, 1])  # 更加动态的变化
organization = np.array([1, 2, 3, 4, 3.5, 2.5, 1.5, 0.7])  # 平滑的递增后递减
language = np.array([0.5, 1.5, 2.5, 3.5, 4.5, 3.5, 2.5, 1.5])  # 高峰在中间

# Axes Limits and Labels
xlabel_value = "n$_{aug}$"
xlim_values = [0, len(n_aug) - 1]

ylabel_value = "Performance Gain (%)"
ylim_values = [0, max(content) + 1]

# Labels
label_Content="Content"
label_Organization="Organization"
label_Language="Language"

# Titles
title = "Dynamic Performance Gain Across Different n$_{aug}$ Levels"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plot
fig, ax = plt.subplots(figsize=(8, 3))
ax.plot(
    n_aug, content, "o-", label=label_Content, color="royalblue", linewidth=2, markersize=8
)
ax.plot(
    n_aug,
    organization,
    "s--",
    label=label_Organization,
    color="crimson",
    linewidth=2,
    markersize=8,
)
ax.plot(
    n_aug,
    language,
    "^:",
    label=label_Language,
    color="limegreen",
    linewidth=2,
    markersize=8,
)

# Enhancements for visual appeal
ax.set_facecolor("#e6f0ff")  # Light blue background
ax.spines["top"].set_color("none")
ax.spines["right"].set_color("none")
ax.spines["left"].set_color("gray")
ax.spines["bottom"].set_color("gray")

# Setting axis limits and ticks dynamically based on data
ax.set_ylim(ylim_values)
ax.set_xlim(xlim_values)

# Customizing labels and grid
ax.set_xlabel(xlabel_value, fontsize=14)
ax.set_ylabel(ylabel_value, fontsize=14)
ax.set_title(title, fontsize=16)

# Custom legend
ax.legend(loc="upper right", fontsize=12, frameon=True, shadow=True)

# Grid
ax.grid(True, linestyle="--", alpha=0.5, color="grey")

# ===================
# Part 4: Saving Output
# ===================
# Tight layout for better spacing
plt.tight_layout()
plt.savefig('line_55.pdf', bbox_inches='tight')
