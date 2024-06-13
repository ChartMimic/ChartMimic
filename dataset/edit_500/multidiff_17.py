import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data for Area Chart - Represents percentage increases in knowledge by subject area

# Investment levels
n_levels = ["0", "1", "2", "3", "4", "5"]
low_risk = np.array([30, 11, 23, 17, 16, 15])
medium_risk = np.array([20, 13, 25, 13, 15, 5])
high_risk = np.array([18, 15, 10, 8, 7, 6])

# Cumulative data for the stacked Area chart
cumulative_low_risk = low_risk
cumulative_medium_risk = cumulative_low_risk + medium_risk
cumulative_high_risk = cumulative_medium_risk + high_risk

# Data for Bar Chart - Shows the number of investments by financial subdomain
domains = [
    "Equity",
    "Bonds",
    "Real Estate",
    "Commodities",
    "Forex",
    "Cryptocurrency",
    "Options",
]
investments = [200, 280, 320, 340, 260, 430, 210]
titles = ["Investment Returns by Risk Level", "Number of Investments by Financial Subdomain"]
xlabels = ["Investment Level", "Financial Subdomain"]
ylabels = ["Cumulative Return (%)", "Number of Investments"]
ax1labels = ["Low Risk","Medium Risk", "High Risk"]

# Placeholder to show where the area chart and bar chart would be displayed. Actual plotting code is not included.

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Creating the subplot layout
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

# Plotting the Area Chart
ax1.fill_between(
    n_levels, 0, cumulative_low_risk, label=ax1labels[0], color="#008fd5", alpha=0.6
)
ax1.fill_between(
    n_levels,
    cumulative_low_risk,
    cumulative_medium_risk,
    label=ax1labels[1],
    color="#fc4f30",
    alpha=0.6,
)
ax1.fill_between(
    n_levels,
    cumulative_medium_risk,
    cumulative_high_risk,
    label=ax1labels[2],
    color="#e5ae38",
    alpha=0.6,
)
ax1.set_title(titles[0])
ax1.set_xlabel(xlabels[0])
ax1.set_ylabel(ylabels[0])
ax1.legend(loc="upper left")

# Plotting the Bar Chart
ax2.bar(domains, investments, color="#30a2da")
ax2.set_title(titles[1])
ax2.set_xlabel(xlabels[1])
ax2.set_ylabel(ylabels[1])
ax2.set_xticklabels(domains, rotation=45)

# ===================
# Part 4: Saving Output
# ===================
# Adjusting layout and saving the figure
plt.tight_layout()
plt.savefig('multidiff_17.pdf', bbox_inches='tight')
