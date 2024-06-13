# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import squarify

# ===================
# Part 2: Data Preparation
# ===================
# Data
sizes = [50, 20, 15, 5, 5, 5]
labels = ["50%", "20%", "15%", "5%", "5%", "5%"]
colors = ["#FFA07A", "#20B2AA", "#87CEFA", "#778899", "#FFDAB9", "#C0C0C0"]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create a figure with the specified size
fig = plt.figure(figsize=(4, 6))

# Create a treemap
squarify.plot(
    sizes=sizes,
    label=labels,
    color=colors,
    alpha=0.7,
    text_kwargs={"fontsize": 15, "color": "black"},
    ec="black",
)

# Remove axes
plt.axis("off")

# ===================
# Part 4: Saving Output
# ===================
# Show plot with tight layout and save to file
plt.tight_layout()
plt.savefig('tree_4.pdf', bbox_inches='tight')
