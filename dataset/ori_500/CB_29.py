# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Technology fields
tech_fields = [
    "AI",
    "Blockchain",
    "Cloud Computing",
    "IoT",
    "Robotics",
    "Biotech",
    "VR",
    "Cybersecurity",
    "Quantum Computing",
    "Nanotechnology",
]

# Patent filings in 2013
patents_2013 = [120, 50, 80, 90, 70, 60, 30, 40, 10, 20]
# Patent filings in 2022
patents_2022 = [500, 200, 300, 400, 250, 180, 100, 150, 50, 90]
x_label = "Number of Patents"
y_label = "Technology Field"
ax1_title = "Patent Filings in 2013"
ax2_title = "Patent Filings in 2022"
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create a figure with two subplots (1x2) and shared y-axis
fig, axes = plt.subplots(1, 2, figsize=(10, 5), sharey=True)
colors = ["skyblue", "salmon"]

# Plotting the bar graphs
for i, (patents, color) in enumerate(zip([patents_2013, patents_2022], colors)):
    axes[i].barh(tech_fields, patents, color=color, edgecolor="gray")
    axes[i].set_xlabel(x_label)
    # Adding line graph on the same axes
    axes[i].plot(patents, tech_fields, "o-", color="#f7b267")

# Adding data labels
for ax, patents in zip(axes, [patents_2013, patents_2022]):
    for index, value in enumerate(patents):
        ax.text(value + 1, index, f" {value}", va="center")

# Set labels and titles
axes[0].set_title(ax1_title)
axes[1].set_title(ax2_title)
axes[0].set_ylabel(y_label)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout to prevent clipping and overlap
plt.tight_layout()
plt.savefig("CB_29.pdf", bbox_inches="tight")
