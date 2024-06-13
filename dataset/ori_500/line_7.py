# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Sample data
x1 = np.array([0.7, 0.75, 0.8, 0.85, 0.9])
y1 = np.array([76, 78, 80, 79, 77])
e1 = np.array([3, 2, 4, 3, 3])

x2 = np.array([0.1, 0.2, 0.3, 0.4])
y2 = np.array([74, 78, 76, 72])
e2 = np.array([4, 2, 2, 2])

x3 = np.array([0.0, 0.2, 0.4, 0.6, 0.8, 1.0])
y3 = np.array([75, 78, 70, 65, 60, 55])
e3 = np.array([3, 2, 5, 4, 6, 5])

x4 = np.array([400, 600, 800, 1000, 1200])
y4 = np.array([80, 82, 77, 75, 72])
e4 = np.array([2, 3, 4, 3, 2])

# Axes Limits and Labels
xlim_values_1 = [0.685, 0.91]
xticks_values_1 = [0.70, 0.75, 0.80, 0.85, 0.90]
xlim_values_2 = [0.05, 0.43]
xticks_values_2 = np.arange(0.1, 0.5, 0.1)
xlim_values_3 = [-0.05, 1.05]
xticks_values_3 = np.arange(0.0, 1.1, 0.2)
xlim_values_4 = [300, 1250]
xticks_values_4 = np.arange(400, 1201, 200)

ylim_values_1 = [69, 85]
yticks_values_1 = range(70, 85, 2)
ylim_values_2 = [69, 81]
yticks_values_2 = range(70, 81, 2)
ylim_values_3 = [48, 81]
yticks_values_3 = range(50, 81, 5)
ylim_values_4 = [66.5, 86.0]
yticks_values_4 = np.arange(67.5, 85.1, 2.5)

# Labels
label_1 = "ImageNet-1k"
label_2 = "ImageNet-C/P (Fog)"

# Titles
title_1 = "(a) Positive bound."
title_2 = "(b) Negative bound."
title_3 = "(d) Contrastive loss weight."
title_4 = "(c) Fuzzy coefficient."

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create subplots
fig, axs = plt.subplots(1, 4, figsize=(12, 4))

# Global settings for all axes
for ax in axs:
    ax.tick_params(axis="both", which="major", labelsize=14)

# Set the specified x and y axis ranges for the first plot
axs[0].set_xlim(xlim_values_1)
axs[0].set_ylim(ylim_values_1)
axs[0].set_xticks(xticks_values_1)
axs[0].set_yticks(yticks_values_1)

# For the second plot
axs[1].set_xlim(xlim_values_2)
axs[1].set_ylim(ylim_values_2)
axs[1].set_xticks(xticks_values_2)
axs[1].set_yticks(yticks_values_2)

# For the third plot
axs[2].set_xlim(xlim_values_3)
axs[2].set_ylim(ylim_values_3)
axs[2].set_xticks(xticks_values_3)
axs[2].set_yticks(yticks_values_3)

# For the fourth plot
axs[3].set_xlim(xlim_values_4)
axs[3].set_ylim(ylim_values_4)
axs[3].set_xticks(xticks_values_4)
axs[3].set_yticks(yticks_values_4)

# Plot with error bands
axs[0].errorbar(
    x1, y1, yerr=e1, fmt="-o", color="blue", ecolor="#bdbdd7", capsize=5, markersize=4
)
axs[0].fill_between(x1, y1 - e1, y1 + e1, color="#0000ff", alpha=0.2)
axs[0].set_title(title_1, y=-0.18, fontsize=16)
axs[0].grid(True, alpha=0.5)

axs[1].errorbar(
    x2, y2, yerr=e2, fmt="-o", color="blue", ecolor="#bdbdd7", capsize=5, markersize=4
)
axs[1].fill_between(x2, y2 - e2, y2 + e2, color="#0000ff", alpha=0.2)
axs[1].set_title(title_2, y=-0.18, fontsize=16)
axs[1].grid(True, alpha=0.5)

axs[2].errorbar(
    x3, y3, yerr=e3, fmt="-o", color="blue", ecolor="#bdbdd7", capsize=5, markersize=4
)
axs[2].fill_between(x3, y3 - e3, y3 + e3, color="#0000ff", alpha=0.2)
axs[2].set_title(title_3, y=-0.18, fontsize=16)
axs[2].grid(True, alpha=0.5)

axs[3].errorbar(
    x4, y4, yerr=e4, fmt="-o", color="blue", ecolor="#bdbdd7", capsize=5, markersize=4
)
axs[3].fill_between(x4, y4 - e4, y4 + e4, color="#0000ff", alpha=0.2)
axs[3].set_title(title_4, y=-0.18, fontsize=16)
axs[3].grid(True, alpha=0.5)

# Adjust layout
plt.subplots_adjust(wspace=0.3)

# ===================
# Part 4: Saving Output
# ===================
# Adjusting layout to reduce white space
plt.tight_layout()
plt.savefig('line_7.pdf', bbox_inches='tight')
