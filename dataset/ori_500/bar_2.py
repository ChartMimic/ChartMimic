# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Sample data
time = np.arange(0, 45, 5)
trot = np.array([0.3, 0.42, 0.5, 0.53, 0.49, 0.45, 0.42, 0.5, 0.52])
pace = np.array([0.2, 0.25, 0.25, 0.25, 0.25, 0.20, 0.25, 0.20, 0.20])
bound = np.array([0.15, 0.15, 0.10, 0.10, 0.10, 0.15, 0.15, 0.15, 0.15])
pronk = np.array([0.1, 0.12, 0.1, 0.07, 0.11, 0.15, 0.13, 0.1, 0.08])
transition = np.array([0.25, 0.06, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05])
width = 2

barlabel = ["trot", "pace", "bound", "pronk", "transition"]
xticks = [0, 10, 20, 30, 40]
xlabel = "Time (s)"
ylabel = "% Experiments"
title = "Gait Distribution Over Time: Policy ORC=111"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Stacked bar chart
plt.figure(figsize=(6, 3))  # Adjusting figure size to match original image dimensions
plt.bar(time, trot, width, color="#529e3f", label=barlabel[0])
plt.bar(time, pace, width, bottom=trot, color="#c53a32", label=barlabel[1])
plt.bar(time, bound, width, bottom=trot + pace, color="#8e69b8", label=barlabel[2])
plt.bar(time, pronk, width, bottom=trot + pace + bound, color="#85594e", label=barlabel[3])
plt.bar(
    time,
    transition,
    width,
    bottom=trot + pace + bound + pronk,
    color="#7f7f7f",
    label=barlabel[4]
)

# Labels and title
plt.xticks(xticks)
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.title(title)

# Legend
plt.legend(loc="upper right", bbox_to_anchor=(1.4, 1))

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig("bar_2.pdf", bbox_inches="tight")
