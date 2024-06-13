# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Sample data
data = np.random.rand(10, 5) * 2 - 1  # Random data between -1 and 1
industries = [
    "Academia",
    "Agriculture",
    "Construction and Real Estate",
    "Corporate",
    "Entertainment",
    "Finance",
    "Government",
    "Hospitality",
    "Legal Services",
    "Life Sciences",
]
technologies = ["LLVA", "BakLLVA", "GeminiProVision", "GPT4V", "CODI"]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create the heatmap
fig, ax = plt.subplots(
    figsize=(6, 10)
)  # Adjusting figure size to match original image dimensions
cax = ax.matshow(data, cmap="coolwarm", vmin=-1, vmax=1)

# Set axis labels
ax.set_xticks(np.arange(len(technologies)))
ax.set_yticks(np.arange(len(industries)))
ax.set_xticklabels(technologies)  # Removed rotation and alignment
ax.set_yticklabels(industries)

# Rotate the tick labels and set their alignment
plt.setp(ax.get_xticklabels(), rotation=270, ha="center")

# Add colorbar
cbar = plt.colorbar(
    cax, aspect=10.5
)  # Adjusted shrink and aspect to match reference picture

# ===================
# Part 4: Saving Output
# ===================
# Show the plot
plt.tight_layout()
plt.savefig("heatmap_14.pdf", bbox_inches="tight")
