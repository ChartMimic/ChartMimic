# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

# ===================
# Part 2: Data Preparation
# ===================
# Data for different service categories
categories = [
    "Support",
    "Delivery",
    "Product Quality",
    "Returns",
    "Pricing",
    "Website Usability",
    "Checkout Process",
]
satisfaction_scores = [
    75,
    82,
    78,
    85,
    80,
    88,
    90,
]  # Percentage scores for customer satisfaction
complaint_rates = [
    -15,
    -18,
    -20,
    -12,
    -17,
    -10,
    -8,
]  # Negative values for complaint rates

# Error data for each category
satisfaction_errors = [5, 4, 6, 3, 4, 2, 3]
complaint_errors = [2, 3, 2, 1, 3, 1, 1]
labels = ["Complaint Rates", "Satisfaction Scores"]

# Define colors
satisfaction_colors = [
    "#8ea8c3",
    "#b5c0b7",
    "#a3acd1",
    "#d1c4e9",
    "#d7ccc8",
    "#cfd8dc",
    "#b2dfdb",
]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create figure and axis
fig, ax = plt.subplots(figsize=(8, 6))  # Adjusted size for clarity

complaint_colors = [
    mcolors.to_rgba(color, alpha=0.6) for color in satisfaction_colors
]  # Slightly lighter for complaints

# Plot horizontal bar charts with error bars
ax.barh(
    categories,
    complaint_rates,
    color=complaint_colors,
    edgecolor="black",
    xerr=complaint_errors,
    label=labels[0],
    capsize=3,
)
ax.barh(
    categories,
    satisfaction_scores,
    left=0,
    color=satisfaction_colors,
    edgecolor="black",
    xerr=satisfaction_errors,
    label=labels[1],
    capsize=3,
)

# Adding labels within bars for values
for i, (com_val, sat_val) in enumerate(zip(complaint_rates, satisfaction_scores)):
    ax.text(com_val / 2, i, f"{abs(com_val)}%", va="center", ha="center", color="gray")
    ax.text(sat_val / 2, i, f"{sat_val}%", va="center", ha="center", color="gray")

# Customizing axis and layout
ax.tick_params(axis="y", which="both", left=False)  # Remove y-axis tick marks
ax.set_xlim(min(complaint_rates) - 10, max(satisfaction_scores) + 10)
ax.set_xticks([])
ax.spines["left"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.axvline(0, color="black")  # Draw a vertical line at x=0 for separation

# Labels at the ends
ax.text(-15, 7, labels[0], ha="right", va="bottom")
ax.text(85, 7, labels[1], ha="left", va="bottom")

# Invert the y-axis for readability
ax.invert_yaxis()

# ===================
# Part 4: Saving Output
# ===================
# Show plot with tight layout
plt.tight_layout()
plt.savefig("errorbar_26.pdf", bbox_inches="tight")
