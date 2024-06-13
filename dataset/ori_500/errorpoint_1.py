# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Sample data (replace with actual data)
categories = [
    "Kashmir",
    "Religion",
    "Crime and Justice",
    "CAA",
    "Pulwama-Balakot",
    "Politics",
]
means = np.random.uniform(0.05, 0.15, len(categories))
std_devs = np.random.uniform(0.01, 0.05, len(categories))
dataset_mean = np.mean(means)

# Labels and Plot Types
label_Mean = "Mean"
label_Dataset_mean = "Dataset mean"

# Axes Limits and Labels
ylabel_value = "Shouting Fraction (Fraction of videos)"
ylim_values = [0.01, 0.18]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create figure and axis
fig, ax = plt.subplots(figsize=(8, 5))

# Error bar plot
ax.errorbar(
    categories,
    means,
    yerr=std_devs,
    fmt="o",
    color="blue",
    ecolor="blue",
    capsize=5,
    label=label_Mean,
)

# Dataset mean line
ax.axhline(y=dataset_mean, color="grey", linestyle="--", label=label_Dataset_mean)

# Customizing the plot
ax.set_ylabel(ylabel_value)
ax.set_xticklabels(categories, rotation=45, ha="right")
ax.legend()
ax.set_ylim(ylim_values)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout to prevent clipping of tick-labels
plt.tight_layout()
plt.savefig("errorpoint_1.pdf", bbox_inches="tight")
