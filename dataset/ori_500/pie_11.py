# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Different data for another example
labels = ["Food", "Transport", "Utilities", "Entertainment", "Others"]
outer_sizes = [350, 450, 200, 120, 80]  # usage of platforms in a tech company
inner_sizes = [150, 250, 120, 60, 20]  # usage of platforms for a specific project

outer_colors = ["#ff9999", "#66b3ff", "#99ff99", "#ffcc99", "#c2c2f0"]
inner_colors = ["#c4e17f", "#76dd1e", "#5a69af", "#edc214", "#ebefc9"]
outer_hatch = ["/", "\\", "|", "-", "+"]  # Different hatching for outer ring
inner_hatch = ["x", "*", "o", "O", "."]  # Different hatching for inner ring

explode_outer = (0.1, 0, 0, 0, 0)  # only explode the 1st slice (IOS)
title = "Expenses - Company vs. Project"
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
fig, ax = plt.subplots(figsize=(8, 8))

# Outer ring
wedges, texts, autotexts = ax.pie(
    outer_sizes,
    labels=labels,
    radius=1.2,
    colors=outer_colors,
    explode=explode_outer,
    autopct="%1.1f%%",
    pctdistance=0.85,
    startangle=160,
    wedgeprops=dict(width=0.3, edgecolor="w", hatch="*"),
)

# Inner ring
wedges2, texts2, autotexts2 = ax.pie(
    inner_sizes,
    radius=0.9,
    colors=inner_colors,
    autopct="%1.1f%%",
    pctdistance=0.75,
    startangle=160,
    wedgeprops=dict(width=0.3, edgecolor="w", hatch="o"),
)

# Customizing the autotexts for better visibility
for autotext in autotexts + autotexts2:
    autotext.set_color("black")
    autotext.set_fontsize(10)

# Title for the double layer pie chart
ax.set_title(title, fontsize=16, y=1.05)

# ===================
# Part 4: Saving Output
# ===================
# Improve layout to make room for legend or labels if necessary
plt.tight_layout()

# Show the plot
plt.savefig('pie_11.pdf', bbox_inches='tight')
