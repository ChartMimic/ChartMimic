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
modes = ["4211", "2411", "2141", "1124"]
srcc_values = [0.9628, 0.9604, 0.9612, 0.9561]
plcc_values = [0.9640, 0.9624, 0.9641, 0.9592]
sum_values = [1.9252, 1.9223, 1.9241, 1.915]
labels = ["SRCC", "PLCC", "Sum (SRCC + PLCC)"]
xlabel = "Modes"
ylabel = "Values"
title = "SRCC and PLCC values with their sum for different modes"
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Bar plot
fig, ax1 = plt.subplots(
    figsize=(10, 6)
)  # Adjust the figsize to match the original image's dimensions

bar_width = 0.35
index = np.arange(len(modes))

bar1 = ax1.bar(index, srcc_values, bar_width, label=labels[0], color="blue")
bar2 = ax1.bar(
    index + bar_width, plcc_values, bar_width, label=labels[1], color="green"
)

# Line plot
ax2 = ax1.twinx()
(line,) = ax2.plot(index, sum_values, color="red", marker="o", label=labels[2])

# Annotate bars with values
for rect, value in zip(bar1, srcc_values):
    height = rect.get_height()
    ax1.text(
        rect.get_x() + rect.get_width() / 2,
        height + 0.0002,
        f"{value:.4f}",
        ha="center",
        va="bottom",
    )

for rect, value in zip(bar2, plcc_values):
    height = rect.get_height()
    ax1.text(
        rect.get_x() + rect.get_width() / 2,
        height + 0.0002,
        f"{value:.4f}",
        ha="center",
        va="bottom",
    )

# Labels, title and legend
ax1.set_xlabel(xlabel)
ax1.set_ylabel(ylabel)
ax1.set_title(title)
ax1.set_xticks(index + bar_width / 2)
ax1.set_xticklabels(modes)
ax1.set_ylim(0.954, 0.966)
ax1.set_yticks([0.956, 0.958, 0.960, 0.962, 0.964])
ax2.set_ylim(1.914, 1.928)
ax2.set_yticks([1.916, 1.918, 1.920, 1.922, 1.924, 1.926])
ax1.legend(loc="upper left")
ax2.legend(loc="upper right")

ax1.yaxis.grid(True)

# ===================
# Part 4: Saving Output
# ===================
# Adjust figure size to match original image's dimensions
fig.set_size_inches(10, 6)

# Show plot
plt.tight_layout()
plt.savefig("CB_9.pdf", bbox_inches="tight")
