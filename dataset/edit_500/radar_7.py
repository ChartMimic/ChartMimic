import numpy as np; np.random.seed(0)

import matplotlib.pyplot as plt
from math import pi

# ===================
# Part 2: Data Preparation
# ===================
# Define the data for each line
labels = np.array(
    [
        "revenue",
        "profit_margin",
        "market_share",
        "customer_satisfaction",
        "employee_retention",
        "brand_awareness",
        "net_promoter_score",
        "customer_lifetime_value",
        "lead_conversion_rate",
        "social_media_engagement",
        "website_traffic",
        "sales_growth",
        "operational_efficiency",
        "product_quality",
        "inventory_turnover",
        "return_on_investment",
    ]
)
num_vars = len(labels)

values1 = np.array([50, 55, 60, 70, 65, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
values2 = np.array([40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115])
values3 = np.array([30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105])
labels2=["BizAnalyzer", "MarketMetrics", "CorpInsights"]
yticks=[20, 40, 60, 80, 100]
ytickslabel=["20", "40", "60", "80", "100"]
ylim=[10, 130]
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plot
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Compute angle for each axis
angles = [n / float(num_vars) * 2 * pi for n in range(num_vars)]
values1 = np.concatenate((values1, [values1[0]]))
values2 = np.concatenate((values2, [values2[0]]))
values3 = np.concatenate((values3, [values3[0]]))
angles += angles[:1]

# Draw one axe per variable and add labels
plt.xticks(angles[:-1], labels)

# Draw ylabels
ax.set_rlabel_position(0)
plt.yticks(yticks, ytickslabel, color="black", size=7)
plt.ylim(ylim)

# Plot data
ax.plot(
    angles,
    values1,
    linewidth=1,
    linestyle="solid",
    label=labels2[0],
    color="#971d2b",
    marker="o",
)
ax.fill(angles, values1, "#971d2b", alpha=0.1)

ax.plot(
    angles,
    values2,
    linewidth=1,
    linestyle="dashed",
    label=labels2[1],
    color="#6f98c3",
    marker="s",
)
ax.fill(angles, values2, "#6f98c3", alpha=0.1)

ax.plot(
    angles,
    values3,
    linewidth=1,
    linestyle="dotted",
    label=labels2[2],
    color="#f4c17d",
    marker="D",
)
ax.fill(angles, values3, "#f4c17d", alpha=0.1)

# Add legend
plt.legend(loc="lower left", bbox_to_anchor=(-0.15, -0.1))

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout for better fit and save the plot
plt.tight_layout()
plt.savefig('radar_7.pdf', bbox_inches='tight')
