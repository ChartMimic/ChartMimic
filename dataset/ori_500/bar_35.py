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
methods = ["Random", "Uniform", "G2S", "S2G", "ClusterClip"]
scores_llama2 = [5.52, 5.53, 5.83, 5.54, 5.84]
scores_mistral = [6.57, 6.75, 6.81, 7.08, 6.90]

index = [6, 12]

# Colors (approximated from the image)
colors = ["#837ba8", "#aa6262", "#6e9d72", "#c38c6a", "#5e74a0"]

# Labels for legend and plot type
labels = methods
# Limits, labels, and title for the plot
ylim_values = (5.0, 7.5)
ylabel_value = "MT-Bench Score"
xticks_values = index
xtickslabel_values = ["Llama2", "Mistral"]
# Bar width
bar_width = 1
# X-axis positions
r1 = np.arange(len(methods))
r2 = [x + bar_width + len(r1) for x in r1]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
plt.figure(figsize=(8, 5))
# Create bars
for i in range(len(r1)):
    plt.bar(
        index[0] + (i - 2) * bar_width,
        scores_llama2[i],
        color=colors[i],
        width=bar_width,
        edgecolor="white",
        label=labels[i],
    )

for i in range(len(r2)):
    plt.bar(
        index[1] + (i - 2) * bar_width,
        scores_mistral[i],
        color=colors[i],
        width=bar_width,
        edgecolor="white",
    )

# Add text on top of the bars
for i in range(len(r1)):
    plt.text(
        index[0] + (i - 2) * bar_width,
        scores_llama2[i] + 0.05,
        str(scores_llama2[i]),
        ha="center",
    )
    plt.text(
        index[1] + (i - 2) * bar_width,
        scores_mistral[i] + 0.05,
        str(scores_mistral[i]),
        ha="center",
    )

# General layout
plt.xticks(xticks_values, xtickslabel_values)
plt.ylabel(ylabel_value)
plt.ylim(*ylim_values)
plt.legend(loc="upper center", ncol=5, bbox_to_anchor=(0.5, 1.1), frameon=False)

plt.tick_params(axis="x", which="both", length=0)
plt.gca().yaxis.grid(True)
plt.gca().set_axisbelow(True)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig("bar_35.pdf", bbox_inches="tight")
