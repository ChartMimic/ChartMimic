# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Placeholder data
m_values = np.logspace(1, 2, 10)
errors_s19 = np.exp(-0.1 * m_values)
errors_s50 = np.exp(-0.2 * m_values - 1)  # Shift up by a factor of 10
errors_s76 = np.exp(-0.3 * m_values - 2)  # Shift up by a factor of 100
errors_s142 = np.exp(-0.4 * m_values - 3)  # Shift up by a factor of 1000
errors_s232 = np.exp(-0.5 * m_values - 4)  # Shift up by a factor of 10000

# Create error bands
errors_s19_err = errors_s19 * 0.4
errors_s50_err = errors_s50 * 0.5
errors_s76_err = errors_s76 * 0.5
errors_s142_err = errors_s142 * 0.6
errors_s232_err = errors_s232 * 0.6
xlabel = "number of matvecs m"
ylabels = [
    r"approximation error: ${\| A -\tilde{A}\|_{F}}$",
    r"sparse recovery error: ${\|S ◦ A -\tilde{A}\|_{F}}$",
]
xlim = [6, 1e2]
ylim = [1e-10, 1]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create figure and axes with specified size (width, height)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

# Plot data and curves for the left subplot
ax1.plot(m_values, errors_s19, ".", color="purple", label="s = 19")
ax1.fill_between(
    m_values,
    errors_s19 - errors_s19_err,
    errors_s19 + errors_s19_err,
    color="purple",
    alpha=0.2,
)
# Fit and plot a line
coeffs = np.polyfit(np.log(m_values), np.log(errors_s19), 2)
fit_func = np.poly1d(coeffs)
ax1.plot(m_values, np.exp(fit_func(np.log(m_values))), "k:")

ax1.plot(m_values, errors_s50, ".", color="pink", label="s = 50")
ax1.fill_between(
    m_values,
    errors_s50 - errors_s50_err,
    errors_s50 + errors_s50_err,
    color="pink",
    alpha=0.2,
)
# Fit and plot a line
coeffs = np.polyfit(np.log(m_values), np.log(errors_s50), 2)
fit_func = np.poly1d(coeffs)
ax1.plot(m_values, np.exp(fit_func(np.log(m_values))), "k:")

ax1.set_xscale("log")
ax1.set_yscale("log")
ax1.set_xlabel(xlabel)
ax1.set_ylabel(ylabels[0])

# Plot data and curves for the right subplot
ax2.plot(m_values, errors_s19, ".", color="purple", label="s = 19")
ax2.fill_between(
    m_values,
    errors_s19 - errors_s19_err,
    errors_s19 + errors_s19_err,
    color="purple",
    alpha=0.2,
)
# Fit and plot a line
coeffs = np.polyfit(np.log(m_values), np.log(errors_s19), 2)
fit_func = np.poly1d(coeffs)
ax2.plot(m_values, np.exp(fit_func(np.log(m_values))), "k:")

ax2.plot(m_values, errors_s50, ".", color="pink", label="s = 50")
ax2.fill_between(
    m_values,
    errors_s50 - errors_s50_err,
    errors_s50 + errors_s50_err,
    color="pink",
    alpha=0.2,
)
# Fit and plot a line
coeffs = np.polyfit(np.log(m_values), np.log(errors_s50), 2)
fit_func = np.poly1d(coeffs)
ax2.plot(m_values, np.exp(fit_func(np.log(m_values))), "k:")

ax2.plot(m_values, errors_s76, ".", color="purple", label="s = 76")
ax2.fill_between(
    m_values,
    errors_s76 - errors_s76_err,
    errors_s76 + errors_s76_err,
    color="purple",
    alpha=0.2,
)
# Fit and plot a line
coeffs = np.polyfit(np.log(m_values), np.log(errors_s76), 2)
fit_func = np.poly1d(coeffs)
ax2.plot(m_values, np.exp(fit_func(np.log(m_values))), "k:")

ax2.plot(m_values, errors_s142, ".", color="pink", label="s = 142")
ax2.fill_between(
    m_values,
    errors_s142 - errors_s142_err,
    errors_s142 + errors_s142_err,
    color="pink",
    alpha=0.2,
)
# Fit and plot a line
coeffs = np.polyfit(np.log(m_values), np.log(errors_s142), 2)
fit_func = np.poly1d(coeffs)
ax2.plot(m_values, np.exp(fit_func(np.log(m_values))), "k:")

ax2.plot(m_values, errors_s232, ".", color="orange", label="s = 232")
ax2.fill_between(
    m_values,
    errors_s232 - errors_s232_err,
    errors_s232 + errors_s232_err,
    color="orange",
    alpha=0.2,
)
# Fit and plot a line
coeffs = np.polyfit(np.log(m_values), np.log(errors_s232), 2)
fit_func = np.poly1d(coeffs)
ax2.plot(m_values, np.exp(fit_func(np.log(m_values))), "k:")

ax2.set_xlim(xlim)
ax2.set_ylim(ylim)
ax2.set_xscale("log")
ax2.set_yscale("log")
ax2.set_xlabel(xlabel)
ax2.set_ylabel(ylabels[1])
ax2.legend(frameon=True)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save plot
plt.tight_layout()
plt.savefig("HR_15.pdf", bbox_inches="tight")
