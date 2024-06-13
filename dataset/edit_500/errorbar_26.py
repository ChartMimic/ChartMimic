import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

# ===================
# Part 2: Data Preparation
# ===================
# Data for different service categories
categories = [
    "Precipitation",
    "Temperature",
    "Humidity",
    "Wind Speed",
    "Visibility",
    "Pressure",
    "Air Quality",
]
weather_indexes = [
    35,
    42,
    58,
    65,
    40,
    38,
    50,
]  # Weather index scores (0-100 scale)
variance_rates = [
    -10,
    -12,
    -15,
    -8,
    -14,
    -7,
    -5,
]  # Negative values for variance rates

# Error data for each category
index_errors = [4, 3, 5, 2, 3, 2, 2]
variance_errors = [1, 2, 2, 1, 2, 1, 1]
labels=["Variance Rates", "Weather Index Scores"]
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
    variance_rates,
    color=complaint_colors,
    edgecolor="black",
    xerr=variance_errors,
    label=labels[0],
    capsize=3,
)
ax.barh(
    categories,
    weather_indexes,
    left=0,
    color=satisfaction_colors,
    edgecolor="black",
    xerr=index_errors,
    label=labels[1],
    capsize=3,
)

# Adding labels within bars for values
for i, (com_val, sat_val) in enumerate(zip(variance_rates, weather_indexes)):
    ax.text(com_val / 2, i, f"{abs(com_val)}%", va="center", ha="center", color="gray")
    ax.text(sat_val / 2, i, f"{sat_val}%", va="center", ha="center", color="gray")

# Customizing axis and layout
ax.tick_params(axis="y", which="both", left=False)  # Remove y-axis tick marks
ax.set_xlim(min(variance_rates) - 10, max(weather_indexes) + 10)
ax.set_xticks([])
ax.spines["left"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.axvline(0, color="black")  # Draw a vertical line at x=0 for separation

# Labels at the ends
ax.text(-15, 7, labels[0], ha="right", va="bottom")
ax.text(55, 7, labels[1], ha="left", va="bottom")

# Invert the y-axis for readability
ax.invert_yaxis()

# ===================
# Part 4: Saving Output
# ===================
# Show plot with tight layout
plt.tight_layout()
plt.savefig('errorbar_26.pdf', bbox_inches='tight')
