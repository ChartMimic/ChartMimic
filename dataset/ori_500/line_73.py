# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)

from matplotlib.colors import LinearSegmentedColormap

# ===================
# Part 2: Data Preparation
# ===================
# Sample linear data
ratios = np.linspace(0.1, 1.0, 20)
pna_performance = 0.3 + 0.8 * ratios  # Simple linear increase
gin_performance = 0.3 + 0.4 * (1 - ratios)  # Corrected to show positive trend

# Error bars to indicate variance
pna_error = np.linspace(0.02, 0.1, 20)
gin_error = np.linspace(0.03, 0.12, 20)
# Axes Limits and Labels
xlabel_value = "Ratio r"
xlim_values = [5, 25]
xticks_values = np.arange(0.1, 1.1, 0.1)

ylabel_value = "Performance"
ylim_values = [0.05, 1.5]
yticks_values = np.arange(0.1, 1.55, 0.2)

# Labels
label_1 = "PNA + ours"
label_2 = "GIN + ours"

# Titles
title = "Modern Linear Performance Evaluation"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create plot
fig, ax = plt.subplots(figsize=(8, 6))

# Set a vibrant color scheme and background
ax.set_facecolor("#f4f4f9")  # A soft off-white background for a modern look
ax.grid(
    True, which="major", linestyle=":", linewidth="0.5", color="gray"
)  # Lighter grid for subtlety

cmap_pna = LinearSegmentedColormap.from_list("mycmap", ["#8a3ffc", "#d4bbff"])
cmap_gin = LinearSegmentedColormap.from_list("mycmap", ["#ff7f0e", "#fed8b1"])

ln_pna = ax.errorbar(
    ratios,
    pna_performance,
    yerr=pna_error,
    fmt="-o",
    color=cmap_pna(0.5),
    label=label_1,
    markersize=8,
    capsize=3,
    linewidth=2,
)
ln_gin = ax.errorbar(
    ratios,
    gin_performance,
    yerr=gin_error,
    fmt="-^",
    color=cmap_gin(0.5),
    label=label_2,
    markersize=8,
    capsize=3,
    linewidth=2,
)

# Adding labels and title with a modern font style
ax.set_xlabel(xlabel_value, fontsize=14, fontweight="regular")
ax.set_ylabel(ylabel_value, fontsize=14, fontweight="regular")
ax.set_title(title , fontsize=16, color="black")

# Customize ticks for clarity and aesthetic
ax.set_xticks(xticks_values)
ax.set_yticks(yticks_values)
ax.set_ylim(ylim_values)

# Enhance the legend with a contemporary look
ax.legend(frameon=True, loc="upper left", fontsize=12, framealpha=1, shadow=True)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig('line_73.pdf', bbox_inches='tight')
