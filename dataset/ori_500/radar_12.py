# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data values
values_k1 = [0.36, 0.37, 0.43, 0.28, 0.4]
values_k2 = [0.22, 0.284, 0.24, 0.46, 0.29]
values_plus = [0.48, 0.496, 0.33, 0.24, 0.5]
categories = ["μ$_{Train}$", "μ$_R$", "μ$_{AUC}$", "N$^{eﬀ}_{TP}$", "N$_{TP}$"]
labels=["GNN${_{k=1}}$", "GNN${_{k=2}}$", "GNN${^{↑}}$"]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Initialise the radar plot
fig, ax = plt.subplots(figsize=(8, 6), subplot_kw=dict(polar=True))

# Number of variables
N = len(categories)

# What will be the angle of each axis in the plot
angles = [n / float(N) * 2 * np.pi for n in range(N)]
angles += angles[:1]

# Draw one axe per variable and add labels
plt.xticks(angles[:-1], categories)

# Draw ylabels
ax.set_rlabel_position(0)
plt.yticks([0.1, 0.2, 0.3, 0.4], [], color="grey", size=7)
plt.ylim(0, 0.5)

# Plot data
ax.plot(
    angles,
    values_k1 + values_k1[:1],
    color="blue",
    linewidth=1,
    linestyle="dotted",
    label=labels[0],
    marker=".",
)
ax.fill(angles, values_k1 + values_k1[:1], color="blue", alpha=0.1)

ax.plot(
    angles,
    values_k2 + values_k2[:1],
    color="orange",
    linewidth=1,
    linestyle="dotted",
    label=labels[1],
    marker=".",
)
ax.fill(angles, values_k2 + values_k2[:1], color="orange", alpha=0.1)

ax.plot(
    angles,
    values_plus + values_plus[:1],
    color="green",
    linewidth=1,
    linestyle="dotted",
    label=labels[2],
    marker=".",
)
ax.fill(angles, values_plus + values_plus[:1], color="green", alpha=0.1)

# add label for each point
for i in range(N):
    ax.text(
        angles[i],
        values_k1[i],
        str(values_k1[i]),
        color="black",
        size=8,
        verticalalignment="bottom",
        horizontalalignment="center",
    )
    ax.text(
        angles[i],
        values_k2[i],
        str(values_k2[i]),
        color="black",
        size=8,
        verticalalignment="bottom",
        horizontalalignment="center",
    )
    ax.text(
        angles[i],
        values_plus[i],
        str(values_plus[i]),
        color="black",
        size=8,
        verticalalignment="bottom",
        horizontalalignment="center",
    )

# Add legend
plt.legend(loc="upper left", bbox_to_anchor=(1, 1))

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout for better fit and save the plot
plt.tight_layout()
plt.savefig('radar_12.pdf', bbox_inches='tight')
