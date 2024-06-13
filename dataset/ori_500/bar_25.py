# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)

import matplotlib.patches as mpatches

# ===================
# Part 2: Data Preparation
# ===================
# Data
categories = ["Alpaca-52k+", "AlpaGasus-1k+", "LIMA-1k+", "LIMA-1k*"]
wins = [78.8, 67.4, 44.2, 59.8]
ties = [11.7, 18.1, 21.9, 21.0]
losses = [9.5, 14.5, 33.9, 19.2]

# Define colors
colors_wins = ["#4881b8", "#4881b8", "#4881b8", "#d55f2b"]
colors_ties = ["#7badd2", "#7badd2", "#7badd2", "#ee934f"]
colors_losses = ["#cadbed", "#cadbed", "#cadbed", "#f6d2a8"]

# Repeat for the second subplot with different data
wins2 = [77.6, 68.3, 43.2, 62.9]
ties2 = [18.0, 23.7, 26.7, 23.6]
losses2 = [4.4, 8.0, 30.1, 13.5]
# Plot data
bar_width = 0.5
indices = np.arange(len(categories))

xlabel = "GPT4-as-a-judge"
xlabel2 = "PaLM2-as-a-judge"

labels = ["Refined-Alpaca-1k-longest wins", "Alpaca-1k-longest wins", "Tie","Tie", "Refined-Alpaca-1k-longest loses", "Alpaca-1k-longest loses"]


# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create figure and axes
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))




# Function to plot bars
def plot_bars(ax, wins, ties, losses, colors_wins, colors_ties, colors_losses):
    for i, (win, tie, loss) in enumerate(zip(wins, ties, losses)):
        ax.barh(i, win, bar_width, color=colors_wins[i], edgecolor="white")
        ax.barh(i, tie, bar_width, left=win, color=colors_ties[i], edgecolor="white")
        ax.barh(
            i,
            loss,
            bar_width,
            left=win + tie,
            color=colors_losses[i],
            edgecolor="white",
        )
        ax.text(win / 2, i, f"{win}", ha="center", va="center", color="white")
        ax.text(win + tie / 2, i, f"{tie}", ha="center", va="center", color="black")
        ax.text(
            win + tie + loss / 2, i, f"{loss}", ha="center", va="center", color="black"
        )


plot_bars(ax1, wins, ties, losses, colors_wins, colors_ties, colors_losses)

# Set labels, title, and legend for ax1
ax1.set_yticks(indices)
ax1.set_yticklabels(categories)
ax1.invert_yaxis()  # labels read top-to-bottom
ax1.set_xlabel(xlabel)
ax1.set_xticks([])

plot_bars(ax2, wins2, ties2, losses2, colors_wins, colors_ties, colors_losses)
# Set labels, title, and legend for ax2
ax2.set_yticks(indices)
ax2.set_yticklabels(categories)
ax2.invert_yaxis()  # labels read top-to-bottom
ax2.set_xlabel(xlabel2)
ax2.set_xticks([])

# Adjust layout and set background color
fig.patch.set_facecolor("white")
for ax in [ax1, ax2]:
    ax.set_facecolor("white")
    ax.spines["top"].set_edgecolor("gray")
    ax.spines["right"].set_edgecolor("gray")
    ax.spines["bottom"].set_edgecolor("gray")
    ax.spines["left"].set_edgecolor("gray")

# Create a global legend
patch1 = mpatches.Patch(color="#d55f2b", label=labels[0])
patch2 = mpatches.Patch(color="#4881b8", label=labels[1])
patch3 = mpatches.Patch(color="#ee934f", label=labels[2])
patch4 = mpatches.Patch(color="#7badd2", label=labels[3])
patch5 = mpatches.Patch(color="#f6d2a8", label=labels[4])
patch6 = mpatches.Patch(color="#cadbed", label=labels[5])
fig.legend(
    handles=[patch1, patch2, patch3, patch4, patch5, patch6],
    loc="upper center",
    ncol=3,
    bbox_to_anchor=(0.5, 1.15),
)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save the figure
plt.tight_layout()
plt.savefig('bar_25.pdf', bbox_inches='tight')
