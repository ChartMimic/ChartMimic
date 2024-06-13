# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Updated Urban Transportation Data for three major cities
metrics = ["Traffic Volume", "Public Transit", "Accident Rate"]
values = np.array(
    [
        [220, 180, 220],  # New York
        [150, 120, 130],  # Los Angeles
        [130, 160, 110],  # Chicago
    ]
)

# Updated asymmetric error values, now more proportionate to the data scale
errors = np.array(
    [
        [[25, 20], [15, 15], [25, 20]],  # Errors for New York (lower, upper)
        [[20, 15], [10, 15], [20, 10]],  # Errors for Los Angeles
        [[15, 20], [15, 10], [15, 15]],  # Errors for Chicago
    ]
)

# Creating subplots for each city
cities = ["New York", "Los Angeles", "Chicago"]

ylabel = "Metric Values"
ylim = [80, 280]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
fig, axs = plt.subplots(1, 3, figsize=(10, 4))  # Compact and square figure layout


# Function to plot each city's data
def plot_city_data(ax, errors, city_index, city_name):
    x = np.arange(len(metrics))  # the label locations
    bar_colors = ["#6a8347", "#377eb8", "#d62728"]
    barerrors = np.array(errors).T[:, :, city_index]
    bars = ax.bar(x, values[city_index], yerr=barerrors, color=bar_colors, capsize=5)
    for bar, lower_error, upper_error in zip(bars, barerrors[0], barerrors[1]):
        # Position for lower error text
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() - lower_error - 15,
            f"-{lower_error}",
            va="bottom",
            ha="center",
            color="black",
        )
        # Position for upper error text
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + upper_error + 3,
            f"+{upper_error}",
            ha="center",
            color="black",
        )

    ax.set_title(city_name)
    ax.set_xticks(x)
    ax.set_xticklabels(metrics, rotation=90)
    ax.set_ylabel(ylabel)
    ax.set_ylim(ylim)  # Uniform scale for all charts


for i, city in enumerate(cities):
    plot_city_data(axs[i], errors, i, city)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig("errorbar_29.pdf", bbox_inches="tight")
