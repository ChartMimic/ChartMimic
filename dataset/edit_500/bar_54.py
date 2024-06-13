# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data
categories = ["Cardiology", "Neurology", "Orthopedics", "Pediatrics", "Dermatology"]
values = [25, 32, 28, 20, 15]
titles = "Probability of Breakthroughs in Medical Specialties"
xlabel = "Probability of Breakthrough"
# Create color map
colors = cm.viridis(np.linspace(0, 1, len(values)))

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create horizontal bar chart
plt.figure(figsize=(6, 2))  # Adjusting figure size to match original image dimensions
plt.barh(categories, values, color=colors)

# Adding title and labels
plt.title(titles)
plt.xlabel(xlabel)
xticks = []
xlabels = []
# Apply the xticks and labels
plt.xticks(xticks, xlabels)
for spine in plt.gca().spines.values():
    spine.set_visible(False)

# ===================
# Part 4: Saving Output
# ===================
# Show plot with tight layout
plt.tight_layout()
plt.savefig('bar_54.pdf', bbox_inches='tight')
