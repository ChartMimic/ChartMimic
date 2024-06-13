import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Generating new data
x = np.linspace(0, 20, 10)
y = np.random.uniform(200, 400, 10)
upper_error = np.random.uniform(20, 50, 10)
down_error = np.random.uniform(10, 30, 10)
left_error = [0.5] * 10
right_error = [1.0] * 10
title = "temperature readings, asymmetric error"
xhline = 300
label = "temperature errorbar"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
fig, ax = plt.subplots(figsize=(10, 7))
ax.errorbar(
    x,
    y,
    xerr=[left_error, right_error],
    yerr=[down_error, upper_error],
    fmt="*",
    color="#4b9c7a",
    capsize=3,
    label=label,
)
for i, (xi, yi, uperror, downerror) in enumerate(zip(x, y, upper_error, down_error)):
    ax.text(
        xi + 0.3, yi + 0.5 * uperror, r"${+%.3f}$" % (uperror), va="center", ha="center"
    )
    ax.text(
        xi + 0.3,
        yi - 0.5 * downerror,
        r"${-%.3f}$" % (downerror),
        va="center",
        ha="center",
    )
ax.set_title(title)
ax.legend()
ax.axhline(xhline, color="y", linestyle="--")

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig('errorpoint_8.pdf', bbox_inches='tight')
