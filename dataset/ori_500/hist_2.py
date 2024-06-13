# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Simulating data
sizes = np.linspace(250, 100, 4, dtype=int)  # Generate sizes from 1000 to 100

data1 = np.abs(np.random.normal(0.7, 0.1, sizes[0]))
data2 = np.abs(np.random.normal(0.9, 0.1, sizes[1]))
data3 = np.abs(np.random.normal(0.9, 0.1, sizes[2]))
data4 = np.abs(np.random.normal(0.95, 0.1, sizes[3]))
labels = [
    "SAM-dependent methyltransferase",
    "Thioredoxin-like",
    "Tetratricopeptide-like helical domain",
    "CheY-like",
]
xlabel = "TM-score"
ylabel = "Frequency"
bins = np.linspace(0.4, 1.0, 20)
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
plt.savefig("hist_2.pdf", bbox_inches="tight")
