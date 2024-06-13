# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
clusters = {
    "cluster_1": np.random.normal(loc=(0, 2), scale=1, size=(50, 2)),
    "cluster_2": np.random.normal(loc=(5, 5), scale=1, size=(30, 2)),
    "cluster_3": np.random.normal(loc=(-3, 0), scale=1, size=(40, 2)),
    "cluster_4": np.random.normal(loc=(5, -5), scale=1, size=(60, 2)),
    "cluster_5": np.random.normal(loc=(-5, -5), scale=1, size=(70, 2)),
    "cluster_6": np.random.normal(loc=(5, 10), scale=1, size=(45, 2)),
}

# Colors for each cluster (replace with actual colors)
colors = {
    "cluster_1": "red",
    "cluster_2": "blue",
    "cluster_3": "green",
    "cluster_4": "purple",
    "cluster_5": "orange",
    "cluster_6": "yellow",
}
insetaxes=[0.2, 0.7, 0.3, 0.2]
insetxlim=[-2, 0]
insetylim=[-0.5, 1.5]
insetxticks=[-2.0, -1.0, 0]
insetyticks=[-0.5, 0.5, 1.5]
arrowstart=(-3.0, 6.0)
arrowend=(0.38, 0.5)
annotaterecx = [-2, 0]
annotaterecy = [-0.5, 1.5]

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
