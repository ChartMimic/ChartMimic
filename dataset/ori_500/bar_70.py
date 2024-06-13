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
annotators = ["1", "2", "3", "4", "5", "6"]
scores = {
    "1": [10, 12, 8, 11, 10],
    "2": [10, 12, 5, 15, 8],
    "3": [8, 12, 8, 10, 12],
    "4": [15, 9, 6, 10, 10],
    "5": [12, 12, 8, 12, 6],
    "6": [10, 7, 10, 15, 8],
}

# Define a color map for gradients
cmap = plt.get_cmap("BuGn")

title = "Human Labeling and Agreement Bias Checking"
xlabel = "Human Annotator"
ylabel = "Scores"

ylim = [0, 50]
yticks = range(0, 51, 10)
score_labels = [f"Score {i+1}" for i in range(5)]
legendtitle = "Scores"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
fig, ax = plt.subplots(figsize=(8, 5))  # Adjusting figure size

for i, annotator in enumerate(annotators):
    bottom = 0
    score_list = scores[annotator]
    for j, score in enumerate(score_list):
        color = cmap(
            1 - j / len(score_list)
        )  # Determine color based on position in list
        bar = ax.bar(annotator, score, bottom=bottom, color=color)
        bottom += score
        # Annotate each segment

        if j == len(score_list) - 1:
            ax.text(
                bar[0].get_x() + bar[0].get_width() / 2,
                bottom - score / 2,
                str(score),
                ha="center",
                va="bottom",
                color="black",
            )
        else:
            ax.text(
                bar[0].get_x() + bar[0].get_width() / 2,
                bottom - score / 2,
                str(score),
                ha="center",
                va="center",
                color="white",
            )

# Adding title and labels
ax.set_title(title)
ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)
ax.set_ylim(ylim)  # Adjusting limit to make space for text annotations
ax.set_yticks(yticks)

# Adding legend with score indications
ax.legend(score_labels, title=legendtitle, bbox_to_anchor=(1.05, 1), loc="upper left")
ax.yaxis.grid(linestyle="--")

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig("bar_70.pdf", bbox_inches="tight")
