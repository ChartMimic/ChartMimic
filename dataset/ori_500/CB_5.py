# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Fixing random state for reproducibility
# some random data
x = np.random.rand(300)
y = np.random.rand(300)
xlabel = "TM-score"
ylabel = "Seq-ident"
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Start with a square Figure.
fig = plt.figure(figsize=(6, 6))
# Add a gridspec with two rows and two columns and a ratio of 1 to 4 between
# the size of the marginal axes and the main axes in both directions.
# Also adjust the subplot parameters for a square plot.
gs = fig.add_gridspec(
    2,
    2,
    width_ratios=(4, 1),
    height_ratios=(1, 4),
    left=0.1,
    right=0.9,
    bottom=0.1,
    top=0.9,
    wspace=0.0,
    hspace=0.0,
)
# Create the Axes.
ax = fig.add_subplot(gs[1, 0])
ax_histx = fig.add_subplot(gs[0, 0], sharex=ax)
ax_histy = fig.add_subplot(gs[1, 1], sharey=ax)

# Draw the scatter plot and marginals.
# no labels
ax_histx.tick_params(axis="x", labelbottom=False)
ax_histy.tick_params(axis="y", labelleft=False)

# the scatter plot:
ax.scatter(x, y, color="#3b76af", alpha=0.6)

# now determine nice limits by hand:
binwidth = 0.05
xymax = max(np.max(np.abs(x)), np.max(np.abs(y)))
lim = (int(xymax / binwidth) + 1) * binwidth

bins = np.arange(0, lim + binwidth, binwidth)
ax_histx.hist(x, bins=bins, color="white", edgecolor="#3b76af")
ax_histy.hist(
    y, bins=bins, orientation="horizontal", color="white", edgecolor="#3b76af"
)

# remove the y-axis labels
ax_histx.set_yticks([])
ax_histy.set_xticks([])

# remove the top, left, and right spines
ax_histx.spines["top"].set_visible(False)
ax_histx.spines["left"].set_visible(False)
ax_histx.spines["right"].set_visible(False)
ax_histy.spines["top"].set_visible(False)
ax_histy.spines["bottom"].set_visible(False)
ax_histy.spines["right"].set_visible(False)

ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig("CB_5.pdf", bbox_inches="tight")
