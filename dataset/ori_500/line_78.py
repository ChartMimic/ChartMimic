# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)

from matplotlib.colors import LinearSegmentedColormap

# ===================
# Part 2: Data Preparation
# ===================
# Time series data: Quarterly sales growth for 6 brands over 2 years (8 quarters)
quarters = ["Q1", "Q2", "Q3", "Q4", "Q1_2", "Q2_2", "Q3_2", "Q4_2"]
sales_growth = {
    "Brand A": np.random.rand(8) + np.linspace(0.5, 2, 8),
    "Brand B": np.random.rand(8) + np.linspace(0.5, 2, 8),
    "Brand C": np.random.rand(8) + np.linspace(0.5, 2, 8),
    "Brand D": np.random.rand(8) + np.linspace(0.5, 2, 8),
    "Brand E": np.random.rand(8) + np.linspace(0.5, 2, 8),
    "Brand F": np.random.rand(8) + np.linspace(0.5, 2, 8),
}
# Axes Limits and Labels
xlabel_value = "Quarter"
ylabel_value = "Sales Growth"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Creating custom gradient color maps for each brand
colors = ["#ff5f6d", "#36d1dc", "#cc2b5e", "#11998e", "#aa076b", "#ffd89b"]

# Plot setup
fig, axs = plt.subplots(3, 2, figsize=(10, 10))  # 3x2 subplot grid
axs = axs.flatten()

# Markers and line styles for diversity
markers = ["o", "^", "s", "p", "*", "x"]
line_styles = ["-", "--", "-.", ":", "-", "--"]

# Plot each brand with its distinct color gradient and style
for ax, (brand, sales), color, marker, line_style in zip(
    axs, sales_growth.items(), colors, markers, line_styles
):
    points = ax.plot(
        quarters,
        sales,
        label=f"{brand} Sales Growth",
        marker=marker,
        linestyle=line_style,
        linewidth=2,
        color=color,
    )
    ax.plot(
        quarters, sales, marker=marker, linestyle=line_style, color=color, linewidth=2
    )
    ax.set_title(f"{brand}", fontsize=14)
    ax.set_xlabel(xlabel_value, fontsize=12)
    ax.set_ylabel(ylabel_value, fontsize=12)
    ax.set_facecolor("#f0f0f0")  # Light grey background for clarity
    ax.grid(True, linestyle="--", alpha=0.5)
    ax.legend(loc="upper left")

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig('line_78.pdf', bbox_inches='tight')
