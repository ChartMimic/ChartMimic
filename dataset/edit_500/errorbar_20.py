import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)
# ===================
# Part 2: Data Preparation
# ===================
# Meteorological data for different cities
cities = ["San Francisco", "Berlin", "Mumbai", "Sydney"]
x = np.arange(len(cities))  # Location of labels on the x-axis

# Simplifying data arrays to two seasons per metric
population_growth = np.array(
    [np.random.uniform(1.5, 3.5, 4), np.random.uniform(1.5, 3.5, 4)]
).T  # Spring and Autumn population growth
employment_rate = np.array(
    [np.random.uniform(60, 90, 4), np.random.uniform(60, 90, 4)]
).T  # Spring and Autumn employment rate
green_space = np.array(
    [np.random.uniform(20, 50, 4), np.random.uniform(20, 50, 4)]
).T  # Spring and Autumn green space percentage
waste_recycling = np.array(
    [np.random.uniform(30, 70, 4), np.random.uniform(30, 70, 4)]
).T  # Spring and Autumn waste recycling rate

# Errors for each season
pop_growth_errors = np.array([np.random.uniform(0.1, 0.5, 4), np.random.uniform(0.1, 0.5, 4)]).T
emp_rate_errors = np.array([np.random.uniform(1, 5, 4), np.random.uniform(1, 5, 4)]).T
green_space_errors = np.array([np.random.uniform(2, 5, 4), np.random.uniform(2, 5, 4)]).T
waste_recycling_errors = np.array([np.random.uniform(3, 7, 4), np.random.uniform(3, 7, 4)]).T

labels = ["Spring", "Autumn"]
titles = [
    "Annual Population Growth",
    "Employment Rate",
    "Green Space Percentage",
    "Waste Recycling Rate",
]
ylabels = ["Growth (%)", "Rate (%)", "Percentage (%)", "Rate (%)"]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plotting
fig, axs = plt.subplots(2, 2, figsize=(10, 5))  # Adjusted to 2 rows and 2 columns
axs = axs.flatten()
# Define colors for each set of bars to keep the design cohesive and attractive
colors = [
    ["#ff9999", "#66b3ff"],  # Spring and Autumn for temperature
    ["#99ff99", "#2878b5"],  # Spring and Autumn for employment_rate
    ["#f7b7a3", "#f7c6c7"],  # Spring and Autumn for wind speed
    ["#9ac9db", "#9b59b6"],
]  # Spring and Autumn for waste_recycling


# Helper function to plot data
def plot_data(ax, j, data, errors, title, ylabel):
    for i in range(2):  # Adjusted to only two bars per city
        ax.bar(
            x + i * 0.2,
            data[:, i],
            yerr=errors[:, i],
            color=colors[j][i],
            label=labels[i],
            width=0.2,
            capsize=3,
        )
    ax.set_title(title)
    ax.set_xticks(x + 0.1)  # Adjust position to center the group
    ax.set_xticklabels(cities)
    ax.set_ylabel(ylabel)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, 1.4), ncol=2)


# Plot each category of meteorological data
plot_data(
    axs[0],
    0,
    population_growth,
    pop_growth_errors,
    titles[0],
    ylabels[0],
)
plot_data(axs[1], 1, employment_rate, emp_rate_errors, titles[1], ylabels[1])
plot_data(axs[2], 2, green_space, green_space_errors, titles[2], ylabels[2])
plot_data(axs[3], 3, waste_recycling, waste_recycling_errors, titles[3], ylabels[3])

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig("errorbar_20.pdf", bbox_inches="tight")
