# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data
emotions = ["Ang", "Cnt", "Dis", "Fea", "Joy", "Ntr", "Sad", "Sur"]
negative = [500, 300, 200, 1000, 0, 0, 500, 0]
positive = [0, 0, 0, 0, 2000, 0, 0, 0]
none = [0, 0, 0, 0, 0, 3500, 0, 0]
mixed = [0, 0, 0, 0, 0, 0, 0, 300]
labels = ["negative", "positive", "none", "mixed"]
xlabel = "Emotions"
ylabel = "Frequency"
ylim = [0, 4000]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Set figure size to match the original image's dimensions
plt.figure(figsize=(6, 4))

# Plotting
bar_width = 0.8
index = np.arange(len(emotions))

plt.bar(index, negative, bar_width, color="red", label=labels[0])
plt.bar(index, positive, bar_width, color="green", label=labels[1], bottom=negative)
plt.bar(
    index,
    none,
    bar_width,
    color="grey",
    label=labels[2],
    bottom=[i + j for i, j in zip(negative, positive)],
)
plt.bar(
    index,
    mixed,
    bar_width,
    color="orange",
    label=labels[3],
    bottom=[i + j + k for i, j, k in zip(negative, positive, none)],
)

# Labels and Title
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.ylim(ylim)
# plt.title('Emotion Frequencies by Sentiment')
plt.xticks(index, emotions)
plt.legend(loc="upper left")

# ===================
# Part 4: Saving Output
# ===================
# Show plot
plt.tight_layout()
plt.savefig("bar_26.pdf", bbox_inches="tight")
