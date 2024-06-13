import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Generating new data
x = np.linspace(0, 30, 9)
y = np.random.uniform(120, 210, 9)
left_error = np.random.uniform(5, 15, 9)
right_error = np.random.uniform(5, 15, 9)
title = "pressure measurements, asymmetric error"
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
fig, ax = plt.subplots(figsize=(10, 7))
ax.errorbar(
    x,
    y,
    xerr=[left_error, right_error],
    fmt="o",
    color="#6d32a8",
    capsize=0,
    label="errorbar",
)
for i, (xi, yi, lefterror, righterror) in enumerate(zip(x, y, left_error, right_error)):
    ax.text(
        xi - 0.8 * lefterror,
        yi + 0.1,
        r"${-%.1f}$" % (lefterror),
        va="center",
        ha="center",
    )
    ax.text(
        xi + 0.8 * righterror,
        yi + 0.1,
        r"${+%.1f}$" % (righterror),
        va="center",
        ha="center",
    )
ax.set_title(title)
ax.legend(loc="upper left")
ax.xaxis.grid(True)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig('errorpoint_9.pdf', bbox_inches='tight')
