# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Sample data for demonstration purposes
data_gmml = [
    np.random.normal(9.5, 1, 50),
    np.random.normal(9, 1, 50),
    np.random.normal(8, 1, 50),
]
data_gml = [
    np.random.normal(8, 1, 50),
    np.random.normal(10, 1, 50),
    np.random.normal(8, 1, 50),
]
data_ao = [
    np.random.normal(10, 1, 50),
    np.random.normal(9.5, 1, 50),
    np.random.normal(7, 1, 50),
]

# Positions of the boxplots
positions_gmml = [1, 5, 9]
positions_gml = [2, 6, 10]
positions_ao = [3, 7, 11]
xticklabels = ["Perfect", "-10dB", "0dB"]
xticks = [2, 6, 10]
xlabel = "CEE (dB)"
ylabel = "SE (bps/Hz)"
legend_labels = ["GMML (25%-75%)", "GML (25%-75%)", "AO (25%-75%)"]
ylim = [4, 12]
legendtitle = "Method"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create figure and axes
fig, ax = plt.subplots(figsize=(8, 6))

# Plotting the boxplots
bp_gmml = ax.boxplot(
    data_gmml,
    positions=positions_gmml,
    widths=1,
    patch_artist=True,
    boxprops=dict(facecolor="#ab5b4e"),
    medianprops=dict(color="black"),
    showfliers=False,
)
bp_gml = ax.boxplot(
    data_gml,
    positions=positions_gml,
    widths=1,
    patch_artist=True,
    boxprops=dict(facecolor="#54addb"),
    medianprops=dict(color="black"),
    showfliers=False,
)
bp_ao = ax.boxplot(
    data_ao,
    positions=positions_ao,
    widths=1,
    patch_artist=True,
    boxprops=dict(facecolor="#a6edd1"),
    medianprops=dict(color="black"),
    showfliers=False,
)

# Customizing the axes
ax.set_xticks(xticks)
ax.set_xticklabels(xticklabels)
ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)
ax.set_ylim(ylim)
ax.yaxis.grid(True, linestyle="--", linewidth=0.5)
ax.xaxis.grid(True, linestyle="--", linewidth=0.5)

# Adding legend

ax.legend(
    [bp_gmml["boxes"][0], bp_gml["boxes"][0], bp_ao["boxes"][0]],
    legend_labels,
    loc="lower left",
    title="Method",
)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig("box_6.pdf", bbox_inches="tight")
