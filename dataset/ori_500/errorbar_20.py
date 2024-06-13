# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)
# ===================
# Part 2: Data Preparation
# ===================
# Meteorological data for different cities
cities = ["New York", "London", "Beijing", "Tokyo"]
x = np.arange(len(cities))  # Location of labels on the x-axis

# Simplifying data arrays to two seasons per metric
temperatures = np.array(
    [np.random.uniform(10, 20, 4), np.random.uniform(10, 20, 4)]
).T  # Spring and Autumn temperatures
rainfall = np.array(
    [np.random.uniform(800, 1200, 4), np.random.uniform(800, 1200, 4)]
).T  # Spring and Autumn rainfall
wind_speeds = np.array(
    [np.random.uniform(2, 5, 4), np.random.uniform(2, 5, 4)]
).T  # Spring and Autumn wind speeds
aqi = np.array(
    [np.random.uniform(20, 80, 4), np.random.uniform(20, 80, 4)]
).T  # Spring and Autumn AQI
# Errors for each season
temp_errors = np.array([np.random.randint(1, 3, 4), np.random.randint(1, 3, 4)]).T
rain_errors = np.array([np.random.randint(50, 100, 4), np.random.randint(50, 100, 4)]).T
wind_errors = np.array([np.random.randint(1, 2, 4), np.random.randint(1, 2, 4)]).T
aqi_errors = np.array([np.random.randint(5, 15, 4), np.random.randint(5, 15, 4)]).T
labels = ["Spring", "Autumn"]
titles = [
    "Annual Average Temperature",
    "Annual Rainfall",
    "Wind Speed",
    "Air Quality Index",
]
ylabels = ["Temperature (°C)", "Rainfall (mm)", "Speed (m/s)", "AQI"]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plotting
fig, axs = plt.subplots(2, 2, figsize=(10, 5))  # Adjusted to 2 rows and 2 columns
axs = axs.flatten()
# Define colors for each set of bars to keep the design cohesive and attractive
colors = [
    ["#ff9999", "#66b3ff"],  # Spring and Autumn for temperature
    ["#99ff99", "#2878b5"],  # Spring and Autumn for rainfall
    ["#f7b7a3", "#f7c6c7"],  # Spring and Autumn for wind speed
    ["#9ac9db", "#9b59b6"],
]  # Spring and Autumn for AQI


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
    temperatures,
    temp_errors,
    titles[0],
    ylabels[0],
)
plot_data(axs[1], 1, rainfall, rain_errors, titles[1], ylabels[1])
plot_data(axs[2], 2, wind_speeds, wind_errors, titles[2], ylabels[2])
plot_data(axs[3], 3, aqi, aqi_errors, titles[3], ylabels[3])

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig("errorbar_20.pdf", bbox_inches="tight")
