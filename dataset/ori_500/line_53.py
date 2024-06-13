# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Enhanced sample data to accommodate more subplots
x1 = np.array([0.7, 0.75, 0.8, 0.85, 0.9])
y1 = np.random.uniform(75, 85, size=len(x1))
e1 = np.random.uniform(1, 4, size=len(x1))

x2 = np.array([0.1, 0.2, 0.3, 0.4])
y2 = np.random.uniform(70, 80, size=len(x2))
e2 = np.random.uniform(1, 4, size=len(x2))

x3 = np.array([0.0, 0.2, 0.4, 0.6, 0.8, 1.0])
y3 = np.random.uniform(50, 80, size=len(x3))
e3 = np.random.uniform(1, 6, size=len(x3))

x4 = np.array([400, 600, 800, 1000, 1200])
y4 = np.random.uniform(65, 85, size=len(x4))
e4 = np.random.uniform(1, 4, size=len(x4))

x5 = np.array([0.5, 0.6, 0.7, 0.8, 0.9])
y5 = np.random.uniform(50, 80, size=len(x5))
e5 = np.random.uniform(1, 4, size=len(x5))

x6 = np.array([300, 500, 700, 900, 1100])
y6 = np.random.uniform(65, 85, size=len(x6))
e6 = np.random.uniform(1, 4, size=len(x6))

# Titles
titles = [
    "Positive Bound",
    "Negative Bound",
    "Contrastive Loss Weight",
    "Fuzzy Coefficient",
    "Additional Metric 1",
    "Additional Metric 2",
]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create 2x3 subplots for a unified visual presentation
fig, axs = plt.subplots(2, 3, figsize=(12, 8))

colors = ["red", "green", "blue", "purple", "magenta", "cyan"]

data_pairs = [
    (x1, y1, e1),
    (x2, y2, e2),
    (x3, y3, e3),
    (x4, y4, e4),
    (x5, y5, e5),
    (x6, y6, e6),
]

for ax, (x, y, e), title, color in zip(axs.flat, data_pairs, titles, colors):
    ax.errorbar(
        x, y, yerr=e, fmt="-o", color=color, ecolor="lightgray", capsize=5, label=title
    )
    ax.set_title(title)
    ax.set_xticks(x)
    ax.set_ylim(min(y) - min(e) - 0.1, max(y) + max(e) + 0.1)
    ax.legend(loc="upper left")

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout to ensure no overlap and labels are clearly visible
plt.tight_layout()
plt.savefig('line_53.pdf', bbox_inches='tight')
