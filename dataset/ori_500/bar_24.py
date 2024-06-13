# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data
models = [
    "Majority",
    "Flan-T5",
    "GPT-3.5",
    "GPT-4",
    "Wizard13b",
    "Vicuna13b",
    "Vicuna33b",
    "Mistral17b",
]
accuracy = [0.302, 0.601, 0.468, 0.653, 0.384, 0.379, 0.347, 0.364]
colors = [
    "#3f5e8a",
    "#41778c",
    "#478f8c",
    "#51a686",
    "#69bd78",
    "#8fcf63",
    "#c4de50",
    "#fae856",
]
xlabel = "Models"
xticks = np.arange(len(models))
ylabel = "Accuracy"
ylim = [0, 1.0]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create figure and bar chart
fig, ax = plt.subplots(figsize=(8, 4))
bars = ax.bar(models, accuracy, color=colors)

# Add accuracy values on top of the bars
for bar in bars:
    yval = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        yval,
        round(yval, 3),
        ha="center",
        va="bottom",
    )

# Set axis labels and title
ax.set_ylabel(xlabel)
ax.set_xticks(xticks)
ax.set_xticklabels(models, rotation=45, ha="center")
ax.set_xlabel(ylabel)

ax.set_ylim(ylim)

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig("bar_24.pdf", bbox_inches="tight")
