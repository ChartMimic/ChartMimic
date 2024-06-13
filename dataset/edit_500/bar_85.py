# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data reflecting energy statistics for various countries, scaled for better visualization
categories = ["Healthcare", "Technology", "Education", "Agriculture"][::-1]
total_funding = (
    np.array([1200, 950, 800, 1100][::-1]) / 10
)  # in Million Dollars, scaled down
research_investment_ratio = np.array(
    [60, 70, 90, 80][::-1]
)  # percentage of total funding
projects_completed = (
    np.array([150, 200, 180, 220][::-1]) / 10
)  # in Thousands, scaled down
staff_involved = np.array(
    [40, 55, 35, 50][::-1]
)  # in Thousands, scaled down

categories2 = ["Transport", "Finance", "Retail", "Energy"][::-1]
total_funding2 = (
    np.array([900, 750, 1000, 650][::-1]) / 10
)  # in Million Dollars, scaled down
research_investment_ratio2 = np.array(
    [85, 60, 75, 95][::-1]
)  # percentage of total funding
projects_completed2 = (
    np.array([110, 50, 160, 90][::-1]) / 10
)  # in Thousands, scaled down
staff_involved2 = (
    np.array([90, 20, 130, 70][::-1]) / 10
)  # in Thousands, scaled down

labels = [
    "Total Funding (10^2 Million $)",
    "Research Investment Ratio (%)",
    "Projects Completed (10^1 Thousands)",
    "Staff Involved (10^1 Thousands)",
]
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Stacked Bar Chart in subplots
fig, axs = plt.subplots(2, 1, figsize=(8, 8), sharex=True)  # 2 rows, 1 column
bar_width = 0.8
y_pos = range(len(categories))
y_pos2 = range(len(categories2))

colors = ["tomato", "wheat", "#81acce", "darkseagreen"]

data_ratios = [
    total_funding,
    research_investment_ratio,
    projects_completed,
    staff_involved,
]
data_ratios2 = [
    total_funding2,
    research_investment_ratio2,
    projects_completed2,
    staff_involved2,
]

axs[0].invert_yaxis()  # labels read top-to-bottom
axs[0].set_yticks(y_pos)
axs[0].set_yticklabels(categories)
axs[0].grid(axis="x", color="gray", linestyle="--", linewidth=0.5)
axs[0].set_axisbelow(True)

axs[1].invert_yaxis()  # labels read top-to-bottom
axs[1].set_yticks(y_pos2)
axs[1].set_yticklabels(categories2)
axs[1].grid(axis="x", color="gray", linestyle="--", linewidth=0.5)
axs[1].set_axisbelow(True)

# Plot each ratio on separate subplots
for idx, data_ratio in enumerate(data_ratios[:3]):
    lefts = np.zeros(len(categories))
    for data, color, label in zip(data_ratios, colors, labels):
        axs[0].barh(
            y_pos,
            data,
            bar_width,
            left=lefts,
            color=color,
            label=label if idx == 0 else "",
        )
        lefts += data

for idx, data_ratio in enumerate(data_ratios2[:3]):
    lefts = np.zeros(len(categories2))
    for data, color, label in zip(
        data_ratios2, colors, labels
    ):  # Use data_ratios2 here
        axs[1].barh(
            y_pos2,
            data,
            bar_width,
            left=lefts,
            color=color,
            label=label if idx == 0 else "",
        )
        lefts += data
fig.legend(labels, loc="upper center", bbox_to_anchor=(0.5, 1.1), ncol=2)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save the figure
plt.tight_layout()
plt.savefig('bar_85.pdf', bbox_inches='tight')
