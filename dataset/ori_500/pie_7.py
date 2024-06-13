# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data to plot
labels = ["Youtube", "Facebook", "Instagram", "Twitter", "LinkedIn"]
sizes = [25, 35, 20, 10, 10]
colors = plt.cm.Blues(np.linspace(0.3, 1, len(sizes)))
explode = (0, 0, 0.1, 0, 0)

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plot
plt.figure(figsize=(8, 6))
plt.pie(
    sizes,
    explode=explode,
    colors=colors,
    autopct="%1.1f%%",
    shadow=False,
    startangle=140,
)
plt.axis("equal")

# Add legend
plt.legend(labels, loc="upper left")
plt.title("Social Media Usage", fontsize=16, y=1.05)

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig('pie_7.pdf', bbox_inches='tight')
