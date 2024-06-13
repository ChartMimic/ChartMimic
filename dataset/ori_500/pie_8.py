# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data to plot
labels = ["NAACL", "EMNLP", "ACL", "COLING", "EACL"]
sizes = [25.4, 20.3, 34.7, 12.2, 7.4]
colors = plt.cm.Paired(np.linspace(0, 1, len(sizes)))
explode = (0, 0, 0.1, 0, 0)  # only "explode" the 3rd slice (Instagram)
title = "NLP Conference Influence"
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plot setup
fig, ax = plt.subplots(figsize=(6, 6))
wedges, texts, autotexts = ax.pie(
    sizes,
    explode=explode,
    colors=colors,
    autopct="%1.1f%%",
    shadow=False,
    startangle=140,
)

# Adding annotations
bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
kw = dict(arrowprops=dict(arrowstyle="-"), bbox=bbox_props, zorder=0, va="center")

for i, p in enumerate(wedges):
    ang = (p.theta2 - p.theta1) / 2.0 + p.theta1
    y = np.sin(np.deg2rad(ang))
    x = np.cos(np.deg2rad(ang))
    horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
    connectionstyle = "angle,angleA=0,angleB={}".format(ang)
    kw["arrowprops"].update({"connectionstyle": connectionstyle})
    ax.annotate(
        labels[i],
        xy=(x, y),
        xytext=(1.35 * np.sign(x), 1.2 * y),
        horizontalalignment=horizontalalignment,
        **kw
    )

# Title and equal axis
ax.set_title(title, fontsize=16, x=0.5, y=1)

# ===================
# Part 4: Saving Output
# ===================
# Show plot
plt.tight_layout()
plt.savefig('pie_8.pdf', bbox_inches='tight')
