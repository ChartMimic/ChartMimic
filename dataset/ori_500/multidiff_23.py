# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)

from scipy.stats import gaussian_kde
from matplotlib.gridspec import GridSpec

# ===================
# Part 2: Data Preparation
# ===================
# Seed for reproducibility

# Generate synthetic traffic data
# Vehicle counts at different times of day
morning_traffic = np.random.poisson(300, 500)  # Morning traffic counts
evening_traffic = np.random.poisson(500, 500)  # Evening traffic counts

# Speed data at different locations
urban_speeds = np.random.normal(45, 10, 1000)  # Urban speeds in km/h
highway_speeds = np.random.normal(100, 20, 1000)  # Highway speeds in km/h

# Elevation data along a route
route_elevation = np.linspace(0, 1000, 1000)
elevation_changes = np.sin(np.linspace(0, 20, 1000)) * 50 + route_elevation

ax1labels=["Morning Traffic", "Evening Traffic"]
titles=["Traffic Volume by Time of Day", "Speed Distribution by Location","Elevation Changes Along a Route"]
xlabels=["Number of Vehicles",  "Distance (km)"]
ylabels=["Frequency", "Speed (km/h)", "Elevation (m)"]
ax2xtickslabels=["Urban", "Highway"]
ax2xticks=[1, 2]
bins = np.linspace(100, 700, 31)



# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create the figure using GridSpec
fig = plt.figure(figsize=(10, 10))
gs = GridSpec(2, 2, figure=fig)

# Histogram plot across top (1,1 and 1,2)
ax1 = fig.add_subplot(gs[0, :])
# Define bin edges and width to align bars side by side

ax1.hist(
    morning_traffic,
    bins=bins,
    alpha=0.7,
    label=ax1labels[0],
    color="#dca684",
    edgecolor="black",
)
ax1.hist(
    evening_traffic,
    bins=bins,
    alpha=0.7,
    label=ax1labels[1],
    color="#8f8c6d",
    edgecolor="black",
)
ax1.set_title(titles[0])
ax1.set_xlabel(xlabels[0])
ax1.set_ylabel(ylabels[0])
ax1.legend()

# Violin plot on bottom left (2,1)
ax2 = fig.add_subplot(gs[1, 0])
ax2.violinplot([urban_speeds, highway_speeds], showmeans=False, showmedians=True)
ax2.set_title(titles[1])
ax2.set_ylabel(ylabels[1])
ax2.set_xticks(ax2xticks)
ax2.set_xticklabels(ax2xtickslabels)
ax2.grid(True)

# Fill between plot on bottom right (2,2)
ax3 = fig.add_subplot(gs[1, 1])
ax3.fill_between(route_elevation, elevation_changes, color="blue", alpha=0.2)
ax3.set_title(titles[2])
ax3.set_xlabel(xlabels[1])
ax3.set_ylabel(ylabels[2])

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout for a better visual appearance
plt.tight_layout()
plt.savefig('multidiff_23.pdf', bbox_inches='tight')
