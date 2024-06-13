# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Data
categories = ["Vicuna", "Koala", "WizardLM", "SInstruct", "LIMA"][::-1]
recost_wins = [53, 80, 116, 99, 179][::-1]
ties = [6, 33, 49, 50, 23][::-1]
alpaca_wins = [21, 67, 53, 103, 98][::-1]

labels = ["Recost (1%) wins", "Tie", "Alpaca wins"]
bar_width = 0.5
y_pos = range(len(categories))


# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Stacked Bar Chart
fig, ax = plt.subplots(
    figsize=(8, 5)
)  # Adjusted to match the original image's dimensions

ax.barh(y_pos, recost_wins, bar_width, color="#e4754f", label=labels[0])
ax.barh(y_pos, ties, bar_width, left=recost_wins, color="#feffc7", label=labels[1])
ax.barh(
    y_pos,
    alpaca_wins,
    bar_width,
    left=[i + j for i, j in zip(recost_wins, ties)],
    color="#81acce",
    label=labels[2],
)

# Adding the numerical values within each segment
for i in range(len(categories)):
    ax.text(
        recost_wins[i] / 2,
        i,
        str(recost_wins[i]),
        ha="center",
        va="center",
        color="white",
    )
    ax.text(
        recost_wins[i] + ties[i] / 2,
        i,
        str(ties[i]),
        ha="center",
        va="center",
        color="black",
    )
    ax.text(
        recost_wins[i] + ties[i] + alpaca_wins[i] / 2,
        i,
        str(alpaca_wins[i]),
        ha="center",
        va="center",
        color="white",
    )

# Labels and Legend
ax.set_xticks([])
ax.set_yticks(y_pos)
ax.set_yticklabels(categories)
ax.legend(loc="upper right")

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig("bar_39.pdf", bbox_inches="tight")
