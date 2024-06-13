# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

# ===================
# Part 2: Data Preparation
# ===================
# Data
labels = ["GCN", "RvNN", "Hyphen", "GET", "WSDMS", "DELL"]
democratic = [0.75, 0.8, 0.78, 0.85, 0.75, 0.8]
mixed = [0.8, 0.85, 0.82, 0.83, 0.84, 0.85]
republican = [0.84, 0.80, 0.81, 0.8, 0.75, 0.74]

x = np.arange(len(labels))  # the label locations
width = 0.25  # the width of the bars

# Variables for plot configuration
ylabel = "Macro F1-score"
xlabel_pheme = "Pheme"
xlabel_llm_mis = "LLM-mis"
xticks = x
xticklabels = labels
legend_label_democratic = "Democratic"
legend_label_mixed = "Mixed"
legend_label_republican = "Republican"
ylim_ax1 = (0.70, 0.85)
ylim_ax2 = (0.75, 0.90)
yticks_ax1 = [0.7, 0.75, 0.80, 0.85]
yticks_ax2 = [0.75, 0.80, 0.85, 0.90]

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
rects2 = ax1.bar(
    x, mixed, width, label=legend_label_mixed, color="#8895a3", edgecolor="black"
)
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
    x - width - 0.04, democratic, width, color="#84a9e7", edgecolor="black"
)
rects5 = ax2.bar(x, mixed, width, color="#8895a3", edgecolor="black")
rects6 = ax2.bar(
    x + width + 0.04, republican, width, color="#e15241", edgecolor="black"
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
plt.savefig("bar_14.pdf", bbox_inches="tight")
