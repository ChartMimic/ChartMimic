# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Data
categories = ["LIMA", "Vicuna", "Koala", "Wizardlm", "Self-Instruct"]
AP_1kL_wins = [68, 82, 68, 72, 68]
Tie = [24, 15, 22, 19, 23]
AG_1k_wins = [8, 3, 10, 9, 9]

bar_width = 0.5
indices = range(len(categories))

labels = ["AP-1kL wins", "Tie", "AG-1k wins"]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Figure size
fig, ax = plt.subplots(
    figsize=(8, 5)
)  # Adjusted to match the original image's dimensions

# Bar chart


# Plotting bars with new colors
bars1 = ax.barh(indices, AP_1kL_wins, bar_width, label=labels[0], color="#1f77b4")
bars2 = ax.barh(indices, Tie, bar_width, left=AP_1kL_wins, label=labels[1], color="#8da0cb")
bars3 = ax.barh(
    indices,
    AG_1k_wins,
    bar_width,
    left=[i + j for i, j in zip(AP_1kL_wins, Tie)],
    label=labels[2],
    color="#c7c7c7",
)

# Adding text labels with new positions and font size
for i, bar in enumerate(bars1):
    ax.text(
        bar.get_width() / 2,
        bar.get_y() + bar.get_height() / 2,
        f"{AP_1kL_wins[i]}",
        ha="center",
        va="center",
        color="white",
        fontsize=14,
    )
for i, bar in enumerate(bars2):
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_y() + bar.get_height() / 2,
        f"{Tie[i]}",
        ha="center",
        va="center",
        color="black",
        fontsize=14,
    )
for i, bar in enumerate(bars3):
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_y() + bar.get_height() / 2,
        f"{AG_1k_wins[i]}",
        ha="center",
        va="center",
        color="black",
        fontsize=14,
    )

# Labels and title
ax.set_yticks(indices)
ax.set_yticklabels(categories, fontsize=14)
ax.invert_yaxis()  # Labels read top-to-bottom
ax.set_xticks([])

# Legend with new position
ax.legend(loc="upper left", bbox_to_anchor=(0.1, 1.15), ncol=3, fontsize=14)

# ===================
# Part 4: Saving Output
# ===================
# Tight layout
plt.tight_layout()
plt.savefig("bar_20.pdf", bbox_inches="tight")
