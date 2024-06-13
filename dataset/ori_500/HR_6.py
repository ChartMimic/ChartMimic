# ===================
# Part 1: Importing Libraries
# ===================
import numpy as np

np.random.seed(0)

import matplotlib.pyplot as plt
from matplotlib.colors import Normalize

# ===================
# Part 2: Data Preparation
# ===================
# Generate sample data
alpha = np.linspace(0, 2, 15)
beta = np.linspace(0, 0.5, 15)
Alpha, Beta = np.meshgrid(alpha, beta)
gradient = (Alpha.max() - Alpha) / Alpha.max() + (Beta.max() - Beta) / Beta.max()
Z = 0.0015 - gradient * (0.0015 + 0.0015) / 2
new_Z = []
for line in Z:
    new_Z.append(line[::-1])
dashed_line = alpha * 0.25  # Adjusted function for dashed line
xlabel = r"$\alpha$"
ylabel = r"$\beta$"
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create a figure with specific dimensions
fig, ax = plt.subplots(figsize=(8, 7))

# Create a heatmap
norm = Normalize(vmin=np.min(Z), vmax=np.max(Z))
cmap = plt.get_cmap("bwr")
heatmap = ax.imshow(
    new_Z, aspect="auto", cmap=cmap, norm=norm, extent=[0, 2, 0, 0.5], origin="lower"
)

# Add a colorbar
cbar = plt.colorbar(heatmap, ax=ax, label="$\Delta t$")
cbar.ax.tick_params(labelsize=8)

# Add a dashed line (approximation)
ax.plot(alpha, dashed_line, "g--")

# Set labels and title
ax.set_xlabel(xlabel, fontsize=12)
ax.set_ylabel(ylabel, fontsize=12)

# ===================
# Part 4: Saving Output
# ===================
# Adjust the layout and display the plot
plt.tight_layout()
plt.savefig("HR_6.pdf", bbox_inches="tight")
