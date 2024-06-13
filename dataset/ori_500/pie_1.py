# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Data to plot
sizes = [30.5, 29.8, 13.2, 11.3, 10.6, 4.6]
colors = ["#29b2aa", "#63b5fc", "#e6e6f9", "#ffd638", "#766be9", "#c0c0c0"]
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1)  # add explode parameter to separate slices

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plot
fig, ax = plt.subplots(figsize=(5, 5))
ax.pie(
    sizes,
    colors=colors,
    autopct="%1.1f%%",
    startangle=140,
    wedgeprops=dict(edgecolor="w"),
    explode=explode,
)

# ===================
# Part 4: Saving Output
# ===================
# Show plot with tight layout
plt.tight_layout()
plt.savefig('pie_1.pdf', bbox_inches='tight')
