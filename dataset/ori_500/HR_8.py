# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Define the parallelogram boundary points
# Adjust these points as needed to form a parallelogram
boundary_points = np.array([[0, 0], [3, -1], [2, 2], [-1, 3]])

# Define the data for each subplot
data1 = np.random.rand(100000, 2)  # 10^5 points
data1[:, 0] = data1[:, 0] * 2  # Scale x component from 0 to 2
data2 = np.random.rand(1000, 2)  # 10^3 points
data3 = np.random.rand(1000, 2)  # 10^3 points
data3[:, 0] = data3[:, 0] + 1

ylabel = [
    "Memory-2 mutants payoff",
    "Reactive-2 mutants payoff",
    "Self-reactive-2 mutants payoff",
]
xlabel = "Reactive-2 payoff"
labels = ["(P, P)", "(T, S)", "(R, R)", "(S,T)"]  # Adjust or add labels as needed
xlim = [-2, 4]
ylim = [-2, 4]
legendtitle = "num. of points = {}"
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Define the figure size
fig = plt.figure(figsize=(10, 4))

# Create subplots
for i, data in enumerate([data1, data2, data3], 1):
    ax = fig.add_subplot(1, 3, i)
    # Fill the parallelogram
    ax.fill(boundary_points[:, 0], boundary_points[:, 1], color="lightblue", alpha=0.5)
    ax.set_xlim(xlim)  # Adjusted x limits to better fit the parallelogram
    ax.set_ylim(ylim)  # Adjusted y limits to better fit the parallelogram
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel[i - 1])
    if i != 1:
        ax.set_yticks([])

    for point, label in zip(boundary_points, labels):
        if point[0] < 1:
            ax.text(point[0] - 0.8, point[1] - 0.5, label, color="black", fontsize=8)
        else:
            ax.text(point[0], point[1] + 0.2, label, color="black", fontsize=8)
    scatter = ax.scatter(data[:, 0], data[:, 1], color="red", s=1)
    ax.legend([scatter], [legendtitle.format(5 if i == 1 else 3)], loc="upper right")
    ax.plot(
        np.append(boundary_points[:, 0], boundary_points[0, 0]),
        np.append(boundary_points[:, 1], boundary_points[0, 1]),
        color="blue",
    )

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout
plt.tight_layout()
plt.savefig("HR_8.pdf", bbox_inches="tight")
