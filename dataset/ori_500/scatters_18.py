# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Day one, the age and speed of 13 cars:
x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
y = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])

# Day two, the age and speed of 15 cars:
x2 = np.array([2, 2, 8, 1, 15, 8, 12, 9, 7, 3, 11, 4, 7, 14, 12])
y2 = np.array([100, 105, 84, 105, 90, 99, 90, 95, 94, 100, 79, 112, 91, 80, 85])

legend_labels = ["Day 1", "Day 2"]
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
plt.figure(figsize=(6, 6))
plt.scatter(x, y)
plt.scatter(x2, y2)
plt.grid(True)
plt.legend(legend_labels)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig('scatters_18.pdf', bbox_inches='tight')