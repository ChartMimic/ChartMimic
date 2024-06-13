import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data for the bar charts
universities = ["Harvard University", "Stanford University", "MIT", "UC Berkeley"]
graduate_employment_rate = [82.5, 75.3, 88.7, 69.4]
postgraduate_employment_rate = [90.1, 85.4, 92.3, 78.5]
error_graduate = [3.5, 4.1, 2.8, 3.9]  # Error values for graduate employment rate
error_postgraduate = [2.5, 3.2, 2.1, 3.0]  # Error values for postgraduate employment rate
x = np.arange(len(graduate_employment_rate))  # x-coordinates for the bars
labels = ["Graduate Employment Rate", "Postgraduate Employment Rate"]
title = "Comparison of Employment Rates Across Universities"
ylims = [[60, 100], [70, 100]]
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Set the figure size
fig, ax1 = plt.subplots(figsize=(8, 5))
# Bar width
width = 0.35

# Plotting 'graduate_employment_rate' on the primary y-axis
bars1 = ax1.bar(
    x - width / 2,
    graduate_employment_rate,
    width,
    label=labels[0],
    color="#4695a2",
    yerr=error_graduate,
    capsize=5,
    edgecolor="black",
)

# Create the secondary y-axis for 'postgraduate_employment_rate'
ax2 = ax1.twinx()
bars2 = ax2.bar(
    x + width / 2,
    postgraduate_employment_rate,
    width,
    label=labels[1],
    color="coral",
    yerr=error_postgraduate,
    capsize=5,
    edgecolor="black",
)

# Adding annotations directly on the bars for clarity
for i, bar in enumerate(bars1):
    height = bar.get_height()
    label_x_pos = bar.get_x() + bar.get_width() / 2
    ax1.text(
        label_x_pos,
        height - error_graduate[i] - 1,
        f"{height}%",
        rotation=90,
        ha="center",
        va="bottom" if height < 0 else "top",
    )
for j, bar in enumerate(bars2):
    height = bar.get_height()
    label_x_pos = bar.get_x() + bar.get_width() / 2
    ax2.text(
        label_x_pos,
        height - error_postgraduate[j] - 1,
        f"{height}%",
        rotation=90,
        ha="center",
        va="bottom" if height < 0 else "top",
    )


fig.suptitle(title)
# Adding labels, title, and custom x-axis tick labels
ax1.set_ylabel(labels[0], color="#5b93a0")
ax2.set_ylabel(labels[1], color="coral")
ax1.set_xticks(x)
ax1.set_xticklabels(universities)

# Add a horizontal line at y=0 if needed
ax1.axhline(0, color="grey", linewidth=0.8)

# Adjusting y-axis limits to fit the annotations and errors
ax1.set_ylim(ylims[0])
ax2.set_ylim(ylims[1])

# Adding grid lines for better readability
ax1.yaxis.grid(linestyle="--", linewidth="0.5", color="grey")
ax1.set_axisbelow(True)

ax2.yaxis.grid(linestyle="--", color="grey")
ax2.set_axisbelow(True)
# Adding legend
fig.legend(loc="upper center", bbox_to_anchor=(0.5, 1.05), ncol=2)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout
plt.tight_layout()
plt.savefig('errorbar_25.pdf', bbox_inches='tight')
