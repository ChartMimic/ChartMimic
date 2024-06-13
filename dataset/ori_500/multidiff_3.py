# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)

from matplotlib.gridspec import GridSpec

# ===================
# Part 2: Data Preparation
# ===================
# Generate sample data for the histogram representing stock returns
returns = np.random.normal(
    loc=0.05, scale=0.2, size=1000
)  # Average daily return of 5% with 20% volatility
losses = np.random.normal(loc=-0.05, scale=0.1, size=1000)  # Losses as negative returns

# Generate sample data for the scatter plot representing investment clusters
x = np.random.uniform(-1, 1, 100)
y = np.random.normal(1, 0.5, 100)
z = np.random.normal(-1, 0.5, 100)

ax1title = "Histogram of Stock Returns"
ax1xlabel = "Returns"
ax1ylabel = "Frequency"
ax1legend = ["Gains", "Losses"]
ax2title = "Investment Clusters"
ax2labels=["Tech Stocks", "Energy Stocks"]
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Histogram for stock returns
# Create a figure and a 1x2 grid layout
fig = plt.figure(figsize=(10, 5))
gs = GridSpec(1, 2, figure=fig)

ax1 = fig.add_subplot(gs[0, 0])
ax1.hist(
    [returns, losses], bins=50, stacked=True, color=["#2ca02c", "#d62728"], alpha=0.6
)
ax1.set_title(ax1title)
ax1.set_xlabel(ax1xlabel)
ax1.set_ylabel(ax1ylabel)
ax1.legend(ax1legend)

# Scatter plot for investment clusters
ax2 = fig.add_subplot(gs[0, 1])
ax2.scatter(x, y, c="gold", label=ax2labels[0])
ax2.scatter(x, z, c="deepskyblue", label=ax2labels[1])
ax2.set_title(ax2title)
ax2.legend()
ax2.grid(True)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save to file
plt.tight_layout()
plt.savefig('multidiff_3.pdf', bbox_inches='tight')
