# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Sample data for the boxplots
data1 = [
    np.random.normal(22.7, 0.2, 100),
    np.random.normal(22.9, 0.15, 100),
    np.random.normal(23.1, 0.1, 100),
]
data2 = [
    np.random.normal(19.3, 0.2, 100),
    np.random.normal(19.5, 0.15, 100),
    np.random.normal(19.7, 0.1, 100),
]
titles = ["0.25 HIAR", "0.1 HIAR"]
ylabels = ["PSNR (dB)", "PSNR (dB)"]
xticklabels = ["Vanilla DIP", "SGLD DIP", "Ours"]
yticks = [np.arange(22.2, 23.5, 0.2), np.arange(19.0, 20.3, 0.2)]


# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create a figure with custom size to match the original image's dimensions
fig, axs = plt.subplots(1, 2, figsize=(10, 5))

# Create the boxplots
bp1 = axs[0].boxplot(data1, medianprops=dict(color="orange"))
bp2 = axs[1].boxplot(data2, medianprops=dict(color="orange"))

# Set titles for subplots
axs[0].set_title(titles[0])
axs[1].set_title(titles[1])

# Set y-axis labels
axs[0].set_ylabel(ylabels[0])
axs[1].set_ylabel(ylabels[1])

axs[0].set_yticks(yticks[0])
axs[1].set_yticks(yticks[1])

# Set x-axis labels
axs[0].set_xticklabels(xticklabels, rotation=45)
axs[1].set_xticklabels(xticklabels, rotation=45)

axs[0].grid("both")
axs[1].grid("both")

# Adjust layout to match the reference picture's dimensions and spacing
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1, wspace=0.4, hspace=0.4)

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig("box_9.pdf", bbox_inches="tight")
