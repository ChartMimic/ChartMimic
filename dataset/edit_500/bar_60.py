# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Data for the plots
car_models = ["Sedan", "SUV", "Truck", "Hybrid", "Electric"]
fuel_efficiency_changes = [10.5, -5.2, -2.0, 12.3, 15.7]

# Axes Limits and Labels
ax_title = "Fuel Efficiency Improvements"
xticks_values = range(-20, 21, 5)
xlabel = "▲%"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Set the figure size to match the original image's dimensions
fig, ax = plt.subplots(figsize=(10, 8))

# Plot for Fuel Efficiency Improvements
bars = ax.barh(car_models, fuel_efficiency_changes, color="white", edgecolor="black", hatch="//")
for bar, value in zip(bars, fuel_efficiency_changes):
    if value < 0:
        bar.set_hatch("\\\\")
        bar.set_edgecolor("red")
ax.set_title(ax_title)
for i, v in enumerate(fuel_efficiency_changes):
    ax.text(
        v - 0.5 if v < 0 else v + 0.5,
        i,
        f"{v}%",
        color="black" if v > 0 else "red",
        va="center",
        ha="right" if v < 0 else "left",
    )
# Add a vertical line at x=0
ax.axvline(0, color="black")
ax.set_xticks(xticks_values)
# Remove y-axis tick marks
ax.tick_params(axis="y", which="both", left=False)

# Hide all axes except the bottom one
for spine in ["left", "right", "top"]:
    ax.spines[spine].set_visible(False)

# Add x-axis label
ax.set_xlabel(xlabel)

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig('bar_60.pdf', bbox_inches='tight')
