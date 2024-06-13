# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Define regions as groups
regions = [
    "North America",
    "Europe",
    "Asia",
    "South America",
    "Africa",
    "Australia",
    "Central America",
    "Middle East",
    "Southeast Asia",
    "Scandinavia",
]

# Educational data: High School Graduation Rates (solid_bar) and Higher Education Enrollment Rates (striped_bar)
graduation_rates = (
    np.random.rand(10) * 20 + 60
)  # Graduation rates ranging from 60% to 80%
enrollment_rates = (
    np.random.rand(10) * 10 + 30
)  # Enrollment rates ranging from 30% to 40%

# Errors for both metrics
graduation_errors = np.random.rand(10) * 8 + 5  # Error bars for graduation rates
enrollment_errors = np.random.rand(10) * 6 + 5  # Error bars for enrollment rates

# Labels and Plot Types
label_High_School_Graduation = "High School Graduation"
label_Higher_Education_Enrollment = "Higher Education Enrollment"

# Axes Limits and Labels
ylabel_value = "Percentage (%)"
title = "Educational Metrics by Region"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plotting
fig, ax = plt.subplots(figsize=(10, 6))

# X-axis positions for the bars
x = np.arange(len(regions))

# Create vertical stacked bar chart
ax.bar(
    x,
    graduation_rates,
    color="#8bb09e",
    yerr=graduation_errors,
    label=label_High_School_Graduation,
    capsize=3,
)
ax.bar(
    x,
    enrollment_rates,
    bottom=graduation_rates,
    color="#eaca8f",
    yerr=enrollment_errors,
    label=label_Higher_Education_Enrollment,
    capsize=3,
)

# Add labels and title
ax.set_ylabel(ylabel_value)
ax.set_title(title)
ax.set_xticks(x)
ax.set_xticklabels(regions, rotation=45, ha="right")
ax.legend()

# ===================
# Part 4: Saving Output
# ===================
# Show plot
plt.tight_layout()
plt.savefig("errorbar_24.pdf", bbox_inches="tight")
