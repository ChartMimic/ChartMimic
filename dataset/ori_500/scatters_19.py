# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data for the scatter plot
x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
y = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])
xlabel = "X-axis"
ylabel = "Y-axis"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
plt.figure(figsize=(6, 6))
plt.scatter(x, y, c=colors, cmap="viridis")
plt.grid(True)
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.colorbar()

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig('scatters_19.pdf', bbox_inches='tight')
