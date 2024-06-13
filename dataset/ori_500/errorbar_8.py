# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data (estimated from the image)
models = [
    "BERT",
    "RoBERTa",
    "DistilBERT",
    "XLNet",
    "Electra",
    "Albert",
    "BART",
    "DeBERTa",
    "Llama2",
]
ground_truth_accuracy = [50, 55, 60, 65, 40, 30, 70, 45, 35]
weak_labels_accuracy = [45, 50, 55, 60, 35, 25, 65, 40, 30]
error = [10, 8, 12, 10, 5, 7, 8, 10, 5]
labels = ["Ground-truth labels", "Weak labels"]
ylabel = "Accuracy (%)"
ylim = [0, 80]
yticks = np.arange(0, 71, 10)


# ===================
# Part 3: Plot Configuration and Rendering
# ===================
fig = plt.subplots(figsize=(10, 3))
# Bar width
bar_width = 0.35

# X position of bars
r1 = np.arange(len(ground_truth_accuracy))
r2 = [x + bar_width for x in r1]

# Create bars
plt.bar(
    r1,
    ground_truth_accuracy,
    color="#d47e6d",
    width=bar_width,
    label=labels[0],
    yerr=error,
    capsize=7,
)
plt.bar(
    r2,
    weak_labels_accuracy,
    color="#76a4c5",
    width=bar_width,
    label=labels[1],
    yerr=error,
    capsize=7,
)

# Add xticks on the middle of the group bars
plt.xticks([r + bar_width / 2 for r in range(len(ground_truth_accuracy))], models)

# Create legend & Show graphic
plt.ylabel(ylabel)
plt.legend(frameon=False, loc="upper right")  # Remove legend background

# Set background color and grid
plt.gca().set_facecolor("#e5e5e5")
plt.grid(color="white", linestyle="-", linewidth=0.25, axis="both")
plt.gca().set_axisbelow(True)

# Set y-axis limits
plt.ylim(ylim)
plt.yticks(yticks)

for spine in plt.gca().spines.values():
    spine.set_visible(False)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig("errorbar_8.pdf", bbox_inches="tight")
