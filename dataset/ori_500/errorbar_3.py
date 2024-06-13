# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Sample data (replace with actual values)
groups = [
    "64 / 0.5 / 0.001",
    "64 / 0.5 / 0.0001",
    "64 / 0.3 / 0.001",
    "64 / 0.3 / 0.0001",
    "64 / 0.1 / 0.001",
    "64 / 0.1 / 0.0001",
    "256 / 0.5 / 0.001",
    "256 / 0.5 / 0.0001",
    "256 / 0.3 / 0.001",
    "256 / 0.3 / 0.0001",
    "256 / 0.1 / 0.001",
    "256 / 0.1 / 0.0001",
    "128 / 0.5 / 0.001",
    "128 / 0.5 / 0.0001",
    "128 / 0.3 / 0.001",
    "128 / 0.3 / 0.0001",
    "128 / 0.1 / 0.001",
    "128 / 0.1 / 0.0001",
]
solid_bar_values = np.random.rand(18)
striped_bar_values = np.random.rand(18)
error = np.random.rand(18) * 0.1

# Labels and Plot Types
label_Striped = "Striped"
label_Solid = "Solid"

# Axes Limits and Labels
xlabel_value = "Metric"
ylabel_value = "Hyperparameters"
title = "FashionMNIST (NEURAL)"
ylim_values = [-0.4, 17.4]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Set figure size to match the original image's dimensions
plt.figure(figsize=(10, 10))

# Create grouped bar chart with error bars
bar_width = 0.4
index = np.arange(len(groups))
plt.barh(
    index - 0.2,
    striped_bar_values,
    bar_width,
    color="#d8d7db",
    hatch="//",
    xerr=error,
    label=label_Striped,
    capsize=3,
    edgecolor="black",
    alpha=0.6,
)
plt.barh(
    index + 0.2,
    solid_bar_values,
    bar_width,
    color="#ebb08c",
    hatch="//",
    xerr=error,
    label=label_Solid,
    capsize=3,
    edgecolor="black",
    alpha=0.6,
)

# Add labels and title
plt.xlabel(xlabel_value)
plt.ylabel(ylabel_value)
plt.title(title)
plt.yticks(index, groups, rotation=0)
# plt.gca().set_xlim(0,)
plt.gca().set_ylim(ylim_values)

# ===================
# Part 4: Saving Output
# ===================
# Show plot
plt.tight_layout()
plt.savefig("errorbar_3.pdf", bbox_inches="tight")
