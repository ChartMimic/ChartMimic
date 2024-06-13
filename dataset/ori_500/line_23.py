# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data corrected to match lengths
x = [2**0.2, 2**1, 2**2, 2**3, 2**4, 2**5, 2**6, 2**7, 2**8.6]
y = [
    67.32,
    82.98,
    89.53,
    90.47,
    88.23,
    92.41,
    93.7,
    96.75,
    97.12,
]  # Removed extra values to match x's length
labels = [
    "67.32",
    "82.98",
    "89.53",
    "90.47",
    "88.23",
    "92.41",
    "93.7",
    "96.75",
    "97.12",
]  # Adjusted to match the corrected y

# Axes Limits and Labels
xlabel_value = "Number of Training Objects"
xlim_values = [2**0, 2**8]
xticks_values = [2**1, 2**3, 2**5, 2**7]
xticklabels = ["$2^{1}$", "$2^{3}$", "$2^{5}$", "$2^{7}$"]

ylabel_value = "Coverage Ratio (%)"
ylim_values = [66, 99]
yticks_values = np.arange(70, 96, 5)

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plot
fig, ax = plt.subplots(
    figsize=(5, 2)
)  # Adjust the size to match the original image's dimensions
ax.plot(
    x,
    y,
    marker="o",
    color="#4c72b0",
    linestyle="-",
    linewidth=2,
    markersize=6,
    mfc="#ff8c00",
    mec="white",
)

# Annotate each point with its label
for i, label in enumerate(labels):
    ax.annotate(
        label,
        (x[i], y[i]),
        textcoords="offset points",
        xytext=(0, 10),
        ha="center",
        fontsize=7,
    )

# Set x-axis to be logarithmic
ax.set_xscale("log", base=2)  # Corrected 'basex' to 'base'

# Set x-axis labels to be in the format of 2^n
ax.set_xticks(xticks_values)
ax.set_xticklabels(
    xticklabels,
)
ax.set_xlim(xlim_values)  # Set limits to include a small margin

# Set y-axis ticks
plt.yticks(yticks_values, fontsize=10)
plt.ylim(ylim_values)  # Adjusted y-axis limit

# Remove tick lines outside the plotting area
ax.tick_params(
    axis="both", which="both", length=0, color="#d2d2d2"
)  # Remove tick marks and set their color

# Set labels and title
plt.xlabel(xlabel_value)
plt.ylabel(ylabel_value)

# Change the plot background color
ax.set_facecolor("#eaeaf2")

# Show grid
plt.grid(True, which="both", linestyle="-", linewidth=1, color="white")

# Change the axis colors
ax = plt.gca()
ax.spines["bottom"].set_color("#f5f5f5")
ax.spines["top"].set_color("#f5f5f5")  # Optional: hide or set color
ax.spines["left"].set_color("#f5f5f5")
ax.spines["right"].set_color("#f5f5f5")  # Optional: hide or set color

# ===================
# Part 4: Saving Output
# ===================
# Adjusting layout to add more space on the right
plt.tight_layout()
plt.savefig('line_23.pdf', bbox_inches='tight')
