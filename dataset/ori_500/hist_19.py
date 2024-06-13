# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Sample data with more random distribution
data1 = np.random.normal(0.05, 0.02, 10000)
data2 = np.random.normal(0.1, 0.03, 10000)
data3 = np.random.normal(0.08, 0.025, 10000)  # Additional data with more variance
data4 = np.random.normal(0.12, 0.03, 10000)  # Additional data with more variance
suptitle = "Defect Detection Data Distribution"
binslist = [100, 100]
titles = ["MNIST - Defect Detection", "FashionMNIST - Defect Detection"]
labels = ["Non-defective", "Defective"]
ranges = (0, 0.2)
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create figure and axes with specified figure size
fig, axs = plt.subplots(2, 1, figsize=(10, 7), gridspec_kw={"hspace": 0.5})

# Overall title (suptitle)
fig.suptitle(suptitle)

# First histogram (MNIST)
n, bins, patches = axs[0].hist(
    data1, bins=binslist[0], range=ranges, alpha=0.75, label=labels[0], color="#1f77b4"
)
axs[0].hist(data3, bins=bins, alpha=0.75, label=labels[1], color="#ff7f0e")
axs[0].set_title(titles[0])
axs[0].grid(True)  # Adding grid
axs[0].legend()  # Adding legend

# Second histogram (FashionMNIST)
axs[1].hist(
    data2,
    bins=binslist[1],
    range=(0, 0.3),
    alpha=0.75,
    label=labels[0],
    color="#2ca02c",
)
axs[1].hist(data4, bins=bins, alpha=0.75, label=labels[1], color="#d62728")
axs[1].set_title(titles[1])
axs[1].grid(True)  # Adding grid
axs[1].legend()  # Adding legend

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout
plt.tight_layout(
    rect=[0, 0.03, 1, 0.95]
)  # Adjust the layout to accommodate the overall title

plt.savefig("hist_19.pdf", bbox_inches="tight")
