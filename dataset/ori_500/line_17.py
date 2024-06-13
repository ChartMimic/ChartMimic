# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data for plotting
parameters = np.array([10, 30, 50, 70, 90, 110])
kl_divergence = np.array([0.03, 0.04, 0.015, 0.006, 0.0025, 0.001])

# Axes Limits and Labels
xlabel_value = "Number of Parameters"
xlim_values = [0, 125]
xticks_values = np.arange(0, 121, 20)

ylabel_value = "Log KL Divergence"
ylim_values = [10**-5, 10**-1]
yticks_values = [10**-5, 10**-4, 10**-3, 10**-2, 10**-1]
yticklabels = ["$10^{-5}$", "$10^{-4}$", "$10^{-3}$", "$10^{-2}$", "$10^{-1}$"]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create the plot
fig, ax = plt.subplots(figsize=(6, 4))  # Use subplots to get access to the axis object
ax.plot(parameters, kl_divergence, marker="o", linestyle="-", color="#1f77b4")

# Set the scale of the y-axis to logarithmic
ax.set_yscale("log")

# Set y-axis to only display specific ticks and extend y-axis to leave space at top
ax.set_yticks(yticks_values)
ax.set_yticklabels(yticklabels)
ax.set_ylim(ylim_values)  # Set limits to include a small margin

# Remove minor ticks
ax.tick_params(axis="y", which="minor", left=False)

# Setting x-axis ticks
ax.set_xticks(xticks_values)  # Set x-ticks to be every 20
ax.set_xlim(xlim_values)  # Set limits to include a small margin

# Adjusting tick label size
plt.xticks(fontsize=10, fontweight="100")
plt.yticks(fontsize=10, fontweight="100")

# Remove tick lines outside the plotting area
ax.tick_params(
    axis="both", which="both", length=0, color="#d2d2d2"
)  # Remove tick marks and set their color

# Set labels and title
ax.set_xlabel(xlabel_value, fontsize=14)
ax.set_ylabel(ylabel_value, fontsize=14)

# Show grid with lighter color and only major lines
ax.grid(True, which="major", color="lightgrey", linestyle="-", linewidth=0.5)

# Change the axis colors
ax.spines["bottom"].set_color("#d2d2d2")
ax.spines["top"].set_color("#d2d2d2")  # Optional: hide or set color
ax.spines["left"].set_color("#d2d2d2")
ax.spines["right"].set_color("#d2d2d2")  # Optional: hide or set color

# ===================
# Part 4: Saving Output
# ===================
# Adjusting layout to add more space on the right
plt.tight_layout()
plt.savefig('line_17.pdf', bbox_inches='tight')
