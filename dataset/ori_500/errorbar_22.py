# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data for appliances in different categories
appliances = ["Refrigerator", "Washing Machine", "Dishwasher"]
efficiency_standard = [0.15, -0.10, 0.05]  # Standard model efficiency
efficiency_advanced = [0.25, -0.05, 0.15]  # Advanced model efficiency
efficiency_optimal = [0.30, 0.05, 0.20]  # Optimal model efficiency
error = [0.02, 0.03, 0.02]  # Error margins for the efficiency values

# Bar positions
x = np.arange(len(appliances))
width = 0.25  # width of the bars

labels = ["Standard Model", "Advanced Model", "Optimal Model"]
ylabel = "Energy Efficiency"
title = "Energy Efficiency Ratings by Appliance Model"
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plotting
fig, ax = plt.subplots(figsize=(8, 5))
bars1 = ax.bar(
    x - width,
    efficiency_standard,
    width,
    label=labels[0],
    color="lightcoral",
    yerr=error,
    capsize=5,
    hatch="//",
)
bars2 = ax.bar(
    x,
    efficiency_advanced,
    width,
    label=labels[1],
    color="lightgreen",
    yerr=error,
    capsize=5,
    hatch="\\",
)
bars3 = ax.bar(
    x + width,
    efficiency_optimal,
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
plt.savefig("errorbar_22.pdf", bbox_inches="tight")
