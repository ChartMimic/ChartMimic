# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Sample data for the boxplots (actual data not provided in the question)
data = [
    [4.2, 4.5, 4.8, 4.9, 5.0],
    [4.0, 4.3, 4.6, 4.7, 4.8],
    [3.0, 3.5, 4.0, 4.5, 5.0],
    [3.2, 3.6, 4.1, 4.6, 5.1],
    [3.4, 3.8, 4.2, 4.7, 5.2],
]

# Category names for the x-axis
categories = [
    "AlphaBeta",
    "${z^+}$",
    "Gamma(γ = 0.05)",
    "Gamma(γ = 0.1)",
    "Gamma(γ = 0.25)",
]

# Axes Limits and Labels
xticks_values = range(1, len(categories) + 1)
ylim_values = [2, 6.5]
yticks_values = [2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0]
yticks_label = ["2.5", "3.0", "3.5", "4.0", "4.5", "5.0", "5.5", "6.0"]
ylabel_value = "${(↑)∆A^F}$"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create the boxplot
plt.figure(figsize=(8, 6))  # Size in inches (converted from provided dimensions)
plt.boxplot(data, medianprops=dict(color="orange"))

# Set the x-axis labels
plt.xticks(xticks_values, categories)
plt.ylim(ylim_values)
plt.yticks(
    yticks_values,
    yticks_label,
)
# Set the y-axis label
plt.ylabel(ylabel_value)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig("box_12.pdf", bbox_inches="tight")
