import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Emotion labels
emotions = [
    "Excitement",
    "Calmness",
    "Melancholy",
    "Confidence",
    "Apprehension",
    "Frustration",
    "Appreciation",
    "Comfort",
    "Happiness",
    "Criticism",
]
# New approximate frequency values with changed dimensions
frequencies = [12.5, 11.0, 10.8, 10.5, 10.2, 10.0, 9.8, 9.5, 9.2, 9.0]
frequencies2 = [3.2, 3.8, 4.5, 5.3, 5.8, 6.0, 6.3, 7.2, 7.6, 8.0]
xlabel1 = "Metric 1"
xlabel2 = "Metric 2"
ylabel = "Emotion Frequency (%)"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create horizontal bar chart
fig, axes = plt.subplots(1, 2, figsize=(10, 4), layout="constrained", sharey=True)
axes[0].barh(emotions, frequencies, color="lightcoral", edgecolor="gray")
axes[1].barh(emotions, frequencies2, color="lightblue", edgecolor="gray")

# Adding data labels
for index, value in enumerate(frequencies):
    axes[0].text(value, index, f" {value}%", va="center")
# Adding data labels
for index, value in enumerate(frequencies2):
    axes[1].text(value, index, f" {value}%", va="center")

# Set labels and title
axes[0].set_xlabel(xlabel1)
axes[0].set_ylabel(ylabel)
axes[1].set_xlabel(xlabel2)

# ===================
# Part 4: Saving Output
# ===================
# Show the plot with tight layout
plt.tight_layout()
plt.savefig('bar_83.pdf', bbox_inches='tight')
