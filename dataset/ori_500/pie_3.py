# ===================
# Part 1: Importing Libraries
# ===================

import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
labels = ["David", "John", "Marry", "Peter"]
sizes = [11, 29, 20, 40]
legend_labels = labels
legend_loc = "upper center"
legend_ncol = 4
legend_frameon = False
legend_bbox_to_anchor = (0.5, 1.05)

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
fig, ax = plt.subplots(figsize=(5, 5))
ax.pie(sizes, autopct="%1.1f%%", startangle=90)
plt.legend(
    legend_labels, loc=legend_loc, ncol=legend_ncol, frameon=legend_frameon, bbox_to_anchor=legend_bbox_to_anchor
)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig('pie_3.pdf', bbox_inches='tight')

