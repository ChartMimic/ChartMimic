import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0); np.random.seed(0)

# ===================
# Part 2: Data Preparation
# ===================
# Data
N = 5
car = (0, 0.4, 0.6, 0.2)
bicycle = (0, 0.5, 0.7, 0.3)
train = (0, 0.6, 0.5, 0.1)
bus = (0, 0.3, 0.4, 0.2)
airplane = (0, 0.2, 0.3, 0.1)


ind = np.arange(4)  # the x locations for the groups
width = 0.1  # the width of the bars

# Axes Limits and Labels
ylabel_value = "Scores"
xlim_values = [0.7, 3.7]
xticklabels = ("0", "20", "40", "60")
legend_labels = (
        "Car",
        "Bicycle",
        "Train",
        "Bus",
        "Airplane",
    )
colors = (
    "#495c80",
    "#6d8abb",
    "#eadcd1",
    "#5899b8",
    "#2b5a75",
)

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
fig = plt.figure(figsize=(7, 5))  # Adjusting figure size as per the given dimensions
ax = fig.add_subplot(111)

rects1 = ax.bar(ind, car, width, color=colors[0])
rects2 = ax.bar(ind + width, bicycle, width, color=colors[1])
rects3 = ax.bar(ind + 2 * width, train, width, color=colors[2])
rects4 = ax.bar(ind + 3 * width, bus, width, color=colors[3])
rects5 = ax.bar(ind + 4 * width, airplane, width, color=colors[4])

ax.set_ylabel(ylabel_value)
ax.set_xlim(xlim_values)
ax.set_xticks(ind + 7 * width)
ax.set_xticklabels(xticklabels)

ax.legend(
    (rects1[0], rects2[0], rects3[0], rects4[0], rects5[0]),
    legend_labels,
)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig('bar_1.pdf', bbox_inches='tight')
