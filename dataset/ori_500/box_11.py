# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Sample data for the boxplots
data1 = [19, 20, 21, 22, 21.5, 20.5, 19.5]
data2 = [18, 19, 20, 19.5, 18.5, 19.2, 18.8]
xticklabels = ["Llama-70b\n(T2TT)", "Llama-70b\n(S2TT)"]
ylabel = "BLEU"
xlim = [0.5, 3]
ylim = [16, 23]
yticks = [16, 18, 20, 22]
textlabel = "1.0 BLEU "
hlines = [20.5, 19.5]


# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create a figure and axis with the specified dimensions
fig, ax = plt.subplots(figsize=(6, 4))

# Create the boxplots
bp1 = ax.boxplot(
    data1, positions=[1], widths=0.6, patch_artist=True, boxprops=dict(facecolor="none")
)
bp2 = ax.boxplot(
    data2, positions=[2], widths=0.6, patch_artist=True, boxprops=dict(facecolor="none")
)

# Set the labels for the x-axis
ax.set_xticklabels(xticklabels, ha="center")
ax.set_xlim()

# Set the labels for the y-axis
ax.set_ylabel(ylabel)

# Set the y-axis limits
ax.set_ylim(ylim)
ax.set_yticks(yticks)

# Add a custom annotation for the 1.0 BLEU difference
ax.annotate(
    "",
    xy=(2.25, 20.5),
    xytext=(2.25, 19.0),
    arrowprops=dict(facecolor="black", arrowstyle="->"),
    horizontalalignment="center",
)

# Add the text for the 1.0 BLEU difference
ax.text(2.5, 19.7, textlabel, horizontalalignment="center")

# Add the dashed line for the 1.0 BLEU difference
ax.hlines(hlines[0], 1, 2.25, colors="grey", linestyles="dashed")
ax.hlines(hlines[1], 2, 2.25, colors="grey", linestyles="dashed")

# ===================
# Part 4: Saving Output
# ===================
# Adjust the layout and show the plot
plt.tight_layout()
plt.savefig("box_11.pdf", bbox_inches="tight")
