# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# example data
x = np.array([0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0])
y = np.exp(-x)
xerr = 0.2
yerr = 0.15

# lower & upper limits of the error
lolims = np.array([0.3, 0, 0.4, 0, 0, 1, 0, 0, 1.2, 0], dtype=bool)
uplims = np.array([0.5, 0, 0, 0.1, 0, 0.5, 0, 0.3, 0, 0], dtype=bool)
ls = "None"
labels = [
    "standard",
    "upper limits",
    "lower limits",
    "upper and lower limits",
    "random",
]
title = "Errorbar upper and lower limits"
xlim = [0, 5.5]
colors =[ "#b2e7aa", "#fae18f", "#d75949", "#f0906d", "#a1a8d6"]
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
fig, ax = plt.subplots(figsize=(9, 6))

# standard error bars
ax.errorbar(x, y, xerr=xerr, yerr=yerr, label=labels[0], linestyle=ls, color=colors[0])
# including upper limits
ax.errorbar(
    x, y + 1, xerr=xerr, yerr=yerr, uplims=uplims, label=labels[1], linestyle=ls, color=colors[1]
)

# including lower limits
ax.errorbar(
    x, y + 0.25, xerr=xerr, yerr=yerr, lolims=lolims, label=labels[2], linestyle=ls, color=colors[2]
)

# including upper and lower limits
ax.errorbar(
    x,
    y + 1.25,
    xerr=xerr,
    yerr=yerr,
    lolims=lolims,
    uplims=uplims,
    marker="o",
    markersize=8,
    label=labels[3],
    linestyle=ls,
    color=colors[3],
)

# Plot a series with lower and upper limits in both x & y
# constant x-error with varying y-error
xerr = 0.2
yerr = np.full_like(x, 0.2)
yerr[[3, 6]] = 0.3

# mock up some limits by modifying previous data
xlolims = lolims
xuplims = uplims
lolims = np.zeros_like(x)
uplims = np.zeros_like(x)
lolims[[6]] = True  # only limited at this index
uplims[[3]] = True  # only limited at this index

# do the plotting
ax.errorbar(
    x,
    y + 2.1,
    xerr=xerr,
    yerr=yerr,
    xlolims=xlolims,
    xuplims=xuplims,
    uplims=uplims,
    lolims=lolims,
    marker="o",
    markersize=8,
    linestyle="none",
    label=labels[4],
    color=colors[4],
)

# tidy up the figure
ax.set_xlim(xlim)
ax.set_title(title)
plt.legend(bbox_to_anchor=(0.5, 1.15), ncol=5, loc="upper center")

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig("errorpoint_6.pdf", bbox_inches="tight")
