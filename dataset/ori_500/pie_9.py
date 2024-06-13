# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Different data for another example
labels = ["Solar", "Wind", "Hydro", "Coal", "Other"]
outer_sizes = [200, 300, 150, 250, 100]  # Energy sources distribution in a country
inner_sizes = [80, 120, 60, 180, 40]  # Energy sources distribution for a specific project

outer_colors = ["#ffcc00", "#00cc99", "#0066cc", "#cc3300", "#999966"]
inner_colors = ["#ffd700", "#66ffcc", "#3399ff", "#ff6666", "#cccc99"]

explode_outer = (0.1, 0, 0, 0, 0)  # only explode the 1st slice (Solar)

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
    explode=explode_outer,
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

# Title for the double layer pie chart
ax.set_title("Energy Consumption - National vs. Project", fontsize=20, y=1.05)

# ===================
# Part 4: Saving Output
# ===================
# Show the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig('pie_9.pdf', bbox_inches='tight')
