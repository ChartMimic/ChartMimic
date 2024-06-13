# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Different data for another example
labels = ["Frogs 15%", "Hogs 30%", "Dogs 45%", "Logs 10%"]
outer_sizes = [30, 40, 20, 10]  # usage of platforms in a tech company
inner_sizes = [10, 20, 10, 20]  # usage of platforms for a specific project

outer_colors = ["#ff9999", "#66b3ff", "#99ff99", "#c2c2f0"]
inner_colors = ["#c4e17f", "#76dd1e", "#5a69af", "#ebefc9"]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
fig, ax = plt.subplots(figsize=(6, 6))

# Outer ring
wedges, texts, autotexts = ax.pie(
    outer_sizes,
    labels=labels,
    radius=1.2,
    colors=outer_colors,
    autopct="%1.1f%%",
    pctdistance=0.85,
    startangle=160,
)

# Inner ring
wedges2, texts2, autotexts2 = ax.pie(
    inner_sizes,
    radius=0.8,
    colors=inner_colors,
    autopct="%1.1f%%",
    pctdistance=0.75,
    startangle=160,
)

# Equal aspect ratio ensures that pie chart is drawn as a circle
ax.axis("equal")

# ===================
# Part 4: Saving Output
# ===================
# Show the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig('pie_2.pdf', bbox_inches='tight')
