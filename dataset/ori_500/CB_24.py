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
# Sample data for demonstration purposes
x1 = np.linspace(40, 80, 100)
y1 = norm.pdf(x1, 60, 5)
x2 = np.linspace(80, 120, 100)
y2 = norm.pdf(x2, 100, 5)
x3 = np.linspace(120, 160, 100)
y3 = norm.pdf(x3, 140, 5)
labels = ["D0", "D1", "D2"]
xlabel = "Execution Duration(clock)"
ylabel = "Distribution"
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create the figure and axis
fig, ax = plt.subplots(figsize=(8, 6))

# Plot the distributions
ax.plot(x1, y1, "r--", label=labels[0])
ax.plot(x2, y2, "orange", label=labels[1])
ax.plot(x3, y3, "b:", label=labels[2])

# according to the above distribution and draw histogram for each distribution
# set filled color
ax.hist(np.random.normal(60, 5, 1000), bins=5, density=True, color="pink")
ax.hist(np.random.normal(100, 5, 1000), bins=5, density=True, color="bisque")
ax.hist(np.random.normal(140, 5, 1000), bins=5, density=True, color="lightblue")

# Add annotations
ax.annotate(
    "",
    xy=(60, 0.06),
    xytext=(100, 0.06),
    arrowprops=dict(facecolor="black", arrowstyle="<->"),
)
ax.annotate(
    "",
    xy=(60, 0.08),
    xytext=(140, 0.08),
    arrowprops=dict(facecolor="black", arrowstyle="<->"),
)
ax.annotate(
    "",
    xy=(100, 0.05),
    xytext=(140, 0.05),
    arrowprops=dict(facecolor="black", arrowstyle="<->"),
)

# add text on 80, 0.06
ax.text(80, 0.061, "40", fontsize=12, ha="center")
ax.text(100, 0.081, "80", fontsize=12, ha="center")
ax.text(120, 0.051, "40", fontsize=12, ha="center")

# Set labels and title
ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)

ax.set_ylim(0.00, 0.10)
ax.set_yticks([0.00, 0.03, 0.06, 0.09])

# Add legend
ax.legend(ncol=3)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save the plot
plt.tight_layout()
plt.savefig("CB_24.pdf", bbox_inches="tight")
