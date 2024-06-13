# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Create traffic data
data = np.array(
    [
        [250, 300, 220, 280, 260],  # Daily energy consumption (in megawatts)
        [55, 60, 52, 58, 54],  # Renewable energy usage (% of total consumption)
        [40, 35, 45, 42, 38],  # Energy efficiency rating (score out of 100)
        [5, 6, 4, 5, 6],  # Outage frequency (outages per month)
        [90, 85, 88, 87, 89],  # Customer satisfaction (satisfaction score out of 100)
    ]
)
categories = [
    "Daily Energy Consumption",
    "Renewable Energy Usage",
    "Energy Efficiency Rating",
    "Outage Frequency",
    "Customer Satisfaction",
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
plt.savefig('bar_99.pdf', bbox_inches='tight')
