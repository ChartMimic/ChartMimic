# ===================
# Part 1: Importing Libraries
# ===================

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# ===================
# Part 2: Data Preparation
# ===================
# Data for plotting (approximated from the image)
names = ["AR", "LSTMAD-β", "LSTMAD-α", "AE", "FITS", "Donut"]
x = [10, 20, 30, 40, 50, 60]
y = [0.85, 0.8, 0.75, 0.7, 0.65, 0.6]
sizes = [300, 600, 900, 1200, 1500, 1800]
colors = ["purple", "blue", "green", "yellow", "orange", "red"]

# Plot and legend labels
scatter_label = "Bubble Size: Number of Anomalies Detected"

# Axis limits
xlim_values = None  # Not explicitly set in the code
ylim_values = (0.5, 0.9)

# Axis labels
xlabel_value = "Inference Time (seconds)"
ylabel_value = "Average Score"

# Axis ticks
xticks_values = x  # Set by FixedLocator
yticks_values = None  # Not explicitly set in the code

# Axis ticks labels
xtickslabel_values = None  # Not explicitly set in the code
ytickslabel_values = None  # Not explicitly set in the code

# Title
title_value = None  # Not explicitly set in the code

# Horizontal and vertical lines
axhline_values = None  # Not explicitly set in the code
axvline_values = None  # Not explicitly set in the code

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create a scatter plot
fig, ax = plt.subplots(figsize=(8, 6))
scatter = ax.scatter(x, y, s=sizes, c=colors, alpha=0.5, edgecolors="black", label=scatter_label)

# Add labels for each bubble
for i, txt in enumerate(names):
    ax.annotate(txt, (x[i], y[i]), ha="center", va="center", fontsize=8)

# Set the x-axis to a logarithmic scale
ax.set_xscale("log")
ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f"{int(x):d}"))
ax.xaxis.set_major_locator(ticker.FixedLocator(x))

# Set axis labels
ax.set_xlabel(xlabel_value, fontsize=10)
ax.set_ylabel(ylabel_value, fontsize=10)
ax.set_ylim(ylim_values)

# Add grid
ax.grid(True, which="both", linestyle="--", linewidth=0.5)

# Set background color to white
fig.patch.set_facecolor("white")
ax.set_facecolor("white")

# Add legend
ax.legend()

# ===================
# Part 4: Saving Output
# ===================
# Show the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig('scatters_11.pdf', bbox_inches='tight')
