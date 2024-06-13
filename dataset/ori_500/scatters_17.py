# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Simulating data for the left plot
x_main = np.random.normal(-10, 10, 100)
y_main = np.random.normal(10, 10, 100)
xlabel = "Δ Robust Accuracy (%)"
ylabel = "Δ RNFR (%)"
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create the main figure and axis
plt.figure(figsize=(9, 6))

# Scatter plot for the left plot
colors = np.random.rand(100)
sizes = 1000 * np.random.rand(100)
plt.scatter(x_main, y_main, c=colors, s=sizes, alpha=0.3, cmap="viridis")
plt.grid(True)

# Set labels and title for the plot
plt.xlabel(xlabel)
plt.ylabel(ylabel)

# ===================
# Part 4: Saving Output
# ===================
# Show the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig('scatters_17.pdf', bbox_inches='tight')
