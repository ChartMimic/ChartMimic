import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data representing social statistics for three different cities
categories = ["Manufacturing", "Technology", "Healthcare"]
metrics = [
    "Innovation Index",
    "Employee Satisfaction",
    "Market Share Growth",
    "Environmental Impact",
]
performance = np.array(
    [
        [65, 85, 75, 50], 
        [70, 90, 80, 60], 
        [60, 75, 85, 55],  
    ]
)
errors = np.array(
    [
        [4, 5, 6, 5], 
        [5, 6, 7, 6],  
        [6, 7, 5, 6],  
    ]
)
ylim = [40, 100]
ylabel = "Index/Percentage"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Figure size to match a 3x1 subplot layout
fig, axes = plt.subplots(3, 1, figsize=(10, 9), sharex=True)

# Colors, choosing a different palette to differentiate the plots
colors = ["#8e44ad", "#3498db", "#e74c3c", "#f1c40f"]

# Plotting bars
for i, ax in enumerate(axes):
    for j, metric in enumerate(metrics):
        ax.bar(
            j,
            performance[i, j],
            width=0.8,
            color=colors[j],
            yerr=errors[i, j],
            capsize=0,
            label=metric if i == 0 else "",
        )

    # Setting x-axis labels, y-axis limits, and titles
    ax.set_xticks(range(len(metrics)))
    ax.set_xticklabels(metrics, rotation=45)
    ax.set_ylim(ylim)
    ax.set_xlabel(f"({chr(97+i)}) {categories[i]}")
    ax.set_ylabel(ylabel)
    ax.yaxis.grid(True)
    ax.set_axisbelow(True)

# Adding a legend outside of the plot on top
fig.legend(loc="upper center", bbox_to_anchor=(0.5, 1.05), ncol=len(metrics))

# ===================
# Part 4: Saving Output
# ===================
# Adjusting layout to prevent overlap and ensure labels are visible
plt.tight_layout()
plt.savefig('errorbar_19.pdf', bbox_inches='tight')
