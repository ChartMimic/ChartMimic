import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data (estimated from the image)
models = [
    "Tesla Model S",
    "Ford F-150",
    "Toyota Corolla",
    "Chevrolet Silverado",
    "Honda Civic",
    "BMW 3 Series",
    "Audi A4",
    "Mercedes-Benz C-Class",
    "Volkswagen Golf",
]
ground_truth_fuel_efficiency = [120, 95, 110, 80, 105, 85, 115, 90, 100]
estimated_fuel_efficiency = [115, 90, 105, 75, 100, 80, 110, 85, 95]
error = [5, 7, 5, 8, 5, 7, 5, 8, 5]
labels=["Ground-truth fuel efficiency", "Estimated fuel efficiency"]
ylabel="Fuel Efficiency (MPGe)"
ylim=[0, 130]
yticks=np.arange(0, 131, 10)



# ===================
# Part 3: Plot Configuration and Rendering
# ===================
fig = plt.subplots(figsize=(10, 3))
# Bar width
bar_width = 0.35

# X position of bars
r1 = np.arange(len(ground_truth_fuel_efficiency))
r2 = [x + bar_width for x in r1]

# Create bars
plt.bar(
    r1,
    ground_truth_fuel_efficiency,
    color="#d47e6d",
    width=bar_width,
    label=labels[0],
    yerr=error,
    capsize=7,
)
plt.bar(
    r2,
    estimated_fuel_efficiency,
    color="#76a4c5",
    width=bar_width,
    label=labels[1],
    yerr=error,
    capsize=7,
)

# Add xticks on the middle of the group bars
plt.xticks([r + bar_width / 2 for r in range(len(ground_truth_fuel_efficiency))], models)

# Create legend & Show graphic
plt.ylabel(ylabel)
plt.legend(frameon=False, loc="upper right")  # Remove legend background

# Set background color and grid
plt.gca().set_facecolor("#e5e5e5")
plt.grid(color="white", linestyle="-", linewidth=0.25, axis="both")
plt.gca().set_axisbelow(True)

# Set y-axis limits
plt.ylim(ylim)
plt.yticks(yticks)

for spine in plt.gca().spines.values():
    spine.set_visible(False)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig('errorbar_8.pdf', bbox_inches='tight')
