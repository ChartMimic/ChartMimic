# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

from scipy.stats import norm

# ===================
# Part 2: Data Preparation
# ===================
# Define the data for each subplot using random numbers and normal distribution
total_data = np.random.normal(1660.10, 23.78, 1000)
proposer_data = np.random.normal(211.42, 2.63, 1000)
attestor_data = np.random.normal(1398.78, 20.69, 1000)
sync_data = np.random.normal(49.90, 0.62, 1000)
titles = ["Total", "Proposer", "Attestor", "Sync committee member"]
xlabels = [
    "Daily reward (Ether)",
    "Daily reward (Ether)",
    "Daily reward (Ether)",
    "Daily reward (Ether",
]
ylabels = ["Probability", "Probability", "Probability", "Probability"]
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Set the figure size to match the original image's dimensions
plt.figure(figsize=(10, 8))

# Define the subplot grid with reduced space between subplots
grid = plt.GridSpec(2, 2, wspace=0.4, hspace=0.5)

# Total subplot
ax_total = plt.subplot(grid[0, 0])
ax_total.hist(
    total_data, bins=20, color="#0c279f", edgecolor="black", density=True, linewidth=1
)
ax_total.plot(
    np.sort(total_data),
    norm.pdf(np.sort(total_data), np.mean(total_data), np.std(total_data)),
    color="#3a809d",
)
ax_total.set_title(titles[0])
ax_total.set_xlabel(xlabels[0])
ax_total.set_ylabel(ylabels[0])
ax_total.set_ylim(0, 0.020)
ax_total.text(
    0.7,
    0.8,
    f"$\mu = {np.mean(total_data):.2f}$\n$\sigma = {np.std(total_data):.2f}$",
    transform=ax_total.transAxes,
    fontsize=9,
)

# Proposer subplot
ax_proposer = plt.subplot(grid[0, 1])
ax_proposer.hist(
    proposer_data,
    bins=20,
    color="#cd6838",
    edgecolor="black",
    density=True,
    linewidth=1,
)
ax_proposer.plot(
    np.sort(proposer_data),
    norm.pdf(np.sort(proposer_data), np.mean(proposer_data), np.std(proposer_data)),
    color="#3a809d",
)
ax_proposer.set_title(titles[1])
ax_proposer.set_xlabel(xlabels[1])
ax_proposer.set_ylabel(ylabels[1])
ax_proposer.set_ylim(0, 0.20)
ax_proposer.text(
    0.7,
    0.8,
    f"$\mu = {np.mean(proposer_data):.2f}$\n$\sigma = {np.std(proposer_data):.2f}$",
    transform=ax_proposer.transAxes,
    fontsize=9,
)

# Attestor subplot
ax_attestor = plt.subplot(grid[1, 0])
ax_attestor.hist(
    attestor_data,
    bins=20,
    color="#9cc25c",
    edgecolor="black",
    density=True,
    linewidth=1,
)
ax_attestor.plot(
    np.sort(attestor_data),
    norm.pdf(np.sort(attestor_data), np.mean(attestor_data), np.std(attestor_data)),
    color="#3a809d",
)
ax_attestor.set_title(titles[2])
ax_attestor.set_xlabel(xlabels[2])
ax_attestor.set_ylabel(ylabels[2])
ax_attestor.set_ylim(0, 0.020)
ax_attestor.text(
    0.7,
    0.8,
    f"$\mu = {np.mean(attestor_data):.2f}$\n$\sigma = {np.std(attestor_data):.2f}$",
    transform=ax_attestor.transAxes,
    fontsize=9,
)

# Sync committee member subplot
ax_sync = plt.subplot(grid[1, 1])
ax_sync.hist(
    sync_data, bins=20, color="#f9df4b", edgecolor="black", density=True, linewidth=1
)
ax_sync.plot(
    np.sort(sync_data),
    norm.pdf(np.sort(sync_data), np.mean(sync_data), np.std(sync_data)),
    color="#3a809d",
)
ax_sync.set_title(titles[3])
ax_sync.set_xlabel(xlabels[3])
ax_sync.set_ylabel(ylabels[3])
ax_sync.set_ylim(0, 0.8)
ax_sync.text(
    0.7,
    0.8,
    f"$\mu = {np.mean(sync_data):.2f}$\n$\sigma = {np.std(sync_data):.2f}$",
    transform=ax_sync.transAxes,
    fontsize=9,
)

# ===================
# Part 4: Saving Output
# ===================
# Show the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig("CB_22.pdf", bbox_inches="tight")
