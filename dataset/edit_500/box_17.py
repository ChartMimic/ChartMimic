import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Random data to simulate the boxplot
data = [np.random.normal(100, 30, 100) for _ in range(10)]
xticklabels = [f"Experiment {i+1}" for i in range(10)]
ylabel = "Measurement"
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create the boxplot
fig, ax = plt.subplots(
    figsize=(8, 4)
)  # Adjust the figure size to match the original image's dimensions
boxprops = dict(linestyle="-", linewidth=2, color="blue")
medianprops = dict(linestyle="-", linewidth=2, color="orange")
meanprops = dict(marker=None)  # Hide mean points

bp = ax.boxplot(
    data,
    patch_artist=True,
    showmeans=True,
    meanprops=meanprops,
    showfliers=False,
    boxprops=boxprops,
    medianprops=medianprops,
)

for patch in bp["boxes"]:
    patch.set(facecolor="lightblue")

# Set the x-axis labels
ax.set_xticklabels(xticklabels, rotation=0)

# Set the y-axis label
ax.set_ylabel(ylabel)

# Add markers for minimum values
for i, line in enumerate(bp["whiskers"][::2]):
    mid_val = (line.get_ydata()[0] + line.get_ydata()[1]) / 2 + line.get_ydata()[
        1
    ]  # Get the y value of the minimum whisker
    ax.plot(
        i + 1, mid_val, marker="o", color="red"
    )  # Add a marker at the minimum value

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig('box_17.pdf', bbox_inches='tight')
