# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Data for the plots
models = ["GRU4Rec", "Caser", "SASRec", "BERT4Rec", "FMLP-Rec"]
beauty_values = [14.3, 19.9, 2.4, 11.2, 2.2]
movielens_values = [3.1, 2.9, 4.1, 5.1, 3.0]
yelp_values = [19.7, -0.5, -0.5, 4.8, -0.7]

title1 = "Beauty"
axvline1 = 0
title2 = "MovieLens-1M"
axvline2 = 0
title3 = "Yelp"
axvline3 = 0

xticks1 = [0, 2.5, 5]
xticks2 = [0, 2.5, 5]
xticks3 = [0, 10, 20]

xlable = "▲%"


# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Set the figure size to match the original image's dimensions
fig, axes = plt.subplots(1, 3, figsize=(10, 4))

# Plot for Beauty
axes[0].barh(models, beauty_values, color="white", edgecolor="black")
axes[0].set_title(title1)
for i, v in enumerate(beauty_values):
    axes[0].text(
        v - 0.5 if v < 0 else v + 0.5,
        i,
        f"{v}%",
        color="black",
        va="center",
        ha="right" if v < 0 else "left",
    )
axes[0].axvline(axvline1, color="black")

# Plot for MovieLens-1M
axes[1].barh(models, movielens_values, color="white", edgecolor="black")
axes[1].set_title(title2)
for i, v in enumerate(movielens_values):
    axes[1].text(
        v - 0.2 if v < 0 else v + 0.2,
        i,
        f"{v}%",
        color="black" if v > 0 else "red",
        va="center",
        ha="right" if v < 0 else "left",
    )
axes[1].axvline(axvline2, color="black")
axes[1].set_xticks(xticks1)

# Plot for Yelp
axes[2].barh(models, yelp_values, color="white", edgecolor="black")
axes[2].set_title(title3)
for i, v in enumerate(yelp_values):
    axes[2].text(
        v - 0.5 if v < 0 else v + 0.5,
        i,
        f"{v}%",
        color="black" if v > 0 else "red",
        va="center",
        ha="right" if v < 0 else "left",
    )
axes[2].axvline(axvline3, color="black")
axes[2].set_xticks(xticks2)

# Hide all axes except the bottom one
for ax in axes:
    for spine in ["left", "right", "top"]:
        ax.spines[spine].set_visible(False)

# Hide y-axis labels for axes[1] and axes[2]
axes[1].set_yticks([])
axes[1].set_yticklabels([])
axes[2].set_yticks([])
axes[2].set_yticklabels([])

# Add x-axis label for all axes
for ax in axes:
    ax.set_xlabel(xlable)

plt.subplots_adjust(wspace=0.5)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig("bar_12.pdf", bbox_inches="tight")
