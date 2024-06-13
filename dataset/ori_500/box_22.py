# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
data = [
    np.random.normal(0.0, 0.05, 100),
    np.random.normal(0.005, 0.06, 100),
    np.random.normal(0.015, 0.03, 100),
    np.random.normal(0.03, 0.035, 100),
    np.random.normal(0.028, 0.05, 100),
]

labels = ["50", "100", "150", "200", "350"]

# Axes Limits and Labels
ylim_values = [-0.06, 0.06]
xlabel_value = "Search depth"
ylabel_value = "Reward"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create the boxplot
fig, ax = plt.subplots(
    figsize=(6, 5)
)  # Adjusting figure size as per the dimensions provided
bp = ax.boxplot(
    data,
    labels=labels,
    patch_artist=True,
    boxprops=dict(facecolor="#3171ad", color="black"),
    showfliers=False,
    showcaps=False,
    medianprops=dict(color="black"),
    whiskerprops=dict(color="black", linestyle="-", linewidth=0),
    capprops=dict(color="black", linestyle="-"),
)

ax.set_ylim(ylim_values)
# Set labels
ax.set_xlabel(xlabel_value)
ax.set_ylabel(ylabel_value)

# Set grid
ax.grid(True)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig("box_22.pdf", bbox_inches="tight")
