import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Data for the bar chart
levels = ["Beginner", "Intermediate", "Advanced"]
yoga = [550, 300, 350]
cardio = [300, 450, 400]
strength_training = [600, 550, 600]

labels = ["Yoga", "Cardio", "Strength Training"]
ylabel = "Avg. Calories Burned"
ylim = [0, 650]

yindex = [0, 100, 200, 300, 400, 500]
ylabel_ticks = ["0", "100", "200", "300", "400", "500"]


# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Set the figure size to match the original image's dimensions
plt.figure(figsize=(8, 3))

# Create the bar chart
bar_width = 0.25
index = range(len(levels))

plt.bar(
    [i - bar_width for i in index],
    yoga,
    width=bar_width,
    color="#ffffbd",
    edgecolor="black",
    label=labels[0],
)
plt.bar(index, cardio, width=bar_width, color="#97ccfb", edgecolor="black", label=labels[1])
plt.bar(
    [i + bar_width for i in index],
    strength_training,
    width=bar_width,
    color="#ea8777",
    edgecolor="black",
    label=labels[2],
)

# Add the text labels on top of the bars
for i in index:
    plt.text(
        i - bar_width,
        yoga[i] + 10,
        f"{yoga[i]/1000:.1f}k",
        ha="center",
    )
    plt.text(i, cardio[i] + 10, f"{cardio[i]/1000:.1f}k", ha="center")
    plt.text(i + bar_width, strength_training[i] + 10, f"{strength_training[i]/1000:.1f}k", ha="center")

# Set the x-axis labels, y-axis label, and chart title
plt.xticks(index, levels)
plt.ylabel(ylabel)
plt.ylim(ylim)
plt.yticks(yindex, ylabel_ticks)

# Add a legend
plt.legend(loc="upper center", bbox_to_anchor=(0.5, 1.15), ncol=3)

# Hide the right and top spines
plt.gca().spines["right"].set_visible(False)
plt.gca().spines["top"].set_visible(False)

# ===================
# Part 4: Saving Output
# ===================
# Show the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig('bar_5.pdf', bbox_inches='tight')
