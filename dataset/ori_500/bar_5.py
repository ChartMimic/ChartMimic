# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Data for the bar chart
levels = ["Level 1", "Level 2", "Level 4"]
tent_pl_cotta = [50000, 50000, 50000]
eta = [30040, 28000, 22900]
cetta = [22000, 20600, 16800]

labels = ["Tent/PL/CoTTA", "ETA", "CETTA (ours)"]
ylabel = "# Avg. Uploaded Samples"
ylim = [0, 55000]

y_index = [0, 10000, 20000, 30000, 40000, 50000]
y_label_ticks = ["0", "10k", "20k", "30k", "40k", "50k"]

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
    tent_pl_cotta,
    width=bar_width,
    color="#ffffbd",
    edgecolor="black",
    label=labels[0],
)
plt.bar(index, eta, width=bar_width, color="#97ccfb", edgecolor="black", label=labels[1])
plt.bar(
    [i + bar_width for i in index],
    cetta,
    width=bar_width,
    color="#ea8777",
    edgecolor="black",
    label=labels[2],
)

# Add the text labels on top of the bars
for i in index:
    plt.text(
        i - bar_width,
        tent_pl_cotta[i] + 1000,
        f"{tent_pl_cotta[i]/1000:.1f}k",
        ha="center",
    )
    plt.text(i, eta[i] + 1000, f"{eta[i]/1000:.1f}k", ha="center")
    plt.text(i + bar_width, cetta[i] + 1000, f"{cetta[i]/1000:.1f}k", ha="center")

# Set the x-axis labels, y-axis label, and chart title
plt.xticks(index, levels)
plt.ylabel(ylabel)
plt.ylim(0, 55000)
plt.yticks(y_index, y_label_ticks)

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
plt.savefig("bar_5.pdf", bbox_inches="tight")
