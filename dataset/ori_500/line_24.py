# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Sample data
iterations = np.arange(0, 10, 1)
average = np.array([750, 725, 700, 680, 660, 645, 635, 625, 615, 610])
std_dev = np.array([50, 45, 40, 35, 30, 25, 20, 15, 10, 5])

# Axes Limits and Labels
xlabel_value = "Iterations"

ylabel_value = "N-ELBO"
ylim_values = [560, 790]
yticks_values = np.arange(600, 751, 50)

# Labels
label_Average = "Average"
label_Standard_Deviation ="Standard Deviation"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plotting the average line
plt.figure(figsize=(6, 4))
plt.plot(iterations, average, label=label_Average, marker="o", color="#1f77b4")

# Plotting the standard deviation as a shaded area
plt.fill_between(
    iterations,
    average - std_dev,
    average + std_dev,
    color="#1f77b4",
    alpha=0.2,
    label=label_Standard_Deviation,
)

# Adjusting y-axis range to match the reference picture
plt.ylim(ylim_values)

# Adding yticks
plt.yticks(yticks_values)
plt.ylim(ylim_values)

# Adding labels and title with smaller font size
plt.xlabel(xlabel_value, fontsize=10)
plt.ylabel(ylabel_value, fontsize=10)

# Adding legend with no border
plt.legend(frameon=True, fontsize=10)

# Adding grid
plt.grid(True, color="#d1d1d1")

# ===================
# Part 4: Saving Output
# ===================
# Adjusting layout to add more space on the right
plt.tight_layout()
plt.savefig('line_24.pdf', bbox_inches='tight')
