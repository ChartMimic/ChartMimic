# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import squarify

# ===================
# Part 2: Data Preparation
# ===================
# Data
sizes = [0.20, 0.10, 0.23, 0.27, 0.12, 0.08]
labels = [
    "Python\n20%",
    "Java\n10%",
    "C++\n23%",
    "Javascript\n27%",
    "C#\n12%",
    "Other\n8%",
]
colors = ["#6e5e75", "#926587", "#b86289", "#da777c", "#eaa38a", "#f1ccb4"]

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
    text_kwargs={"fontsize": 18, "color": "white"},
    pad=0.25,
)

# Remove axes
plt.axis("off")

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
# Show plot
plt.savefig('tree_2.pdf', bbox_inches='tight')
