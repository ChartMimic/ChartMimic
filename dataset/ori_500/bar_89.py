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
accuracies2 = [0.3, 0.5, 0.8, 0.6, 0.4, 0.65, 0.43, 0.69, 0.58, 1.0]
accuracies3 = [0.7, 0.6, 0.5, 0.7, 0.7, 0.64, 0.76, 0.56, 0.38, 1.0]
xlabel = "Top-10 superfamilies in training dataset"
ylabel1 = "Accuracy"
ylabel2 = "Recall"
ylabel3 = "Precision"
ylim = [0.0, 1.1]
yticks = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
yline = 0.6

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create the bar chart
fig, axes = plt.subplots(
    3, 1, figsize=(10, 6), sharex=True
)  # Adjusting figure size to match the original image's dimensions
axes[0].bar(superfamilies, accuracies, color="#7fa9cc")
axes[1].bar(superfamilies, accuracies2, color="#e39c90")
axes[2].bar(superfamilies, accuracies3, color="#af86ce")

# Add a horizontal line for the average accuracy
axes[0].axhline(y=yline, color="red", linestyle="--")

# Add labels and title
plt.xlabel(xlabel)
axes[0].set_ylabel(ylabel1)
axes[1].set_ylabel(ylabel2)
axes[2].set_ylabel(ylabel3)

# Set y-axis limits
plt.ylim(0.0, 1.1)
# Set x-axis, y-axis ticks
plt.xticks(superfamilies)
plt.yticks([0.0, 0.2, 0.4, 0.6, 0.8, 1.0])

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig("bar_89.pdf", bbox_inches="tight")
