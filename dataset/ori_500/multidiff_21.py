# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Redefined data for Area Chart - Growth in various investment types over time
periods = ["2019", "2020", "2021", "2022"]
stocks = np.array([80, 60, 40, 20])
bonds = np.array([70, 50, 30, 10])
realestate = np.array([60, 40, 20, 0])

# Adjust the cumulative calculation for clarity in visualization
cumulative_stocks = stocks
cumulative_bonds = cumulative_stocks + bonds
cumulative_realestate = cumulative_bonds + realestate

# New data for Bar Chart - Financial product popularity
products = ["Savings", "CDs", "Stocks", "Bonds", "ETFs", "Mutual Funds"]
popularity = [210, 190, 170, 160, 150, 140]

# Redefined data for Histogram - Two sets: loan amount distribution in urban vs rural areas
urban_loans = np.random.normal(30000, 7000, 1000)
rural_loans = np.random.normal(20000, 8000, 1000)
bins = np.linspace(5000, 45000, 30)  # Uniform bin size for both histograms
ax1labels=["Stocks", "Bonds", "Real Estate"]
titles=["Investment Growth Over Time", "Popularity of Financial Products", "Loan Amount Distribution by Region"]
xlabels=["Year", "Product Type", "Loan Amount ($)"]
ylabels=["Total Investment (%)", "Number of Accounts", "Frequency"]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create figure with subplots
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(10, 5))

# Plotting the Area Chart with new data
ax1.stackplot(
    periods,
    cumulative_stocks,
    cumulative_bonds,
    cumulative_realestate,
    labels=ax1labels,
    colors=["#7bb274", "#5b92e5", "#ffcc5c"],
    alpha=0.8,
)
ax1.set_title(titles[0])
ax1.set_xlabel(xlabels[0])
ax1.set_ylabel(ylabels[0])
ax1.legend(loc="upper right")

# Plotting the Bar Chart with different data
ax2.bar(products, popularity, color="#a7c7e7")
ax2.set_title(titles[1])
ax2.set_xlabel(xlabels[1])
ax2.set_ylabel(ylabels[1])
ax2.set_xticklabels(products, rotation=45)

# Plotting two overlapping Histograms
ax3.hist(urban_loans, bins=bins, color="#84c1ff", alpha=0.7, label="Urban Loans")
ax3.hist(rural_loans, bins=bins, color="#ffa07a", alpha=0.7, label="Rural Loans")
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
