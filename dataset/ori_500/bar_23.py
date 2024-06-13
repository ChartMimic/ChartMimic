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
models = ["GPT4", "GPT-few-shot", "GPT3.5", "StarCoder", "Code Llama", "NCL"]
accuracy = [3.5, 3.0, 2.5, 3.0, 3.5, 2.0]
completeness = [3.0, 2.5, 2.0, 2.5, 3.0, 1.5]
conciseness = [2.5, 2.0, 1.5, 2.0, 2.5, 1.0]
readability = [3.0, 2.5, 2.0, 2.5, 3.0, 1.5]

x = np.arange(len(models))  # the label locations
width = 0.2  # the width of the bars

labels = ["Accuracy", "Completeness", "Conciseness", "Readability"]
ylabel = "Ratings"
xlabel = "Language Models"
title = "Ratings of Language Models on a Scale from 1-4"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
fig, ax = plt.subplots(figsize=(9, 5))

# Plotting
rects1 = ax.bar(x - width * 1.5, accuracy, width, label=labels[0], color="#5878a3")
rects2 = ax.bar(
    x - width / 2, completeness, width, label=labels[1], color="#e59344"
)
rects3 = ax.bar(x + width / 2, conciseness, width, label=labels[2], color="#d1605e")
rects4 = ax.bar(
    x + width * 1.5, readability, width, label=labels[3], color="#85b6b2"
)

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel(ylabel)
ax.set_xlabel(xlabel)
ax.set_title(title)
ax.set_xticks(x)
ax.set_xticklabels(models)
ax.legend()

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig("bar_23.pdf", bbox_inches="tight")
