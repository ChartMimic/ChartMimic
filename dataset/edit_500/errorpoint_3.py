import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data for plotting
authors = [
    "This study*",
    "Smith et al.",
    "Smith et al.",
    "Johnson et al.",
    "Lee et al.",
    "Lee et al.",
    "Miller et al.",
    "Miller et al.",
    "Davis et al.",
    "Davis et al.",
]
values = [
    4.572,
    4.635,
    4.589,
    4.625,
    4.598,
    4.612,
    4.620,
    4.629,
    4.647,
    4.610,
]
errors = [
    [0.025, -0.023],
    [0.018, -0.017],
    [0.016, -0.015],
    [0.030, -0.032],
    [0.022, -0.021],
    [0.027, -0.026],
    [0.019, -0.018],
    [0.021, -0.020],
    [0.025, -0.024],
    [0.026, -0.025],
]
methods = [
    "Method A+Sample X",
    r"${Method B+Sample Y}$",
    r"${Method C+Sample Z}$",
    r"Method D+${Sample W}$",
    "Method E+Sample X (Condition 1)",
    "Method F+Sample Y (Condition 2)",
    "Method G+Sample Z (Condition 3)",
    "Method H+Sample W",
    r"${Method I+Sample V}$",
    r"${Method J+Sample U}$",
]
xticks = np.arange(4.5, 4.7, 0.05)
xlim = [4.5, 4.7]
xvline = 4.6
xvspan = [4.58, 4.62]

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
ax.axvspan(xvspan[0],xvspan[1], color="purple", alpha=0.3)

# Text for methods with adjusted font size
for i, method in enumerate(methods):
    ax.text(4.7, i, method, va="center", ha="left", fontsize=11)

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
plt.savefig('errorpoint_3.pdf', bbox_inches='tight')
