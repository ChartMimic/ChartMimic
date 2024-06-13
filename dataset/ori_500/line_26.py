# ===================
# Part 1: Importing Libraries
# ===================

import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)

from matplotlib.ticker import MultipleLocator

# ===================
# Part 2: Data Preparation
# ===================
# Data for plotting
vocab_sizes = ["256", "512", "1024", "2048", "4096", "8192", "16384"]
bpe_values = [0.4, 0.8, 0.9, 0.95, 0.95, 0.95, 0.95]
wordpunct_values = [0.3, 0.6, 0.8, 0.85, 0.9, 0.9, 0.9]
whitespace_values = [0.5, 0.65, 0.7, 0.75, 0.7, 0.65, 0.6]

# Variables for plot configuration
line_labels = ["BPE", "Wordpunct", "Whitespace"]
xlim_values = (0, len(vocab_sizes) - 1)
ylim_values = (0.2, 1.0)
xlabel_value = "Vocabulary Size"
ylabel_value = None
xticks_values = range(len(vocab_sizes))
yticks_values = np.arange(0.2, 1.1, 0.2)
xtickslabel_values = vocab_sizes
ytickslabel_values = None
title_value = "Test set TPR | FPR = $10^{-4}$"
axhline_value = None
axvline_value = None

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plotting the lines
plt.figure(figsize=(8, 6))
plt.plot(
    vocab_sizes,
    bpe_values,
    "o--",
    clip_on=False,
    zorder=10,
    color="#0c5da5",
    label=line_labels[0],
)
plt.plot(
    vocab_sizes,
    wordpunct_values,
    "o--",
    clip_on=False,
    zorder=10,
    color="#ff9500",
    label=line_labels[1],
)
plt.plot(
    vocab_sizes,
    whitespace_values,
    "o--",
    clip_on=False,
    zorder=10,
    color="#00b945",
    label=line_labels[2],
)

# Setting x and y ticks
plt.xticks(xticks_values, xtickslabel_values, fontsize=14)
plt.xlim(xlim_values)
plt.yticks(yticks_values, fontsize=14)

# Adding minor y-axis ticks with a step of 0.05
ax = plt.gca()
# ax.yaxis.set_minor_locator(MultipleLocator(0.05))

# Adjust tick parameters
ax.tick_params(axis="both", which="both", length=5, color="gray")  # Move ticks inside
ax.tick_params(
    axis="y", which="minor", length=2
)  # Ensure minor ticks are visible but smaller

# Title and labels
plt.title(title_value, fontsize=14)
plt.xlabel(xlabel_value, fontsize=14)

# Enable gridlines for minor ticks
plt.grid(True, color="#b0b0b0", which="major", linestyle="-", linewidth=0.5)

# Legend with serif font family
plt.legend(
    frameon=False, fontsize=12, loc="lower center", bbox_to_anchor=(0.5, -0.2), ncol=3
)

# ===================
# Part 4: Saving Output
# ===================
# Adjusting layout to add more space on the right
plt.tight_layout()

plt.savefig('line_26.pdf', bbox_inches='tight')

