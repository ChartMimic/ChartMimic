import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
categories = ["Canada", "France", "China", "Australia", "South Korea"]

values = [0.75, 0.68, 0.55, 0.45, 0.60]
errors = [0.04, 0.03, 0.04, 0.05, 0.03]

categories2 = ["Canada", "France", "China", "Australia", "South Korea"]
values2 = [18, 17, 30, 22, 14]
errors2 = [1.2, 0.6, 1.8, 1.4, 0.7]

titles = ["Internet Penetration Rate", "Mobile Device Ownership Ratio"]
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
plt.savefig('errorbar_17.pdf', bbox_inches='tight')
