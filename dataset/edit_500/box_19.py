import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Sample data for demonstration purposes
data1 = np.random.normal(10, 2, 20)
data2 = np.random.normal(15, 3, 20)
data3 = np.random.normal(12, 2.5, 20)

data = [data1, data2, data3]
ylabel = "Performance Score"
xticklabels = ["NeuralNet A", "NeuralNet B", "NeuralNet C"]
xticks = [1, 2, 3]
ylim = [0, 20]
categories = ["Image Classification", "Text Generation", "Speech Recognition"]
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Set figure size to match the original image's dimensions
plt.figure(figsize=(10, 4))

# Define colors for each boxplot
colors = ["#c0dbcd", "#edd1b9", "#d1d6e3"]

# Create subplots for each category
for i, category in enumerate(categories, 1):
    plt.subplot(1, 3, i)
    bplot = plt.boxplot(
        data,
        patch_artist=True,
        widths=0.7,
        medianprops=dict(color="black"),
        whiskerprops=dict(color="black"),
        capprops=dict(color="black"),
    )

    # Set colors for each box
    for patch, color in zip(bplot["boxes"], colors):
        patch.set_facecolor(color)

    # Scatter plot for data points
    for j in range(1, 4):
        y = data[j - 1]
        x = np.random.normal(j, 0.04, size=len(y))
        plt.plot(x, y, "k.", alpha=0.7)

    plt.title(category)
    plt.xticks(xticks, xticklabels)
    plt.ylim(ylim)
    if i == 1:
        plt.ylabel(ylabel)
    plt.gca().xaxis.grid(True)
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout to prevent overlap
plt.tight_layout()
plt.savefig('box_19.pdf', bbox_inches='tight')
