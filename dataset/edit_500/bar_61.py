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
categories = [
    "Gene Expression",
    "Protein Levels",
    "Cell Count",
    "Mutation Rate",
]
gene_expression = [750, 1200, 980, 870]  # Example data in arbitrary units
protein_levels = [620, 1100, 900, 780]  # Example data in arbitrary units
cell_count = [2000, 1800, 1300, 950]  # Example data in millions of cells
labels = ["Gene Expression (AU)", "Protein Levels (AU)", "Cell Count (Millions)"]
xticks = np.arange(0, 4500, 500)

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Stacked Bar Chart
fig, ax = plt.subplots(figsize=(8, 5))
bar_width = 0.5
y_pos = range(len(categories))

ax.barh(
    y_pos,
    gene_expression,
    bar_width,
    color="#d66555",
    edgecolor="#2a3b4d",
    hatch="*",
    label=labels[0]
)
ax.barh(
    y_pos,
    protein_levels,
    bar_width,
    left=gene_expression,
    color="#88a27d",
    edgecolor="#2a3b4d",
    hatch="+",
    label=labels[1]
)
ax.barh(
    y_pos,
    cell_count,
    bar_width,
    left=[i + j for i, j in zip(gene_expression, protein_levels)],
    color="#a1b5ce",
    edgecolor="#2a3b4d",
    hatch="/",
    label=labels[2],
)

# Labels and Legend
ax.set_xticks(xticks)
ax.set_yticks(y_pos)
ax.grid(axis="x", color="gray", linestyle="--")
ax.set_axisbelow(True)
ax.set_yticklabels(categories)
ax.legend(loc="upper center", bbox_to_anchor=(0.5, 1.2), ncols=3)

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig("bar_61.pdf", bbox_inches="tight")