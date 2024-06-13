# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Data
categories = [
    "DLMA-7B VS. LLAMa-7B",
    "DLMA-7B VS. CD-7B",
    "DLMA-7B VS. RLAIF-7B",
    "DLMA-7B VS. RLCD-7B",
    "DLMA-13B VS. LLAMa-13B",
    "DLMA-13B VS. CD-13B",
    "DLMA-13B VS. RLAIF-13B",
    "DLMA-13B VS. RLCD-13B",
]
dlma_win = [60.2, 60.2, 46.8, 34.7, 62.5, 62.5, 49.2, 30.9]
tie = [28.8, 28.8, 39.1, 39.1, 27.7, 27.7, 36.3, 38.7]
dlma_lose = [11.0, 11.0, 14.1, 26.2, 9.8, 9.8, 14.5, 30.5]
textcontent = "DLMA VS. Baseline Methods On HHH (Evaluated by GPT4)"
legendlabels = ["DLMA win", "Tie", "DLMA lose"]

# Colors
colors = ["#6eca87", "#468ef7", "#ea8777"]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plot
fig, ax = plt.subplots(
    figsize=(8, 6)
)  # Adjusted figure size to match the original image's dimensions

bar_width = 0.6  # Adjusted bar width for tighter layout
bar_spacing = 0.15  # Adjusted spacing between bars

for i, category in enumerate(categories):
    ax.barh(category, dlma_win[i], height=bar_width, color=colors[0])
    ax.barh(category, tie[i], height=bar_width, left=dlma_win[i], color=colors[1])
    ax.barh(
        category,
        dlma_lose[i],
        height=bar_width,
        left=dlma_win[i] + tie[i],
        color=colors[2],
    )
    ax.text(
        5,
        category,
        f"{dlma_win[i]}%",
        ha="center",
        va="center",
        color="white",
        fontsize=10,
    )
    ax.text(
        dlma_win[i] + tie[i] / 2,
        category,
        f"{tie[i]}%",
        ha="center",
        va="center",
        color="white",
        fontsize=10,
    )
    ax.text(
        95,
        category,
        f"{dlma_lose[i]}%",
        ha="center",
        va="center",
        color="white",
        fontsize=10,
    )

# Remove spines
ax.spines["right"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.spines["left"].set_visible(False)

# Remove x-axis
ax.xaxis.set_visible(False)
# Adjust y-axis
ax.invert_yaxis()

# Add label below the x-axis
plt.figtext(
    0.6,
    0.01,
    textcontent,
    ha="center",
    fontsize=10,
)

# Legend
ax.legend(
    legendlabels,
    loc="upper center",
    ncol=3,
    fontsize=12,
    bbox_to_anchor=(0.5, 1.05),
)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig("bar_19.pdf", bbox_inches="tight")
