# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)

# ===================
# Part 2: Data Preparation
# ===================
# Placeholder data
categories = [
    "BERT-Base",
    "RoBERTa-Large",
    "DistilBERT",
    "ALBERT-XXLarge",
    "T5-Large",
    "GPT-3",
    "GPT-Neo",
    "GPT-J",
    "GPT-4",
]

scores = {
    "SQuAD": [88.5, 90.2, 86.7, 89.4, 91.8, 93.6, 87.4, 88.9, 95.1],
    "MNLI": [84.1, 89.8, 82.7, 86.9, 89.3, 91.2, 85.4, 86.8, 94.0],
    "QNLI": [92.4, 94.3, 89.7, 91.5, 93.7, 95.2, 90.8, 92.1, 96.5],
    "RTE": [71.6, 79.1, 67.8, 75.4, 78.2, 83.6, 72.5, 73.9, 86.0],
    "CoLA": [60.3, 68.4, 58.6, 65.7, 70.2, 73.8, 61.7, 63.9, 78.4],
    "STS-B": [88.1, 91.5, 85.7, 90.1, 93.0, 94.5, 86.4, 88.7, 95.9],
    "MRPC": [87.5, 89.2, 85.1, 88.7, 90.8, 92.4, 86.9, 88.3, 93.6],
    "QQP": [89.8, 91.3, 87.4, 90.6, 92.7, 94.1, 88.2, 89.9, 96.0],
    "BoolQ": [76.4, 80.3, 73.9, 78.5, 82.0, 85.6, 77.1, 78.4, 88.9],
}

ylim = [50, 100]
ylabel = "Performance Score (%)"
yticks = [50, 60, 70, 80, 90, 100]
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
plt.figure(figsize=(10, 8))

# Create subplots for each category
n_rows = 3
n_cols = 3
subplot_idx = 1
for category, score in scores.items():
    ax = plt.subplot(n_rows, n_cols, subplot_idx)
    subplot_idx += 1

    # Create bar chart
    x = np.arange(len(categories))
    ax.bar(
        x,
        score,
        color=[
            "#697ac7",
            "#8598dd",
            "#a0b4eb",
            "#cdd7ea",
            "#dddcdc",
            "#e5d1c5",
            "#e5d1c5",
            "#e5beaa",
            "#dba38d",
            "#c98371",
            "#b25f55",
        ],
    )

    # Add data labels
    for j, val in enumerate(score):
        ax.text(j, val + 1, f"{val}", ha="center", va="bottom", fontsize=6)

    # Set title and labels
    ax.set_title(category)
    ax.set_xticks(x)
    ax.set_xticklabels(categories, rotation=45, ha="right", fontsize=6)
    ax.set_ylim(ylim)
    ax.set_ylabel(ylabel)
    ax.set_yticks(yticks)

    plt.tick_params(axis="both", which="both", length=0)

    # Add y grid
    plt.gca().yaxis.grid(True)
    plt.gca().set_axisbelow(True)

    ax = plt.gca()
    ax.spines["top"].set_color("gray")
    ax.spines["right"].set_color("gray")
    ax.spines["bottom"].set_color("gray")
    ax.spines["left"].set_color("gray")

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout
plt.tight_layout()
plt.savefig('bar_43.pdf', bbox_inches='tight')
