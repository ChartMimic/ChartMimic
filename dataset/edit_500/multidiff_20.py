import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)

from scipy.stats import gaussian_kde

# ===================
# Part 2: Data Preparation
# ===================
# Seed for reproducibility

# Generating synthetic data for the violin plot
# Average annual temperatures for two regions over different years

# Yearly investment returns for two different regions
region1_returns = np.random.normal(10, 1.5, 150)  # Returns in region 1, mean 7%, std 1.5%
region2_returns = np.random.normal(8, 2, 150)  # Returns in region 2, mean 8%, std 2%

# Generating synthetic data for the density plot
# Returns in percentage for three investment categories over time
stocks = np.random.normal(10, 2, 1000)  # Stock returns
bonds = np.random.normal(5, 1, 1000)  # Bond returns
real_estate = np.random.normal(7, 1.5, 1000)  # Real estate returns

xs = np.linspace(0, 15, 200)  # x-axis representing return percentage range

# Labels and titles for the plots
labels = ["Stocks", "Bonds", "Real Estate"]
titles = ["Average Annual Investment Returns", "Investment Return Distribution"]
ylabels = ["Return (%)", "Density"]
ax1xticks = [1, 2]
ax1xtickslabels = ["Region 1", "Region 2"]
ax2xlabel = "Return (%)"

# Placeholder to show where the plots would be displayed. Actual plotting code is not included.
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Creating the figure and axes
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))

# Violin plot
violin_data = [region1_returns, region2_returns]
axes[0].violinplot(violin_data, showmeans=False, showmedians=True)
axes[0].set_title(titles[0])
axes[0].set_ylabel(ylabels[1])
axes[0].set_xticks(ax1xticks)
axes[0].set_xticklabels(ax1xtickslabels)
axes[0].grid(True)

# Density plot
colors = ["blue", "green", "red"]

for data, color, label in zip([stocks, bonds, real_estate], colors, labels):
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
