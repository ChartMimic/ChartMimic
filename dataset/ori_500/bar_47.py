# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data for the bar charts
categories = ["HH", "Reddit", "IMDB", "AVG"]
win = [22, 25, 30, 26, 45, 50, 20, 38, 40, 30, 50, 40, 50, 55, 42, 50]
tie = [50, 40, 60, 50, 20, 35, 50, 35, 30, 10, 30, 23, 20, 22, 20, 20]
lose = [28, 35, 10, 24, 35, 15, 30, 27, 30, 60, 20, 37, 30, 22, 38, 30]

labels = ["Win", "Tie", "Lose"]
titles = ["COPR v.s. Golden (Human Eval)", "COPR v.s. DPO-ER (Human Eval)", "COPR v.s. Golden (GPT-4 Eval)", "COPR v.s. DPO-ER (GPT-4 Eval)"]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create a figure with custom size
fig, axes = plt.subplots(2, 2, figsize=(13, 6))


# Function to create a bar chart
def create_bar_chart(ax, win, tie, lose, title):
    bar_width = 0.5
    indices = np.arange(len(categories))

    ax.barh(indices, win, bar_width, color="#9e2621", label=labels[0])
    ax.barh(indices, tie, bar_width, left=win, color="#ea7a5c", label=labels[1])
    ax.barh(
        indices, lose, bar_width, left=np.add(win, tie), color="#fae6da", label=labels[2]
    )

    ax.set_yticks(indices)
    ax.set_yticklabels(categories)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_title(title)
    ax.set_xlim(0, 100)

    for i, (w, t, l) in enumerate(zip(win, tie, lose)):
        ax.text(w / 2, i, f"{w}%", ha="center", va="center", color="white")
        ax.text(w + t / 2, i, f"{t}%", ha="center", va="center", color="black")
        ax.text(w + t + l / 2, i, f"{l}%", ha="center", va="center", color="black")
        for spine in ax.spines.values():
            spine.set_visible(False)
        ax.set_yticklabels(categories, rotation=45)


# Create each bar chart
create_bar_chart(
    axes[0, 0], win[:4], tie[:4], lose[:4], titles[0]
)
create_bar_chart(
    axes[1, 0], win[4:8], tie[4:8], lose[4:8], titles[1]
)
create_bar_chart(
    axes[0, 1], win[8:12], tie[8:12], lose[8:12], titles[2]
)
create_bar_chart(
    axes[1, 1], win[12:], tie[12:], lose[12:], titles[3]
)

# Add a legend
handles, labels = axes[0, 0].get_legend_handles_labels()
fig.legend(handles, labels, loc="lower center", ncol=3)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save the figure
plt.tight_layout(rect=[0, 0.05, 1, 1])
plt.savefig("bar_47.pdf", bbox_inches="tight")
