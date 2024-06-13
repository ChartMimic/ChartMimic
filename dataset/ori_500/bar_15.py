# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Sample data
annotators = ["1", "2", "3", "4", "5", "6"]
scores = {
    "1": [10, 12, 8, 11, 10],
    "2": [10, 12, 5, 15, 8],
    "3": [8, 12, 8, 10, 12],
    "4": [15, 9, 6, 10, 10],
    "5": [12, 12, 8, 12, 6],
    "6": [10, 7, 10, 15, 8],
}

# Colors for each score
colors = ["#cd4231", "#ed9264", "#f8df9a", "#d6e8e5", "#9bbdde"]

# Variables for plot configuration
title = "Human Labeling and Agreement Bias Checking"
xlabel = "Human Annotator"
ylabel = "Scores"
ylim = (0, 50)
yticks = [0, 10, 20, 30, 40, 50]
legend_title = "Scores"
legend_labels = [1, 2, 3, 4, 5]
legend_loc = "upper left"
legend_bbox_to_anchor = (1.05, 1.1)
legend_reverse = True

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plotting the stacked bar chart
fig, ax = plt.subplots(
    figsize=(8, 5)
)  # Adjusting figure size to match original image dimensions

for i, annotator in enumerate(annotators):
    bottom = 0
    for j, score in enumerate(scores[annotator]):
        ax.bar(annotator, score, bottom=bottom, color=colors[j])
        bottom += score

# Adding title and labels
ax.set_title(title)
ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)
ax.set_ylim(ylim)
ax.set_yticks(yticks)
ax.tick_params(axis="both", which="both", length=0)

# Adding legend
ax.legend(
    legend_labels,
    title=legend_title,
    frameon=False,
    bbox_to_anchor=legend_bbox_to_anchor,
    loc=legend_loc,
    reverse=legend_reverse,
)

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig("bar_15.pdf", bbox_inches="tight")
