# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

from scipy.stats import norm

# ===================
# Part 2: Data Preparation
# ===================
# Sample data for demonstration
data_out = np.random.normal(loc=-8, scale=3.5, size=500)
data_in = np.random.normal(loc=8, scale=3.5, size=500)

# Labels and Plot Types
ax1_label = "Out"
ax2_label = "In"
ax1_text = r"$-\frac{m^{*}}{2}$"
ax2_text = r"$\frac{m^{*}}{2}$"

# Axes Limits and Labels
xlabel_value = "LR Test"
ylabel_value = "Density"
xticks_values = [-20, -15, -10, -5, 0, 5, 10, 15, 20]
xlim_values = [-22, 22]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create figure and axis
fig, ax = plt.subplots(
    figsize=(10, 8)
)  # Adjusted to match the original image's dimensions

# Plot histograms
ax.hist(data_out, bins=15, density=True, alpha=1, color="#1982c4", label=ax1_label)
ax.hist(data_in, bins=15, density=True, alpha=1, color="#ff595e", label=ax2_label)

# Plot normal distributions
xmin, xmax = ax.get_xlim()
x = np.linspace(xmin, xmax, 100)
p_out = norm.pdf(x, np.mean(data_out), np.std(data_out))
p_in = norm.pdf(x, np.mean(data_in), np.std(data_in))
ax.plot(x, p_out, color="#7bc8f6", linewidth=3)
ax.plot(x, p_in, color="#f87469", linewidth=3)

# Add dashed lines at mean
ax.axvline(np.mean(data_out), color="black", linestyle="dashed")
ax.axvline(np.mean(data_in), color="black", linestyle="dashed")

# Add text labels for dashed lines
ax.text(
    np.mean(data_out) + 1.5,
    ax.get_ylim()[1] - 0.01,
    ax1_text,
    ha="center",
    va="top",
    fontsize=18,
)
ax.text(
    np.mean(data_in) + 1.5,
    ax.get_ylim()[1] - 0.005,
    ax2_text,
    ha="center",
    va="top",
    fontsize=18,
)

# Set labels and title
ax.set_xlabel(xlabel_value)
ax.set_ylabel(ylabel_value)
ax.set_xticks(xticks_values)
ax.set_xlim(xlim_values)

# Add legend
ax.legend()

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save plot
plt.tight_layout()
plt.savefig("CB_1.pdf", bbox_inches="tight")
