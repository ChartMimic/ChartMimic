import numpy as np; np.random.seed(0)

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from scipy.stats import gaussian_kde

# ===================
# Part 2: Data Preparation
# ===================
# Sample data to represent luxury fashion brands
brands = ["Nike", "Adidas", "Under Armour", "Puma", "Reebok"]
prices = [85, 95, 80, 70, 75]  # Average price per item for each brand (in dollars)
popularity = [9.0, 8.5, 7.5, 7.0, 6.5]  # Popularity index out of 10

# Data for violin plot; customer satisfaction scores (1-10 scale)
satisfaction_data = np.random.normal(loc=[8, 7.5, 6, 7, 7], scale=0.5, size=(50, 5))

# Updated labels for sports domain
ax0xlabel = "Average Price ($)"
ax0ylabel = "Popularity Index"
ax0title = "Sports Brand Popularity vs Price"
ax1xticks = range(len(brands))
ax1xlabel = "Brands"
ax1ylabel = "Customer Satisfaction"
ax1title = "Distribution of Customer Satisfaction Across Sports Brands"

x = np.linspace(4, 10, 400)
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create 1x2 subplot layout
fig = plt.figure(figsize=(10, 6))
gs = gridspec.GridSpec(1, 2, width_ratios=[1, 2])

# Scatter plot on the left
ax0 = fig.add_subplot(gs[0])
sc = ax0.scatter(
    prices, popularity, s=100, c=np.linspace(0.1, 0.9, len(brands)), cmap="viridis"
)
for i, brand in enumerate(brands):
    ax0.text(prices[i], popularity[i] + 0.05, brand, fontsize=9)
ax0.set_xlabel(ax0xlabel)
ax0.set_ylabel(ax0ylabel)
ax0.set_title(ax0title)

# Violin plot on the right
ax1 = fig.add_subplot(gs[1])

# Creating half-violins
for i, brand in enumerate(brands):
    kde = gaussian_kde(satisfaction_data[:, i])
    y = kde(x)
    max_y = max(y)
    ax1.fill_betweenx(x, -y / max_y * 0.5 + i, i, color="lightblue", alpha=0.5)
    ax1.fill_betweenx(x, y / max_y * 0.5 + i, i, color="blue", alpha=0.5)

ax1.set_xticks(ax1xticks)
ax1.set_xticklabels(brands)
ax1.set_xlabel(ax1xlabel)
ax1.set_ylabel(ax1ylabel)
ax1.set_title(ax1title)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
# Show plot
plt.savefig('multidiff_6.pdf', bbox_inches='tight')
