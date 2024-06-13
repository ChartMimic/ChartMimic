import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data
schools = ["Greenwood High", "Riverside Academy", "Maple Leaf School"]
pre_test_scores = [65, 78, 72]
post_test_scores = [75, 83, 79]
improvement_program = [80, 82, 82]
error_margins = [3, 2, 4]

# Bar positions
x = np.arange(len(schools))
width = 0.25
labels = ["Pre-Test", "Post-Test", "Improvement Program"]
ylabel = "Scores"
title = "Scores by school and method"
ylim = [60, 90]


# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plotting
fig, ax = plt.subplots(figsize=(8, 5))
bars1 = ax.bar(
    x - width,
    pre_test_scores,
    width,
    label=labels[0],
    color="lightskyblue",
    hatch="\\",
    yerr=error_margins,
    capsize=5,
    error_kw=dict(ecolor="black"),
)
bars2 = ax.bar(
    x,
    post_test_scores,
    width,
    label=labels[1],
    color="lightsalmon",
    hatch="//",
    yerr=error_margins,
    capsize=5,
    error_kw=dict(ecolor="black"),
)
bars3 = ax.bar(
    x + width,
    improvement_program,
    width,
    label=labels[2],
    color="palegreen",
    hatch="o",
    yerr=error_margins,
    capsize=5,
    error_kw=dict(ecolor="black"),
)

# Adding text for labels, title, and custom x-axis tick labels
ax.set_ylabel(ylabel)
ax.set_title(title)
ax.set_xticks(x)
ax.set_xticklabels(schools)
ax.set_ylim(ylim)  # Adjust y-axis scale to match reference picture
ax.legend(loc="upper center", ncol=3)  # Move legend to match reference picture


# Adding the data labels on the bars
def add_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(
            "{}".format(round(height, 3)),
            xy=(
                bar.get_x() + bar.get_width() / 2,
                height + error_margins[bars.index(bar)],
            ),  # Adjust label position to be above error bars
            xytext=(0, 3),  # 3 points vertical offset
            textcoords="offset points",
            ha="center",
            va="bottom",
        )


add_labels(bars1)
add_labels(bars2)
add_labels(bars3)

# ===================
# Part 4: Saving Output
# ===================
# Show the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig('errorbar_11.pdf', bbox_inches='tight')
