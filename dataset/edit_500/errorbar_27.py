import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

# ===================
# Part 2: Data Preparation
# ===================
# Data for different service categories
categories = [
    "Cloud Cover",
    "Sunshine Hours",
    "Rainfall",
    "Snowfall",
    "UV Index",
    "Wind Gusts",
    "Storm Intensity",
]
weather_scores = [
    68,
    75,
    69,
    82,
    78,
    85,
    70,
]  # Scores for different weather conditions (0-100 scale)
extreme_event_rates = [
    -12,
    -14,
    -16,
    -10,
    -15,
    -8,
    -5,
]  # Negative values for extreme event rates

labels = ["Extreme Event Rates", "Weather Scores"]
textlabels = ["Increase rates", "Decrease rates"]

# Error data for each category
weather_errors = [4, 3, 5, 2, 3, 2, 2]
extreme_event_errors = [1, 2, 2, 1, 2, 1, 1]

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
    extreme_event_rates,
    color=complaint_colors,
    edgecolor="black",
    yerr=extreme_event_errors,
    label=labels[0],
    capsize=3,
)
ax.bar(
    categories,
    weather_scores,
    bottom=0,
    color=satisfaction_colors,
    edgecolor="black",
    yerr=weather_errors,
    label=labels[1],
    capsize=3,
)

# Adding labels within bars for values
for i, (com_val, sat_val) in enumerate(zip(extreme_event_rates, weather_scores)):
    ax.text(i, com_val / 2, f"{abs(com_val)}%", va="center", ha="center", color="gray")
    ax.text(i, sat_val / 2, f"{sat_val}%", va="center", ha="center", color="gray")

# Customizing axis and layout
ax.tick_params(axis="x", which="both", bottom=False)  # Remove x-axis tick marks
ax.set_ylim(min(extreme_event_rates) - 10, max(weather_scores) + 10)
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
plt.savefig('errorbar_27.pdf', bbox_inches='tight')
