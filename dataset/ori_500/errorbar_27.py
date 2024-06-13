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

labels = ["Complaint Rates", "Satisfaction Scores"]
textlabels = ["Disagree rates", "agree rates"]

# Error data for each category
satisfaction_errors = [5, 4, 6, 3, 4, 2, 3]
complaint_errors = [2, 3, 2, 1, 3, 1, 1]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 6))  # Adjusted size for clarity

# Define colors
satisfaction_colors = [
    "#ffcccb",
    "#ffa07a",
    "#ff6347",
    "#ff4500",
    "#ff8c00",
    "#ffd700",
    "#ffebcd",
]
complaint_colors = [
    mcolors.to_rgba(color, alpha=0.6) for color in satisfaction_colors
]  # Slightly lighter for complaints

# Plot vertical bar charts with error bars
ax.bar(
    categories,
    complaint_rates,
    color=complaint_colors,
    edgecolor="black",
    yerr=complaint_errors,
    label=labels[0],
    capsize=3,
)
ax.bar(
    categories,
    satisfaction_scores,
    bottom=0,
    color=satisfaction_colors,
    edgecolor="black",
    yerr=satisfaction_errors,
    label=labels[1],
    capsize=3,
)

# Adding labels within bars for values
for i, (com_val, sat_val) in enumerate(zip(complaint_rates, satisfaction_scores)):
    ax.text(i, com_val / 2, f"{abs(com_val)}%", va="center", ha="center", color="gray")
    ax.text(i, sat_val / 2, f"{sat_val}%", va="center", ha="center", color="gray")

# Customizing axis and layout
ax.tick_params(axis="x", which="both", bottom=False)  # Remove x-axis tick marks
ax.set_ylim(min(complaint_rates) - 10, max(satisfaction_scores) + 10)
ax.set_yticks([])
ax.spines["left"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.axhline(0, color="black")  # Draw a horizontal line at y=0 for separation

# Labels at the ends
ax.text(-0.5, -25, textlabels[0], ha="right", va="bottom", rotation="vertical")
ax.text(-0.5, 25, textlabels[1], ha="right", va="bottom", rotation="vertical")

# ===================
# Part 4: Saving Output
# ===================
# Show plot
plt.tight_layout()
plt.savefig("errorbar_27.pdf", bbox_inches="tight")
