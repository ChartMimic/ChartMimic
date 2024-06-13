# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data for Area Chart - Represents percentage increases in knowledge by subject area
n_levels = ["0", "1", "2", "3", "4", "5"]
education = np.array([10, 15, 20, 25, 30, 35])
law = np.array([5, 10, 15, 20, 25, 30])
technology = np.array([0, 5, 10, 15, 20, 25])

# Cumulative data for the stacked Area chart
cumulative_education = education
cumulative_law = cumulative_education + law
cumulative_technology = cumulative_law + technology

# Data for Bar Chart - Shows the number of publications by domain
domains = [
    "Education",
    "Law",
    "Technology",
    "History",
    "Geography",
    "Humanities",
    "Finance",
]
publications = [200, 150, 300, 100, 120, 180, 210]
titles=["Knowledge Increase by Subject Area", "Number of Publications by Domain"]
xlabels=["Study Level", "Domain"]
ylabels=["Cumulative Knowledge (%)", "Publications"]
ax1labels=["Education","Law", "Technology"]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Creating the subplot layout
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

# Plotting the Area Chart
ax1.fill_between(
    n_levels, 0, cumulative_education, label=ax1labels[0], color="#008fd5", alpha=0.6
)
ax1.fill_between(
    n_levels,
    cumulative_education,
    cumulative_law,
    label=ax1labels[1],
    color="#fc4f30",
    alpha=0.6,
)
ax1.fill_between(
    n_levels,
    cumulative_law,
    cumulative_technology,
    label=ax1labels[2],
    color="#e5ae38",
    alpha=0.6,
)
ax1.set_title(titles[0])
ax1.set_xlabel(xlabels[0])
ax1.set_ylabel(ylabels[0])
ax1.legend(loc="upper left")

# Plotting the Bar Chart
ax2.bar(domains, publications, color="#30a2da")
ax2.set_title(titles[1])
ax2.set_xlabel(xlabels[1])
ax2.set_ylabel(ylabels[1])
ax2.set_xticklabels(domains, rotation=45)

# ===================
# Part 4: Saving Output
# ===================
# Adjusting layout and saving the figure
plt.tight_layout()
plt.savefig('multidiff_17.pdf', bbox_inches='tight')
