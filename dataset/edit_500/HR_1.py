import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Define the bubble sizes and colors for each task
bubble_sizes = {280: 500, 208: 450, 176: 400, 136: 300, 64: 150, 0: 20}
label2idx = {"Efficiency": 0, "Accuracy": 1, "Latency": 2, "Throughput": 3}
idx2label = {v: k for k, v in label2idx.items()}

bubble_sizes = {280: 500, 208: 450, 176: 400, 136: 300, 64: 150, 0: 20}
colors = {0: "#6a95c4", 1: "#88acc7", 2: "#adbca9", 3: "#e2b2a0"}
label2idx = {"Efficiency": 0, "Accuracy": 1, "Latency": 2, "Throughput": 3}
idx2label = {v: k for k, v in label2idx.items()}

data = {
    "Config-1": {
        "Efficiency": [176, 136, 64, 208],
        "Accuracy": [208, 64, 136, 176],
        "Latency": [64, 208, 176, 136],
        "Throughput": [136, 176, 208, 64],
    },
    "Config-2": {
        "Efficiency": [280, 208, 176, 136],
        "Accuracy": [176, 136, 64, 208],
        "Latency": [208, 64, 136, 176],
        "Throughput": [64, 280, 136, 176],
    },
    "Config-3": {
        "Efficiency": [136, 176, 208, 64],
        "Accuracy": [208, 280, 136, 176],
        "Latency": [64, 176, 280, 208],
        "Throughput": [176, 208, 64, 136],
    },
    "Config-4": {
        "Efficiency": [64, 136, 176, 208],
        "Accuracy": [136, 176, 208, 280],
        "Latency": [176, 64, 136, 208],
        "Throughput": [208, 176, 64, 136],
    },
}
title = "Performance Metrics"

colors = {0: "#6a95c4", 1: "#88acc7", 2: "#adbca9", 3: "#e2b2a0"}
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create the subplots
fig, axs = plt.subplots(1, 4, figsize=(10, 3), sharey=True)

# Loop through each subplot and plot the data
for i, (title, tasks) in enumerate(data.items()):
    ax = axs[i % 4]
    ax.set_title(title)

    for task, values in tasks.items():
        ax.scatter(
            x=range(len(values)),
            y=[label2idx[task]] * len(values),
            s=[bubble_sizes[_] for _ in values],
            c=colors[label2idx[task]],
            label=task,
        )
        for j, v in enumerate(values):
            ax.text(j, label2idx[task], str(v), ha="center", va="center")
    ax.set_xticks(range(len(values)))
    ax.set_xticklabels([i for i in range(len(values))])
    ax.set_xlim(-0.5, len(values) - 0.5)
    ax.set_ylim(-0.5, len(label2idx) - 0.5)
    ax.set_yticks([])
    ax.set_xlabel("Client")

# Add the legend
handles, labels = axs[0].get_legend_handles_labels()

# set the title 'task' of legend to the left of the legend
fig.legend(
    handles,
    labels,
    loc="lower center",
    ncol=4,
    markerscale=0.5,
    fontsize="small",
    bbox_to_anchor=(0.5, -0.1),
    title=title,
    title_fontsize="small",
)

# ===================
# Part 4: Saving Output
# ===================
# Adjust the layout and save the plot
plt.tight_layout()
plt.savefig('HR_1.pdf', bbox_inches='tight')
