# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Sample data to create contour lines similar to the picture
x = np.linspace(90, 160, 100)
y = np.linspace(50, 110, 100)
X, Y = np.meshgrid(x, y)
Z1 = np.exp(-((X - 125) ** 2 + (Y - 80) ** 2) / 100)
Z2 = np.exp(-((X - 135) ** 2 + (Y - 70) ** 2) / 100)
labels = ["Female", "Male"]
xlabel = "SBP (mmHg)"
ylabel = "DBP (mmHg)"
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create the plot
fig, ax = plt.subplots(figsize=(8, 8))

# Contour lines for Female (blue) and Male (red)
CS1 = ax.contour(X, Y, Z1, colors="blue", label=labels[0])
CS2 = ax.contour(X, Y, Z2, colors="red", label=labels[1])

# Labels for x and y axes
plt.xlabel(xlabel)
plt.ylabel(ylabel)

# Adding a legend manually
h1, _ = CS1.legend_elements()
h2, _ = CS2.legend_elements()
ax.legend([h1[0], h2[0]], labels)

# Set the aspect of the plot to match the original image
ax.set_aspect("auto")
ax.grid()
ax.set_facecolor("#e8e8e8")
ax.set_ylim(50, 100)
ax.set_xlim(100, 160)

# ===================
# Part 4: Saving Output
# ===================
# Show the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig("contour_3.pdf", bbox_inches="tight")
