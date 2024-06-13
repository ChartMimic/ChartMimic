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
steps = ["0", "1", "2", "3", "4"]
avg_following_rate = [0.267, 0.277, 0.298, 0.271, 0.385]
following_format_error_rate = [1.0, 0.833, 0.507, 1.0, 0.917]
following_related_error_rate = [0.6, 0.481, 0.507, 0.634, 0.608]

# X-axis positions for each group of bars
x = np.arange(len(steps))

# Bar width
bar_width = 0.25
labels = ["Avg. Following Rate", "Following-related Format Error Rate", "Following-related Error Rate"]
title = "Instruction Following Results In Different Steps (gpt-3.5-turbo)"
xlabel = "Steps"
ylabel = "Scores"
yticks = np.arange(0, 1.3, 0.2)

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Figure and axis
fig, ax = plt.subplots(figsize=(10, 5))  # Adjusted to match original image dimensions

# Plotting bars
rects1 = ax.bar(
    x - bar_width,
    avg_following_rate,
    bar_width,
    label=labels[0],
    color="#666666",
    edgecolor="white",
)
rects2 = ax.bar(
    x,
    following_format_error_rate,
    bar_width,
    label=labels[1],
    color="#5584af",
    edgecolor="white",
)
rects3 = ax.bar(
    x + bar_width,
    following_related_error_rate,
    bar_width,
    label=labels[2],
    color="#4a8f74",
    edgecolor="white",
)


# Adding percentage labels on top of each bar
def add_labels(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(
            f"{height*100:.1f}%",
            xy=(rect.get_x() + rect.get_width() / 2, height),
            xytext=(0, 3),  # 3 points vertical offset
            textcoords="offset points",
            ha="center",
            va="bottom",
        )


add_labels(rects1)
add_labels(rects2)
add_labels(rects3)

# Title and labels
ax.set_title(title)
ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)

# X and Y ticks
ax.set_xticks(x)
ax.set_xticklabels(steps)
ax.set_yticks(yticks)

# Legend
ax.legend(loc="upper center", ncol=3, frameon=False)

# Grid lines
ax.yaxis.grid(True)
ax.set_axisbelow(True)

grid_color = "#bdbdbd"
# Set border color
for spine in ax.spines.values():
    spine.set_edgecolor(grid_color)
# hidden ticks
plt.tick_params(axis="both", which="both", length=0)

# ===================
# Part 4: Saving Output
# ===================
# Show plot with tight layout
plt.tight_layout()
plt.savefig("bar_33.pdf", bbox_inches="tight")
