# ===================
# Part 1: Importing Libraries
# ===================
import math
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

from matplotlib.collections import PolyCollection


# ===================
# Part 2: Data Preparation
# ===================
# Fixing random state for reproducibility
def polygon_under_graph(x, y):
    """
    Construct the vertex list which defines the polygon filling the space under
    the (x, y) line graph. This assumes x is in ascending order.
    """
    return [(x[0], 0.0), *zip(x, y), (x[-1], 0.0)]


x = np.linspace(0.0, 10.0, 31)
vaccination_numbers = range(1, 4)

# verts[i] is a list of (x, y) pairs defining polygon i.
gamma = np.vectorize(math.gamma)
verts = [
    polygon_under_graph(x, v**x * np.exp(-v) / gamma(x + 1))
    for v in vaccination_numbers
]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
ax = plt.figure(figsize=(8, 6)).add_subplot(projection="3d")
facecolors = plt.colormaps["rainbow"](np.linspace(0, 1, len(verts)))

poly = PolyCollection(verts, facecolors=facecolors, alpha=0.7)
ax.add_collection3d(poly, zs=vaccination_numbers, zdir="y")

ax.set(
    xlim=(0, 10),
    ylim=(1, 4),
    zlim=(0, 0.35),
    xlabel="Age",
    ylabel="Vaccination Number",
    zlabel="Incidence Rate",
)

ax.set_yticks([1, 2, 3])
ax.set_box_aspect(aspect=None, zoom=0.8)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig("3d_14.pdf", bbox_inches="tight")
