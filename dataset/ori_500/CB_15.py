# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Data for pie chart
pie_labels = ["Incomparable", "Same", "Different"]
pie_sizes = [73.3, 23.7, 3.0]
pie_counts = [99, 32, 4]
pie_colors = ["#4CAF50", "#2196F3", "#FFC107"]

# Data for stacked bar chart
bar_labels = ["No trend for both", "No trend for German", "No trend for English"]
bar_sizes = [44.4, 44.4, 11.1]
bar_counts = [44, 44, 11]
bar_colors = ["#A5D6A7", "#66BB6A", "#388E3C"]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Pie chart
# Create figure and axes
fig, (ax1, ax2) = plt.subplots(
    1, 2, figsize=(8, 4), gridspec_kw={"width_ratios": [6, 1]}
)

ax1.pie(
    pie_sizes,
    labels=pie_labels,
    colors=pie_colors,
    autopct=lambda p: "{:.1f}%\n({})".format(p, int(round(p * sum(pie_counts) / 100))),
    startangle=140,
)
ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

# Stacked bar chart
bar_positions = [0]  # Single bar at position 0
bottom = 0  # Initial bottom is 0 for the first bar segment

for size, color, count, bar_label in zip(bar_sizes, bar_colors, bar_counts, bar_labels):
    ax2.bar(
        bar_positions,
        [size],
        color=color,
        edgecolor=None,
        bottom=[bottom],
        label=bar_label,
        width=0.1,
    )
    # Calculate the middle position for the text
    mid_pos = bottom + (size / 2)
    # Add text annotation inside the bar
    ax2.text(
        0,
        mid_pos,
        "{} {}%".format(bar_label.split(" ")[-1], size),
        color="black",
        ha="center",
        va="center",
    )
    bottom += size  # Update bottom for the next bar segment


ax2.set_axis_off()

# set the title
ax2.set_title("Incomparable")

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save plot
plt.tight_layout()
plt.savefig("CB_15.pdf", bbox_inches="tight")
