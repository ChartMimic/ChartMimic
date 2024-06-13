import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Redefined data for Area Chart - Growth in various investment types over time

# Time periods and corresponding average grades in different subjects
periods = ["2019", "2020", "2021", "2022"]
math_grades = np.array([80, 78, 85, 82])
science_grades = np.array([75, 80, 82, 88])
history_grades = np.array([70, 72, 75, 78])

# Adjust the cumulative calculation for clarity in visualization
cumulative_math = math_grades
cumulative_science = cumulative_math + science_grades
cumulative_history = cumulative_science + history_grades

# New data for Bar Chart - Popularity of educational resources
resources = ["Books", "Laboratories", "Teachers", "Online Tools", "Tutoring", "Extracurriculars"]
popularity = [70, 80, 90, 110, 140, 200]

# Redefined data for Histogram - Financial aid distribution in urban vs rural areas
urban_aid = np.random.normal(15000, 3000, 1000)  # Financial aid amounts in urban areas
rural_aid = np.random.normal(10000, 3500, 1000)  # Financial aid amounts in rural areas
bins = np.linspace(5000, 25000, 30)  # Uniform bin size for both histograms

# Labels and titles for the plots
ax1labels = ["Math", "Science", "History"]
titles = ["Average Grades Over Time", "Popularity of Educational Resources", "Financial Aid Distribution by Region"]
xlabels = ["Year", "Resource Type", "Financial Aid Amount ($)"]
ylabels = ["Cumulative Grades", "Number of Students", "Frequency"]

# Placeholder to show where the stacked area chart, bar chart, and histograms would be displayed. Actual plotting code is not included.

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create figure with subplots
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(10, 5))

# Plotting the Area Chart with new data
ax1.stackplot(
    periods,
    cumulative_math,
    cumulative_science,
    cumulative_history,
    labels=ax1labels,
    colors=["#7bb274", "#5b92e5", "#ffcc5c"],
    alpha=0.8,
)
ax1.set_title(titles[0])
ax1.set_xlabel(xlabels[0])
ax1.set_ylabel(ylabels[0])
ax1.legend(loc="upper right")

# Plotting the Bar Chart with different data
ax2.bar(resources, popularity, color="#a7c7e7")
ax2.set_title(titles[1])
ax2.set_xlabel(xlabels[1])
ax2.set_ylabel(ylabels[1])
ax2.set_xticklabels(resources, rotation=45)

# Plotting two overlapping Histograms
ax3.hist(urban_aid, bins=bins, color="#84c1ff", alpha=0.7, label="Urban Loans")
ax3.hist(rural_aid, bins=bins, color="#ffa07a", alpha=0.7, label="Rural Loans")
ax3.set_title(titles[2])
ax3.set_xlabel(xlabels[2])
ax3.set_ylabel(ylabels[2])
ax3.legend()

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save the plot as a PDF file
plt.tight_layout()
plt.savefig('multidiff_21.pdf', bbox_inches='tight')
