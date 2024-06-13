# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Generate random data for the bars representing average monthly sales
data = np.random.rand(3, 5) * 100  # Three regions, five products
products = ["Product A", "Product B", "Product C", "Product D", "Product E"]
suptitle = "Average Monthly Sales by Product Across Regions"
# Define colors for the bars (one for each region for clarity)
colors = ["#7CAE00", "#00BFC4", "#F8766D"]
ylim = [0, 100]
titles = [f"Region {i+1} Sales" for i in range(3)]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create a single figure with 1x3 subplots for each region
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

# Loop over each subplot and add bar charts for each region
for i, ax in enumerate(axs.ravel()):
    ax.bar(products, data[i], color=colors[i])
    ax.set_title(titles[i])
    ax.set_ylim(ylim)  # Set a common y-axis limit for comparability

    # Optionally, add a grid and customize further
    ax.grid(True, which="both", axis="y", linestyle="--", alpha=0.7)

# Add an overall title and labels
fig.suptitle(suptitle)
plt.setp(axs, xticks=np.arange(len(products)), xticklabels=products)

# ===================
# Part 4: Saving Output
# ===================
# Adjust the layout
fig.tight_layout(rect=[0, 0.03, 1, 0.95])  # Adjust top to accommodate suptitle

# Show and save the plot
plt.savefig("bar_100.pdf", bbox_inches="tight")
