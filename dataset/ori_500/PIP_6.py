# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Sample data to approximate the curves in the picture
x = np.linspace(0, 10000, 100)
y1 = 70000 - 30000 * np.exp(-x / 1000)
y2 = 69000 - 30000 * np.exp(-x / 1250)
y3 = 68000 - 30000 * np.exp(-x / 1500)
y4 = 65000 - 30000 * np.exp(-x / 2000)

# Labels and Plot Types
label_WI = "WI"
label_ISQ = "ISQ"
label_WIQL = "WIQL"
label_Greedy = "Greedy"

# Axes Limits and Labels
xlabel_value = "Time Steps"
ylabel_value = "Discounted cumulative reward"
zoomed_in_axes = [0.45, 0.2, 0.3, 0.3]
xlim_values = [9600, 10000]
ylim_values = [65000, 71000]
xticks_values = [9600, 9800, 10000]
yticks_values = [67000, 67000, 69000, 71000]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create the main figure and axis
fig, ax = plt.subplots(figsize=(8, 6))

# Plot the curves
ax.plot(x, y1, "r", label=label_WI)
ax.plot(x, y2, "g", label=label_ISQ)
ax.plot(x, y3, "m", label=label_WIQL)
ax.plot(x, y4, "b", label=label_Greedy)

# Set labels and title
ax.set_xlabel(xlabel_value)
ax.set_ylabel(ylabel_value)

# Create the inset with the zoomed-in view
ax_inset = fig.add_axes(
    zoomed_in_axes
)  # Adjust the position to align with the right side of the main plot
ax_inset.plot(x, y1, "r")
ax_inset.plot(x, y2, "g")
ax_inset.plot(x, y3, "m")
ax_inset.plot(x, y4, "b")
ax_inset.set_xlim(xlim_values)
ax_inset.set_ylim(ylim_values)
ax_inset.set_xticks(xticks_values)
ax_inset.set_yticks(yticks_values)
ax_inset.spines["bottom"].set_color("black")  # Add black border to the inset
ax_inset.spines["left"].set_color("black")
ax_inset.spines["top"].set_color("black")
ax_inset.spines["right"].set_color("black")

# Add the legend to the main axis, outside the plot area
ax.legend(loc="lower right")

# ===================
# Part 4: Saving Output
# ===================
# Show the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig('PIP_6.pdf', bbox_inches='tight')
