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
subjects = ["Math", "Science", "English", "History", "Art", "PE"]
test_scores = [75, 78, 92, 74, 78, 75]
homework_completion = [60, 75, 95, 70, 75, 68]
class_participation = [65, 82, 90, 68, 73, 65]
attendance = [71, 92, 97, 89, 75, 64]

x = np.arange(len(subjects))  # the label locations
width = 0.2  # the width of the bars

labels = ["Test Scores", "Homework Completion", "Class Participation", "Attendance"]
ylabel = "Percentages"
xlabel = "Subjects"
title = "Education Metrics Across Different Subjects"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
fig, ax = plt.subplots(figsize=(9, 5))

# Plotting
rects1 = ax.bar(x - width * 1.5, test_scores, width, label=labels[0], color="#5878a3")
rects2 = ax.bar(
    x - width / 2, homework_completion, width, label=labels[1], color="#e59344"
)
rects3 = ax.bar(
    x + width / 2, class_participation, width, label=labels[2], color="#d1605e"
)
rects4 = ax.bar(
    x + width * 1.5, attendance, width, label=labels[3], color="#85b6b2"
)

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel(ylabel)
ax.set_xlabel(xlabel)
ax.set_title(title)
ax.set_xticks(x)
ax.set_xticklabels(subjects)
ax.legend(loc='upper right')

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig("bar_23.pdf", bbox_inches="tight")
