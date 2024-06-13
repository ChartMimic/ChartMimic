# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
x = np.linspace(0, 20, 20)
original_data = np.sin(x) + np.random.normal(
    0, 0.1, 20
)  # Original data with some noise
smoothed_data = np.convolve(
    original_data, np.ones(5) / 5, mode="valid"
)  # Smoothed data
difference_data = np.diff(original_data)  # Difference data
cumulative_data = np.cumsum(original_data)  # Cumulative sum data

# Axes Limits and Labels
xlabel_value = "Time"

ylabel_value_1 = "Value"
ylabel_value_2 = "Delta Value"
ylabel_value_3 = "Cumulative Value"

# Labels
label_1 = "Smoothed Data"
label_2 = "Difference Data"
label_3 = "Cumulative Sum"

# Titles
title_1 = "Smoothed Representation"
title_2 = "First Difference of Data"
title_3 = "Cumulative Sum Over Time"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create a 3-subplot layout
fig, axs = plt.subplots(3, 1, figsize=(5, 10))

# First subplot: Smoothed Data
axs[0].plot(
    x[2:-2],
    smoothed_data,
    label=label_1,
    color="purple",
    linestyle="-",
    marker="o",
)
axs[0].set_title(title_1)
axs[0].set_ylabel(ylabel_value_1)
axs[0].legend(loc="upper right")
axs[0].grid(True, linestyle="--", alpha=0.5)

# Second subplot: Difference Data
axs[1].plot(
    x[1:],
    difference_data,
    label=label_2,
    color="orange",
    linestyle="-",
    marker="x",
)
axs[1].set_title(title_2)
axs[1].set_ylabel(ylabel_value_2)
axs[1].legend(loc="upper right")
axs[1].grid(True, linestyle="--", alpha=0.5)

# Third subplot: Cumulative Sum
axs[2].plot(
    x, cumulative_data, label=label_3, color="green", linestyle="-", marker="s"
)
axs[2].set_title(title_3)
axs[2].set_xlabel(xlabel_value)
axs[2].set_ylabel(ylabel_value_3)
axs[2].legend(loc="upper right")
axs[2].grid(True, linestyle="--", alpha=0.5)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout for better spacing and display
plt.tight_layout()

# Show the plot
plt.savefig('line_50.pdf', bbox_inches='tight')
