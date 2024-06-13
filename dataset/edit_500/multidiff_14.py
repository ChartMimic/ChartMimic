import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Sample data for the line plot
x = np.array([0, 10000, 20000, 30000, 40000, 50000])  # Balances in dollars
y = np.array([-2.5, -2.3, -2.1, -1.7, -1.5, -0.7])  # Corresponding loss in percentage
error = np.array([0.1, 0.15, 0.12, 0.18, 0.2, 0.22])  # Standard deviation of loss percentage

# Sample data for the box plot (e.g., quarterly returns for different investment strategies)
data = [np.random.normal(5, 1.5, 100) for _ in range(5)]
positions = [0, 10000, 20000, 30000, 40000]  # Positions representing different time intervals or accounts
# Add scatter data points (e.g., anomaly returns)
scatters_data = np.random.normal(0.5, 0.1, len(positions))

titles = ["(a) Account Balance vs Loss", "(b) Quarterly Returns"]
xlabels = ["Account Balance ($)", "Time Period (quarters)"]
ylabels = ["Loss (%)", "Return (%)"]
xtickslabels = [["0", "10k", "20k", "30k", "40k", "50k"], ["Q1", "Q2", "Q3", "Q4", "Q5"]]
yticks = [np.arange(-0.5, -3.0, -0.5), np.arange(0, 10, 2)]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create figure and axes
fig, axs = plt.subplots(2, 1, figsize=(5, 6))

# Line plot
axs[0].errorbar(
    x,
    y,
    yerr=error,
    fmt="o-",
    ecolor="lightgray",
    markersize=8,
    linewidth=1,
    color="black",
)
axs[0].fill_between(x, y - error, y + error, color="lightgray", alpha=0.5)
axs[0].set_title(titles[0])
axs[0].set_xlabel(xlabels[0])
# axs[0].set_ylabel('Loss')
axs[0].grid(True)
axs[0].set_xticks(x)
axs[0].set_xticklabels(xtickslabels[0])
axs[0].set_yticks(yticks[0])

# Box plot
# set all linewidth to 1
axs[1].boxplot(
    data,
    positions=positions,
    widths=5000,
    showfliers=False,
    boxprops=dict(color="grey", linewidth=2),
    medianprops=dict(color="grey", linewidth=2),
    whiskerprops=dict(color="grey", linewidth=2),
    capprops=dict(color="grey", linewidth=2),
)
axs[1].set_title(titles[1])
axs[1].set_xlabel(xlabels[1])
axs[1].set_ylabel(ylabels[1])
axs[1].yaxis.grid(True)
axs[1].set_xticks(positions)
axs[1].set_xticklabels(xtickslabels[1])
axs[1].set_yticks(yticks[1])

axs[1].scatter(positions, scatters_data, marker="^", color="gray", s=100, zorder=3)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout
plt.tight_layout()

plt.savefig('multidiff_14.pdf', bbox_inches='tight')
