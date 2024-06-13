import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Simulating data
sizes = np.linspace(500, 200, 4, dtype=int)  # Generate sizes from 500 to 200

data1 = np.abs(np.random.normal(2.5, 0.4, sizes[0]))
data2 = np.abs(np.random.normal(1.8, 0.4, sizes[1]))
data3 = np.abs(np.random.normal(2.1, 0.4, sizes[2]))
data4 = np.abs(np.random.normal(2.0, 0.4, sizes[3]))
labels = [
    "Electric Vehicle Range",
    "Wind Turbine Efficiency",
    "Battery Storage Capacity",
    "Geothermal Temperature",
]
xlabel = "Measurement Value"
ylabel = "Frequency"
bins = np.linspace(0, 4, 20)
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Histogram plot

colors = ["#6a9ad0", "#5985e1", "#4faeea", "#b1cf95"]

plt.figure(figsize=(9, 6))  # Adjusted to match the original image's dimensions

plt.hist(
    [data1, data2, data3, data4],
    bins=bins,
    stacked=True,
    label=labels,
    color=colors,
    edgecolor="black",
)

# Labels and title
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.legend()

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig('hist_2.pdf', bbox_inches='tight')
