# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data
categories = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
values = [0.18, 0.15, 0.12, 0.09, 0.06, 0.03, -0.06, -0.03, -0.02, -0.03]
errors = [0.05, 0.04, 0.03, 0.03, 0.02, 0.02, 0.02, 0.02, 0.01, 0.01]
colors = [
    "#c0d5e6",
    "#709ec6",
    "#f2a965",
    "#c6e1c2",
    "#7fba74",
    "#eac0bf",
    "#d36e6c",
    "#7f7f7f",
    "#bcbd22",
    "#a88a83",
]

# Axes Limits and Labels
ylabel_value = "Posterior accuracy\n(Δ to no prompting)"
ylim_values = [-0.08, 0.22]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create figure and axis
fig, ax = plt.subplots(figsize=(8, 6))

# Bar chart
bars = ax.bar(
    categories, values, yerr=errors, color=colors, capsize=0, edgecolor="none"
)
ax.set_xticks([])
# Set labels
ax.set_ylabel(ylabel_value)

# Set x-axis limits and y-axis limits
ax.set_ylim(ylim_values)

# Remove top and right spines
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(True)
ax.spines["bottom"].set_visible(True)

# Remove grid lines
ax.yaxis.grid(False)
ax.xaxis.grid(False)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout to prevent clipping of ylabel
plt.tight_layout()
plt.savefig("errorbar_14.pdf", bbox_inches="tight")
