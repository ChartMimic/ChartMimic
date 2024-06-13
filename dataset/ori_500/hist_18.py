# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Expanded data
grammy_award_categories = [
    "Record of the Year",
    "Album of the Year",
    "Song of the Year",
    "Best New Artist",
    "Best Pop Solo Performance",  # Additional categories
]
number_of_nominations = np.array(
    [
        np.random.randint(60, 200, 100),  # Record of the Year
        np.random.randint(50, 150, 100),  # Album of the Year
        np.random.randint(100, 250, 100),  # Song of the Year
        np.random.randint(30, 100, 100),  # Best New Artist
        np.random.randint(40, 120, 100),  # Best Pop Solo Performance
    ]
)


xlabel = "Number of Nominations"
ylabel = "Frequency"
title = "Histogram of Grammy Nominations Across Expanded Categories 2019-2023"
# Create a histogram for each category
bins = np.linspace(0, 300, 30)  # Adjusted bin range to accommodate new data

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
plt.figure(figsize=(12, 8))
# Define new distinct warmer colors with enough colors for the new categories
warmer_colors = ["#FF4500", "#FF8C00", "#FFA500", "#FF6347", "#FFD700"]
for i, category in enumerate(grammy_award_categories):
    plt.hist(
        number_of_nominations[i],
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
plt.savefig("hist_18.pdf", bbox_inches="tight")
