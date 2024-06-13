import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Updated sample data for the boxplots
data1 = [75, 78, 80, 82, 81, 79, 77]
data2 = [72, 74, 75, 73, 72.5, 73.8, 73]
xticklabels = ["Solar Output\n(Winter)", "Solar Output\n(Summer)"]
ylabel = "Efficiency (%)"
xlim = [0.5, 3]
ylim = [70, 85]
yticks = [70, 75, 80, 85]
textlabel = "1.0% Efficiency"
hlines = [80, 75]


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
    xy=(2.25, hlines[0]),
    xytext=(2.25, hlines[1]),
    arrowprops=dict(facecolor="black", arrowstyle="->"),
    horizontalalignment="center",
)

# Add the text for the 1.0 BLEU difference
ax.text(2.5, hlines[1]+2.5, textlabel, horizontalalignment="center")

# Add the dashed line for the 1.0 BLEU difference
ax.hlines(hlines[0], 1, 2.25, colors="grey", linestyles="dashed")
ax.hlines(hlines[1], 2, 2.25, colors="grey", linestyles="dashed")

# ===================
# Part 4: Saving Output
# ===================
# Adjust the layout and show the plot
plt.tight_layout()
plt.savefig('box_11.pdf', bbox_inches='tight')
