# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Simulated data
collab_x = np.array(
    ["All", "MLP", "GCN", "NCN", "NCNC", "NeoGNN-BUDDY", "SEAL", "Node2Vec"]
)
collab_y = np.array([75, 73, 72, 70, 69, 71, 73, 74])
collab_err = np.array([2, 3, 1, 1, 2, 2, 3, 2])
collab_y2 = np.array(
    [67, 65, 64, 62, 61, 63, 65, 66]
)  # Adjusted data for clear spacing
collab_err2 = np.array([3, 3, 1, 2, 2, 3, 3, 4])

ppa_x = np.array(
    ["All", "MLP", "GCN", "NCN", "NCNC", "NeoGNN-BUDDY", "SEAL", "Node2Vec"]
)
ppa_y = np.array([65, 63, 62, 60, 59, 61, 63, 64])
ppa_err = np.array([3, 2, 1, 2, 3, 2, 2, 1])
ppa_y2 = np.array([70, 69, 69, 68, 67, 69, 70, 68])  # Adjusted data for clear spacing
ppa_err2 = np.array([2, 3, 1, 1, 2, 2, 3, 2])

# Axes Limits and Labels
ylabel_value = "Hits@50"
ylim_values = [55, 80]
yticks_values = np.arange(55, 81, 5)

# Labels
label_1 = "ogbl-collab 2022"
label_2 = "ogbl-collab 2023"
label_3 = "ogbl-ppa 2022"
label_4 = "ogbl-ppa 2023"

# Titles
title_1 = "ogbl-collab Results"
title_2 = "ogbl-ppa Results"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create a subplot layout of 1x2
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5), sharey=True)

# First subplot for ogbl-collab
ax1.errorbar(
    collab_x,
    collab_y,
    yerr=collab_err,
    fmt="o-",
    label=label_1,
    color="#3d89be",
    capsize=5,
)
ax1.errorbar(
    collab_x,
    collab_y2,
    yerr=collab_err2,
    fmt="^-",
    label=label_2,
    color="#00BFFF",
    capsize=5,
)
ax1.set_title(title_1)
ax1.set_xticks(collab_x)
ax1.set_xticklabels(collab_x, rotation=45, ha="right", fontsize=12)
ax1.set_yticks(yticks_values)
ax1.set_ylim(ylim_values)
ax1.grid(True, which="both", linestyle="--", linewidth=0.5, alpha=0.5)
ax1.set_ylabel(ylabel_value, fontsize=16)
ax1.legend(loc="lower left", fontsize=12)

# Second subplot for ogbl-ppa
ax2.errorbar(
    ppa_x,
    ppa_y,
    yerr=ppa_err,
    fmt="s--",
    label=label_3,
    color="#ff7f0e",
    capsize=5,
)
ax2.errorbar(
    ppa_x,
    ppa_y2,
    yerr=ppa_err2,
    fmt="o-.",
    label=label_4,
    color="#FFA500",
    capsize=5,
)
ax2.set_title(title_2)
ax2.set_xticks(ppa_x)
ax2.set_xticklabels(ppa_x, rotation=45, ha="right", fontsize=12)
ax2.grid(True, which="both", linestyle="--", linewidth=0.5, alpha=0.5)
ax2.legend(loc="upper left", fontsize=12)

# ===================
# Part 4: Saving Output
# ===================
# Enhance overall layout
plt.tight_layout()
plt.savefig('line_43.pdf', bbox_inches='tight')
