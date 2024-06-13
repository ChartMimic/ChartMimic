import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Generate sample data
# Simulated data for different classes and categories
project_performance = {
    "Project A": {
        "Design Phase": np.random.normal(85, 10, 100),
        "Implementation Phase": np.random.normal(90, 12, 100),
    },
    "Project B": {
        "Design Phase": np.random.normal(80, 15, 100),
        "Implementation Phase": np.random.normal(85, 10, 100),
    },
    "Project C": {
        "Design Phase": np.random.normal(88, 14, 100),
        "Implementation Phase": np.random.normal(87, 10, 100),
    },
    "Project D": {
        "Design Phase": np.random.normal(82, 9, 100),
        "Implementation Phase": np.random.normal(89, 13, 100),
    },
}
title="Distribution of Project Performance:"
xticklabels=["Design Phase", "Implementation Phase"]
xticks=[1, 2]
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create a figure and an array of axes: 2x2 subplot grid
fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))

# Prepare data for violin plot
data_to_plot = []
for class_name, genders in project_performance.items():
    data_to_plot.extend([grades for gender, grades in genders.items()])

# Flatten the axes array for easy iteration
axs = axs.flatten()

for i, (class_name, ax) in enumerate(zip(project_performance, axs)):
    gender_grades = project_performance[class_name]
    ax.violinplot([gender_grades["Design Phase"], gender_grades["Implementation Phase"]])
    ax.set_title(f"{title} {class_name}")
    ax.set_xticks(xticks)
    ax.set_xticklabels(xticklabels)

# ===================
# Part 4: Saving Output
# ===================
# Improve spacing between subplots
plt.tight_layout()

plt.savefig('violin_9.pdf', bbox_inches='tight')
