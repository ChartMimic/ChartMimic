# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data for Area Chart
n_aug = ["2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022"]
hardware_progress = np.array([20, 22, 25, 30, 35, 40, 42, 45])
software_progress = np.array([10, 12, 15, 18, 20, 25, 30, 35])
ai_progress = np.array([5, 8, 12, 17, 23, 30, 35, 40])

# Data for Box Plot
data_big_tech = np.random.normal(50, 10, 100)
data_startups = np.random.normal(30, 15, 100)
data_academia = np.random.normal(20, 20, 100)
data_government = np.random.normal(10, 5, 100)
data = [data_big_tech, data_startups, data_academia, data_government]
ax1labels=["Hardware", "Software", "AI"]
titles=["Technological Advancements", "Innovation Gaps Across Different Sectors in Technology"]
xlabels=["Year"]
ax2xtickslabels=["Big Tech", "Startups", "Academia", "Government"]
ylabels=["Progress (%)", "Innovation Gap (%)"]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create a figure with two subplots in a vertical layout
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 10))

# ----- Area Chart for Technological Advancements -----
# Calculate cumulative values for stacked area chart
cumulative_hardware = hardware_progress
cumulative_software = cumulative_hardware + software_progress
cumulative_ai = cumulative_software + ai_progress

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
