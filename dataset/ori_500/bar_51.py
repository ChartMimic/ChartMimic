# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Data
professions = [
    "Farmer",
    "Scooter mechanic",
    "Household management",
    "Construction/Renovation",
    "Gardening",
    "Making Bricks",
    "Carpenter",
    "Baker",
    "Crafting/knitting",
    "Cleaning / laundry",
]
number_of_videos = [2008, 2060, 2158, 2343, 2548, 2915, 3216, 3543, 4190, 5375]

# Axes Limits and Labels
xlabel_value = "Number of Videos"
title = "Number of Videos by Profession"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create horizontal bar chart
plt.figure(figsize=(12, 8))  # Adjust figure size to match original image's dimensions
plt.barh(professions, number_of_videos, color="#685bc6")  # Change bar color to purple
plt.xlabel(xlabel_value)
plt.title(title)

# Add data labels
for index, value in enumerate(number_of_videos):
    plt.text(
        value + 50, index, str(value), va="center", fontsize=10
    )  # Adjust text position and font size

plt.yticks(rotation=45)

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig("bar_51.pdf", bbox_inches="tight")
