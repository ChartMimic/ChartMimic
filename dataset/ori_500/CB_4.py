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
methods = [
    "Linear probing",
    "BitFit",
    "Prompt Tuning",
    "Full finetuning",
    "LoRA",
    "Ours (LoSA)",
]
train_sec_img = [0.2, 0.4, 0.6, 1.0, 0.5, 0.25]
inference_GFLOPs = [1.0, 1.0, 1.0, 1.0, 1.2, 0.9]
param_log10 = [0.3, 0.7, 1.4, 1.0, 0.75, 0.75]
train_memory = [0.6, 0.5, 1.8, 1.0, 0.5, 0.5]
accuracy = [72, 76, 78, 82, 80, 81]
labels = ["Train sec / img", "Inference GFLOPs", "Param, log10", "Train Memory"]
x_name = "Methods"
bar_name = "Normalized Requirements (lower is better)"
line_name = "Accuracy, iNaturalist 2021"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Set figure size to match original image's dimensions
fig, ax1 = plt.subplots(figsize=(10, 5))

# Bar plot
bar_width = 0.2
index = np.arange(len(methods))
bar1 = ax1.bar(index, train_sec_img, bar_width, label=labels[0], color="#3b76af")
bar2 = ax1.bar(
    index + bar_width,
    inference_GFLOPs,
    bar_width,
    label=labels[1],
    color="#ef8636",
)
bar3 = ax1.bar(
    index + 2 * bar_width, param_log10, bar_width, label=labels[2], color="#529e3f"
)
bar4 = ax1.bar(
    index + 3 * bar_width,
    train_memory,
    bar_width,
    label=labels[3],
    color="#c53a32",
)

# Line plot
ax2 = ax1.twinx()
line = ax2.plot(
    index + bar_width + bar_width / 2,
    accuracy,
    label="Accuracy",
    color="black",
    marker="o",
    markersize=14,
    linewidth=2,
    markeredgecolor="white",
)

# Labels, title and legend
ax1.set_xlabel(x_name, fontsize=12)
ax1.set_ylabel(bar_name, fontsize=12)
ax1.set_xticks(index + bar_width + bar_width / 2)
ax1.set_xticklabels(methods, fontsize=12)
ax1.legend(loc="upper left")
ax2.legend(loc="upper right")
ax2.set_ylabel(line_name, fontsize=12)

ax1.tick_params(axis="y", labelsize=12)
ax2.tick_params(axis="y", labelsize=12)

# ===================
# Part 4: Saving Output
# ===================
# Show plot
plt.tight_layout()
plt.savefig("CB_4.pdf", bbox_inches="tight")
