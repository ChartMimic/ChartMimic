import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Generate random bimodal data with different distributions for each plot
data1_travel_time = np.concatenate(
    [np.random.normal(45, 8, 700), np.random.normal(20, 5, 300)]
)
data2_travel_time = np.concatenate(
    [np.random.normal(35, 7, 500), np.random.normal(25, 4, 500)]
)

data1_delivery_cost = np.concatenate(
    [np.random.normal(100, 20, 600), np.random.normal(50, 15, 400)]
)
data2_delivery_cost = np.concatenate(
    [np.random.normal(90, 25, 700), np.random.normal(60, 10, 300)]
)

data1_customer_satisfaction = np.concatenate(
    [np.random.normal(8, 1, 500), np.random.normal(4, 0.5, 500)]
)
data2_customer_satisfaction = np.concatenate(
    [np.random.normal(7, 1.2, 700), np.random.normal(6, 0.75, 300)]
)

data1_order_volume = np.concatenate(
    [np.random.normal(200, 30, 400), np.random.normal(100, 20, 600)]
)
data2_order_volume = np.concatenate(
    [np.random.normal(180, 25, 500), np.random.normal(80, 10, 500)]
)

binslist = [30, 30]
labels = ["2022", "2023"]
xlabel = "Value"
ylabel = "Density"
titles = ["(a) Travel Time Distribution", "(b) Delivery Cost Distribution", "(c) Customer Satisfaction Scores", "(d) Order Volume Over Time"]
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create the plots
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Plot histograms for each subplot
datasets = [
    (data1_travel_time, data2_travel_time),
    (data1_delivery_cost, data2_delivery_cost),
    (data1_customer_satisfaction, data2_customer_satisfaction),
    (data1_order_volume, data2_order_volume),
]
for (data1, data2), ax in zip(datasets, axs.flatten()):
    ax.hist(
        data1,
        bins=binslist[0],
        density=True,
        alpha=0.6,
        color="deepskyblue",
        label=labels[0],
        edgecolor="black",
        linewidth=0.5,
    )
    ax.hist(
        data2,
        bins=binslist[1],
        density=True,
        alpha=0.6,
        color="orangered",
        label=labels[1],
        edgecolor="black",
        linewidth=0.5,
    )
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(True)
    ax.legend()

# Set titles for each subplot
axs[0, 0].set_title(titles[0])
axs[0, 1].set_title(titles[1])
axs[1, 0].set_title(titles[2])
axs[1, 1].set_title(titles[3])

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save the figure
plt.tight_layout()
plt.savefig('hist_20.pdf', bbox_inches='tight')
