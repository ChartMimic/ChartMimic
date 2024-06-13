# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Data
categories = ["Harvest Wheat", "Milk Cow", "Herd Goats"]
values = [41, 30, 27]  # Adjust the values to ensure realistic distribution

# Axes limits, labels, and ticks
xlabel = "Frequency of Success"
xticks = [0,5,10,15,20,25,30,35,40,45,50]
xtickslabel = ["0", "", "10", "", "20", "", "30", "", "40", "", "50"]
title = "Frequency of Success in Agricultural Tasks"

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
plt.savefig('bar_32.pdf', bbox_inches='tight')
