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
categories = [
    "greeting",
    "request",
    "criticism",
    "apology",
    "persuasion",
    "thanking",
    "leave-taking",
]
synthetic_data = [
    -8,
    -31,
    -24,
    -7,
    -10,
    -10,
    -10,
]  # Add negative sign to synthetic data
human_data = [16, 28, 11, 5, 15, 16, 9]
synthetic_data2 = [-9, -15, -12, -4, -7, -4, -8]  # Add negative sign to synthetic data
human_data2 = [14, 20, 16, 7, 12, 13, 10]
labels = ["synthetic data", "human-authored data"]
titles = ["Original", "New"]


# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create figure and axis
fig, axes = plt.subplots(1, 2, figsize=(10, 6), sharey=True)  # 432x432 pixels

colors_human = plt.get_cmap("Paired_r")(np.linspace(0.15, 0.85, len(categories)))

axes[0].barh(
    categories,
    synthetic_data,
    color=colors_human,
    edgecolor="black",
    label=labels[0],
)
axes[0].barh(
    categories,
    human_data,
    left=0,
    color=colors_human,
    edgecolor="black",
    label=labels[1],
    alpha=0.7,
)  # Set left to 0 for human data

# Plot horizontal bar chart
axes[1].barh(
    categories,
    synthetic_data2,
    color=colors_human,
    edgecolor="black",
    label=labels[0],
)
axes[1].barh(
    categories,
    human_data2,
    left=0,
    color=colors_human,
    edgecolor="black",
    label=labels[1],
    alpha=0.7,
)  # Set left to 0 for human data

# Add data labels
for i, (syn_val, hum_val) in enumerate(zip(synthetic_data, human_data)):
    axes[0].text(
        syn_val, i, f"{abs(syn_val)}%", va="center", ha="left", color="black"
    )  # Use absolute value for synthetic data
    axes[0].text(hum_val, i, f"{hum_val}%", va="center", ha="right", color="black")

# Remove y-axis tick marks
axes[0].tick_params(axis="y", which="both", left=False)

# Set x-axis limits
axes[0].set_xlim(
    min(synthetic_data) - 10, max(human_data) + 10
)  # Set x-axis limits to include negative values
axes[0].set_xticks([])
axes[1].set_xlim(
    min(synthetic_data2) - 10, max(human_data2) + 10
)  # Set x-axis limits to include negative values

# Draw a vertical line at x=0
axes[0].axvline(0, color="black")
axes[1].axvline(0, color="black")
axes[1].xaxis.grid(True, linestyle="--")

# Add text to x=0
axes[0].text(-4, 7, labels[0], ha="right", va="bottom")
axes[0].text(4, 7, labels[1], ha="left", va="bottom")

# Add text to x=0
axes[1].text(-4, 7, labels[0], ha="right", va="bottom")
axes[1].text(4, 7, labels[1], ha="left", va="bottom")

# Invert y-axis
axes[0].invert_yaxis()
axes[1].invert_yaxis()

# Add title
axes[0].set_title(titles[0], pad=30)
axes[1].set_title(titles[1], pad=30)

# ===================
# Part 4: Saving Output
# ===================
# Show plot
plt.tight_layout()
plt.savefig("bar_86.pdf", bbox_inches="tight")
