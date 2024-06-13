# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
number_of_bins = 40

# An example of three data sets to compare
number_of_data_points = 387
labels = ["Control Group", "Treatment Group 1", "Treatment Group 2"]
data_sets = [
    np.random.normal(2, 3, number_of_data_points),
    np.random.normal(3, 1, number_of_data_points),
    np.random.normal(-3, 1, number_of_data_points),
]

# The bin_edges are the same for all of the histograms
hist_range = (np.min(data_sets), np.max(data_sets))
bin_edges = np.linspace(hist_range[0], hist_range[1], number_of_bins + 1)
centers = bin_edges[:-1] + np.diff(bin_edges) / 2
xlabel = "Number of Observations"
ylabel = "Value Range"
title = "Comparative Distribution of Three Different Groups"
colors = ["#739e47", "#e25d33", "#f19d38"]
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Cycle through and plot each histogram
# Computed quantities to aid plotting
binned_data_sets = [
    np.histogram(d, range=hist_range, bins=number_of_bins)[0] for d in data_sets
]
binned_maximums = np.max(binned_data_sets, axis=1)
x_locations = np.arange(0, sum(binned_maximums), np.max(binned_maximums))

fig, ax = plt.subplots(figsize=(7, 5))
for x_loc, binned_data in zip(x_locations, binned_data_sets):
    lefts = x_loc - 0.5 * binned_data
    ax.barh(
        centers, binned_data, height=np.diff(bin_edges), left=lefts, color=colors.pop(0)
    )

# Set the x-axis labels
ax.set_xticks(x_locations)
ax.set_xticklabels(labels)

# Set labels and title with specific names
ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)
ax.set_title(title)

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig("HR_22.pdf", bbox_inches="tight")
