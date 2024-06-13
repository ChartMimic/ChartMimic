# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# ===================
# Part 2: Data Preparation
# ===================
# Data for the plots
models = ["GRU4Rec", "Caser", "SASRec", "BERT4Rec", "FMLP-Rec"]
beauty_values = [10, -5, 6, 8, -5]
movielens_values = [3.1, 2.9, -4.1, 5.1, 3.0]
yelp_values = [1.7, -0.5, -0.5, 4.8, -0.7]
more_values = [19.7, -3, -10, 4.8, -6]
titles = ["Beauty", "MovieLens-1M", "Yelp", "More"]
xticks = [[-10, 0, 10], [-6, 0, 6], [-5, 0, 5], [-20, 0, 20]]
xlabel = "▲%"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Set the figure size to match the original image's dimensions
fig, axes = plt.subplots(2, 2, figsize=(10, 8), sharey=True)

# Plot for Beauty
axes[0][0].barh(models, beauty_values, color="white", hatch="+", edgecolor="black")
axes[0][0].set_title(titles[0])
for i, v in enumerate(beauty_values):
    axes[0][0].text(
        v - 0.5 if v < 0 else v + 0.5,
        i,
        f"{v}%",
        color="black",
        va="center",
        ha="right" if v < 0 else "left",
    )
axes[0][0].axvline(0, color="black")
axes[0][0].set_xticks(xticks[0])

# Plot for MovieLens-1M
axes[0][1].barh(models, movielens_values, color="white", edgecolor="black")
axes[0][1].set_title(titles[1])
for i, v in enumerate(movielens_values):
    axes[0][1].text(
        v - 0.2 if v < 0 else v + 0.2,
        i,
        f"{v}%",
        color="black" if v > 0 else "red",
        va="center",
        ha="right" if v < 0 else "left",
    )
axes[0][1].axvline(0, color="black")
axes[0][1].set_xticks(xticks[1])

# Plot for Yelp
axes[1][0].barh(models, yelp_values, color="white", edgecolor="black")
axes[1][0].set_title(titles[2])
for i, v in enumerate(yelp_values):
    axes[1][0].text(
        v - 0.5 if v < 0 else v + 0.5,
        i,
        f"{v}%",
        color="black" if v > 0 else "red",
        va="center",
        ha="right" if v < 0 else "left",
    )
axes[1][0].axvline(0, color="black")
axes[1][0].set_xticks(xticks[2])

# Plot for More
axes[1][1].barh(models, more_values, color="white", hatch="//", edgecolor="black")
axes[1][1].set_title(titles[3])
for i, v in enumerate(more_values):
    axes[1][1].text(
        v - 0.5 if v < 0 else v + 0.5,
        i,
        f"{v}%",
        color="black" if v > 0 else "red",
        va="center",
        ha="right" if v < 0 else "left",
    )
axes[1][1].axvline(0, color="black")
axes[1][1].set_xticks(xticks[3])

# Hide all axes except the bottom one
for i in range(2):
    for j in range(2):
        axes[i][j].set_xlabel(xlabel)
        for spine in ["left", "right", "top"]:
            axes[i][j].spines[spine].set_visible(False)

# Hide y-axis labels for axes[0][1] and axes[1][1]
axes[0][1].set_yticks([])
axes[0][1].set_yticklabels([])
axes[1][1].set_yticks([])
axes[1][1].set_yticklabels([])

plt.subplots_adjust(wspace=0.5)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig("bar_87.pdf", bbox_inches="tight")
