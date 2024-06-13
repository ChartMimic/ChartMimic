# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)

import matplotlib.patches as mpatches

# ===================
# Part 2: Data Preparation
# ===================
# Data
categories = ["Species A", "Species B", "Species C", "Species D"]
protein_levels = [55.3, 62.1, 48.7, 70.2]
carbohydrate_levels = [20.5, 18.2, 25.3, 19.1]
lipid_levels = [24.2, 19.7, 26.0, 10.7]

# Define colors
colors_protein = ["#4881b8", "#4881b8", "#4881b8", "#d55f2b"]
colors_carbohydrate = ["#7badd2", "#7badd2", "#7badd2", "#ee934f"]
colors_lipid = ["#cadbed", "#cadbed", "#cadbed", "#f6d2a8"]

# Repeat for the second subplot with different data
protein_levels2 = [57.8, 60.3, 47.2, 68.5]
carbohydrate_levels2 = [19.2, 20.7, 23.5, 18.6]
lipid_levels2 = [23.0, 19.0, 29.3, 12.9]

# Plot data
bar_width = 0.5
indices = np.arange(len(categories))

xlabel = "Sample Set 1"
xlabel2 = "Sample Set 2"

labels = ["High Protein", "Moderate Protein", "High Carbohydrate", "Moderate Carbohydrate", "High Lipid", "Moderate Lipid"]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create figure and axes
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

# Function to plot bars
def plot_bars(ax, protein_levels, carbohydrate_levels, lipid_levels, colors_protein, colors_carbohydrate, colors_lipid):
    for i, (protein, carbohydrate, lipid) in enumerate(zip(protein_levels, carbohydrate_levels, lipid_levels)):
        ax.barh(i, protein, bar_width, color=colors_protein[i], edgecolor="white")
        ax.barh(i, carbohydrate, bar_width, left=protein, color=colors_carbohydrate[i], edgecolor="white")
        ax.barh(i, lipid, bar_width, left=protein + carbohydrate, color=colors_lipid[i], edgecolor="white")
        ax.text(protein / 2, i, f"{protein}", ha="center", va="center", color="white")
        ax.text(protein + carbohydrate / 2, i, f"{carbohydrate}", ha="center", va="center", color="black")
        ax.text(protein + carbohydrate + lipid / 2, i, f"{lipid}", ha="center", va="center", color="black")

plot_bars(ax1, protein_levels, carbohydrate_levels, lipid_levels, colors_protein, colors_carbohydrate, colors_lipid)

# Set labels, title, and legend for ax1
ax1.set_yticks(indices)
ax1.set_yticklabels(categories)
ax1.invert_yaxis()  # labels read top-to-bottom
ax1.set_xlabel(xlabel)
ax1.set_xticks([])

plot_bars(ax2, protein_levels2, carbohydrate_levels2, lipid_levels2, colors_protein, colors_carbohydrate, colors_lipid)

# Set labels, title, and legend for ax2
ax2.set_yticks(indices)
ax2.set_yticklabels(categories)
ax2.invert_yaxis()  # labels read top-to-bottom
ax2.set_xlabel(xlabel2)
ax2.set_xticks([])

# Adjust layout and set background color
fig.patch.set_facecolor("white")
for ax in [ax1, ax2]:
    ax.set_facecolor("white")
    ax.spines["top"].set_edgecolor("gray")
    ax.spines["right"].set_edgecolor("gray")
    ax.spines["bottom"].set_edgecolor("gray")
    ax.spines["left"].set_edgecolor("gray")

# Create a global legend
patch1 = mpatches.Patch(color="#d55f2b", label=labels[0])
patch2 = mpatches.Patch(color="#4881b8", label=labels[1])
patch3 = mpatches.Patch(color="#ee934f", label=labels[2])
patch4 = mpatches.Patch(color="#7badd2", label=labels[3])
patch5 = mpatches.Patch(color="#f6d2a8", label=labels[4])
patch6 = mpatches.Patch(color="#cadbed", label=labels[5])
fig.legend(
    handles=[patch1, patch2, patch3, patch4, patch5, patch6],
    loc="upper center",
    ncol=3,
    bbox_to_anchor=(0.5, 1.15),
)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save the figure
plt.tight_layout()
plt.savefig('bar_25.pdf', bbox_inches='tight')
