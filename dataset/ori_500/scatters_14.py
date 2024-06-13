# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Data for plotting
categories = [
    "spotlight",
    "sliding",
    "wool",
    "weasel",
    "space",
    "partridge",
    "mushroom",
    "bighorn",
]
majority_accuracy = [0.95, 0.70, 0.55, 0.50, 0.40, 0.40, 0.35, 0.30]
minority_accuracy = [0.10, 0.22, 0.35, 0.40, 0.50, 0.55, 0.60, 0.60]
xlabel = "Classes"
ylabel = "Accuracy"
labels = ["Majority", "Minority"]
title = "Accuracies for the ImageNet Classes (ClarifAI)"
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Set figure size to match the original image's dimensions
plt.figure(figsize=(6, 3))

# Plotting the data without error bars
plt.scatter(categories, majority_accuracy, color="blue", label=labels[0])
plt.scatter(categories, minority_accuracy, color="red", label=labels[1])

# Adding labels and title
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.title(title)

# Adding grid
plt.grid(True, linestyle="--", linewidth=0.5)

# Rotate x-axis labels for better readability
plt.xticks(rotation=90)
plt.ylim(0, 1.5)
# Adjusting legend placement to match the reference picture
plt.legend(loc="upper right")

# ===================
# Part 4: Saving Output
# ===================
# Show plot with tight layout to match the reference picture
plt.tight_layout()
plt.savefig('scatters_14.pdf', bbox_inches='tight')