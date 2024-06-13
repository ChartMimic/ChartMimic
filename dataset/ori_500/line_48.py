# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Generate new data for a complex scenario
months = np.arange(1, 13, 1)  # Months of the year
sales = np.random.normal(1055, 250, len(months))  # Simulate monthly sales
temperature = (
    5 * np.sin(0.5 * np.pi * months / 12) + 20
)  # Simulate average monthly temperature

# Axes Limits and Labels
xlabel_value = "Month"

ylabel_value_1 = "Sales"
ylabel_value_2 = "Temperature (°C)"

# Labels
label_1 = "Monthly Sales"
label_2 = "Average Temperature"

# Titles
title = "Sales and Temperature Correlation Over a Year"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create the main figure and axis
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot sales data with primary axis
color = "tab:blue"
ax1.set_xlabel(xlabel_value)
ax1.set_ylabel(ylabel_value_1, color=color)
ax1.plot(months, sales, label=label_1, color=color, marker="o", linestyle="-")
ax1.tick_params(axis="y", labelcolor=color)
ax1.set_xticks(months)
ax1.set_title(title)

# Create a second y-axis for temperature
ax2 = ax1.twinx()  # Instantiate a second axes that shares the same x-axis
color = "tab:red"
ax2.set_ylabel(
    ylabel_value_2, color=color
)  # We already handled the x-label with ax1
ax2.plot(
    months,
    temperature,
    label=label_2,
    color=color,
    marker="s",
    linestyle="--",
)
ax2.tick_params(axis="y", labelcolor=color)

# Add legends to the plot
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines + lines2, labels + labels2, loc="upper left", frameon=True)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout for better spacing and display
plt.tight_layout()

# Show the plot
plt.savefig('line_48.pdf', bbox_inches='tight')
