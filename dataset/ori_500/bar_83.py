# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Emotion labels
emotions = [
    "Amusement",
    "Unbothered",
    "Sadness",
    "Pride",
    "Nervousness",
    "Annoyance",
    "Gratitude",
    "Relief",
    "Joy",
    "Disapproval",
]

# Approximate frequency values based on the image
frequencies = [7.6, 7.0, 6.7, 6.6, 6.0, 6.0, 3.5, 3.5, 3.0, 2.1]
frequencies2 = [2.6, 3.0, 3.7, 4.6, 5.0, 5.0, 5.5, 6.5, 7.0, 7.1]
xlabel1 = "Frequency Metric 1 (%)"
xlabel2 = "Frequency Metric 2 (%)"
ylabel = "Emotion"

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
plt.savefig("bar_83.pdf", bbox_inches="tight")
