# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Placeholder data
categories = [
    "LSTM-2-730b",
    "Mistral-7b-v0.1",
    "Mixtral-8x7b-v0.1",
    "Yi-34b",
    "Zephyr-7b-beta",
    "Qwen-72b",
    "Meditron-70b",
    "Med-PaLM",
    "Med-PaLM 2",
    "GPT-4",
    "Gemini Pro",
]
scores = {
    "MedMCQA": [48.1, 48.0, 57.2, 59.3, 45.9, 64.9, 48.4, 57.6, 72.3, 79.1, 54.3],
    "MedQA (USMLE)": [56.0, 50.8, 62.2, 64.4, 51.7, 64.4, 58.0, 67.6, 86.5, 90.2, 58.0],
    "PubMedQA": [74.4, 75.8, 76.8, 77.4, 76.8, 79.0, 76.2, 79.0, 81.8, 82.0, 70.7],
    "MMLU Anatomy": [55.6, 56.3, 70.4, 75.6, 58.5, 71.1, 54.1, 63.7, 84.4, 89.6, 66.7],
    "MMLU Clinical knowledge": [
        70.2,
        69.4,
        79.2,
        77.7,
        64.2,
        82.3,
        67.9,
        80.4,
        88.7,
        95.8,
        76.7,
    ],
    "MMLU College biology": [
        78.5,
        68.8,
        84.0,
        86.1,
        66.7,
        94.8,
        78.5,
        88.9,
        95.8,
        93.2,
        88.0,
    ],
    "MMLU College medicine": [
        68.8,
        57.8,
        67.6,
        69.4,
        61.3,
        78.6,
        63.6,
        76.3,
        83.2,
        89.0,
        69.2,
    ],
    "MMLU Medical genetics": [
        72.0,
        71.0,
        76.0,
        90.0,
        66.0,
        82.0,
        76.0,
        75.0,
        92.0,
        93.0,
        75.8,
    ],
    "MMLU Medical genetics": [
        72.0,
        71.0,
        76.0,
        90.0,
        66.0,
        82.0,
        76.0,
        75.0,
        92.0,
        93.0,
        75.8,
    ],
    "MMLU Professional medicine": [
        76.8,
        68.8,
        79.8,
        80.9,
        65.4,
        83.1,
        74.3,
        83.8,
        95.2,
        95.2,
        77.7,
    ],
}

ylim = [40, 100]
ylabel = "Performance Score (%)"
yticks = [40, 50, 60, 70, 80, 90, 100]

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
plt.savefig("bar_43.pdf", bbox_inches="tight")
