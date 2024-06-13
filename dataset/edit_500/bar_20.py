# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Data
categories = ["Electric Cars", "Hybrid Cars", "Diesel Trucks", "Electric Bikes", "Scooters"]
emissions_reduction = [85, 60, 20, 75, 50]
cost_savings = [50, 40, 15, 70, 45]
adoption_rate = [30, 40, 25, 35, 50]

# Bar chart
bar_width = 0.5
indices = range(len(categories))

labels = ["Emissions Reduction", "Cost Savings", "Adoption Rate"]



# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Figure size
fig, ax = plt.subplots(
    figsize=(8, 5)
)  # Adjusted to match the original image's dimensions



# Plotting bars with new colors
bars1 = ax.barh(indices, emissions_reduction, bar_width, label=labels[0], color="#1f77b4")
bars2 = ax.barh(indices, cost_savings, bar_width, left=emissions_reduction, label=labels[1], color="#8da0cb")
bars3 = ax.barh(
    indices,
    adoption_rate,
    bar_width,
    left=[i + j for i, j in zip(emissions_reduction, cost_savings)],
    label=labels[2],
    color="#c7c7c7",
)

# Adding text labels with new positions and font size
for i, bar in enumerate(bars1):
    ax.text(
        bar.get_width() / 2,
        bar.get_y() + bar.get_height() / 2,
        f"{emissions_reduction[i]}",
        ha="center",
        va="center",
        color="white",
        fontsize=14,
    )
for i, bar in enumerate(bars2):
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_y() + bar.get_height() / 2,
        f"{cost_savings[i]}",
        ha="center",
        va="center",
        color="black",
        fontsize=14,
    )
for i, bar in enumerate(bars3):
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_y() + bar.get_height() / 2,
        f"{adoption_rate[i]}",
        ha="center",
        va="center",
        color="black",
        fontsize=14,
    )

# Labels and title
ax.set_yticks(indices)
ax.set_yticklabels(categories, fontsize=14)
ax.invert_yaxis()  # Labels read top-to-bottom
ax.set_xticks([])

# Legend with new position
ax.legend(loc="upper left", bbox_to_anchor=(0.1, 1.15), ncol=3)

# ===================
# Part 4: Saving Output
# ===================
# Tight layout
plt.tight_layout()
plt.savefig('bar_20.pdf', bbox_inches='tight')
