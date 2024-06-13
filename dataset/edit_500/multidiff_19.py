import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================

# ErrorBar Plot Data
# Countries
# Countries and their average investment returns
countries = ["USA", "UK", "Germany", "France", "Italy", "Spain"]
investment_returns = [6.4, 7.6, 8.0, 7.8, 6.2, 5.2]
errors = [0.5, 0.4, 0.3, 0.5, 0.6, 0.4]

# ErrorPoint Plot Data
investment_types = ["Stocks", "Bonds", "Real Estate", "Commodities", "Forex"]
occurrences = np.random.uniform(5, 15, len(investment_types))
std_devs = np.random.uniform(0.5, 2.0, len(investment_types))
dataset_mean = np.mean(occurrences)

# Titles and labels for the plots
titles = ["Average Investment Returns by Country", "Investment Occurrence Rates by Type"]
ylabels = ["Investment Return (%)", "Occurrences (%)"]
ylim = [0, 16]
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# ErrorBar Plot
# Create figure and axes for the subplots
fig, axes = plt.subplots(2, 1, figsize=(8, 10))

axes[0].bar(
    countries, investment_returns, yerr=errors, color="#ff9b54", capsize=5, ecolor="grey"
)
axes[0].set_title(titles[0])
axes[0].set_ylabel(ylabels[0])
axes[0].grid(True)

# ErrorPoint Plot
axes[1].errorbar(
    investment_types,
    occurrences,
    yerr=std_devs,
    fmt="o",
    color="#1b9aaa",
    ecolor="#1b9aaa",
    capsize=5,
    ms=8,
)
axes[1].axhline(y=dataset_mean, color="grey", linestyle="--")
axes[1].set_title(titles[0])
axes[1].set_ylabel(ylabels[0])
axes[1].set_ylim(ylim)
axes[1].grid(True)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout to avoid overlap and save the figure
plt.tight_layout()
plt.savefig('multidiff_19.pdf', bbox_inches='tight')
