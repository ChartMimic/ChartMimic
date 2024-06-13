# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Data for the bar charts
categories = ["RoboCodeX", "GPT-4V"]  # Swap the order
success = [0.5, 0.6]  # Swap the order
grounding_error = [0.15, 0.1]  # Swap the order
occupancy_error = [0.1, 0.05]  # Swap the order
gripper_collision = [0.05, 0.05]  # Swap the order
trajectory_optimization_error = [0.1, 0.1]  # Swap the order
grasping_failed = [0.1, 0.1]  # Swap the order

# Colors for each segment
colors = ["green", "grey", "orange", "yellow", "blue", "purple"]
bar_width = 0.5
y_pos = range(len(categories))
labels = ["Success", "Grounding Error", "Occupancy Error", "Gripper collision", "Trajectory optimization Error", "Grasping failed"]
xlabel = "Percentage of Total Trials"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create a figure with a specific size to match the original image's dimensions
fig, ax = plt.subplots(figsize=(10, 3))

# Stack the bars horizontally
ax.barh(y_pos, success, bar_width, color=colors[0], label=labels[0])
ax.barh(
    y_pos,
    grounding_error,
    bar_width,
    left=success,
    color=colors[1],
    label=labels[1],
)
ax.barh(
    y_pos,
    occupancy_error,
    bar_width,
    left=[i + j for i, j in zip(success, grounding_error)],
    color=colors[2],
    label=labels[2],
)
ax.barh(
    y_pos,
    gripper_collision,
    bar_width,
    left=[i + j + k for i, j, k in zip(success, grounding_error, occupancy_error)],
    color=colors[3],
    label=labels[3],
)
ax.barh(
    y_pos,
    trajectory_optimization_error,
    bar_width,
    left=[
        i + j + k + l
        for i, j, k, l in zip(
            success, grounding_error, occupancy_error, gripper_collision
        )
    ],
    color=colors[4],
    label=labels[4],
)
ax.barh(
    y_pos,
    grasping_failed,
    bar_width,
    left=[
        i + j + k + l + m
        for i, j, k, l, m in zip(
            success,
            grounding_error,
            occupancy_error,
            gripper_collision,
            trajectory_optimization_error,
        )
    ],
    color=colors[5],
    label=labels[5],
)

# Set the y-axis labels
ax.set_yticks(y_pos)
ax.set_yticklabels(categories)

# Set the x-axis label
ax.set_xlabel(xlabel)

# Add a legend
ax.legend(loc="upper center", bbox_to_anchor=(0.5, 1.5), ncol=3, frameon=False)

# ===================
# Part 4: Saving Output
# ===================
# Show the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig("bar_27.pdf", bbox_inches="tight")
