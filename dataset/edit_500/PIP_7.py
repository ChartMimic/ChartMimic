import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Sample data to approximate the curves in the picture
x = np.linspace(0, 200, 200)
y1 = np.linspace(0.7, 1.2, 200) * (1 + np.random.normal(0, 0.05, 200))
y2 = np.linspace(0.8, 1.0, 200) * (1 + np.random.normal(0, 0.05, 200))

labels = ["Experimental", "Control"]
xlabel = "Iterations"
ylabel = "Performance Metric"
insetxlim = [100, 120]
insetylim = [0.75, 1.0]
insetxticks = [100, 110, 120]
insetyticks = [0.75, 0.85, 0.95]
insetaxes = [0.2, 0.6, 0.25, 0.25]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create the main figure and axis
fig, ax = plt.subplots(figsize=(6, 4))

# Plot the curves
ax.plot(x, y1, "#0072B2", label=labels[0])
ax.plot(x, y2, "#D55E00", label=labels[1])

# Set labels and title
ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)

# Create the inset with the zoomed-in view
ax_inset = fig.add_axes(
    insetaxes
)  # Adjust the position to align with the right side of the main plot
ax_inset.plot(x, y1, "#0072B2")
ax_inset.plot(x, y2, "#D55E00")
ax_inset.set_xlim(insetxlim)
ax_inset.set_ylim(insetylim)
ax_inset.set_xticks(insetxticks)
ax_inset.set_yticks(insetyticks)
ax_inset.spines["bottom"].set_color("black")  # Add black border to the inset
ax_inset.spines["left"].set_color("black")
ax_inset.spines["top"].set_color("black")
ax_inset.spines["right"].set_color("black")

# Add the legend to the main axis, outside the plot area
ax.legend(loc="lower left")

# ===================
# Part 4: Saving Output
# ===================
# Show the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig('PIP_7.pdf', bbox_inches='tight')
