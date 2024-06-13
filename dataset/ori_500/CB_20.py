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
x = np.random.rand(100) * 0.8 + 0.2
y = np.random.rand(100)
line_x = [0.3, 0.6, 0.7, 0.9, 1.0]
line_y = [0.05, 0.1, 0.15, 0.50, 0.75]
scatter_name = "Subgroups"
line_name = "Calibration curve"
xlabel = "redicted probability"
ylabel = "Fraction of positives"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Start with a square Figure.
fig = plt.figure(figsize=(6, 6))
gs = fig.add_gridspec(
    2,
    1,
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

# Draw the scatter plot and marginals.
# no labels
ax_histx.tick_params(axis="x", labelbottom=False)

# the scatter plot:
ax.scatter(x, y, color="#e3b388", edgecolor="white", s=50, label=scatter_name)

# add a line on ax
ax.plot(
    line_x,
    line_y,
    color="black",
    linewidth=2,
    marker="o",
    markersize=6,
    label=line_name,
)

# draw a diagonal line
ax.plot([0, 1], [0, 1], color="black", linestyle="--")

# now determine nice limits by hand:
binwidth = 0.05
xymax = max(np.max(np.abs(x)), np.max(np.abs(y)))
lim = (int(xymax / binwidth) + 1) * binwidth
bins = np.arange(0, lim + binwidth, binwidth)
ax_histx.hist(x, bins=bins, color="#d6a3b3", edgecolor="black")

# remove the y-axis labels
ax_histx.set_yticks([])

# remove the top, left, and right spines
ax_histx.spines["top"].set_visible(False)
ax_histx.spines["left"].set_visible(False)
ax_histx.spines["right"].set_visible(False)

ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)

ax.set_xticks([0.00, 0.25, 0.50, 0.75, 1.00])
ax.set_yticks([0.00, 0.25, 0.50, 0.75, 1.00])
ax.set_xlim(-0.05, 1.05)
ax.set_ylim(-0.05, 1.05)

ax.legend(loc="upper left")

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig("CB_20.pdf", bbox_inches="tight")
