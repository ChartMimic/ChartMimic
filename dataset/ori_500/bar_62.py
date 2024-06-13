# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

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
    -12,
    -35,
    -28,
    -15,
    -18,
    -14,
    -16,
]  # Add negative sign to synthetic data
human_data = [18, 32, 15, 8, 20, 22, 12]

labels = ["synthetic data", "human-authored data"]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create figure and axis
fig, ax = plt.subplots(figsize=(6, 6))  # 432x432 pixels

# Define base colors
base_colors = [
    "#1f77b4",
    "#ff7f0e",
    "#2ca02c",
    "#d62728",
    "#9467bd",
    "#8c564b",
    "#e377c2",
]

# Generate colors with different saturation
colors_human = base_colors
colors_synthetic = [
    mcolors.to_rgba(color, alpha=0.5) for color in base_colors
]  # Decrease saturation by changing alpha

# Plot horizontal bar chart
ax.barh(categories, synthetic_data, color=colors_synthetic, label=labels[0])
ax.barh(
    categories, human_data, left=0, color=colors_human, label=labels[1]
)  # Set left to 0 for human data

# Add data labels inside the bars
for i, (syn_val, hum_val) in enumerate(zip(synthetic_data, human_data)):
    ax.text(
        syn_val / 2, i, f"{abs(syn_val)}%", va="center", ha="center", color="white"
    )  # Use absolute value for synthetic data
    ax.text(hum_val / 2, i, f"{hum_val}%", va="center", ha="center", color="white")

# Remove y-axis tick marks
ax.tick_params(axis="y", which="both", left=False)

# Set x-axis limits
ax.set_xlim(
    min(synthetic_data) - 10, max(human_data) + 10
)  # Set x-axis limits to include negative values
ax.set_xticks([])
# Hide left and right spines
ax.spines["left"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["top"].set_visible(False)

# Draw a vertical line at x=0
ax.axvline(0, color="black")

# Add text to x=0
ax.text(-4, 7, labels[0], ha="right", va="bottom")
ax.text(4, 7, labels[1], ha="left", va="bottom")

# Invert y-axis
ax.invert_yaxis()

# ===================
# Part 4: Saving Output
# ===================
# Show plot with tight layout
plt.tight_layout()

# Save the figure
plt.savefig("bar_62.pdf", bbox_inches="tight")
