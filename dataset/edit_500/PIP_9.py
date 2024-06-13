import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
clusters = {
    "cluster_1": np.random.normal(loc=(2, -1), scale=1.2, size=(50, 2)),
    "cluster_2": np.random.normal(loc=(6, 6), scale=0.8, size=(30, 2)),
    "cluster_3": np.random.normal(loc=(-2, 3), scale=1, size=(40, 2)),
    "cluster_4": np.random.normal(loc=(7, -4), scale=1.1, size=(60, 2)),
    "cluster_5": np.random.normal(loc=(-4, -6), scale=0.9, size=(70, 2)),
    "cluster_6": np.random.normal(loc=(4, 9), scale=1.3, size=(45, 2)),
}

# Colors for each cluster (replace with actual colors)
colors = {
    "cluster_1": "cyan",
    "cluster_2": "magenta",
    "cluster_3": "lime",
    "cluster_4": "navy",
    "cluster_5": "brown",
    "cluster_6": "pink",
}

insetaxes = [0.25, 0.75, 0.25, 0.15]
insetxlim = [-1.5, 1.5]
insetylim = [-1, 2]
insetxticks = [-1.5, 0, 1.5]
insetyticks = [-1, 0.5, 2]
arrowstart = (-2, 8)
arrowend = (0.35, 0.55)
annotaterecx = [-1.5, 1.5]
annotaterecy = [-1, 2]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create the scatter plot
fig, ax = plt.subplots(figsize=(6, 6))
for cluster, data in clusters.items():
    ax.scatter(data[:, 0], data[:, 1], c=colors[cluster], alpha=0.5)

ax.plot([annotaterecx[0], annotaterecx[1]], [annotaterecy[1], annotaterecy[1]], color="black", lw=1)
ax.plot([annotaterecx[0], annotaterecx[1]], [annotaterecy[0], annotaterecy[0]], color="black", lw=1)
ax.plot([annotaterecx[0], annotaterecx[0]], [annotaterecy[0], annotaterecy[1]], color="black", lw=1)
ax.plot([annotaterecx[1], annotaterecx[1]], [annotaterecy[0], annotaterecy[1]], color="black", lw=1)

# Create the inset with the zoomed-in view
ax_inset = fig.add_axes(
    insetaxes
)  # Adjust the position to align with the right side of the main plot
for cluster, data in clusters.items():
    ax_inset.scatter(data[:, 0], data[:, 1], c=colors[cluster], alpha=0.5)
ax_inset.set_xlim(insetxlim)
ax_inset.set_ylim(insetylim)
ax_inset.set_xticks(insetxticks)
ax_inset.set_yticks(insetyticks)
ax_inset.spines["bottom"].set_color("black")  # Add black border to the inset
ax_inset.spines["left"].set_color("black")
ax_inset.spines["top"].set_color("black")
ax_inset.spines["right"].set_color("black")

ax.annotate(
    "",
    xy=arrowstart,
    xytext=arrowend,
    textcoords="axes fraction",
    arrowprops=dict(facecolor="black", lw=0.1),
)

# ===================
# Part 4: Saving Output
# ===================
# Show the plot
plt.tight_layout()
plt.savefig('PIP_9.pdf', bbox_inches='tight')
