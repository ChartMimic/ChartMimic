import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Data for plotting
sizes = ["Q1", "Q2", "Q3", "Q4", "Q5", "Q6"]
samples = [
    "(45 samples)",
    "(90 samples)",
    "(135 samples)",
    "(180 samples)",
    "(225 samples)",
    "(270 samples)",
]
x = range(len(sizes))
y = [29.35, 27.45, 24.67, 26.54, 27.98, 28.76]
errors = [2.1, 1.9, 2.0, 1.8, 1.7, 1.5]
ylabel = "Success Rate (%)"
xlabel = "Data Collection Period"
ylim = [20, 32]
yticks = [20, 22, 24, 26, 28, 30]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plotting the bar chart
plt.figure(
    figsize=(10, 7)
)  # Adjusting figure size to match original image's dimensions
bars = plt.bar(x, y, yerr=errors, color="skyblue", capsize=5)

# Adding data labels on top of the bars
for bar in bars:
    yval = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        yval + 0.5,
        round(yval, 2),
        ha="right",
        va="bottom",
    )

# Setting the x-axis labels with both percentages and sample sizes
plt.xticks(x, [f"{size}\n{sample}" for size, sample in zip(sizes, samples)])

# Setting the y-axis label
plt.ylabel(ylabel)

# Setting the title of the chart
plt.xlabel(xlabel)

# Adjusting y-axis range
plt.ylim(ylim)
plt.yticks(yticks)
# Adding grid to the background
plt.grid(axis="both", alpha=0.7, which="both", color="gray")

# Making the axis lines visible
plt.gca().spines["top"].set_visible(True)
plt.gca().spines["right"].set_visible(True)
plt.gca().spines["bottom"].set_visible(True)
plt.gca().spines["left"].set_visible(True)

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig('errorbar_5.pdf', bbox_inches='tight')
