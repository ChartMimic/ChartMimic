import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Simulating data for a new domain: Health
sizes = np.linspace(500, 200, 6, dtype=int)  # Generate sizes from 500 to 200
data = [
    np.abs(np.random.normal(0, 0.4, size)) for size in sizes
]  # Generate data with mean 0 and take absolute value

labels = [
    "Blood Pressure",
    "Cholesterol Levels",
    "Body Mass Index",
    "Heart Rate",
    "Blood Sugar",
    "Oxygen Saturation",
]
xlabel="Health Metric Value"
ylabel="Number of Patients"
xlim=[0, 2]
xticks=[0.0, 0.5, 1.0, 1.5, 2.0]
bins=40

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Histogram plot
colors = ["#d4f5f4", "#ffffc2", "#dacdfb", "#f4bab6", "#b8eabd", "#bfd6f4"]

plt.figure(figsize=(8, 7))
plt.hist(
    data,
    bins=bins,
    stacked=True,
    edgecolor="black",
    linewidth=1.2,
    color=colors,
    label=labels,
)

# Set background color to white
ax = plt.gca()
ax.set_facecolor("white")

# Labels and title
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.xlim(xlim)
plt.xticks(xticks)
handles, labels = plt.gca().get_legend_handles_labels()

# Reverse handles and labels
handles = handles[::-1]
labels = labels[::-1]

plt.legend(handles, labels)

# ===================
# Part 4: Saving Output
# ===================
# Adjusting the plot to match the original image's dimensions
plt.tight_layout()
plt.savefig('hist_1.pdf', bbox_inches='tight')
