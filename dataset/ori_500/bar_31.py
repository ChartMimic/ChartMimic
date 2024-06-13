# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Data
categories = [
    "LLM-based vs. TPLM-based",
    "LLM-based vs. Template",
    "LLM-based vs. Markdown",
    "TPLM-based vs. Template",
    "TPLM-based vs. Markdown",
    "Markdown vs. Template",
][::-1]
win = [17.0, 20.0, 25.0, 30.5, 31.5, 19.5][::-1]
tie = [54.0, 67.5, 56.5, 57.5, 54.5, 61.0][::-1]
loss = [29.0, 12.5, 18.5, 12.0, 14.0, 19.5][::-1]

labels = ["Win", "Tie", "Loss"]
xticks = [0, 20, 40, 60, 80, 100]
xtickslabel = ["0", "20", "40", "60", "80", "100"]
bar_width = 0.6
indices = range(len(categories))

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create stacked bar chart
fig, ax = plt.subplots(figsize=(10, 6))  # Adjust figure size to 720x432 pixels

bars1 = ax.barh(indices, win, bar_width, label=labels[0], color="#9cc8e4")
bars2 = ax.barh(indices, tie, bar_width, left=win, label=labels[1], color="#b7da91")
bars3 = ax.barh(
    indices,
    loss,
    bar_width,
    left=[i + j for i, j in zip(win, tie)],
    label=labels[2],
    color="#ef8b88",
)

# Add text labels to the bars
for bars, color in zip([bars1, bars2, bars3], ["#9cc8e4", "#b7da91", "#ef8b88"]):
    for bar in bars:
        width = bar.get_width()
        center = bar.get_x() + width / 2
        ax.text(
            center,
            bar.get_y() + bar.get_height() / 2,
            f"{width:.1f}%",
            va="center",
            ha="center",
            color="black",
            fontsize=10,
        )

# Set the y-axis labels
ax.set_yticks(indices)
ax.set_yticklabels(categories, ha="right")

# Set the x-axis labels
ax.set_xticks(xticks)
ax.set_xticklabels(xtickslabel)

# Add legend
ax.legend(
    loc="upper center", bbox_to_anchor=(0.4, 1.05), shadow=True, ncol=3, frameon=False
)

# Remove spines
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save the figure
plt.tight_layout()
plt.savefig("bar_31.pdf", bbox_inches="tight")
