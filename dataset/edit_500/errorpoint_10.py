import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================

labels = ["alpha", "beta", "gamma"]

x = np.linspace(0, 25, 6)
y1 = np.random.uniform(50, 100, 6)
y2 = np.random.uniform(60, 120, 6)
y3 = np.random.uniform(30, 80, 6)
error1 = [np.random.uniform(5, 10, 6), np.random.uniform(5, 10, 6)]
error2 = [np.random.uniform(8, 15, 6), np.random.uniform(8, 15, 6)]  # Symmetric horizontal error
error3 = np.random.uniform(4, 10, 6)
title = "Sensor Readings, Symmetric Error"
xvline = 12

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create a figure with three subplots and shared x-axis
fig, (ax0, ax1, ax2) = plt.subplots(figsize=(6, 9), nrows=3, sharex=True)
colors1 = plt.get_cmap("Set2")(np.linspace(0.2, 0.8, 6))
colors2 = plt.get_cmap("coolwarm_r")(np.linspace(0.2, 0.8, 6))
# First subplot with symmetric vertical error bars
for i in range(len(x)):
    ax0.errorbar(
        x[i],
        y1[i],
        yerr=[[error1[0][i]], [error1[1][i]]],
        fmt="o",
        color=colors1[i],
        capsize=4,
    )
    ax0.text(x[i] - 0.5, y1[i], f"{y1[i]:.2f}", fontsize=8, ha="right")
ax0.set_title(title)
ax0.axhline(y=14.5, linestyle="--", color="#192770")
ax0.yaxis.grid(True)
ax0.xaxis.grid(False)

# Second subplot with symmetric horizontal error bars
for i in range(len(x)):
    ax1.errorbar(
        x[i],
        y2[i],
        xerr=[[error2[0][i]], [error2[1][i]]],
        fmt="o",
        color=colors2[i],
        markersize=8,
    )
    ax1.text(x[i] + 0.5, y2[i] + 0.1, f"{y2[i]:.2f}", fontsize=8, ha="left")
ax1.set_title(title)
ax1.axvline(x=xvline, linestyle="--", color="#265b2b")
ax1.xaxis.grid(True)
ax1.yaxis.grid(False)

# Third subplot with symmetric vertical error bars
ax2.errorbar(x, y3, yerr=error3, fmt="*", color="#465d87", capsize=2)
ax2.set_title(title)
ax2.legend([labels[2]])
ax2.yaxis.grid(True)
ax2.xaxis.grid(False)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and display the plot
plt.tight_layout()
plt.savefig('errorpoint_10.pdf', bbox_inches='tight')
