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
xlabel = "Frequency (%)"
ylabel = "Emotion"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create horizontal bar chart
plt.figure(figsize=(8, 8))  # Adjust figure size
plt.barh(emotions, frequencies, color="lightcoral", edgecolor="gray")

# Adding data labels
for index, value in enumerate(frequencies):
    plt.text(value, index, f" {value}%", va="center")
# Set labels and title
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.gca().spines["top"].set_visible(False)
plt.gca().spines["right"].set_visible(False)
plt.gca().spines["bottom"].set_visible(False)
plt.gca().spines["left"].set_visible(False)

# ===================
# Part 4: Saving Output
# ===================
# Show the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig("bar_55.pdf", bbox_inches="tight")
