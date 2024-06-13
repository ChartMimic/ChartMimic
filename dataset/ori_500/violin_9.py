# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Generate sample data
class_grades = {
    "Class 1": {
        "Boys": np.random.normal(70, 10, 100),
        "Girls": np.random.normal(75, 12, 100),
    },
    "Class 2": {
        "Boys": np.random.normal(65, 15, 100),
        "Girls": np.random.normal(70, 10, 100),
    },
    "Class 3": {
        "Boys": np.random.normal(80, 14, 100),
        "Girls": np.random.normal(78, 10, 100),
    },
    "Class 4": {
        "Boys": np.random.normal(75, 9, 100),
        "Girls": np.random.normal(80, 13, 100),
    },
}
title="Distribution of Grades:"
xticklabels=["Boys", "Girls"]
xticks=[1, 2]



# Prepare data for violin plot
data_to_plot = []
for class_name, genders in class_grades.items():
    data_to_plot.extend([grades for gender, grades in genders.items()])

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create a figure and an array of axes: 2x2 subplot grid
fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))

# Flatten the axes array for easy iteration
axs = axs.flatten()

for i, (class_name, ax) in enumerate(zip(class_grades, axs)):
    gender_grades = class_grades[class_name]
    ax.violinplot([gender_grades["Boys"], gender_grades["Girls"]])
    ax.set_title(f"{title} {class_name}")
    ax.set_xticks(xticks)
    ax.set_xticklabels(xticklabels)

# ===================
# Part 4: Saving Output
# ===================
# Improve spacing between subplots
plt.tight_layout()

plt.savefig('violin_9.pdf', bbox_inches='tight')
