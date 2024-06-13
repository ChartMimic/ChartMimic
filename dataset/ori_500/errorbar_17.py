# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
categories = ["United States", "Germany", "India", "Brazil", "Japan"]

values = [0.88, 0.65, 0.25, 0.36, 0.62]
errors = [0.03, 0.02, 0.05, 0.04, 0.03]

categories2 = ["United States", "Germany", "India", "Brazil", "Japan"]
values2 = [16, 15, 35, 20, 12]
errors2 = [1, 0.5, 2, 1.5, 0.5]

titles = ["Higher Education Enrollment Rate", "Student-Teacher Ratio"]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
colors = plt.get_cmap("Set3")(np.linspace(0.2, 0.8, 5))
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6, 6))
ax1.barh(categories, values, xerr=errors, color=colors, capsize=3)
ax2.barh(categories2, values2, xerr=errors2, color=colors, capsize=3)

ax1.set_title(titles[0])
ax2.set_title(titles[1])

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig("errorbar_17.pdf", bbox_inches="tight")
