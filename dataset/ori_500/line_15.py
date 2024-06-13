# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)

import matplotlib.ticker as ticker

# ===================
# Part 2: Data Preparation
# ===================
# Sample data to mimic the trends in the provided image
tasks = np.arange(1, 21)
baCE = np.linspace(90, 60, 20) + np.random.normal(0, 3, 20)
lwf = np.linspace(75, 50, 20) + np.random.normal(0, 3, 20)
ewc = np.linspace(50, 30, 20) + np.random.normal(0, 3, 20)
seq = np.linspace(20, 15, 20) + np.random.normal(0, 1, 20)

# Axes Limits and Labels
xlabel_value = "Task"
xlim_values = [0.5, 20.5]
xticks_values = np.arange(1, 21, 1)

ylabel_value = "Average Accuracy (%)"
ylim_values = [0, 100]
yticks_values = np.arange(0, 101, 10)

# Labels
label_BaCE = "BaCE"
label_LWF = "LWF"
label_EWC = "EWC"
label_SEQ = "SEQ"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plotting the data
plt.figure(figsize=(8, 6))
plt.plot(
    tasks,
    baCE,
    marker="s",
    markersize=7,
    color="#393b79",
    mfc="w",
    mew=2,
    label=label_BaCE,
    linewidth=2,
)
plt.plot(
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
plt.plot(
    tasks,
    ewc,
    marker="D",
    markersize=7,
    color="#a55194",
    mfc="w",
    mew=2,
    label=label_EWC,
    linewidth=2,
)
plt.plot(
    tasks,
    seq,
    marker="o",
    markersize=4,
    color="#de9ed6",
    mfc="w",
    mew=2,
    label=label_SEQ,
    linewidth=2,
)  # Adjusted color for SEQ

# Set y-axis to only display specific ticks and extend y-axis to leave space at top
plt.yticks(yticks_values)
plt.ylim(ylim_values)  # Adjusted y-axis limit

# Setting x-axis ticks
plt.xticks(xticks_values)  # Ticks from 1 to 20, interval of 1
plt.xlim(xlim_values)  # Slightly beyond 1 and 20 for a margin

# Adding labels and title
plt.xlabel(xlabel_value, fontsize=16)
plt.ylabel(ylabel_value, fontsize=16)

# Adding legend with a different style and position
plt.legend(frameon=True, fontsize=11, loc="upper right")

# Adding gridlines
plt.grid(True, linestyle="-", linewidth=0.5, axis="y", alpha=1)

# Adjusting tick label size
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# ===================
# Part 4: Saving Output
# ===================
# Adjusting layout to reduce white space
plt.tight_layout()
plt.savefig('line_15.pdf', bbox_inches='tight')
