# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Generate some example environmental data
categories = ["Light Industry", "Heavy Industry", "Transportation", "Residential"]

# Data for the graph: negative values for pollution emissions (in thousands of metric tons)
values1_A = [-np.random.uniform(300, 1000) for _ in categories]  # Current Year
values2_A = [-np.random.uniform(300, 1000) for _ in categories]  # Previous Year
labels = ["Current Year", "Previous Year"]
xlabel = "Industry Sectors"
ylabel = "Pollution Emissions (thousands of metric tons)"
title = "Environmental Impact by Sector"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Set up the figure size
fig, ax = plt.subplots(figsize=(10, 6))

# Make the bar plot with hatch patterns
ax.bar(
    categories,
    values1_A,
    color="skyblue",
    hatch="/",
    label="Current Year",
    edgecolor="black",
)
ax.bar(
    categories,
    values2_A,
    color="sandybrown",
    hatch="\\",
    label="Previous Year",
    bottom=values1_A,
    edgecolor="black",
)

# Labeling and customizing
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.title(title)
plt.legend()

# Adding grid lines for better readability
plt.grid(axis="y", linestyle="--", alpha=0.7)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and display
plt.tight_layout()

# Save the plot as a PDF file
plt.savefig("bar_76.pdf", bbox_inches="tight")
