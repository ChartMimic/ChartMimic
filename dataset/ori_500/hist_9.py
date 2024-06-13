# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Sample data (replace with your actual data)
data1 = np.random.normal(0.08, 0.01, 10000)
data2 = np.random.normal(0.1, 0.02, 10000)
binslist = [100, 100]
titles = ["MNIST", "FashionMNIST"]
rangelist = [(0, 0.12), (0, 0.25)]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create figure and axes with specified figure size
fig, axs = plt.subplots(2, 1, figsize=(10, 7), gridspec_kw={"hspace": 0.3})

# First histogram (MNIST)
axs[0].hist(data1, bins=binslist[0], range=rangelist[0], color="#3b75af")
axs[0].set_title(titles[0])

# Second histogram (FashionMNIST)
axs[1].hist(data2, bins=binslist[1], range=rangelist[1], color="#3b75af")
axs[1].set_title(titles[1])

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save plot
plt.tight_layout()
plt.savefig("hist_9.pdf", bbox_inches="tight")
