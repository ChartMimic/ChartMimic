# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
methods = [
    None,
    "none",
    "nearest",
    "bilinear",
    "bicubic",
    "spline16",
    "spline36",
    "hanning",
    "hamming",
    "hermite",
    "kaiser",
    "quadric",
    "catrom",
    "gaussian",
    "bessel",
    "mitchell",
    "sinc",
    "lanczos",
]

grid = np.random.rand(4, 4)

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
fig, axs = plt.subplots(
    nrows=3, ncols=6, figsize=(9, 6), subplot_kw={"xticks": [], "yticks": []}
)

for ax, interp_method in zip(axs.flat, methods):
    ax.imshow(grid, interpolation=interp_method, cmap="viridis")
    ax.set_title(str(interp_method))

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig("heatmap_26.pdf", bbox_inches="tight")
