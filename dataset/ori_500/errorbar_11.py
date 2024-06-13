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
hospitals = ["Hospital 1", "Hospital 2", "Hospital 3"]
baseline1 = [0.748, 0.762, 0.709]
baseline2 = [0.715, 0.748, 0.687]
fedmm = [0.759, 0.780, 0.713]
error = [0.05, 0.04, 0.06]

# Bar positions
x = np.arange(len(hospitals))
width = 0.25
labels = ["Baseline 1", "Baseline 2", "FedMM"]
ylabel = "Accuracy"
title = "Accuracy by hospital and method"
ylim = [0.5, 0.95]


# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plotting
fig, ax = plt.subplots(figsize=(8, 5))
bars1 = ax.bar(
    x - width,
    baseline1,
    width,
    label=labels[0],
    color="lightskyblue",
    hatch="\\",
    yerr=error,
    capsize=5,
    error_kw=dict(ecolor="black"),
)
bars2 = ax.bar(
    x,
    baseline2,
    width,
    label=labels[1],
    color="lightsalmon",
    hatch="//",
    yerr=error,
    capsize=5,
    error_kw=dict(ecolor="black"),
)
bars3 = ax.bar(
    x + width,
    fedmm,
    width,
    label=labels[2],
    color="palegreen",
    hatch="o",
    yerr=error,
    capsize=5,
    error_kw=dict(ecolor="black"),
)

# Adding text for labels, title, and custom x-axis tick labels
ax.set_ylabel(ylabel)
ax.set_title(title)
ax.set_xticks(x)
ax.set_xticklabels(hospitals)
ax.set_ylim(ylim)  # Adjust y-axis scale to match reference picture
ax.legend(loc="upper center", ncol=3)  # Move legend to match reference picture


# Adding the data labels on the bars
def add_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(
            "{}".format(round(height, 3)),
            xy=(
                bar.get_x() + bar.get_width() / 2,
                height + error[bars.index(bar)],
            ),  # Adjust label position to be above error bars
            xytext=(0, 3),  # 3 points vertical offset
            textcoords="offset points",
            ha="center",
            va="bottom",
        )


add_labels(bars1)
add_labels(bars2)
add_labels(bars3)

# ===================
# Part 4: Saving Output
# ===================
# Show the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig("errorbar_11.pdf", bbox_inches="tight")
