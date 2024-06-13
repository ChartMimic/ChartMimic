# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data for plotting, using random noise to add variability
N = np.array([10, 20, 30, 40, 50, 60])
standard = np.power(10, -np.linspace(10, 6, len(N)))
constrained = np.full_like(standard, 1e-12)

# New random data for variability
experimental = np.power(10, -np.random.uniform(1, 6, len(N)))
hypothetical = np.power(10, -np.linspace(1.5, 6.5, len(N)))

# Axes Limits and Labels
xlabel_value = "N"

ylabel_value = "Precision"

# Labels
label_Standard="Standard"
label_Constrained="Constrained"
label_Experimental="Experimental"
label_Hypothetical="Hypothetical"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Set the figure size
plt.figure(figsize=(10, 6))

# Plot the data using different styles and colors
plt.loglog(
    N,
    standard,
    "o-",
    color="#1f77b4",
    label=label_Standard,
    markerfacecolor="#1f77b4",
    markersize=8,
    linewidth=2,
)
plt.loglog(
    N,
    constrained,
    "x-",
    color="#ff7f0e",
    label=label_Constrained,
    markersize=8,
    linewidth=2,
)
plt.loglog(
    N,
    experimental,
    "s--",
    color="green",
    label=label_Experimental,
    markersize=8,
    linewidth=2,
)
plt.loglog(
    N,
    hypothetical,
    "^-",
    color="purple",
    label=label_Hypothetical,
    markersize=8,
    linewidth=2,
)

# Customize the x and y axes limits and labels
plt.xlabel(xlabel_value, fontsize=14)
plt.ylabel(ylabel_value, fontsize=14)
plt.xticks(N, labels=[str(n) for n in N])  # Ensuring x-ticks match the N values
plt.xlim(
    left=N[0] * 0.9, right=N[-1] * 1.1
)  # Set x-axis limits to prevent cutting off data points
plt.ylim(
    bottom=1e-14, top=1e-1
)  # Extend y-axis to leave some space above and below the data

# Adjust the legend position
plt.legend(bbox_to_anchor=(1, 0.5), fontsize=12, frameon=True)

# Add grid lines for better readability
plt.grid(True, which="both", ls="--", color="grey", linewidth=1, alpha=0.5)

# ===================
# Part 4: Saving Output
# ===================
# Adjust the layout and save the plot
plt.tight_layout()
plt.savefig('line_44.pdf', bbox_inches='tight')
