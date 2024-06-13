# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Sample data
x1 = np.array([0.7, 0.75, 0.8, 0.85, 0.9])
y1 = np.array([76, 78, 80, 79, 77])
e1 = np.array([3, 2, 4, 3, 3])

x2 = np.array([0.1, 0.2, 0.3, 0.4])
y2 = np.array([74, 78, 76, 72])
e2 = np.array([4, 2, 2, 2])

x3 = np.array([0.0, 0.2, 0.4, 0.6, 0.8, 1.0])
y3 = np.array([75, 78, 70, 65, 60, 55])
e3 = np.array([3, 2, 5, 4, 6, 5])

x4 = np.array([400, 600, 800, 1000, 1200])
y4 = np.array([80, 82, 77, 75, 72])
e4 = np.array([2, 3, 4, 3, 2])

# Titles
titles = [
    "(a) Positive bound",
    "(b) Negative bound",
    "(d) Contrastive loss weight",
    "(c) Fuzzy coefficient",
]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create 2x2 subplots
fig, axs = plt.subplots(2, 2, figsize=(9, 6))

# Flatten the axis array for easy iteration
axs = axs.flatten()

# Setting data for each subplot
data = [(x1, y1, e1), (x2, y2, e2), (x3, y3, e3), (x4, y4, e4)]

# Plot with error bars in each subplot
for ax, (x, y, e), title in zip(axs, data, titles):
    ax.errorbar(
        x, y, yerr=e, fmt="-o", color="blue", ecolor="red", capsize=5, markersize=6
    )
    ax.set_title(title, fontsize=16)
    ax.grid(True, alpha=0.5)
    ax.set_xticks(x)
    ax.set_yticks(np.linspace(min(y) - min(e), max(y) + max(e), num=5, endpoint=True))

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save the figure
plt.tight_layout()
plt.savefig('line_52.pdf', bbox_inches='tight')
