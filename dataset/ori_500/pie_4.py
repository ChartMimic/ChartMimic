# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
labels = ["Germany 12%", "France 18%", "UK 42%", "Italy 28%"]
sizes = [12, 18, 42, 28]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
fig, ax = plt.subplots(figsize=(5, 5))
ax.pie(sizes, labels=labels,hatch=['**O', 'oO', 'O.O', '.||.'])
plt.title("Countries in Europe")

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig('pie_4.pdf', bbox_inches='tight')
