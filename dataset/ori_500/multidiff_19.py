# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================

# ErrorBar Plot Data
# Countries
countries = ["USA", "UK", "Germany", "France", "Italy", "Spain"]
# Hypothetical average crime rates
crime_rates = [3.2, 2.8, 2.5, 2.9, 3.1, 2.6]
# Standard errors for the above crime rates
errors = [0.3, 0.25, 0.2, 0.3, 0.35, 0.25]

# ErrorPoint Plot Data
# Types of crimes
crime_types = ["Theft", "Assault", "Fraud", "Drug Trafficking", "Vandalism"]
# Randomly generated means and standard deviations for occurrences
occurrences = np.random.uniform(0.5, 1.5, len(crime_types))
std_devs = np.random.uniform(0.05, 0.2, len(crime_types))
dataset_mean = np.mean(occurrences)
titles=["Average Legal Crime Rates by Country", "Crime Occurrence Rates by Type"]
ylabels=["Crime Rate per 100,000 Inhabitants", "Occurrences (per 100,000 Inhabitants)"]
ylim=[0, 2]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create figure and axes for the subplots
fig, axes = plt.subplots(2, 1, figsize=(8, 10))

# ErrorBar Plot
axes[0].bar(
    countries, crime_rates, yerr=errors, color="#ff9b54", capsize=5, ecolor="grey"
)
axes[0].set_title(titles[0])
axes[0].set_ylabel(ylabels[0])
axes[0].grid(True)

# ErrorPoint Plot
axes[1].errorbar(
    crime_types,
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
