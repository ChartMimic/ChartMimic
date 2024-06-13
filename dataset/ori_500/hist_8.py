# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Sample data (replace with actual data)
image_overlap = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
number_of_queries = [500, 1000, 2000, 3000, 5500, 5700, 5800, 4000, 1000]

# Axes Limits and Labels
xlabel_value = "% images overlap"
ylabel_value = "Number of queries"
xlim_values = [0, 1.0]
ylim_values = [0, 6000]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create a histogram
plt.figure(figsize=(6, 5))  # Adjusted to match the original image's dimensions
plt.hist(image_overlap, bins=9, weights=number_of_queries, color="#7f95c0")

# Set the labels and title
plt.xlabel(xlabel_value)
plt.ylabel(ylabel_value)

# Remove ticks on both axes
plt.tick_params(axis="both", which="both", length=0)

# Set the range for the axes
plt.xlim(xlim_values)
plt.ylim(ylim_values)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and display the plot
plt.tight_layout()
plt.savefig("hist_8.pdf", bbox_inches="tight")
