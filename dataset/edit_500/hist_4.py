import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Sample data (replace with actual data)
# Generate new data
tech_usage_data = np.random.exponential(30, 1000)
healthcare_data = np.random.gamma(2, 20, 1000)

# Define bins aligned for both histograms
bins = np.histogram(np.hstack((tech_usage_data, healthcare_data)), bins=30)[1]
labels = ["Tech Usage", "Healthcare"]
xlabel = "Usage Difference (Healthcare vs. Tech)"
ylabel = "Number of Observations"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create figure and axis
fig, ax = plt.subplots(
    figsize=(5, 3)
)  # Adjusted to match the original image's dimensions

# Calculate the histogram data for each set and plot them
ax.hist(
    tech_usage_data,
    bins=bins,
    color="#f2a965",
    edgecolor="#fdf460",
    linewidth=1.2,
    label=labels[0],
    align="mid",
    histtype="stepfilled",
    alpha=0.7,
)
ax.hist(
    healthcare_data,
    bins=bins,
    color="#709dc6",
    edgecolor="#ca3531",
    linewidth=1.2,
    label=labels[1],
    align="mid",
    histtype="stepfilled",
    alpha=0.7,
)

# To show the overlapping areas, we plot the two histograms with transparency
ax.hist(
    tech_usage_data,
    bins=bins,
    color="#f2a965",
    edgecolor="#fdf460",
    linewidth=1.2,
    alpha=0.7,
    align="mid",
    histtype="stepfilled",
)
ax.hist(
    healthcare_data,
    bins=bins,
    color="#709dc6",
    edgecolor="#ca3531",
    linewidth=1.2,
    alpha=0.7,
    align="mid",
    histtype="stepfilled",
)

# Set labels
ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)

# Add legend
ax.legend()

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout
plt.tight_layout()

# Save the plot
plt.savefig('hist_4.pdf', bbox_inches='tight')
