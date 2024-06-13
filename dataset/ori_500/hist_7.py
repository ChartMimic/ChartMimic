# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data for plotting
confidence = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
accuracy = np.array([0.2, 0.3, 0.4, 0.5, 0.6, 0.5, 0.4, 0.3, 0.8])
calibration_error = 0.31
text = f"Calibration Error:\n{calibration_error}"

# Axes Limits and Labels
xlabel_value = "Confidence"
ylabel_value = "Accuracy in bin"
title = "Cascade"
xlim_values = [0, 1]
ylim_values = [0, 1]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Set figure size to match the original image's dimensions
plt.figure(figsize=(8, 8))

# Plot histogram using plt.hist and specify bins
plt.hist(confidence, bins=9, weights=accuracy, color="tan", edgecolor="black")

# Add diagonal dashed line
plt.plot([0, 1], [0, 1], "k--", linestyle="--", linewidth=1, color="#808080")

# Add text for calibration error
plt.text(0.08, 0.85, text, color="#c06c27", fontsize=18)

# Set labels and title
plt.xlabel(xlabel_value)
plt.ylabel(ylabel_value)
plt.title(title)

# Adjust x and y axis limits to match the reference picture
plt.xlim(xlim_values)
plt.ylim(ylim_values)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save the plot
plt.tight_layout()
plt.savefig("hist_7.pdf", bbox_inches="tight")
