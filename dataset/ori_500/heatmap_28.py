# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# New data
fruits = ["apples", "bananas", "cherries", "dates", "elderberries", "figs", "grapes"]
vendors = [
    "Vendor A",
    "Vendor B",
    "Vendor C",
    "Vendor D",
    "Vendor E",
    "Vendor F",
    "Vendor G",
]

sales = np.array(
    [
        [1.5, 2.2, 1.8, 3.2, 0.5, 3.8, 0.3],
        [2.8, 0.5, 3.6, 1.8, 2.2, 0.7, 0.6],
        [1.0, 2.1, 0.9, 4.0, 1.5, 4.2, 0.4],
        [0.7, 0.6, 0.4, 0.5, 3.4, 0.5, 0.6],
        [0.9, 1.6, 0.7, 2.3, 2.0, 5.9, 0.5],
        [1.2, 1.3, 0.5, 0.6, 0.7, 3.1, 4.8],
        [0.3, 1.9, 0.6, 1.3, 0.8, 1.8, 5.9],
    ]
)

title = "Sales of vendors (in tons/year)"
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
fig, ax = plt.subplots(figsize=(8, 6))

im = ax.imshow(sales, cmap="OrRd")

# Show all ticks and label them with the respective list entries
ax.set_xticks(np.arange(len(vendors)), labels=vendors)
ax.set_yticks(np.arange(len(fruits)), labels=fruits)

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

# Loop over data dimensions and create text annotations.
for i in range(len(fruits)):
    for j in range(len(vendors)):
        text = ax.text(j, i, sales[i, j], ha="center", va="center", color="black")

ax.set_title(title)

# ===================
# Part 4: Saving Output
# ===================
fig.tight_layout()
plt.savefig("heatmap_28.pdf", bbox_inches="tight")
