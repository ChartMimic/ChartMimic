# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)

import matplotlib.lines as mlines
import matplotlib.patches as mpatches


# ===================
# Part 2: Data Preparation
# ===================
# Define the vector field function
def vector_field(X, Y):
    # Placeholder function for the vector field
    # Replace with the actual function based on the provided image
    U = -Y
    V = X
    return U, V


def modified_vector_field(X, Y):
    # An example modification could be changing the vector magnitudes or directions as follows:
    U = -1 - X**2 + Y
    V = 1 + X - Y**2
    return U, V


# Create a grid of points
x = np.linspace(0, 0.6, 10)
y = np.linspace(0, 0.6, 10)
X, Y = np.meshgrid(x, y)

# Compute the vector field
U, V = vector_field(X, Y)

# Compute the modified vector field
U_mod, V_mod = modified_vector_field(X, Y)

# Plot the curves as inverse functions with slightly different denominators for variation
x = np.linspace(0.2, 0.5, 100)
xlabel = "X$_1$"
ylabel = "X$_2$"
patch_labels = ["True Field", "SINDy Learned Field"]
line_labels = ["Train Sample", "Test Sample", "SINDy Train", "SINDy Test"]
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
plt.figure(figsize=(8, 6))
plt.quiver(X, Y, U, V, color="#f15b50", alpha=0.6)
plt.quiver(X, Y, U_mod, V_mod, color="#6e5dc6", alpha=0.6)
plt.plot(x, 0.09 / (x**1.2), color="#3b75af")
plt.plot(x, 0.08 / (x**1.2 + 0.04), color="#ef8636")
plt.plot(x, 0.075 / (x**1 + 0.04), color="#519e3e")
plt.plot(x, 0.12 / (x**1 + 0.05), color="#000000")

# Add labels and legend
plt.xlabel(xlabel, fontsize=14, style="italic")
plt.ylabel(ylabel, fontsize=14, style="italic")

red_patch = mpatches.Patch(color="#f15b50", label=patch_labels[0], alpha=0.6)
blue_patch = mpatches.Patch(color="#6e5dc6", label=patch_labels[1], alpha=0.6)

# Create legend for curves
train_line = mlines.Line2D([], [], color="#3b75af", label=line_labels[0])
test_line = mlines.Line2D([], [], color="#ef8636", label=line_labels[1])
sindy_train_line = mlines.Line2D([], [], color="#519e3e", label=line_labels[2])
sindy_test_line = mlines.Line2D([], [], color="#000000", label=line_labels[3])

# Combine all legend handles
handles = [
    red_patch,
    blue_patch,
    train_line,
    test_line,
    sindy_train_line,
    sindy_test_line,
]

# Add the legend to the plot with specified location
plt.legend(handles=handles, loc="lower left")

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save the plot
plt.tight_layout()
plt.savefig('quiver_3.pdf', bbox_inches='tight')
