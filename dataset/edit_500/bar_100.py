import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0); np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Generate random data for the bars representing average monthly sales
data = np.random.rand(3, 5) * 1000  # Three years, five types of crops
crops = ["Wheat", "Corn", "Rice", "Barley", "Soybeans"]
suptitle = "Average Annual Yield by Crop Over Three Years"
# Define colors for the bars (one for each year for clarity)
colors = ["#1f77b4", "#ff7f0e", "#2ca02c"]
ylim=[0,1000]
titles = ["Region 1 Sales", "Region 2 Sales", "Region 3 Sales"]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create a single figure with 1x3 subplots for each region
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

# Loop over each subplot and add bar charts for each region
for i, ax in enumerate(axs.ravel()):
    ax.bar(crops, data[i], color=colors[i])
    ax.set_title(titles[i])
    ax.set_ylim(ylim)  # Set a common y-axis limit for comparability

    # Optionally, add a grid and customize further
    ax.grid(True, which="both", axis="y", linestyle="--", alpha=0.7)

# Add an overall title and labels
fig.suptitle(suptitle)
plt.setp(axs, xticks=np.arange(len(crops)), xticklabels=crops)

# ===================
# Part 4: Saving Output
# ===================
# Adjust the layout
fig.tight_layout(rect=[0, 0.03, 1, 0.95])  # Adjust top to accommodate suptitle

# Show and save the plot
plt.savefig('bar_100.pdf', bbox_inches='tight')
