import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Updated data
categories = [
    "Word", "Excel", "PowerPoint", "Outlook", "Teams", "OneNote", "SharePoint", 
    "Azure", "Dynamics", "Intune", "Yammer", "Sway", "Planner", "Power BI", 
    "PowerApps", "Stream", "Whiteboard", "Lists", "Forms", "Project", "Access", 
    "Avg"
]

# Generate three lists
FeatureOpt, PerformanceOpt, SecurityOpt = np.random.dirichlet(np.ones(3), size=len(categories)).T

FeatureOpt = FeatureOpt * 100
PerformanceOpt = PerformanceOpt * 100
SecurityOpt = SecurityOpt * 100

# Stacked bar chart setup
bar_width = 0.9
r = np.arange(len(categories))
labels = ["FeatureOpt", "PerformanceOpt", "SecurityOpt"]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plot
fig, ax = plt.subplots(figsize=(8, 4))
bar1 = ax.bar(
    r,
    FeatureOpt,
    color="white",
    edgecolor="#4f7c56",
    hatch="\\\\\\",
    width=bar_width,
    label=labels[0],
)
bar2 = ax.bar(
    r,
    PerformanceOpt,
    bottom=FeatureOpt,
    color="white",
    edgecolor="#d3c475",
    hatch="--",
    width=bar_width,
    label=labels[1],
)
bar3 = ax.bar(
    r,
    SecurityOpt,
    bottom=FeatureOpt + PerformanceOpt,
    color="white",
    edgecolor="#2d4aac",
    hatch="++",
    width=bar_width,
    label=labels[2],
)

# Labels, title and legend
# ax.set_xlabel('Benchmarks', fontsize=12)
# ax.set_ylabel('Optimization (%)', fontsize=12)

ax.set_xticks(r)
ax.set_xticklabels(categories, rotation=-45, ha="center")
ax.set_yticks(np.arange(0, 101, 20))
ax.set_ylim(0, 100)
ax.set_yticklabels(["{}%".format(i) for i in range(0, 101, 20)])
ax.legend(loc="upper center", bbox_to_anchor=(0.5, 1.15), ncol=3)

# Grid lines
ax.yaxis.grid(True, linestyle="--")

# ===================
# Part 4: Saving Output
# ===================
# Show plot
plt.tight_layout()
plt.savefig('bar_34.pdf', bbox_inches='tight')
