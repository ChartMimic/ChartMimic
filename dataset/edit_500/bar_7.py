# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0); np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data
categories = ["Traditional Classroom", "Blended Learning", "Online Learning"]
student_satisfaction = [-85, -78, -50]
knowledge_retention = [-90, -82, -50]
engagement_level = [0.83, 0.75, 0.65]

labels = ["Student Satisfaction (%)", "Knowledge Retention (%)", "Engagement Level"]
xlabel = "Teaching Methods"
ylabel = "Percentage (%)"
ylabel2 = "Engagement Level"
xticks = [0, 1, 2]
ylim = [-100, 100]
ylim2 = [-1, 1]
yticks = [-100, -80, -60, -40, -20, 0]
yticks2 = [0, 0.25, 0.5, 0.75, 1]




# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create figure and axes
fig, ax1 = plt.subplots(
    figsize=(8, 6)
)  # Adjusted to match the original image's dimensions
# Create a second y-axis
ax2 = ax1.twinx()

# Bar plots
bar_width = 0.25
index = np.arange(len(categories))

bar1 = ax1.bar(
    index,
    student_satisfaction,
    bar_width,
    label=labels[0],
    color="#6e7a5f",
    edgecolor="black",
    zorder=3,
)
bar2 = ax1.bar(
    index + bar_width,
    knowledge_retention,
    bar_width,
    label=labels[1],
    color="#b8b7a5",
    edgecolor="black",
    zorder=3,
)
bar3 = ax2.bar(
    index + 2 * bar_width,
    engagement_level,
    bar_width,
    label=labels[2],
    color="#f4f1e0",
    edgecolor="black",
    zorder=3,
)

# Add values on top of the bars
for bars in [bar1, bar2]:
    for bar in bars:
        height = bar.get_height()
        ax1.annotate(
            "{}".format(height),
            xy=(bar.get_x() + bar.get_width() / 2, height - 4),
            xytext=(0, 3),  # 3 points vertical offset
            textcoords="offset points",
            ha="center",
            va="top",
        )
for bars in [bar3]:
    for bar in bars:
        height = bar.get_height()
        ax2.annotate(
            "{}".format(height),
            xy=(bar.get_x() + bar.get_width() / 2, height),
            xytext=(0, 3),  # 3 points vertical offset
            textcoords="offset points",
            ha="center",
            va="bottom",
        )

# Set the axes background color and add grid lines
for ax in [ax1, ax2]:
    ax.set_facecolor("#e6e6e6")  # Set the axes background color
    ax.grid(True, color="white", zorder=2)  # Add grid lines

# Axes labels and title
ax1.set_xlabel(xlabel)
ax1.set_ylabel(ylabel)
# ax1.set_title('Comparison of FGT and Feature Embedding Distance')
ax2.set_ylabel(ylabel2)

# Set x-axis category labels
ax1.set_ylim(ylim)
ax2.set_ylim(ylim2)
ax1.set_xticks(index + bar_width)
ax1.set_xticklabels(categories)

# Calculate the number of y-ticks on the left y-axis

ax1.set_yticks(yticks)
ax2.set_yticks(yticks2)

# Create legend & Show plot
handles, labels = ax1.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()
fig.legend(
    handles + handles2,
    labels + labels2,
    loc="lower right",
    bbox_to_anchor=(0.9, 0.1),
    frameon=False,
    framealpha=0,
)

# ===================
# Part 4: Saving Output
# ===================
# Adjust the subplot layout and save the figure
plt.tight_layout()
plt.savefig('bar_7.pdf', bbox_inches='tight')
