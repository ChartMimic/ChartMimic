# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Generate normally distributed data
data = np.random.normal(loc=2.0, scale=1.0, size=10000)

# Axes Limits and Labels
title = "Histogram of Wind Speed Measurements"
xlabel_value = "Wind Speed (km/h)"
ylabel_value = "Number of Measurements"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Set the figure size
plt.figure(figsize=(8, 6))

# Enable the grid
plt.grid(True, linestyle="--", linewidth=0.5, alpha=0.7)

# Histogram of the data
n, bins, patches = plt.hist(data, bins=25, color="skyblue", edgecolor="blue", alpha=0.7)

# Highlight the median of the data
median = np.median(data)
plt.axvline(median, color="purple", linestyle="dashed", linewidth=2)

# Adjust the median text position to not overlap the bars when possible
median_text_position = max(n) * 0.9
for bin_edge, count in zip(bins, n):
    if bin_edge > median and count < median_text_position:
        # Place the text above the median position
        median_text_position = count
        break
plt.text(median + 0.5, median_text_position, f"Median: {median:.2f}", color="purple")

# Title and labels relevant to database statistics
plt.title(title)
plt.xlabel(xlabel_value)
plt.ylabel(ylabel_value)

# ===================
# Part 4: Saving Output
# ===================
# Adjust the layout
plt.tight_layout()

plt.savefig("hist_15.pdf", bbox_inches="tight")
