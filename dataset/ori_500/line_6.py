# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data for plotting
N = np.array([10, 20, 30, 40, 50, 60])
standard = np.array([0.1, 0.01, 0.001, 0.0001, 0.00001, 0.000001])
constrained = np.array([1e-12, 1e-12, 1e-12, 1e-12, 1e-12, 1e-12])

# Axes Limits and Labels
xlabel_value = "N"

ylim_values = [1e-14, 5e-1]
yticks_values = [10**-1, 10**-4, 10**-7, 10**-10, 10**-13]
yticks_labels = ["$10^{-1}$", "$10^{-4}$", "$10^{-7}$", "$10^{-10}$", "$10^{-13}$"]

# Labels
label_Standard = "Standard"
label_Constrained = "Constrained"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Set the figure size
plt.figure(figsize=(9, 6))

# Plot the data
plt.loglog(
    N,
    standard,
    "o-",
    color="#1f77b4",
    label=label_Standard,
    markerfacecolor="#1f77b4",
    markersize=4,
)  # Solid dots for Standard
plt.loglog(N, constrained, "x-", color="#ff7f0e", label=label_Constrained, markersize=6)

# Add labels with increased font size
plt.xlabel(xlabel_value, fontsize=14)

# Set y-axis to only display specific ticks and extend y-axis to leave space at top
plt.yticks(
    yticks_values,
    yticks_labels,
)
plt.ylim(ylim_values)  # Extend y-axis to leave some space above 10^-1

# Explicitly set the tick params for the x-axis
plt.tick_params(axis="x", labelsize=20)  # Ensure x-axis tick labels are of font size 14

# Add legend with transparent background
plt.legend(frameon=True, fontsize=16)

# Add a vertical line at x=10 and enable horizontal grid lines for structure
plt.axvline(x=10, color="grey", linestyle="--", linewidth=1)
plt.grid(
    True, which="both", ls="--", color="grey", linewidth=1, axis="y"
)  # Horizontal grid lines

# ===================
# Part 4: Saving Output
# ===================
# Adjust the layout and display the plot
plt.tight_layout()
plt.savefig('line_6.pdf', bbox_inches='tight')
