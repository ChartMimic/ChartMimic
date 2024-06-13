# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Define the data with correct shape
data = np.array(
    [
        [876, 136, 435, 534, 322, 804],
        [750, 1737, 742, 375, 750, 1825],
        [764, 676, 782, np.nan, 421, np.nan],  # Assumed another NaN value for padding
        [482, 120, 843, 1170, 925, 911],
    ]
)

title = "BabelStream triad Average Memory Bandwidth (GB/s)"
xlabel = "Programming Model"
xticklabels = ["Kokkos", "RAJA", "OMP", "OACC", "SYCL", "Native Port"]
yticklabels = ["Summit", "Perlmutter", "Corona", "Frontier"]
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plotting the heatmap with adjusted colorbar and new theme color
# Create mask for NaN values to hatch them later
mask = np.isnan(data)

# Defining a new color palette
cmap = plt.get_cmap("RdGy")
norm = plt.Normalize(vmin=np.nanmin(data), vmax=np.nanmax(data))

fig, ax = plt.subplots(figsize=(10, 8))
cax = ax.imshow(data, cmap=cmap, norm=norm)
cbar = fig.colorbar(cax, ax=ax, extend="both")

# Add hatches for NaN values
for i, j in zip(*np.where(mask)):
    ax.add_patch(
        plt.Rectangle(
            (j - 0.5, i - 0.5), 1, 1, fill=False, hatch="//", edgecolor="black"
        )
    )

# Adding titles and labels
plt.title(title)
plt.xlabel(xlabel)

# Define the labels for x and y axis
ax.set_xticks(range(6))
ax.set_xticklabels(xticklabels, rotation=45)
ax.set_yticks(range(4))
ax.set_yticklabels(yticklabels, rotation=0)

# Add annotations
for i in range(4):
    for j in range(6):
        if not np.isnan(data[i, j]):
            if data[i, j] > np.nanmean(data) * 1.5:
                ax.text(
                    j, i, f"{data[i, j]:.0f}", ha="center", va="center", color="white"
                )
            else:
                ax.text(
                    j, i, f"{data[i, j]:.0f}", ha="center", va="center", color="black"
                )

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig("heatmap_6.pdf", bbox_inches="tight")
