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
datasets = ["VOC 2012", "COCO 2017"]
jpeg = [3.1, 1.5]
deepjscc = [1.5, 2.5]
ours = [0.5, 1.0]

# X-axis positions
x = np.arange(len(datasets))

# Bar width
width = 0.2
labels = ["JPEG", "DEEPJSCC w/ ofdm", "OURS"]
ylim = [0, 4.3]
ylabel = "Transmission Delay (ms)"
xlabel = "Datasets"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plotting
fig, ax = plt.subplots(
    figsize=(6, 5)
)  # Adjusting figure size to match the original image's dimensions
ax.bar(
    x - width, jpeg, width, label=labels[0], hatch="//", edgecolor="black", color="white"
)
ax.bar(
    x,
    deepjscc,
    width,
    label=labels[1],
    hatch="..",
    edgecolor="black",
    color="white",
)
ax.bar(
    x + width, ours, width, label=labels[2], hatch="xx", edgecolor="black", color="white"
)

# Labels and Title
ax.set_ylim(ylim)
ax.set_ylabel(ylabel)
ax.set_xlabel(xlabel)
ax.set_xticks(x)
ax.set_xticklabels(datasets)
ax.legend(loc="upper left")

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig("bar_28.pdf", bbox_inches="tight")
