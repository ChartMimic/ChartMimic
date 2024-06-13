import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data for appliances in different categories
appliances = ["Smartphone", "Laptop", "Tablet"]
battery_life_standard = [8, -5, 7]  # Standard model battery life in hours
battery_life_advanced = [7, -4, 9]  # Advanced model battery life in hours
battery_life_optimal = [10, -2, 11]  # Optimal model battery life in hours
error = [0.5, 0.3, 0.4]  # Error margins for the battery life values

# Bar positions
x = np.arange(len(appliances))
width = 0.25  # Width of the bars

labels = ["Standard Model", "Advanced Model", "Optimal Model"]
ylabel = "Battery Life (Hours)"
title = "Battery Life Ratings by Device Model"
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plotting
fig, ax = plt.subplots(figsize=(8, 5))
bars1 = ax.bar(
    x - width,
    battery_life_standard,
    width,
    label=labels[0],
    color="lightcoral",
    yerr=error,
    capsize=5,
    hatch="//",
)
bars2 = ax.bar(
    x,
    battery_life_advanced,
    width,
    label=labels[1],
    color="lightgreen",
    yerr=error,
    capsize=5,
    hatch="\\",
)
bars3 = ax.bar(
    x + width,
    battery_life_optimal,
    width,
    label=labels[2],
    color="lightblue",
    yerr=error,
    capsize=5,
    hatch="--",
)

# Adding text for labels, title, and custom x-axis tick labels
ax.set_ylabel(ylabel)
ax.set_title(title)
ax.set_xticks(x)
ax.set_xticklabels(appliances)
ax.axhline(0, color="gray")
ax.legend()  # Adjust legend location as needed


# Adding data labels on the bars
def add_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(
            f"{height:.2f}",
            xy=(
                bar.get_x() + bar.get_width() / 2,
                (
                    height + error[bars.index(bar)]
                    if height > 0
                    else height - error[bars.index(bar)]
                ),
            ),
            xytext=(
                0,
                3 if height > 0 else -12,
            ),  # move text up or down based on bar direction
            textcoords="offset points",
            ha="center",
            va="bottom",
        )


add_labels(bars1)
add_labels(bars2)
add_labels(bars3)

# ===================
# Part 4: Saving Output
# ===================
# Show the plot
plt.tight_layout()
plt.savefig('errorbar_22.pdf', bbox_inches='tight')
