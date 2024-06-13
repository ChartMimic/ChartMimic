import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Expanded data
tech_fields = [
    "Cybersecurity",
    "Blockchain Technology",
    "Internet of Things",
    "5G Technology",
    "Autonomous Vehicles",
]

number_of_patents = np.array(
    [
        np.random.randint(60, 200, 100),  # Cybersecurity
        np.random.randint(50, 150, 100),  # Blockchain Technology
        np.random.randint(100, 250, 100),  # Internet of Things
        np.random.randint(30, 100, 100),  # 5G Technology
        np.random.randint(40, 120, 100),  # Autonomous Vehicles
    ]
)


xlabel = "Number of Patents"
ylabel = "Frequency"
title = "Histogram of Tech Patents Across Various Fields 2019-2023"

bins = np.linspace(0, 300, 30)  # Adjusted bin range to accommodate new data

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
plt.figure(figsize=(12, 8))
warmer_colors = ["#FF4500", "#FF8C00", "#FFA500", "#FF6347", "#FFD700"]

for i, category in enumerate(tech_fields):
    plt.hist(
        number_of_patents[i],
        bins=bins,
        alpha=0.5,
        color=warmer_colors[i % len(warmer_colors)],
        label=category,
    )

plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.title(title)
plt.legend(loc="upper right")

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig('hist_18.pdf', bbox_inches='tight')
