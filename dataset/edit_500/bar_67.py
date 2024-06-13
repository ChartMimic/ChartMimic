# ===================
# Part 1: Importing Libraries
# ===================
import numpy as np; np.random.seed(0)

import matplotlib.pyplot as plt
import colorsys

# ===================
# Part 2: Data Preparation
# ===================
# Redefining the data
models = ["Online Education", "Self-paced Learning", "Virtual Classrooms", "Interactive Simulations", "AI Tutors", "Gamified Learning", "Remote Assessments"]
percentages = [15.0, 25.5, 35.4, 45.3, 55.1, 65.2, 75.3]

# Sorting the data in descending order while keeping track of the models order
sorted_data = sorted(zip(percentages, models), reverse=True)
sorted_percentages, sorted_models = zip(*sorted_data)

title = "Adoption of Educational Technologies"
xlabel = "Educational Technology"
ylabel = "Adoption Percentage (%)"
ylim = [0, np.max(sorted_percentages) + 10]



# Generate random colors with lower saturation
def hsl_to_rgb(h, s, l):
    return colorsys.hls_to_rgb(h, l, s)


# Randomly generate colors
colors = [hsl_to_rgb(hue, 0.5, 0.6) for hue in np.linspace(0, 1, len(models) + 1)[:-1]]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create figure and bar chart with the sorted data
plt.figure(figsize=(12, 8))
bars = plt.bar(sorted_models, sorted_percentages, color=colors)

# Randomly decide where to put the text based on the value of the bar
for bar in bars:
    yval = bar.get_height()
    text_y = (
        yval - 5 if yval > 10 else yval + 1
    )  # Slight modification to avoid negative values
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        text_y,
        f"{yval}%",
        ha="center",
        va="top" if text_y < yval else "bottom",
    )

# Set chart title and labels
plt.title(title)
plt.xlabel(xlabel)
plt.ylabel(ylabel)

# Randomly set y-axis range to a bit higher than the max value
plt.ylim(ylim)

# Randomize the gridlines and ticks
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Randomize tick rotation
plt.xticks(rotation=45)

# Hide the top and right spines
plt.gca().spines["top"].set_visible(False)
plt.gca().spines["right"].set_visible(False)

# ===================
# Part 4: Saving Output
# ===================
# Apply tight layout
plt.tight_layout()

plt.savefig('bar_67.pdf', bbox_inches='tight')
