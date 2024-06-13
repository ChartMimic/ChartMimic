import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Sample data (replace with actual values from the image)
data = {
    "Mean": np.random.rand(6, 6) * 3 + 2,
}

labels = [
    "Urban Population",
    "Rural Population",
    "Suburban Population",
    "Migration Rate",
    "Birth Rate",
    "Death Rate",
]
xlim=[2, 5]
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
fig, ax = plt.subplots(figsize=(5, 5), constrained_layout=True)
colors = ["#d1af8e", "#d09dca", "#d48b4f", "#65b598", "#5894c2", "#deae57"]
bplot = ax.boxplot(
    data["Mean"],
    vert=False,
    patch_artist=True,
    showcaps=False,
    showfliers=False,
    whiskerprops=dict(color="black", linestyle="-", linewidth=0),
    medianprops={"color": "black"},
    boxprops=dict(linestyle="-", linewidth=0),
)
for patch, color in zip(bplot["boxes"], colors):
    patch.set_facecolor(color)
ax.set_title("Mean")
ax.set_yticklabels(labels)
ax.set_xlim(xlim)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.xaxis.grid(True, alpha=0.7)
ax.set_axisbelow(True)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig('box_16.pdf', bbox_inches='tight')
