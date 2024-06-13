# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Data for plotting
names = [
    "SeViLA",
    "LongViViT",
    "ShortViViT",
    "ImageViT",
    "Bard + ImageViT",
    "Bard + ShortViViT",
    "Bard + PALI",
    "MC-ViT-B",
    "MC-ViT-L",
]
x = [25, 30, 35, 30, 35, 40, 45, 40, 45]
y = [38, 40, 42, 44, 46, 48, 50, 55, 40]
sizes = [203, 424, 1000, 4000, 4000, 4000, 4000, 4000, 4000]
colors = ["blue", "blue", "blue", "blue", "blue", "blue", "blue", "red", "red"]
xlabel = "EgoSchema VQA accuracy"
ylabel = "Perception Test VQA accuracy"
legend_sizes = [203, 424, 1000, 4000, 5000]
legend_labels = ["203M", "424M", "1B", "4B", ">4B"]
legend_title = "Number of parameters"
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create figure and plot
fig, ax = plt.subplots(figsize=(8, 6))
scatter = ax.scatter(x, y, s=sizes, c=colors, alpha=0.3)

# Add annotations
for i, name in enumerate(names):
    ax.annotate(
        name,
        (x[i], y[i]),
        textcoords="offset points",
        xytext=(0, 0),
        ha="center",
        fontsize=8,
    )

# Customize the axes
ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)
ax.set_xlim(20, 50)
ax.set_ylim(35, 60)

# Add legend for bubble sizes
for size, label in zip(legend_sizes, legend_labels):
    ax.scatter([], [], c="grey", alpha=0.3, s=size, label=label)

# Adjust the legend to have increased spacing
ax.legend(
    scatterpoints=1,
    frameon=False,
    labelspacing=3,
    handletextpad=-2,
    columnspacing=8,
    title=legend_title,
    fontsize=8,
    loc="upper center",
    bbox_to_anchor=(0.5, 1.3),
    ncol=len(legend_sizes),
)

plt.grid(True)

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig('scatters_12.pdf', bbox_inches='tight')
