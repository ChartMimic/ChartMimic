import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)

from matplotlib.gridspec import GridSpec

# ===================
# Part 2: Data Preparation
# ===================
# Generate sample data for the histogram representing athlete performance improvements
performance_improvements = np.random.normal(
    loc=0.1, scale=0.05, size=1000
)  # Average performance improvement of 10% with 5% volatility
performance_declines = np.random.normal(loc=-0.05, scale=0.03, size=1000)  # Performance declines as negative improvements

# Generate sample data for the scatter plot representing athlete performance clusters
speeds = np.random.uniform(5, 15, 100)  # Simulated speeds in m/s
stamina = np.random.normal(70, 10, 100)  # Simulated stamina (measured as percentage of maximum)
strength = np.random.normal(100, 15, 100)  # Simulated strength (measured in kg lifted)

ax1title = "Histogram of Athlete Performance Improvements"
ax1xlabel = "Performance Change (%)"
ax1ylabel = "Frequency"
ax1legend = ["Improvements", "Declines"]
ax2title = "Athlete Performance Clusters"
ax2labels = ["Speed vs Stamina", "Strength vs Stamina"]
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Histogram for stock performance_improvements
# Create a figure and a 1x2 grid layout
fig = plt.figure(figsize=(10, 5))
gs = GridSpec(1, 2, figure=fig)

ax1 = fig.add_subplot(gs[0, 0])
ax1.hist(
    [performance_improvements, performance_declines], bins=50, stacked=True, color=["#2ca02c", "#d62728"], alpha=0.6
)
ax1.set_title(ax1title)
ax1.set_xlabel(ax1xlabel)
ax1.set_ylabel(ax1ylabel)
ax1.legend(ax1legend)

# Scatter plot for investment clusters
ax2 = fig.add_subplot(gs[0, 1])
ax2.scatter(speeds, stamina, c="gold", label=ax2labels[0])
ax2.scatter(speeds, strength, c="deepskyblue", label=ax2labels[1])
ax2.set_title(ax2title)
ax2.legend()
ax2.grid(True)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save to file
plt.tight_layout()
plt.savefig('multidiff_3.pdf', bbox_inches='tight')
