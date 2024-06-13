# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Data
# Categories and data for a new field: Customer Service Interactions
categories = [
    "Product Inquiry",
    "Order Issue",
    "Complaint",
    "Returns",
    "Technical Support",
    "Billing Question",
    "Feedback",
]
synthetic_data = [
    -9,
    -27,
    -20,
    -12,
    -18,
    -22,
    -15,
]  # Add negative sign to synthetic data
human_data = [18, 30, 14, 8, 20, 25, 12]
labels = ["synthetic data", "human-authored data"]


# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create figure and axis
fig, ax = plt.subplots(figsize=(6, 6))  # 432x432 pixels
colors_human = [
    "#75147c",
    "#685bc6",
    "#6e9d9f",
    "#4a895c",
    "#c3884c",
    "#c56f33",
    "#ec5528",
]
colors_synthetic = [
    "#d4a3da",
    "#7869e6",
    "#b6d7e4",
    "#72cecb",
    "#f9dcbd",
    "#e9a86c",
    "#ef865c",
]
# Plot horizontal bar chart
ax.barh(
    categories,
    synthetic_data,
    color=colors_synthetic,
    edgecolor="black",
    label=labels[0],
)
ax.barh(
    categories,
    human_data,
    left=0,
    color=colors_human,
    edgecolor="black",
    label=labels[1],
)  # Set left to 0 for human data

# Add data labels
for i, (syn_val, hum_val) in enumerate(zip(synthetic_data, human_data)):
    ax.text(
        syn_val, i, f"{abs(syn_val)}%", va="center", ha="right", color="black"
    )  # Use absolute value for synthetic data
    ax.text(hum_val, i, f"{hum_val}%", va="center", ha="left", color="black")

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
plt.savefig('bar_52.pdf', bbox_inches='tight')
