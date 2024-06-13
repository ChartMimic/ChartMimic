# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
x = np.linspace(50, 750, 5)
y_data = {
    "Traffic": np.random.normal(0.18, 0.2, (2, 5)).cumsum(axis=1),
    "ETMm2": np.random.normal(0.12, 0.2, (2, 5)).cumsum(axis=1),
    "ETTh2": np.abs(
        np.sin(np.linspace(0, 3, 5)) * 0.1
        + np.array([[0.15, 0.18, 0.16, 0.17, 0.15], [0.2, 0.22, 0.21, 0.19, 0.2]])
    ),
    "ECL": np.random.exponential(0.2, (2, 5))
    + np.array([[0.3, 0.32, 0.34, 0.35, 0.33], [0.28, 0.3, 0.31, 0.29, 0.27]]),
}
# Axes Limits and Labels
xlabel_value = "Time (s)"
xticks_values = [100, 300, 500, 700]

ylabel_value = "Metric Value"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create figure and subplots
fig, axs = plt.subplots(1, 4, figsize=(18, 4), facecolor="whitesmoke")

# Customize colors and markers
colors = ["#1f77b4", "#ff7f0e"]
markers = ["o-", "s-"]
datasets = ["Traffic", "ETMm2", "ETTh2", "ECL"]

for i, ax in enumerate(axs):
    for j in range(2):
        y = y_data[datasets[i]][j]
        ax.plot(x, y, markers[j], label=f"{datasets[i]} Run {j+1}", color=colors[j])
    ax.set_xticks(xticks_values)
    ax.set_title(f"{datasets[i]} Performance", fontsize=16)
    ax.set_xlabel(xlabel_value, fontsize=12)
    ax.set_ylabel(ylabel_value, fontsize=12)
    ax.grid(True, linestyle="--", which="both", color="gray", alpha=0.5)

# Adjust layout and display legend
plt.legend(loc="center", bbox_to_anchor=(-1.5, -0.3), ncol=4, fontsize=14)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig('line_79.pdf', bbox_inches='tight')
