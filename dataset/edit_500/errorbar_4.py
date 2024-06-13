import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data
airlines = ["Delta", "American", "United", "Southwest", "JetBlue"]
flight_time_means = [2.5, 3.2, 1.8, 2.0, 2.7]
flight_time_errors = [0.5, 0.6, 0.4, 0.5, 0.3]
passenger_count_means = [150.33, 180.67, 120.39, 145.99, 160.52]
passenger_count_errors = [20, 25, 15, 20, 18]

ylabel1 = "Flight Time (hours)"
xlabel1 = "(a) Flight Time by Airline"
ylabel2 = "Number of Passengers"
xlabel2 = "(b) Passenger Count by Airline"


# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create subplots
fig, (ax1, ax2) = plt.subplots(
    1, 2, figsize=(10, 4)
)  # Adjusted for the given dimensions
colors = ["#acd9bb", "#83c3c7", "#5da2c7", "#3a77b0", "#224e8d"]

# Speak duration of airlines
ax1.bar(airlines, flight_time_means, yerr=flight_time_errors, color=colors, capsize=5)
ax1.set_ylabel(ylabel1)
ax1.set_xlabel(xlabel1)
for i, v in enumerate(flight_time_means):
    ax1.text(i, v + flight_time_errors[i] + 0.05, str(v), ha="center", va="bottom")
ax1.spines["top"].set_visible(False)
ax1.spines["right"].set_visible(False)
ax1.yaxis.grid(True)
ax1.set_axisbelow(True)

# Speak tokens of airlines
ax2.bar(airlines, passenger_count_means, yerr=passenger_count_errors, color=colors, capsize=5)
ax2.set_ylabel(ylabel2)
ax2.set_xlabel(xlabel2)
for i, v in enumerate(passenger_count_means):
    ax2.text(i, v + passenger_count_errors[i] + 0.5, str(v), ha="center", va="bottom")

ax2.spines["top"].set_visible(False)
ax2.spines["right"].set_visible(False)
ax2.yaxis.grid(True)
ax2.set_axisbelow(True)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save the figure
plt.tight_layout()
plt.savefig('errorbar_4.pdf', bbox_inches='tight')
