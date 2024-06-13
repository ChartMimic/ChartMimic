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
algorithms = ["GD", "GD w. SA", "ITFR w/o SA", "ITFR"]
accuracy_movielens = [0.355, 0.360, 0.365, 0.360]
unfairness_movielens = [0.10, 0.08, 0.06, 0.08]
accuracy_tenrec = [0.175, 0.180, 0.185, 0.180]
unfairness_tenrec = [0.125, 0.100, 0.075, 0.100]
colors = ["#736aa6", "#983530", "#f2bf42", "#5384ed"]
labels = ["Accuracy", "Unfairness"]

# X-axis positions
x = np.arange(len(algorithms))
indexs = [2, 4]

# Plot labels
movielens_title = "(a) Movielens"
tenrec_title = "(b) Tenrec"
ylabel_movielens = "NDCG@20"
ylabel_tenrec = "CV@20"
yticks_movielens = [0, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40]
yticks_tenrec = [0, 0.02, 0.04, 0.06, 0.08, 0.10, 0.12, 0.14, 0.16, 0.18, 0.20]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(5, 6))

barwidth = 0.3
# Movielens subplot
for i in range(len(x)):
    ax1.bar(
        (i - 2) * 0.3 + indexs[0],
        accuracy_movielens[i],
        width=0.3,
        label="Accuracy",
        color=colors[i],
    )
    ax1.bar(
        (i - 2) * 0.3 + indexs[1],
        unfairness_movielens[i],
        width=0.3,
        label="Unfairness",
        color=colors[i],
    )
ax1.set_title(movielens_title)
ax1.set_xticks([index - 0.15 for index in indexs])
ax1.set_xticklabels(labels)
ax1.set_ylabel(ylabel_movielens)
ax1.set_yticks(yticks_movielens)
ax1.tick_params(axis="both", which="both", length=0)

# Tenrec subplot
for i in range(len(x)):
    ax2.bar(
        (i - 2) * 0.3 + indexs[0],
        accuracy_tenrec[i],
        width=0.3,
        label="Accuracy",
        color=colors[i],
    )
    ax2.bar(
        (i - 2) * 0.3 + indexs[1],
        unfairness_tenrec[i],
        width=0.3,
        label="Unfairness",
        color=colors[i],
    )
ax2.set_title(tenrec_title)
ax2.set_xticks([index - 0.15 for index in indexs])
ax2.set_xticklabels(labels)
ax2.set_ylabel(ylabel_tenrec)
ax2.set_yticks(yticks_tenrec)

ax2.tick_params(axis="both", which="both", length=0)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save the figure
plt.tight_layout()
plt.savefig("bar_48.pdf", bbox_inches="tight")
