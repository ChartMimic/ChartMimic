# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data
time_of_day = ["Morning", "Midday", "Afternoon", "Night"]
traffic_volume = [120, 80, 150, 50]  # Vehicles per hour
average_speed = [30, 45, 35, 55]  # Speed in miles per hour
accident_rate = [12, 8, 5, 3]  # Accidents per hour
fuel_consumption = [50, 40, 60, 30]  # Gallons per hour
emissions = [100, 80, 150, 60]  # Emissions in grams per hour

labels = ["Traffic Volume", "Average Speed", "Accident Rate", "Fuel Consumption", "Emissions"]
xlabel = "Time of Day"
ylabel = "Values"
title = "Transportation Metrics by Time of Day"
yaxhline = 100  # Highlighting the maximum traffic volume as a reference line
ylim = [0, 200]
yticks = np.arange(0, 200, 20)

# Bar width
bar_width = 0.2

# Positions of bars on x-axis
ind = np.arange(len(time_of_day))

texts = ["29%", "29%", "87%", "180%"]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Figure size
plt.figure(figsize=(8, 6))

# Plotting
plt.bar(ind, traffic_volume, width=bar_width, label=labels[0], color="#65bae7")
plt.bar(
    ind,
    average_speed,
    width=bar_width,
    label=labels[1],
    color="#acdcf2",
    hatch="//",
    bottom=traffic_volume,
)
plt.bar(
    ind + bar_width, accident_rate, width=bar_width, label=labels[2], color="#eaa86b"
)
plt.bar(
    ind + bar_width,
    fuel_consumption,
    width=bar_width,
    label=labels[3],
    color="#f4d3b4",
    hatch="/",
    bottom=accident_rate,
)
# Highlighting the most significant improvement
distance = 0.05
plt.annotate(
    "",
    xy=(ind[0] + bar_width, 55),
    xytext=(ind[0] + bar_width, 100),
    arrowprops=dict(facecolor="black", shrink=0.02),
)
plt.text(ind[0] + bar_width + distance, 70, texts[0])
plt.annotate(
    "",
    xy=(ind[3], 50),
    xytext=(ind[3], 100),
    arrowprops=dict(facecolor="black", shrink=0.02),
    va="center",
)
plt.text(ind[3] - distance * 6, 70, texts[1])
plt.annotate(
    "",
    xy=(ind[3] + bar_width, 30),
    xytext=(ind[3] + bar_width, 100),
    arrowprops=dict(facecolor="black", shrink=0.02),
)
plt.text(ind[3] + bar_width + distance, 70, texts[2])
plt.annotate(
    "",
    xy=(ind[3] + bar_width * 2, 30),
    xytext=(ind[3] + bar_width * 2, 10),
    arrowprops=dict(facecolor="red", shrink=0.02),
    ha="center",
)
plt.text(ind[3] + bar_width * 2 + distance, 20, texts[3])
plt.axhline(y=yaxhline, color="blue", linestyle="--", linewidth=2)
# X-axis labels
plt.xticks(ind + bar_width / 2, time_of_day)

# Y-axis labels
plt.ylim(ylim)
plt.yticks(yticks)

# Legend
plt.legend(loc="upper center", bbox_to_anchor=(0.5, 1.2), ncol=2)

# Grid lines
plt.grid(axis="y")

# Labels and Title
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.title(title)
# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig('bar_49.pdf', bbox_inches='tight')
