# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Data for the bar chart
superfamilies = range(1, 11)
accuracies = [0.9, 0.83, 0.86, 0.84, 0.7, 0.85, 0.93, 0.89, 0.88, 1.0]
xlabel = "Top-10 superfamilies in training dataset"
ylabel = "Accuracy"
ylim = (0.0, 1.1)
yticks = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create the bar chart
plt.figure(
    figsize=(10, 6)
)  # Adjusting figure size to match the original image's dimensions
plt.bar(superfamilies, accuracies, color="#7fa9cc")

# Add a horizontal line for the average accuracy
average_accuracy = sum(accuracies) / len(accuracies)
plt.axhline(y=average_accuracy, color="red", linestyle="--")

# Add labels and title
plt.xlabel(xlabel)
plt.ylabel(ylabel)

# Set y-axis limits
plt.ylim(ylim)
# Set x-axis,y-axis ticks
plt.xticks(superfamilies)
plt.yticks(yticks)

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig("bar_8.pdf", bbox_inches="tight")
