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
resolutions = ["224", "128", "64", "32"]
imagenet_1k = [82, 60, 40, 35]
imagenet_f = [59, 50, 30, 10]
pac_fno_imagenet_1k = [0, 2, 10, 30]
pac_fno_imagenet_f = [5, 10, 20, 20]

labels = ["ImageNet-1k", "PAC-FNO", "ImageNet (F)", "PAC-FNO"]
xlabel = "Resolutions"
ylabel = "Top-1 Acc. (%)"
title = "Top-1 Accuracy by Resolution and Method"
yaxhline = 82
ylim = [0, 90]
yticks = np.arange(0, 100, 20)

# Bar width
bar_width = 0.2

# Positions of bars on x-axis
ind = np.arange(len(resolutions))

texts = ["29%", "29%", "87%", "180%"]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Figure size
plt.figure(figsize=(8, 6))

# Plotting
plt.bar(ind, imagenet_1k, width=bar_width, label=labels[0], color="#65bae7")
plt.bar(
    ind,
    pac_fno_imagenet_1k,
    width=bar_width,
    label=labels[1],
    color="#acdcf2",
    hatch="//",
    bottom=imagenet_1k,
)
plt.bar(
    ind + bar_width, imagenet_f, width=bar_width, label=labels[2], color="#eaa86b"
)
plt.bar(
    ind + bar_width,
    pac_fno_imagenet_f,
    width=bar_width,
    label=labels[3],
    color="#f4d3b4",
    hatch="/",
    bottom=imagenet_f,
)
# Highlighting the most significant improvement
distance = 0.05
plt.annotate(
    "",
    xy=(ind[0] + bar_width, 59),
    xytext=(ind[0] + bar_width, 82),
    arrowprops=dict(facecolor="black", shrink=0.02),
)
plt.text(ind[0] + bar_width + distance, 70, texts[0])
plt.annotate(
    "",
    xy=(ind[3], 35),
    xytext=(ind[3], 82),
    arrowprops=dict(facecolor="black", shrink=0.02),
    va="center",
)
plt.text(ind[3] - distance * 6, 70, texts[1])
plt.annotate(
    "",
    xy=(ind[3] + bar_width, 10),
    xytext=(ind[3] + bar_width, 82),
    arrowprops=dict(facecolor="black", shrink=0.02),
)
plt.text(ind[3] + bar_width + distance, 70, texts[2])
plt.annotate(
    "",
    xy=(ind[3] + bar_width * 2, 30),
    xytext=(ind[3] + bar_width * 2, 10),
    arrowprops=dict(facecolor="red", shrink=0.02),
    ha="center",
)
plt.text(ind[3] + bar_width * 2 + distance, 20, texts[3])
plt.axhline(y=yaxhline, color="blue", linestyle="--", linewidth=2)
# X-axis labels
plt.xticks(ind + bar_width / 2, resolutions)

# Y-axis labels
plt.ylim(ylim)
plt.yticks(yticks)

# Legend
plt.legend(loc="upper center", bbox_to_anchor=(0.5, 1.2), ncol=2)

# Grid lines
plt.grid(axis="y")

# Labels and Title
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.title(title)

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig("bar_49.pdf", bbox_inches="tight")
