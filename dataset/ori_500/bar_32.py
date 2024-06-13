# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Data
categories = ["Shear Sheep", "Milk Cow", "Combat Spider"]
values = [0.56, 0.74, 0.72]

# Axes limits, labels, and ticks
xlabel = "Probability of Improvement"
xticks = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
xtickslabel = ["0.0", "", "0.2", "", "0.4", "", "0.6", "", "0.8", "", "1.0"]
title = "Probability of Improvement over VLM Image Encoder Baseline Returns"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create horizontal bar chart
plt.figure(figsize=(6, 2))  # Adjusting figure size to match original image dimensions
plt.barh(categories, values, color="#3b76af")

# Adding data labels
for index, value in enumerate(values):
    plt.text(value, index, f" {value}", va="center", color="black")

# Adding title and labels
plt.title(title)
plt.xlabel(xlabel)
# Apply the xticks and labels
plt.xticks(xticks, xtickslabel)

plt.tick_params(axis="both", which="both", length=0)

# ===================
# Part 4: Saving Output
# ===================
# Show plot with tight layout
plt.tight_layout()
plt.savefig("bar_32.pdf", bbox_inches="tight")
