# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
tasks = np.arange(1, 11)
baCE = np.linspace(90, 60, 10) + np.random.normal(0, 3, 10)
lwf = np.linspace(75, 50, 10) + np.random.normal(0, 3, 10)
ewc = np.linspace(50, 30, 10) + np.random.normal(0, 3, 10)
seq = np.linspace(20, 15, 10) + np.random.normal(0, 1, 10)

# Axes Limits and Labels
xlabel_value = "Task"
xticks_values = np.arange(1, 11, 1)

ylabel_value = "Average Accuracy (%)"
ylim_values = [0, 100]

# Labels
label_BaCE="BaCE"
label_EWC="EWC"
label_LWF="LWF"
label_SEQ="SEQ"

# Titles
title_1 = "Performance Comparison: BaCE vs EWC"
title_2 = "Performance Comparison: LWF vs SEQ"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create a figure and axis
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 3))

# Plot the data in each subplot
ax1.plot(
    tasks,
    baCE,
    marker="s",
    markersize=7,
    color="#2171b5",
    mfc="w",
    mew=2,
    label=label_BaCE,
    linewidth=2,
)
ax1.plot(
    tasks,
    ewc,
    marker="D",
    markersize=7,
    color="#bdd7e7",
    mfc="w",
    mew=2,
    label=label_EWC,
    linewidth=2,
)
ax1.set_title(title_1, fontsize=12)
ax1.set_xlabel(xlabel_value, fontsize=14)
ax1.set_ylabel(ylabel_value, fontsize=14)
ax1.set_ylim(ylim_values)
ax1.set_xticks(xticks_values)
ax1.legend()
ax1.grid(True, linestyle="--", alpha=0.6)

ax2.plot(
    tasks,
    lwf,
    marker="v",
    markersize=7,
    color="#e7969c",
    mfc="w",
    mew=2,
    label=label_LWF,
    linewidth=2,
)
ax2.plot(
    tasks,
    seq,
    marker="o",
    markersize=4,
    color="#de9ed6",
    mfc="w",
    mew=2,
    label=label_SEQ,
    linewidth=2,
)
ax2.set_title(title_2, fontsize=12)
ax2.set_xlabel(xlabel_value, fontsize=14)
ax2.set_ylabel(ylabel_value, fontsize=14)
ax2.set_ylim(ylim_values)
ax2.set_xticks(xticks_values)
ax2.legend()
ax2.grid(True, linestyle="--", alpha=0.6)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout for better spacing and display
plt.tight_layout()

# Show the plot
plt.savefig('line_65.pdf', bbox_inches='tight')
