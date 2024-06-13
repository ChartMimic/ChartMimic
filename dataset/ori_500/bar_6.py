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
    "Excitement",
    "Delight",
    "Oblivious",
    "Embarrassment",
    "Disappointment",
]

# Approximate frequency values based on the image
frequencies = [
    2.1,
    2.7,
    3.0,
    3.5,
    3.5,
    3.8,
    4.0,
    4.0,
    6.0,
    6.0,
    6.0,
    6.6,
    6.7,
    7.0,
    7.6,
]

xlabel = "Frequency (%)"
ylabel = "Emotion"
xticks = list(range(0, 9))
xlim = [0, 8.5]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create horizontal bar chart
plt.figure(figsize=(8, 8))  # Adjust figure size
plt.barh(emotions, frequencies, color="#84ade3")

# Set x-axis limits
plt.xlim(xlim)

# Set x-axis ticks
plt.xticks(xticks)

# Set labels and title
plt.xlabel(xlabel)
plt.ylabel(ylabel)

# ===================
# Part 4: Saving Output
# ===================
# Show the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig("bar_6.pdf", bbox_inches="tight")
