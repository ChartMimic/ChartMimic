import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0); np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data

datasets = ["Cardiology", "Neurology", "Orthopedics"]
M3 = [45, 60, 55]
M4 = [50, 65, 60]
M5 = [55, 72, 65]
M6 = [60, 70, 60]
M7 = [65, 70, 60]

barWidth = 0.15
r1 = np.arange(len(M3))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
r4 = [x + barWidth for x in r3]
r5 = [x + barWidth for x in r4]
labels = ["Hospital A", "Hospital B", "Hospital C", "Hospital D", "Hospital E"]
ylabel = "Quality Score"
ylim = [35, 75]
yticks = [35, 40, 45, 50, 55, 60, 65, 70, 75]


# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create figure
plt.figure(figsize=(10, 6))  # Adjusted to match the original image's dimensions

# Create bars
plt.bar(r1, M3, color="#dee9f5", width=barWidth, edgecolor="black", label=labels[0])
plt.bar(r2, M4, color="#c0d5e9", width=barWidth, edgecolor="black", label=labels[1])
plt.bar(r3, M5, color="#94bdd9", width=barWidth, edgecolor="black", label=labels[2])
plt.bar(r4, M6, color="#669cc9", width=barWidth, edgecolor="black", label=labels[3])
plt.bar(r5, M7, color="#437ab5", width=barWidth, edgecolor="black", label=labels[4])

# Add xticks on the middle of the group bars
plt.xticks([r + barWidth * 2 for r in range(len(M3))], datasets)

# Create legend & Show graphic
plt.legend(loc="upper left")
plt.ylabel(ylabel)
plt.ylim(ylim)
plt.yticks(yticks)

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig('bar_18.pdf', bbox_inches='tight')
