# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
cities = ["Beijing", "Shanghai", "Guangzhou", "Shenzhen", "Chengdu"]
temperatures = [11.2, 16.1, 21.9, 23.2, 16.3]
xlabel = "City"
ylabel = "Average Temperature (°C)"
title = "Average City Temperatures"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
plt.figure(figsize=(8, 4))
plt.bar(cities, temperatures, color="skyblue", edgecolor="black")
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.title(title)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig("bar_77.pdf", bbox_inches="tight")
