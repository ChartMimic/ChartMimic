# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Generate random bimodal data with different distributions for each plot
data1_milk = np.concatenate(
    [np.random.normal(3, 0.5, 700), np.random.normal(1, 0.3, 300)]
)
data2_milk = np.concatenate(
    [np.random.normal(2.5, 0.4, 500), np.random.normal(1.5, 0.2, 500)]
)

data1_dark = np.concatenate(
    [np.random.normal(2, 0.2, 600), np.random.normal(1, 0.3, 400)]
)
data2_dark = np.concatenate(
    [np.random.normal(1.8, 0.5, 700), np.random.normal(1.2, 0.25, 300)]
)

data1_white = np.concatenate(
    [np.random.normal(3.5, 0.6, 500), np.random.normal(1.5, 0.3, 500)]
)
data2_white = np.concatenate(
    [np.random.normal(3, 0.5, 700), np.random.normal(2, 0.25, 300)]
)

data1_ruby = np.concatenate(
    [np.random.normal(2.8, 0.3, 400), np.random.normal(1.2, 0.35, 600)]
)
data2_ruby = np.concatenate(
    [np.random.normal(2.4, 0.4, 500), np.random.normal(0.8, 0.2, 500)]
)
binslist = [30, 30]
labels = ["Swiss", "New Zealand"]
xlabel = "Sweetness"
ylabel = "Density"
titles = [
    "(a) Milk Chocolate",
    "(b) Dark Chocolate",
    "(c) White Chocolate",
    "(d) Ruby Chocolate",
]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create the plots
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Plot histograms for each subplot
datasets = [
    (data1_milk, data2_milk),
    (data1_dark, data2_dark),
    (data1_white, data2_white),
    (data1_ruby, data2_ruby),
]
for (data1, data2), ax in zip(datasets, axs.flatten()):
    ax.hist(
        data1,
        bins=binslist[0],
        density=True,
        alpha=0.6,
        color="deepskyblue",
        label=labels[0],
        edgecolor="black",
        linewidth=0.5,
    )
    ax.hist(
        data2,
        bins=binslist[1],
        density=True,
        alpha=0.6,
        color="orangered",
        label=labels[1],
        edgecolor="black",
        linewidth=0.5,
    )
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(True)
    ax.legend()

# Set titles for each subplot
axs[0, 0].set_title(titles[0])
axs[0, 1].set_title(titles[1])
axs[1, 0].set_title(titles[2])
axs[1, 1].set_title(titles[3])

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save the figure
plt.tight_layout()
plt.savefig("hist_20.pdf", bbox_inches="tight")
