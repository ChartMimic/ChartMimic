# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import squarify

# ===================
# Part 2: Data Preparation
# ===================
# Data
sizes = [25, 15, 20, 10, 12, 18]
labels = [
    "Asian\n25%",
    "European\n15%",
    "North American\n20%",
    "South American\n10%",
    "African\n12%",
    "Australian\n18%",
]
colors = ["#FFC0CB", "#FFD700", "#ADFF2F", "#7FFFD4", "#00BFFF", "#9370DB"]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create a figure with the specified size
fig = plt.figure(figsize=(6, 6))

# Create a treemap
squarify.plot(
    sizes=sizes,
    label=labels,
    color=colors,
    alpha=0.8,
    text_kwargs={"fontsize": 12, "color": "black"},
    pad=True,
    ec="black",
)

# Remove axes
plt.axis("off")

# ===================
# Part 4: Saving Output
# ===================
# Show plot with tight layout and save to file
plt.tight_layout()
plt.savefig('tree_5.pdf', bbox_inches='tight')
