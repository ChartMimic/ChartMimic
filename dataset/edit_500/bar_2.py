import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0); np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Sample data
time = np.arange(0, 45, 5)
sedan = np.array([26, 27, 28, 29, 28, 27, 26, 27, 28])
suv = np.array([20, 19, 24, 18, 19, 20, 12, 18, 19])
truck = np.array([15, 14, 9, 13, 13, 14, 15, 14, 15])
motorcycle = np.array([29, 32, 33, 32, 31, 30, 39, 31, 30])
electric_car = np.array([10, 8, 6, 8, 9, 9, 8, 10, 8])
width = 2

barlabel = ["Sedan", "SUV", "Truck", "Motorcycle", "Electric Car"]
# Labels
xticks = [0, 10, 20, 30, 40]
xlabel = "Time (s)"
ylabel = "Fuel Efficiency (%)"
title = "Fuel Efficiency Distribution Over Time: Transportation Study"


# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Stacked bar chart
plt.figure(figsize=(6, 3))  # Adjusting figure size to match original image dimensions
plt.bar(time, sedan, width, color="#529e3f", label=barlabel[0])
plt.bar(time, suv, width, bottom=sedan, color="#c53a32", label=barlabel[1])
plt.bar(time, truck, width, bottom=sedan + suv, color="#8e69b8", label=barlabel[2])
plt.bar(time, motorcycle, width, bottom=sedan + suv + truck, color="#85594e", label=barlabel[3])
plt.bar(
    time,
    electric_car,
    width,
    bottom=sedan + suv + truck + motorcycle,
    color="#7f7f7f",
    label=barlabel[4],
)

# Labels and title
plt.xticks(xticks)
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.title(title)

# Legend
plt.legend(loc="upper right", bbox_to_anchor=(1.45, 1))

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig('bar_2.pdf', bbox_inches='tight')
