# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Simulated data based on the previous setup
learning_rate = [0.01, 0.05, 0.1, 0.2]
error_rate_64 = np.array([0.18, 0.15, 0.12, 0.10])
error_rate_128 = np.array([0.16, 0.13, 0.11, 0.09])
error_rate_256 = np.array([0.14, 0.11, 0.08, 0.07])
dropout_rate = [0.0, 0.1, 0.2, 0.3]
accuracy_64 = np.array([0.82, 0.85, 0.83, 0.80])
accuracy_128 = np.array([0.84, 0.87, 0.86, 0.83])

# Axes Limits and Labels
xlabel_value = "Parameter Rate"

ylabel_value = "Metric"

# Labels
label_1 = " (Batch Size=64)"
label_2 = " (Batch Size=128)"
label_3 = "Error Rate vs. Learning Rate"
label_4 = "Accuracy vs. Dropout"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create a figure with a 3x2 grid
fig, axs = plt.subplots(3, 2, figsize=(12, 9))

# Custom colors for the plots
colors = ["dodgerblue", "tomato", "limegreen", "gold", "purple"]


# Function to plot the data
def plot_data(ax, x, y1, y2, title, marker1, marker2, color1, color2):
    ax.plot(
        x,
        y1,
        marker=marker1,
        markersize=8,
        linewidth=2,
        color=color1,
        label=f"{title}{label_1}",
    )
    ax.plot(
        x,
        y2,
        marker=marker2,
        markersize=8,
        linewidth=2,
        color=color2,
        label=f"{title}{label_2}",
    )
    ax.set_title(title, fontsize=14)
    ax.set_xlabel(xlabel_value, fontsize=12)
    ax.set_ylabel(ylabel_value, fontsize=12)
    ax.legend(loc="best", fontsize=10, frameon=True, shadow=True)
    ax.grid(True, linestyle="--", alpha=0.5)


# Assigning data to each subplot
plot_data(
    axs[0, 0],
    learning_rate,
    error_rate_64,
    error_rate_128,
    label_3,
    "o",
    "s",
    colors[0],
    colors[1],
)
plot_data(
    axs[0, 1],
    dropout_rate,
    accuracy_64,
    accuracy_128,
    label_4,
    "^",
    "d",
    colors[2],
    colors[3],
)
plot_data(
    axs[1, 0],
    learning_rate,
    error_rate_128,
    error_rate_256,
    label_3,
    ">",
    "<",
    colors[4],
    colors[0],
)
plot_data(
    axs[1, 1],
    dropout_rate,
    accuracy_128,
    accuracy_64,
    label_4,
    "p",
    "*",
    colors[1],
    colors[2],
)
plot_data(
    axs[2, 0],
    learning_rate,
    error_rate_256,
    error_rate_64,
    label_3,
    "H",
    "X",
    colors[3],
    colors[4],
)
plot_data(
    axs[2, 1],
    dropout_rate,
    accuracy_64,
    accuracy_128,
    label_4,
    "+",
    "x",
    colors[0],
    colors[1],
)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and display the plots
plt.tight_layout()
plt.savefig('line_57.pdf', bbox_inches='tight')
