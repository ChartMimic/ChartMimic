# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

from matplotlib.collections import PolyCollection


# ===================
# Part 2: Data Preparation
# ===================
# Function to create polygon under graph
def polygon_under_graph(x, y):
    return [(x[0], 0.0), *zip(x, y), (x[-1], 0.0)]


# Data for bar chart
years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
AI = [7.92, 5.29, 5.68, 9.26, 0.71, 0.87, 0.2, 8.33, 7.78, 8.7]
CS = [2.13, 1.67, 1.89, 4.02, 0.33, 0.41, 0.1, 3.67, 3.45, 3.8]

# Data for distribution graph
x = np.linspace(0.0, 10.0, 31)
technology_levels = range(1, 4)
exp = np.exp
verts = [
    polygon_under_graph(x, exp(-0.5 * (x - t) ** 2)) for t in technology_levels
]  # Gaussian distributions
facecolors = plt.colormaps["plasma"](np.linspace(0, 1, len(verts)))

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Data for bar chart
# Initialize figure and axes
fig = plt.figure(figsize=(10, 8))
ax1 = fig.add_subplot(121, projection="3d")  # 3D bar chart
ax2 = fig.add_subplot(122, projection="3d")  # 3D distribution graph


ax1.bar(years, AI, zs=0, zdir="y", color="#8ac926", alpha=0.8)
ax1.bar(years, CS, zs=1, zdir="y", color="#00b4d8", alpha=0.8)

# Set labels and ticks for bar chart
ax1.set_xlabel("Year")
ax1.set_ylabel("Sector")
ax1.set_zlabel("Investment (Billion USD)")
ax1.set_yticks([0, 1])
ax1.set_yticklabels(["AI", "CS"])

# Add polygons to the plot
poly = PolyCollection(verts, facecolors=facecolors, alpha=0.7)
ax2.add_collection3d(poly, zs=technology_levels, zdir="y")

# Set labels and limits for distribution graph
ax2.set(
    xlim=(0, 10),
    ylim=(1, 4),
    zlim=(0, 1),
    xlabel="Time Since Introduction (Years)",
    ylabel="Technology Level",
    zlabel="Adoption Rate",
)
ax2.set_yticks([1, 2, 3])

# ===================
# Part 4: Saving Output
# ===================
# Adjust the layout and save the figure
plt.tight_layout()
ax1.set_box_aspect(aspect=None, zoom=0.9)
ax2.set_box_aspect(aspect=None, zoom=0.8)
plt.savefig("3d_15.pdf", bbox_inches="tight")
