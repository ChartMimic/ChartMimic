import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Placeholder data for the boxplots
data1 = [np.random.normal(100, 15, 100), np.random.normal(90, 15, 100)]
data2 = [np.random.normal(75, 10, 100), np.random.normal(70, 10, 100)]
data3 = [np.random.normal(60, 8, 100), np.random.normal(65, 5, 100)]
data4 = [np.random.normal(55, 7, 100), np.random.normal(50, 7, 100)]
data5 = [np.random.normal(80, 12, 100), np.random.normal(75, 12, 100)]
titles = ["Math Test Scores", "Reading Test Scores", "Science Test Scores", "Art Test Scores", "Music Test Scores"]
xticklabels = ["Semester 1", "Semester 2"]
xticks = [1, 2]
xlabel = "Semester"
ylabels = "Score", "Score", "Score", "Score", "Score"
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create a figure with custom dimensions to match the original image
fig, axs = plt.subplots(1, 5, figsize=(10, 5))  # Adjusted for clarity

# Define colors for the boxplots
colors = ["#1f77b4", "#ff7f0e"]

# Plot the boxplots with the specified colors and outlier shapes
for i, data in enumerate([data1, data2, data3, data4, data5]):
    bplot = axs[i].boxplot(
        data,
        patch_artist=True,
        notch=False,
        widths=0.7,
        medianprops=dict(color="black"),
        flierprops=dict(
            marker="D", color="black", markerfacecolor="black", markersize=5
        ),
    )
    for patch, color in zip(bplot["boxes"], colors):
        patch.set_facecolor(color)

# Set the titles for each subplot
axs[0].set_title(titles[0])
axs[1].set_title(titles[1])
axs[2].set_title(titles[2])
axs[3].set_title(titles[3])
axs[4].set_title(titles[4])

# Set the x-axis labels with proper spacing
for ax in axs:
    ax.set_xticks(xticks)
    ax.set_xticklabels(xticklabels)
    ax.set_xlabel(xlabel)

# Set the y-axis labels
axs[0].set_ylabel(ylabels[0])
axs[1].set_ylabel(ylabels[1])
axs[2].set_ylabel(ylabels[2])
axs[3].set_ylabel(ylabels[3])
axs[4].set_ylabel(ylabels[4])

# ===================
# Part 4: Saving Output
# ===================
# Adjust the layout and save the figure
plt.tight_layout()
plt.savefig('box_20.pdf', bbox_inches='tight')
