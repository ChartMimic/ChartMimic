# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Simulating data
sizes = np.linspace(300, 100, 6, dtype=int)  # Generate sizes from 1000 to 100
data = [
    np.abs(np.random.normal(0, 0.3, size)) for size in sizes
]  # Generate data with mean 0 and take absolute value

labels = [
    "QuAC",
    "NaturalQuestions - Open-book",
    "NaturalQuestions - Closed-book",
    "NarrativeQA",
    "CNN/DailyMail",
    "XSum",
]

# Adjusting the data and labels for the second histogram
# Modifying data to represent a different distribution and adjusting labels to reflect changes
modified_sizes = np.linspace(300, 200, 6, dtype=int)  # Generate sizes from 300 to 200
modified_data = [
    np.abs(np.random.normal(0, 0.28, size)) for size in modified_sizes
]  # Increase variance to 0.5

modified_labels = [
    "Modified " + label for label in labels
]  # Prepend 'Modified ' to each original label
xlabels = ["Test Winning Distance", "Test Winning Distance"]
ylabels = ["Number of Pairs", "Number of Pairs"]
xlims = [[0, 1], [0, 1]]
xticks = [[0.0, 0.2, 0.4, 0.6, 0.8, 1.0], [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]]
binslist = [30, 30]


# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create a 1 x 2 subplot again for updated plots
fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(16, 7))

colors = ["#70d6ff", "#ff70a6", "#ff9770", "#ffd670", "#e9ff70", "#bfd6f4"]
# First subplot (original settings)
axs[0].hist(
    data,
    bins=binslist[0],
    stacked=True,
    edgecolor="black",
    linewidth=1.2,
    color=colors,
    label=labels,
)
axs[0].set_xlabel(xlabels[0])
axs[0].set_ylabel(ylabels[0])
axs[0].set_xlim(xlims[0])
axs[0].set_xticks(xticks[0])
axs[0].set_facecolor("white")
handles, labels = axs[0].get_legend_handles_labels()
handles = handles[::-1]
labels = labels[::-1]
axs[0].legend(handles, labels, loc="upper right")

# Second subplot (modified settings)
axs[1].hist(
    modified_data,
    bins=binslist[1],
    stacked=True,
    edgecolor="black",
    linewidth=1.2,
    color=colors,
    label=modified_labels,
)
axs[1].set_xlabel(xlabels[1])
axs[1].set_ylabel(ylabels[1])
axs[1].set_xlim(xlims[1])
axs[1].set_xticks(xticks[1])
axs[1].set_facecolor("white")
handles, labels = axs[1].get_legend_handles_labels()
handles = handles[::-1]
labels = labels[::-1]
axs[1].legend(handles, labels, loc="upper right")

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig("hist_17.pdf", bbox_inches="tight")
