# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data for plotting
authors = [
    "This work*",
    "Shah et al.",
    "Shah et al.",
    "Banerjee et al.",
    "Favale et al.",
    "Favale et al.",
    "Gomez-Valent",
    "Gomez-Valent",
    "Benisty et al.",
    "Benisty et al.",
]
values = [
    -19.353,
    -19.257,
    -19.394,
    -19.404,
    -19.314,
    -19.344,
    -19.362,
    -19.374,
    -19.220,
    -19.380,
]
errors = [
    [0.073, -0.078],
    [0.028, -0.027],
    [0.018, -0.017],
    [0.099, -0.104],
    [0.05, 0.108],
    [0.116, -0.090],
    [0.078, -0.067],
    [0.080, -0.080],
    [0.200, -0.200],
    [0.200, -0.200],
]
methods = [
    "CC+Pantheon+",
    r"${θ_{BAO}+r_{CMB}+d_{Pantheon}}$",
    r"${α_{BAO}+r_CMB+d_{Pantheon}}$",
    r"CC+${r_{BAO}}$+Pantheon+ (Ωk ≠ 0)",
    "CC+BAO+Pantheon+ (Ωk ≠ 0)",
    "CC+Pantheon+ (Ωk ≠ 0)",
    "CC+BAO+Pantheon (Ωk ≠ 0)",
    "CC+BAO+Pantheon",
    r"${α_{BAO}+r_{SHOES}+Pantheon}$",
    r"${α_{BAO}+r_{CMB}+d_{Pantheon}}$",
]
xticks = np.arange(-19.6, -19.0, 0.1)
xlim = [-19.6, -19.0]
xvline = -19.219
xvspan = [-19.187, -19.251]


# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plotting
fig, ax = plt.subplots(
    figsize=(10, 8)
)  # Adjust the figsize to match the original image's dimensions

# Error bars with different positive and negative values
for i, (author, value, error) in enumerate(zip(authors, values, errors)):
    ax.errorbar(
        value,
        i,
        xerr=[[abs(error[1])], [error[0]]],
        fmt="o",
        color="black",
        ecolor="black",
        capsize=3,
    )
    ax.text(
        value,
        i - 0.15,
        r"$%.3f^{+%.3f} _{-%.3f}$" % (value, error[0], abs(error[1])),
        va="center",
        ha="center",
        fontsize=9,
    )
# Highlighted region with adjusted color and alpha
ax.axvspan(xvspan[0], xvspan[1], color="purple", alpha=0.3)

# Text for methods with adjusted font size
for i, method in enumerate(methods):
    ax.text(-19.0, i, method, va="center", ha="left", fontsize=11)

# Set labels and title
ax.set_yticks(range(len(authors)))
ax.set_yticklabels(authors)
ax.set_xlabel(r"$M_B$", fontsize=12)
ax.set_xlim(xlim)
ax.invert_yaxis()  # Invert y-axis to match the original image
ax.axvline(x=xvline, linestyle="--", color="red")
# Adjust x-axis ticks and labels
ax.set_xticks(xticks)
ax.set_xticklabels([f"{x:.1f}" for x in xticks])

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save/show the plot
plt.tight_layout()
plt.savefig("errorpoint_3.pdf", bbox_inches="tight")
