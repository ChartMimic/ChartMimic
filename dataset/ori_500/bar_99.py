# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Create traffic data
data = np.array(
    [
        [150, 180, 75, 90, 80],  # Traffic flow (in thousands of vehicles per day)
        [2.5, 2.0, 1.5, 2.0, 2.8],  # Accident rate (accidents per 100,000 vehicles)
        [60, 55, 70, 65, 72],  # Public transport usage (% of population)
        [80, 75, 90, 85, 88],  # Road conditions (road quality index out of 100)
        [85, 80, 75, 90, 88],  # Public satisfaction (satisfaction score out of 100)
    ]
)
categories = [
    "Traffic Flow",
    "Accident Rate",
    "Public Transport Usage",
    "Road Conditions",
    "Public Satisfaction",
]

titles = ["Dataset 1", "Dataset 2", "Dataset 3", "Dataset 4"]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
fig, axs = plt.subplots(2, 2, figsize=(10, 8))  # Creating a 2x2 grid of subplots

colors = plt.get_cmap("Pastel2")(np.linspace(0.15, 0.85, data.shape[0]))
bar_width = 0.5  # Width of the bars


# Function to plot a bar chart in a specific subplot
def plot_bars(ax, data, categories, color, title):
    bars = ax.bar(np.arange(len(categories)), data, color=color, width=bar_width)
    ax.set_title(title)
    ax.set_xticks(np.arange(len(categories)))
    ax.set_xticklabels(categories, rotation=45)
    for bar in bars:
        yval = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2.0,
            yval,
            round(yval, 1),
            va="top",
            ha="center",
        )  # Annotate bars


# Plot data on each subplot
for i, ax in enumerate(axs.flat):
    plot_bars(ax, data[i], categories, colors[i], titles[i])

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout to prevent overlap
fig.tight_layout()
plt.savefig("bar_99.pdf", bbox_inches="tight")
