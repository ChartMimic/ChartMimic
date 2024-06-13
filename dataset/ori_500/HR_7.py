# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
users = np.linspace(0, 100, 100)
utility_left = 0.1 - 0.001 * (users - 50) ** 2
utility_center_left = 0.075 - 0.0008 * (users - 50) ** 2
utility_center = 0.05 - 0.0006 * (users - 50) ** 2
utility_center_right = 0.025 - 0.0004 * (users - 50) ** 2
utility_right = 0.01 - 0.0002 * (users - 50) ** 2
colors = ["blue", "steelblue", "green", "maroon", "red"]

L = np.random.rand(2, 17) * 10
CL = np.random.rand(4, 17) * 10
C = np.random.rand(5, 17) * 10
CR = np.random.rand(4, 17) * 10
R = np.random.rand(2, 17) * 10
L = [sorted(l1, reverse=True) for l1 in L]
CL = [sorted(cl1, reverse=True) for cl1 in CL]
CR = [sorted(cr1) for cr1 in CR]
R = [sorted(r1) for r1 in R]
xlabel = "Users (U)"
ylabel = "Utility (f)"
title = "Utility distribution per topic"
baseline = 0
labels = ["L", "CL", "C", "CR", "R"]
textheight = 16.5
xlabel2 = "Items(C)"
ylabel2 = "Users(U)"
title2 = "User preference matrix (M)"
plotlabels = ["Left", "Center Left", "Center", "Center Right", "Right"]
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Set the figure size to match the original image's dimensions
plt.figure(figsize=(8, 4))

# Create the left plot (Utility distribution per topic)
plt.subplot(1, 2, 1)
plt.plot(users, utility_left, label=plotlabels[0], color=colors[0])
plt.plot(users, utility_center_left, label=plotlabels[1], color=colors[1])
plt.plot(users, utility_center, label=plotlabels[2], color=colors[2])
plt.plot(users, utility_center_right, label=plotlabels[3], color=colors[3])
plt.plot(users, utility_right, label=plotlabels[4], color=colors[4])

plt.gca().spines["right"].set_visible(False)
plt.gca().spines["top"].set_visible(False)

plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.title(title)
plt.legend()

# Create the right plot (User preference matrix (M))
plt.subplot(1, 2, 2)

for index, values in enumerate([L, CL, C, CR, R]):
    for i in range(len(values)):
        plt.scatter(
            [baseline + i] * len(values[i]),
            range(len(values[i])),
            s=values[i],
            c=colors[index],
        )
    plt.text(baseline + len(values) / 2, textheight, labels[index])
    baseline = baseline + len(values)
for spine in plt.gca().spines.values():
    spine.set_visible(False)

plt.xticks([])
plt.yticks([])
plt.xlabel(xlabel2)
plt.ylabel(ylabel2)
plt.title(title2, y=1.05)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and show plot
plt.tight_layout()
plt.savefig("HR_7.pdf", bbox_inches="tight")
