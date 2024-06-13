import numpy as np; np.random.seed(0); np.random.seed(0)

import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Data
X, Y = np.meshgrid(np.linspace(-20, 10, 100), np.linspace(-20, 10, 100))
Z = 100 * np.sin(0.3 * X) * np.cos(0.3 * Y) + 40  # Simulated traffic density data

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Filled contour with labels
fig, ax = plt.subplots(figsize=(6, 6))
cnt = ax.contour(X, Y, Z, colors="k", linewidths=0.5)
ax.clabel(cnt, cnt.levels, inline=True, fontsize=10)
ax.contourf(X, Y, Z, cmap='coolwarm')

# Labels and title relevant to the transportation domain
ax.set_title("Traffic Density Over City Grid")
ax.set_xlabel("Kilometers (X-axis)")
ax.set_ylabel("Kilometers (Y-axis)")
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_xticks(np.arange(0, 11, 1))
ax.set_yticks(np.arange(0, 11, 1))

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig('contour_5.pdf', bbox_inches='tight')
