import numpy as np; np.random.seed(0)

import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Seed for reproducibility

# Expanded categories with descriptive names
categories = [
    "Electric Vehicles",
    "Smartphones",
    "Laptops",
    "Smart Home Devices",
    "Wearables",
    "Tablets",
    "Gaming Consoles",
]

# Increased number of layers with descriptive names
layer_data = {
    f"Q1 {chr(65+i)} Sales": np.random.randint(10, 20, size=len(categories))
    for i in range(6)
}

title="Enhanced Stacked Bar Chart with Textures and Annotated Values"
xlabel="Product Categories"
ylabel="Sales Units"

# Color palette with diverse colors
colors = ["#ff4500", "#ff6347", "#ff8c00", "#ffd700", "#ffff00", "#ffffe0"]

# Hatch patterns to add texture to the bars
hatches = ["/", "\\", "|", "-", "+", "x"]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
fig, ax = plt.subplots(figsize=(10, 7))

bottoms = np.array([0] * len(categories))

for i, (layer, values) in enumerate(layer_data.items()):
    bars = ax.bar(
        categories,
        values,
        bottom=bottoms,
        color=colors[i],
        label=layer,
        hatch=hatches[i],
    )

    # Text styling for better readability
    for bar, bottom in zip(bars, bottoms):
        height = bar.get_height()
    # Update the bottoms for stacking
    bottoms += values

# Chart title and labels with enhanced styles
plt.title(title, fontsize=16)
plt.xlabel(xlabel, fontsize=12)
plt.ylabel(ylabel, fontsize=12)

# Adjust legend to be at the top outside the plot area
plt.legend(
    title=title,
    title_fontsize="13",
    fontsize="11",
    loc="upper center",
    bbox_to_anchor=(0.5, 1.25),
    ncol=3,
)

# Adding grid lines for better readability
ax.yaxis.grid(True, linestyle="--", which="major", color="grey", alpha=0.6)

# ===================
# Part 4: Saving Output
# ===================
# Show the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig('bar_69.pdf', bbox_inches='tight')
