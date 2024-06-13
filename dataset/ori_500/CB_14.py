# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Sample data (replace with actual data)
norm_size_blue = np.random.normal(0.9, 0.2, 1000)
norm_size_pink = np.random.normal(0.9, 0.2, 1000) - 0.4

min_bin = min(min(norm_size_blue), min(norm_size_pink))
max_bin = max(max(norm_size_blue), max(norm_size_pink))

bins = np.linspace(min_bin, max_bin, 30)
bin_width = bins[1] - bins[0]
labels = ["H-ward - centers-cos", "random"]
legend_title = "selector"
title = "summarization_xsum:temperature=0.3,device=cuda"
xlabel = "norm size"
ylabel = "count"
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
figure = plt.figure(figsize=(10, 6))

# Create histogram
count_blue, bins_blue, _ = plt.hist(
    norm_size_blue,
    bins=bins,
    color="#a7c4f2",
    alpha=0.7,
    label=labels[0],
    edgecolor="black",
    linewidth=1.25,
)
count_pink, bins_pink, _ = plt.hist(
    norm_size_pink,
    bins=bins,
    alpha=0.7,
    color="#fdabd2",
    label=labels[1],
    edgecolor="black",
    linewidth=1.25,
)

# Create line plot on top of the histogram and set edge color
plt.plot(bins_blue[:-1] + bin_width * 0.5, count_blue, color="#568ce6", linewidth=1.5)
plt.plot(bins_pink[:-1] + bin_width * 0.5, count_pink, color="#fc5fa9", linewidth=1.5)

# Add legend, title, and labels
plt.legend(loc="upper left", title=legend_title)
plt.title(title)
plt.xlabel(xlabel)
plt.ylabel(ylabel)

# ===================
# Part 4: Saving Output
# ===================
# Show plot with tight layout
plt.tight_layout()
plt.savefig("CB_14.pdf", bbox_inches="tight")
