# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Sample linear data with added random noise for realism
ratios = np.linspace(0.1, 1.0, 10)
pna_performance = 0.8 - 0.5 * ratios + np.random.normal(0, 0.04, 10)
gin_performance = 0.2 + 0.55 * (1.05 - ratios) + np.random.normal(0, 0.09, 10)

# Error bars to indicate variance
pna_error = np.linspace(0.02, 0.05, 10)
gin_error = np.linspace(0.03, 0.05, 10)
# Axes Limits and Labels
xlabel_value = "Ratio r"
xticks_values = np.arange(0.0, 1.1, 0.2)

ylabel_value = "Performance"
ylim_values = [0.0, 1.0]

# Labels
label_1 = "PNA + ours"
label_2 = "GIN + ours"

# Titles
title ="Dynamic Model Performance"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create plot
fig, ax = plt.subplots(figsize=(10, 6))

# Set a soft background color using a simple approach
ax.set_facecolor("#f8f9fa")

# Plot settings with enhanced visual appeal
ax.errorbar(
    ratios,
    pna_performance,
    yerr=pna_error,
    fmt="-o",
    color="#007bff",
    label=label_1,
    markersize=8,
    capsize=5,
    linewidth=2,
    alpha=0.9,
)
ax.errorbar(
    ratios,
    gin_performance,
    yerr=gin_error,
    fmt="-X",
    color="#dc3545",
    label=label_2,
    markersize=8,
    capsize=5,
    linewidth=2,
    alpha=0.9,
)

# Styling the chart with a modern look
ax.grid(True, which="major", linestyle="--", linewidth=0.5, color="grey")
ax.set_xlabel(xlabel_value, fontsize=14)
ax.set_ylabel(ylabel_value, fontsize=14)
ax.set_title(title, fontsize=16, color="#343a40")

# Adjusting ticks and limits for optimal data display
ax.set_xticks(xticks_values)
ax.set_ylim(ylim_values)

# Configuring the legend to be more visually pleasing
ax.legend(frameon=True, loc="best", fontsize=12, framealpha=0.95, shadow=True)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig('line_74.pdf', bbox_inches='tight')
