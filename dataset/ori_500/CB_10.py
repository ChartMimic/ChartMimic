# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Sample (x,y) for the scatter plot
data = {
    "Low": [[np.random.randint(150, 200), np.random.rand() - 3] for _ in range(10)],
    "Middle": [[np.random.randint(200, 300), np.random.rand() - 4] for _ in range(2)],
    "High": [[np.random.randint(300, 400), np.random.rand() - 6] for _ in range(10)],
}

line_x = np.array([150, 200, 250, 300, 350, 400])
line_y = np.array([-1, -2, -3, -4, -5, -6])

colors = ["#3171ad", "#d39334", "#469c76"]  # Use HEX color codes for muted colors
labels = ["Low", "Middle", "High"]
correlation = -0.47
xlabel = "Average Tracked ORB Feature Number"
ylabel = "Log (ATE RMSE)"
legend_title = "Severity"
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create scatter plot
plt.figure(figsize=(7, 5))  # Adjust figure size to match original image dimensions

for key in data:
    x = [item[0] for item in data[key]]
    y = [item[1] for item in data[key]]
    plt.scatter(x, y, color=colors[labels.index(key)], label=key)

# Add regression line
plt.plot(line_x, line_y, color="black")

# Add shaded area for standard deviation
std_dev = 0.5
plt.fill_between(line_x, line_y - std_dev, line_y + std_dev, color="black", alpha=0.1)

# Add legend inside the plot area
plt.legend(title=legend_title, loc="upper right")

# Add correlation text with a box inside the plot area
plt.text(line_x[-2], line_y[-2], f"Correlation: {correlation:.2f}", fontsize=9)

# Set labels and title
plt.xlabel(xlabel)
plt.ylabel(ylabel)

plt.yticks(np.arange(line_y.min(), line_y.max() + 2, 2))

# Set grid
plt.grid(True)

# ===================
# Part 4: Saving Output
# ===================
# Show plot
plt.tight_layout()
plt.savefig("CB_10.pdf", bbox_inches="tight")
