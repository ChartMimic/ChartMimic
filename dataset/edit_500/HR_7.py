import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
import numpy as np

# Generate user data
users = np.linspace(0, 100, 100)
utility_high = 0.25 - 0.001 * (users - 45) ** 2
utility_medium_high = 0.5 - 0.002 * (users - 45) ** 2
utility_medium = 0.15 - 0.0003 * (users -45) ** 2
utility_medium_low = 0.13 - 0.0004 * (users - 50) ** 2
utility_low = 0.07 - 0.003 * (users - 50) ** 2

colors = ["blue", "steelblue", "green", "maroon", "red"]
# Generate random data for user preference matrices
A = np.random.rand(3, 20) * 20
B = np.random.rand(4, 20) * 20
C = np.random.rand(5, 20) * 20
D = np.random.rand(4, 20) * 20
E = np.random.rand(7, 20) * 20

# Sort and adjust the data for visualization
A = [sorted(a1, reverse=True) for a1 in A]
B = [sorted(b1, reverse=True) for b1 in B]
D = [sorted(d1) for d1 in D]
E = [sorted(e1) for e1 in E]
datalist=[A, B, C, D, E]

# Labels and titles for the plots
xlabel = "Users (U)"
ylabel = "Utility (f)"
title = "Utility Distribution per User Group"
baseline = 0
labels = ["A", "B", "C", "D", "E"]
textheight=20

xlabel2 = "Items (I)"
ylabel2 = "Users (U)"
title2 = "User Preference Matrix (P)"
plotlabels = ["Group A", "Group B", "Group C", "Group D", "Group E"]
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Set the figure size to match the original image's dimensions
plt.figure(figsize=(8, 4))

# Create the left plot (Utility distribution per topic)
plt.subplot(1, 2, 1)
plt.plot(users, utility_high, label=plotlabels[0], color=colors[0])
plt.plot(users, utility_medium_high, label=plotlabels[1], color=colors[1])
plt.plot(users, utility_medium, label=plotlabels[2], color=colors[2])
plt.plot(users, utility_medium_low, label=plotlabels[3], color=colors[3])
plt.plot(users, utility_low, label=plotlabels[4], color=colors[4])

plt.gca().spines["right"].set_visible(False)
plt.gca().spines["top"].set_visible(False)

plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.title(title)
plt.legend()

# Create the right plot (User preference matrix (M))
plt.subplot(1, 2, 2)

for index, values in enumerate(datalist):
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
plt.savefig('HR_7.pdf', bbox_inches='tight')
