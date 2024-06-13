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
xlabel = "Test Winning Distance"
ylabel = "Number of Pairs"
xlim = [0, 1]
xticks = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
bins = 30

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Histogram plot
colors = ["#d4f5f4", "#ffffc2", "#dacdfb", "#f4bab6", "#b8eabd", "#bfd6f4"]

plt.figure(figsize=(8, 7))
plt.hist(
    data,
    bins=bins,
    stacked=True,
    edgecolor="black",
    linewidth=1.2,
    color=colors,
    label=labels,
)

# Set background color to white
ax = plt.gca()
ax.set_facecolor("white")

# Labels and title
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.xlim(xlim)
plt.xticks(xticks)
handles, labels = plt.gca().get_legend_handles_labels()

# Reverse handles and labels
handles = handles[::-1]
labels = labels[::-1]

plt.legend(handles, labels)

# ===================
# Part 4: Saving Output
# ===================
# Adjusting the plot to match the original image's dimensions
plt.tight_layout()
plt.savefig("hist_1.pdf", bbox_inches="tight")
