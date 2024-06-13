# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Generate random data for illustration purposes
data1 = np.random.normal(5, 1, 1000)
data2 = np.random.normal(5, 1, 1000)
data3 = np.random.normal(5, 1, 1000)
data4 = np.random.normal(5, 1, 1000)

# Define the titles for each subplot
titles = [
    "MATHWELL",
    "MATHWELL MaC",
    "Llama-2",
    "Llama-2 MaC",
    "LLEMMMA",
    "LLEMMMA MaC",
    "MAmmoTH",
    "MAmmoTH MaC",
]

# Define the colors for each subplot
colors = ["blue", "blue", "red", "red", "purple", "purple", "orange", "orange"]
xlabel = "FKGL"
ylabel = "Density"
bins = 30
xvline = 5

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Set the figure size to match the original image's dimensions
plt.figure(figsize=(7, 8))  # Adjusted to match 720x864 dimensions

# Create subplots
for i in range(8):
    plt.subplot(4, 2, i + 1)
    if i % 2 == 0:
        data = data1 if i < 4 else data3
    else:
        data = data2 if i < 4 else data4
    plt.hist(data, bins=bins, density=True, alpha=0.6, color=colors[i], range=(0, 10))
    plt.title(titles[i])
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.axvline(
        x=xvline, color="k", linestyle="--", linewidth=1
    )  # Changed to dashed line

# ===================
# Part 4: Saving Output
# ===================
# Adjust the layout and show the plot
plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)  # Adjusted padding for tighter layout
plt.savefig("hist_12.pdf", bbox_inches="tight")
