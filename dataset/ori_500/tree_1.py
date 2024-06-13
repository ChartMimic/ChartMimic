# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import squarify

# ===================
# Part 2: Data Preparation
# ===================
# Data
sizes = [30.60, 18.42, 14.21, 10.91, 8.54, 6.26, 6.15, 4.91]
labels = [
    "stackexchange.com\n30.6%",
    "physicsforums.com\n18.42%",
    "mathhelpforum.com\n14.21%",
    "mathoverflow.net\n10.91%",
    "proofwiki.org\n8.54%",
    "gmatclub.com\n6.26%",
    "mathhelpboards.com\n6.15%",
    "mathworks.com\n4.91%",
]
colors = [
    "#a1dab4",
    "#41b6c4",
    "#2c7fb8",
    "#253494",
    "#fed976",
    "#feb24c",
    "#fd8d3c",
    "#f03b20",
]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create a figure with the specified size
fig = plt.figure(figsize=(12, 8))

# Create a treemap
squarify.plot(
    sizes=sizes, label=labels, color=colors, alpha=0.7, text_kwargs={"fontsize": 18}
)

# Remove axes
plt.axis("off")

# ===================
# Part 4: Saving Output
# ===================
# Show plot with tight layout and save to file
plt.tight_layout()
plt.savefig('tree_1.pdf', bbox_inches='tight')
