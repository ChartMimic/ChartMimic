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
    "8x": [[np.random.rand() - 0.7, np.random.rand()] for _ in range(10)],
    "4x": [[np.random.rand() * 1.5 - 1, np.random.rand() - 1] for _ in range(2)],
    "2x": [[np.random.rand() - 2, np.random.rand() - 2] for _ in range(10)],
    "1x": [[np.random.rand() - 3, np.random.rand() - 3] for _ in range(10)],
}

line_x = np.array([-3.0, 0.5])
line_y = np.array([-3, 0.9])

colors = [
    "#c76526",
    "#469c76",
    "#d39334",
    "#3171ad",
]  # Use HEX color codes for muted colors
labels = ["1x", "2x", "4x", "8x"]
correlation = -0.47
xlabel = "Log (Depth L1)"
ylabel = "Log (ATE RMSE)"

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
plt.legend(loc="upper left")

# Add correlation text with a box inside the plot area
plt.text(line_x.mean(), line_y.mean(), f"Correlation: {correlation:.2f}", fontsize=9)

# Set labels and title
plt.xlabel(xlabel)
plt.ylabel(ylabel)

# Set grid
plt.grid(True)

# ===================
# Part 4: Saving Output
# ===================
# Show plot with tight layout
plt.tight_layout()
plt.savefig("CB_11.pdf", bbox_inches="tight")
