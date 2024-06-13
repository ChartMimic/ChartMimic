import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Updated Urban Transportation Data for three major cities
metrics = ["Air Quality", "Water Conservation", "Renewable Energy"]
values = np.array(
    [
        [85, 75, 80],  # Copenhagen
        [70, 65, 75],  # Vancouver
        [60, 55, 70],  # Stockholm
    ]
)

# Updated asymmetric error values, now more proportionate to the data scale
errors = np.array(
    [
        [[10, 8], [7, 8], [9, 8]],  # Errors for Copenhagen (lower, upper)
        [[8, 7], [6, 8], [7, 6]],  # Errors for Vancouver
        [[7, 6], [6, 5], [8, 7]],  # Errors for Stockholm
    ]
)

# Creating subplots for each city
cities = ["Copenhagen", "Vancouver", "Stockholm"]

ylabel = "Environmental Metric Values"
ylim=[40, 100]

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
            bar.get_height() - lower_error - 5,
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
plt.savefig('errorbar_29.pdf', bbox_inches='tight')
