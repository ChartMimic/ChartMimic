# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Sample data
instance_sizes = [
    "15x15",
    "20x15",
    "20x20",
    "30x15",
    "30x20",
    "50x15",
    "50x20",
    "100x20",
]
petriRL = [2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500]
GAM = [2200, 2700, 3200, 3700, 4200, 4700, 5200, 5700]
GIN = [2400, 2900, 3400, 3900, 4400, 4900, 5400, 5900]
DGERD = [2600, 3100, 3600, 4100, 4600, 5100, 5600, 6100]
improvement = [0.18, 0.14, 0.13, 0.12, 0.09, 0, 0, -0.05]
labels = ["PetriRL", "GAM", "GIN", "DGERD"]
xlabel = "Instance size"
ylabel1 = "Makespan (step)"
ylabel2 = "Improvement %"
legend_title = "Methods"
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create figure and axis
fig, ax1 = plt.subplots(figsize=(8, 5))

# Bar plot
bar_width = 0.2
index = np.arange(len(instance_sizes))
ax1.bar(index, petriRL, bar_width, label=labels[0], color="limegreen")
ax1.bar(index + bar_width, GAM, bar_width, label=labels[1], color="sandybrown")
ax1.bar(index + 2 * bar_width, GIN, bar_width, label=labels[2], color="cornflowerblue")
ax1.bar(index + 3 * bar_width, DGERD, bar_width, label=labels[3], color="plum")

# Line plot
ax2 = ax1.twinx()
ax2.plot(
    instance_sizes,
    improvement,
    color="orangered",
    marker="o",
    linestyle="-",
    linewidth=2,
    markersize=5,
)

# Annotate improvement percentages
for i, imp in enumerate(improvement):
    ax2.annotate(
        f"{imp*100:.0f}%",
        (index[i] + bar_width * 1.2, imp),
        textcoords="offset points",
        xytext=(0, 0),
        ha="center",
        color="orangered",
    )

# Set labels and title
ax1.set_xlabel(xlabel)
ax1.set_ylabel(ylabel1)
ax2.set_ylabel(ylabel2)

# Set x-axis tick labels
ax1.set_xticks(index + bar_width * 1.5)
ax1.set_xticklabels(instance_sizes)

# Add legend
ax1.legend(loc="lower center", ncol=4, bbox_to_anchor=(0.5, -0.3), title=legend_title)
ax1.grid(axis="y")
ax1.set_axisbelow(True)

# set ax2.yticklabels to be percentage
ax2.set_yticklabels([f"{x*100:.0f}%" for x in ax2.get_yticks()])

# ===================
# Part 4: Saving Output
# ===================
# Show plot with tight layout
plt.tight_layout()
# Save the plot as a PDF file
plt.savefig("CB_25.pdf", bbox_inches="tight")
