# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)

from scipy.stats import gaussian_kde

# ===================
# Part 2: Data Preparation
# ===================
# Seed for reproducibility

# Generating synthetic data for the violin plot
# Average annual temperatures for two regions over different years
region1_temps = np.random.normal(15, 2, 150)  # Temperatures in region 1
region2_temps = np.random.normal(20, 3, 150)  # Temperatures in region 2

# Generating synthetic data for the density plot
# Elevation data in meters for three geographical zones
lowland = np.random.normal(200, 50, 1000)  # Lowland elevations
highland = np.random.normal(1500, 300, 1000)  # Highland elevations
plateau = np.random.normal(1000, 150, 1000)  # Plateau elevations

xs = np.linspace(0, 2000, 200)

labels = ["Lowland", "Highland", "Plateau"]
titles=["Average Annual Temperature", "Geographical Elevation Distribution"]
ylabels=["Temperature (°C)", "Density"]
ax1xticks=[1, 2]
ax1xtickslabels=["Region 1", "Region 2"]
ax2xlabel="Elevation (m)"
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Creating the figure and axes
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))

# Violin plot
violin_data = [region1_temps, region2_temps]
axes[0].violinplot(violin_data, showmeans=False, showmedians=True)
axes[0].set_title(titles[0])
axes[0].set_ylabel(ylabels[1])
axes[0].set_xticks(ax1xticks)
axes[0].set_xticklabels(ax1xtickslabels)
axes[0].grid(True)

# Density plot
colors = ["blue", "green", "red"]

for data, color, label in zip([lowland, highland, plateau], colors, labels):
    density = gaussian_kde(data)
    axes[1].fill_between(xs, density(xs), color=color, alpha=0.2, label=label)
axes[1].set_title(titles[1])
axes[1].set_xlabel(ax2xlabel)
axes[1].set_ylabel(ylabels[1])
axes[1].legend()

# ===================
# Part 4: Saving Output
# ===================
# Adjusting layout for better visual appearance
plt.tight_layout()
plt.savefig('multidiff_20.pdf', bbox_inches='tight')
