# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Data for plotting
categories = [
    "Best-of-Three",
    "Initial Distribution",
    "0.125 Parameter-Valued\nDistribution",
    "Final Distribution with\nGPT-3.5-Turbo",
    "Final Distribution with\nGPT-4-Turbo",
]
values = [0.15, 0.35, 0.55, 0.65, 0.8]
errors = [0.05, 0.05, 0.05, 0.05, 0.05]
xlabel = "Objective Value"
title = "Mini Crosswords Performance"
label = "ToT (0.675)"
xvline = 0.675


# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plotting the bar chart
plt.figure(
    figsize=(10, 6)
)  # Adjusting figure size to match the original image's dimensions
plt.barh(categories, values, xerr=errors, color="skyblue", capsize=5)
plt.xlabel(xlabel)
plt.title(title)
plt.gca().tick_params(axis="both", length=0)  # Hide tick marks

# Adding the vertical line
plt.axvline(x=xvline, color="red", linestyle="--", label=label)
plt.gca().grid("both", color="gray", alpha=0.7)

# Adding the legend
plt.legend()

for spine in plt.gca().spines.values():
    spine.set_color("gray")

# ===================
# Part 4: Saving Output
# ===================
# Adjusting the layout and saving the figure
plt.tight_layout()
plt.savefig("errorbar_7.pdf", bbox_inches="tight")
