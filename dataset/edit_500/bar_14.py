# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)

# ===================
# Part 2: Data Preparation
# ===================
# Data
labels = ["NN", "DT", "RF", "SVM", "KNN", "LR"]
democratic = [0.70, 0.65, 0.75, 0.72, 0.68, 0.66]  # Different distribution
mixed = [0.68, 0.72, 0.70, 0.71, 0.69, 0.68]       # Different distribution
republican = [0.65, 0.66, 0.67, 0.68, 0.69, 0.70]  # Different distribution

democratic1 = [0.70, 0.65, 0.75, 0.66, 0.72, 0.70]  # Different distribution
mixed1 = [0.68, 0.70, 0.73, 0.71, 0.68, 0.63]       # Different distribution
republican1 = [0.70, 0.66, 0.67, 0.72, 0.73, 0.69]  # Different distribution
x = np.arange(len(labels))  # the label locations
width = 0.25  # the width of the bars

# Variables for plot configuration
ylabel = "Success Rate"
xlabel_pheme = "Performance on Image Classification"
xlabel_llm_mis = "Performance on Text Classification"
xticks = x
xticklabels = labels
legend_label_democratic = "NN"
legend_label_mixed = "DT"
legend_label_republican = "RF"
ylim_ax1 = (0.60, 0.80)
ylim_ax2 = (0.65, 0.85)
yticks_ax1 = [0.60, 0.65, 0.70, 0.75, 0.80]
yticks_ax2 = [0.65, 0.70, 0.75, 0.80,0.85]


# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Setting up the figure and axes for a 2 x 1 layout
fig, (ax1, ax2) = plt.subplots(
    2, 1, figsize=(7, 5), gridspec_kw={"height_ratios": [1, 1], "hspace": 0.3}
)

# Upper plot
rects1 = ax1.bar(
    x - width - 0.04,
    democratic,
    width,
    label=legend_label_democratic,
    color="#84a9e7",
    edgecolor="black",
)
rects2 = ax1.bar(x, mixed, width, label=legend_label_mixed, color="#8895a3", edgecolor="black")
rects3 = ax1.bar(
    x + width + 0.04,
    republican,
    width,
    label=legend_label_republican,
    color="#e15241",
    edgecolor="black",
)
# Lower plot
rects4 = ax2.bar(
    x - width - 0.04, democratic1, width, color="#84a9e7", edgecolor="black"
)
rects5 = ax2.bar(x, mixed1, width, color="#8895a3", edgecolor="black")
rects6 = ax2.bar(
    x + width + 0.04, republican1, width, color="#e15241", edgecolor="black"
)

# Add some text for labels, title and custom x-axis tick labels, etc.
ax1.set_ylabel(ylabel)
ax2.set_ylabel(ylabel)
ax1.set_xlabel(xlabel_pheme)
ax2.set_xlabel(xlabel_llm_mis)
ax1.set_xticks(xticks)
ax1.set_xticklabels(xticklabels)
ax2.set_xticks(xticks)
ax2.set_xticklabels(xticklabels)
ax1.legend(loc="upper center", bbox_to_anchor=(0.5, 1.25), ncol=3, frameon=False)

# Set y-axis limit to match the reference picture
ax1.set_ylim(ylim_ax1)
ax2.set_ylim(ylim_ax2)
ax1.tick_params(axis="x", which="both", length=0)
ax2.tick_params(axis="x", which="both", length=0)
ax1.set_yticks(yticks_ax1)
ax2.set_yticks(yticks_ax2)

# Set grid color and style
ax1.grid(axis="y", color="gray", linestyle="--", linewidth=0.5)
ax2.grid(axis="y", color="gray", linestyle="--", linewidth=0.5)
ax1.tick_params(axis="y", which="major", color="gray")
ax2.tick_params(axis="y", which="major", color="gray")
ax1.set_axisbelow(True)
ax2.set_axisbelow(True)

# Remove top and right borders
ax1.spines["top"].set_visible(False)
ax1.spines["right"].set_visible(False)
ax1.spines["bottom"].set_visible(False)
ax1.spines["left"].set_color("gray")
ax2.spines["top"].set_visible(False)
ax2.spines["right"].set_visible(False)
ax2.spines["bottom"].set_visible(False)
ax2.spines["left"].set_color("gray")

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig('bar_14.pdf', bbox_inches='tight')
