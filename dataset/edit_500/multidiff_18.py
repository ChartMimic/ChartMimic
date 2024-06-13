import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data for Area Chart
n_aug = ["2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022"]
equities_progress = np.random.randint(10, 50, len(n_aug))
bonds_progress = np.random.randint(5, 45, len(n_aug))
real_estate_progress = np.random.randint(0, 40, len(n_aug))
# Data for Box Plot representing innovation gaps across different financial sectors
data_equities = np.random.normal(20, 10, 100)
data_bonds = np.random.normal(40, 12, 100)
data_real_estate = np.random.normal(30, 15, 100)
data_forex = np.random.normal(50, 18, 100)
data = [data_equities, data_bonds, data_real_estate, data_forex]

# Labels and titles for the plots
ax1labels = ["Equities", "Bonds", "Real Estate"]
titles = ["Investment Advancements Over Years", "Innovation Gaps Across Financial Sectors"]
xlabels = ["Year"]
ax2xtickslabels = ["Equities", "Bonds", "Real Estate", "Forex"]
ylabels = ["Investment Progress (%)", "Innovation Gap (%)"]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create a figure with two subplots in a vertical layout
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 10))

# ----- Area Chart for Technological Advancements -----
# Calculate cumulative values for stacked area chart
cumulative_hardware = equities_progress
cumulative_software = cumulative_hardware + bonds_progress
cumulative_ai = cumulative_software + real_estate_progress

# Plotting Area Chart
ax1.fill_between(
    n_aug, 0, cumulative_hardware, label=ax1labels[0], color="#1f77b4", alpha=0.7
)
ax1.fill_between(
    n_aug,
    cumulative_hardware,
    cumulative_software,
    label=ax1labels[1],
    color="#ff7f0e",
    alpha=0.7,
)
ax1.fill_between(
    n_aug, cumulative_software, cumulative_ai, label=ax1labels[2], color="#2ca02c", alpha=0.7
)

ax1.set_title(titles[0])
ax1.set_xlabel(xlabels[0])
ax1.set_ylabel(ylabels[0])
ax1.legend(loc="upper left")
ax1.grid(True)

# ----- Box Plot for Innovation Gaps in Tech Companies -----
# Creating Box Plot
bp = ax2.boxplot(data, patch_artist=True, notch=False, showfliers=False)

# Customizing boxplot colors
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"]
for patch, color in zip(bp["boxes"], colors):
    patch.set_facecolor(color)
for median in bp["medians"]:
    median.set(color="black")

# Setting labels and titles
ax2.set_xticklabels(ax2xtickslabels)
ax2.set_ylabel(ylabels[1])
ax2.set_title(titles[1])
ax2.yaxis.grid(True)
ax2.spines["top"].set_visible(False)
ax2.spines["right"].set_visible(False)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig('multidiff_18.pdf', bbox_inches='tight')
