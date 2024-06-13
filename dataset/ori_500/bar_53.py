# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data for plotting
words = [
    "small",
    "certain",
    "little",
    "fraction",
    "limited",
    "a",
    "day",
    "few",
    "new",
    "specific",
    "substantial",
    "tiny",
    "very",
    "single",
    "slight",
    "relatively",
    "moderate",
    "handful",
    "low",
]
human_distribution = [
    0.19,
    0.18,
    0.15,
    0.1,
    0.05,
    0.03,
    0.16,
    0.08,
    0.04,
    0.06,
    0.02,
    0.01,
    0.05,
    0.03,
    0.02,
    0.01,
    0.04,
    0.02,
    0.01,
]
model_distribution = [
    0.1,
    0.08,
    0.06,
    0.04,
    0.02,
    0.14,
    0.12,
    0.1,
    0.08,
    0.06,
    0.04,
    0.02,
    0.01,
    0.03,
    0.02,
    0.01,
    0.03,
    0.02,
    0.01,
]

x = np.arange(len(words))  # the label locations
labels = ["Human Distribution", "Model Distribution"]
ylabel = "Probability"
title = "Context: The human body can tolerate only a"
xlabel = "Word"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
fig, ax = plt.subplots(
    figsize=(10, 8)
)  # Adjust the figure size to match the original image's dimensions

# Create the bars
for i in range(len(words)):
    ax.bar(
        x[i],
        human_distribution[i],
        color="#FFA07A",
        label=labels[0] if i == 0 else "",
        hatch="///",
        edgecolor="black",
    )
    ax.bar(
        x[i],
        model_distribution[i],
        bottom=human_distribution[i],
        color="#87CEFA",
        label=labels[1] if i == 0 else "",
        alpha=0.5,
        hatch="..",
        edgecolor="black",
    )

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel(ylabel)
ax.set_title(title)
ax.set_xticks(x)
ax.set_xticklabels(words, rotation=90, ha="center")
ax.set_xlabel(xlabel)
ax.legend()

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout
plt.tight_layout()

plt.savefig("bar_53.pdf", bbox_inches="tight")
