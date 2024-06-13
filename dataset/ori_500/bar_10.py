# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Data
categories = [
    "Which",
    "What",
    "How",
    "Will",
    "Are",
    "Is",
    "Choose",
    "Select",
    "Identify",
    "Fill",
]
values = [40, 30, 45, 50, 55, 50, 55, 55, 50, 45]

# Plot labels and titles
ylabel = "Accuracy (%)"
ylim = (0, 60)
yticks = [0, 10, 20, 30, 40, 50, 60]
xticks = categories  # Assuming xticks are the same as categories
xtickslabel_rotation = 0  # Assuming no rotation is needed

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create figure and axis
fig, ax = plt.subplots(figsize=(8, 6))  # Width, Height in inches

# Bar chart
ax.bar(categories, values, color="#7badd2")

# Set labels and title
ax.set_ylabel(ylabel)
ax.set_ylim(ylim)  # Set y-axis limit to match the picture
ax.set_yticks(yticks)
ax.tick_params(axis="both", which="both", length=0)
# Rotate x-axis labels
plt.xticks(ticks=xticks, rotation=xtickslabel_rotation)

# Hide the border
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig("bar_10.pdf", bbox_inches="tight")
