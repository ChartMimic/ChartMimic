import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)

from scipy.stats import gaussian_kde
from matplotlib.gridspec import GridSpec

# ===================
# Part 2: Data Preparation
# ===================
# Seed for reproducibility

# Generate synthetic traffic data

# Heart rate counts at different times of day
morning_heart_rate = np.random.poisson(140, 500)  # Morning heart rate
evening_heart_rate = np.random.poisson(120, 500)  # Evening heart rate

# Step count data at different locations
home_steps = np.random.normal(4000, 800, 1000)  # Steps at home
office_steps = np.random.normal(2000, 1000, 1000)  # Steps at office

# Weight data over a diet period
days = np.linspace(0, 7, 1000)  # Days in a week
weight_changes = np.sin(np.linspace(0, 2 * np.pi, 1000)) * 2 + 70  # Hypothetical weight changes

# Labels and titles for the plots
ax1labels = ["Morning Heart Rate", "Evening Heart Rate"]
titles = ["Heart Rate by Time of Day", "Step Count Distribution by Location", "Weight Changes Over a Diet Week"]
xlabels = ["Heart Rate (bpm)", "Number of Steps", "Days"]
ylabels = ["Frequency", "Frequency", "Weight (kg)"]
ax2xtickslabels = ["Home", "Office"]
ax2xticks = [1, 2]
bins = np.linspace(40, 200, 31)

# Placeholder to show where the histograms and line plot would be displayed. Actual plotting code is not included.

# Placeholder to show where the histograms and line plot would be displayed. Actual plotting code is not included.

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
    morning_heart_rate,
    bins=bins,
    alpha=0.7,
    label=ax1labels[0],
    color="#dca684",
    edgecolor="black",
)
ax1.hist(
    evening_heart_rate,
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
ax2.violinplot([home_steps, office_steps], showmeans=False, showmedians=True)
ax2.set_title(titles[1])
ax2.set_ylabel(ylabels[1])
ax2.set_xticks(ax2xticks)
ax2.set_xticklabels(ax2xtickslabels)
ax2.grid(True)

# Fill between plot on bottom right (2,2)
ax3 = fig.add_subplot(gs[1, 1])
ax3.fill_between(days, weight_changes, color="blue", alpha=0.2)
ax3.set_title(titles[2])
ax3.set_xlabel(xlabels[1])
ax3.set_ylabel(ylabels[2])

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout for a better visual appearance
plt.tight_layout()
plt.savefig('multidiff_23.pdf', bbox_inches='tight')
