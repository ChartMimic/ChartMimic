# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

from scipy.stats import gaussian_kde

# ===================
# Part 2: Data Preparation
# ===================
# Sample data for demonstration purposes
random_bundle = np.random.normal(loc=11, scale=1.5, size=1000)
increase_price = np.random.normal(loc=8.5, scale=1, size=1000)
strategic = np.random.normal(loc=10, scale=0.5, size=1000)
labels = ["Random Bundle", "Increase Price", "Strategic (Ours)"]
avxlabel = "Reserved price p_l"
xlabel = "p"
ylabel = "Shape Density"
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create the figure and axis
fig, ax = plt.subplots(
    figsize=(9, 6)
)  # Adjusted to match the original image's dimensions

# Plot the density plots
for data, color, label in zip(
    [random_bundle, increase_price, strategic],
    ["blue", "red", "green"],
    labels,
):
    density = gaussian_kde(data)
    xs = np.linspace(6.9, 15.5, 200)
    density.covariance_factor = lambda: 0.5
    density._compute_covariance()
    plt.fill_between(xs, density(xs), color=color, alpha=0.2, label=label)

# Plot the reserved price line
plt.axvline(x=9.3, color="red", linestyle="--", label=avxlabel)

# Set labels and title (if any)
ax.set_xlim(6.9, 15.5)
ax.set_xticks([7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0])
ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)

# Show grid
plt.grid(True, linestyle="--")

# Add legend
plt.legend()

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig("density_4.pdf", bbox_inches="tight")
