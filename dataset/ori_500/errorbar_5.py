# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Data for plotting
sizes = ["5%", "10%", "20%", "30%", "40%", "50%"]
samples = [
    "(40 samples)",
    "(81 samples)",
    "(163 samples)",
    "(245 samples)",
    "(326 samples)",
    "(408 samples)",
]
x = range(len(sizes))
y = [63.77, 64.17, 64.31, 64.98, 65.82, 65.78]
errors = [1.5, 1.2, 1.3, 1.1, 1.0, 0.8]
ylabel = "True+info (%)"
xlabel = "Size of Data for Training and Validation"
ylim = [56, 67]
yticks = [56, 58, 60, 62, 64, 66]


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
plt.savefig("errorbar_5.pdf", bbox_inches="tight")
