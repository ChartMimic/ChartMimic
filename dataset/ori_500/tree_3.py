# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import squarify

# ===================
# Part 2: Data Preparation
# ===================
# Data
sizes = [30.60, 13.42, 14.21, 10.91, 8.54, 6.26]
labels = [
    "Nike\n30.6%",
    "Adidas\n13.42%",
    "Puma\n14.21%",
    "Reebok\n10.91%",
    "Under Armour\n8.54%",
    "New Balance\n6.26%",
]
colors = ["#91DCEA", "#64CDCC", "#5FBB68", "#F9D23C", "#F9A729", "#FD6F30"]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create a figure with the specified size
fig = plt.figure(figsize=(12, 8))

# Create a treemap
squarify.plot(
    sizes=sizes,
    label=labels,
    color=colors,
    alpha=0.7,
    text_kwargs={"fontsize": 18},
    ec="black",
)

# Remove axes
plt.axis("off")

# ===================
# Part 4: Saving Output
# ===================
# Show plot with tight layout
plt.tight_layout()
plt.savefig('tree_3.pdf', bbox_inches='tight')
