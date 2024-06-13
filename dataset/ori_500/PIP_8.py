# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Generate sample data for the three clusters with adjusted positions and spread
x1 = np.random.normal(-2, 1, 100)
y1 = np.random.normal(2, 1, 100)

x2 = np.random.normal(-2, 1, 100)
y2 = np.random.normal(-2, 1, 100)

x3 = np.random.normal(1, 1, 100)
y3 = np.random.normal(2, 1, 100)

labels=["Daytime Sunny", "Night Rainy", "PGST"]
insetxlim=[-1, 1]
insetylim=[-1, 1]
insetxticks=[-1.0, 0, 1.0]
insetyticks=[-1.0, 0, 1.0]
axesgrid=[0.65, 0.1, 0.2, 0.2]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Set the figure size to match the original image's dimensions
fig, ax = plt.subplots(figsize=(8, 8))

# Plot the data with adjusted colors
ax.scatter(x1, y1, c="orange", label=labels[0])
ax.scatter(x2, y2, c="blue", label=labels[1])
ax.scatter(x3, y3, c="green", label=labels[2])

# Add the legend with adjusted order of labels
ax.legend(labels, loc="upper right", frameon=True)

# Create the inset with the zoomed-in view
ax_inset = fig.add_axes(
    axesgrid
)  # Adjust the position to align with the right side of the main plot
ax_inset.scatter(x1, y1, c="orange", label=labels[0])
ax_inset.scatter(x2, y2, c="blue", label=labels[1])
ax_inset.scatter(x3, y3, c="green", label=labels[2])
ax_inset.set_xlim(insetxlim)
ax_inset.set_ylim(insetylim)
ax_inset.set_xticks(insetxticks)
ax_inset.set_yticks(insetyticks)
ax_inset.spines["bottom"].set_color("black")  # Add black border to the inset
ax_inset.spines["left"].set_color("black")
ax_inset.spines["top"].set_color("black")
ax_inset.spines["right"].set_color("black")

# ===================
# Part 4: Saving Output
# ===================
# Show the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig('PIP_8.pdf', bbox_inches='tight')
