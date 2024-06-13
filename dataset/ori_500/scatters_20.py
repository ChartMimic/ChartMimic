# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data points
x = np.random.randint(100, size=(20))
y = np.random.randint(100, size=(20))
colors = np.random.randint(100, size=(20))
sizes = 10 * np.random.randint(100, size=(20))
title = "Scatter plot with colorbar"
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plotting the data points
plt.figure(figsize=(8, 6))
plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap="nipy_spectral")

plt.colorbar()
plt.title(title)

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig('scatters_20.pdf', bbox_inches='tight')
