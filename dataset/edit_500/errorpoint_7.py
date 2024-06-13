import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# example data
# Generating new data
x = np.arange(0.1, 10, 0.5)
y = np.log(x)
error = 0.1 + 0.3 * x
lower_error = 0.5 * error
upper_error = error
asymmetric_error = [lower_error, upper_error]
title = "logarithmic variable, asymmetric error"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
fig, (ax0, ax1) = plt.subplots(figsize=(10, 4), ncols=2, sharex=True)

ax0.errorbar(x, y, yerr=error, fmt="o", color="#b383b9")
ax0.set_title(title)

ax1.errorbar(x, y, xerr=asymmetric_error, fmt="o", color="#4b9c7a")
ax1.set_title(title)
ax1.set_yscale("log")

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig('errorpoint_7.pdf', bbox_inches='tight')
