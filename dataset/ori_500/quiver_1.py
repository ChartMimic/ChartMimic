# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

# ===================
# Part 2: Data Preparation
# ===================
# Data for the plot
languages_1 = ["German", "French", "English"]
out_start_1 = [6.5, 7, 7]
out_group_bias_1 = [-2.44, -3.22, -4.00]
in_start_1 = [5.5, 6, 7]
in_group_bias_1 = [+3.38, +2.88, +1.88]
ax1_labels = ["Out-group bias\n(Collectivism)", "In-group bias\n(Individualism)"]

languages_2 = ["Japanese", "Korean", "Chinese"]
out_start_2 = [7.2, 6.2, 7.1]
out_group_bias_2 = [-4.75, -0.50, -4.00]
in_start_2 = [7.2, 7, 7.2]
in_group_bias_2 = [0.78, 0.25, 1.11]
ax2_labels = ["Out-group bias\n(Individualism)", "In-group bias\n(Collectivism)"]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

# Set the y-axis offsets to be in the middle of each grid
offset = 0.5

# First subplot (languages_1)
for i, lang in enumerate(languages_1):
    # Out-group bias line with arrow and black dots at start and end
    ax1.annotate(
        "",
        xy=(out_start_1[i], i + offset * 3 / 2),
        xytext=(out_start_1[i] + out_group_bias_1[i], i + offset * 3 / 2),
        arrowprops=dict(arrowstyle="<-", color="red"),
    )
    ax1.scatter(
        [out_start_1[i], out_start_1[i] + out_group_bias_1[i]],
        [i + offset * 3 / 2, i + offset * 3 / 2],
        color="black",
        s=10,
    )
    ax1.annotate(
        f"{out_group_bias_1[i]:.2f}",
        (out_start_1[i] + out_group_bias_1[i], i + offset * 1.75),
        color="red",
        ha="right",
        va="center",
    )

    # In-group bias line with arrow and black dots at start and end
    ax1.annotate(
        "",
        xy=(in_start_1[i], i + offset / 2),
        xytext=(in_start_1[i] + in_group_bias_1[i], i + offset / 2),
        arrowprops=dict(arrowstyle="<-", color="blue"),
    )
    ax1.scatter(
        [in_start_1[i], in_start_1[i] + in_group_bias_1[i]],
        [i + offset / 2, i + offset / 2],
        color="black",
        s=10,
    )
    ax1.annotate(
        f"{in_group_bias_1[i]:.2f}",
        (in_start_1[i] + in_group_bias_1[i], i + offset * 0.75),
        color="blue",
        ha="left",
        va="center",
    )

# Second subplot (languages_2)
for i, lang in enumerate(languages_2):
    ax2.annotate(
        "",
        xy=(out_start_2[i], i + offset * 3 / 2),
        xytext=(out_start_2[i] + out_group_bias_2[i], i + offset * 3 / 2),
        arrowprops=dict(arrowstyle="<-", color="red"),
    )
    ax2.scatter(
        [out_start_2[i], out_start_2[i] + out_group_bias_2[i]],
        [i + offset * 3 / 2, i + offset * 3 / 2],
        color="black",
        s=10,
    )
    ax2.annotate(
        f"{out_group_bias_2[i]:.2f}",
        (out_start_2[i] + out_group_bias_2[i], i + offset * 1.75),
        color="red",
        ha="right",
        va="center",
    )

    ax2.annotate(
        "",
        xy=(in_start_2[i], i + offset / 2),
        xytext=(in_start_2[i] + in_group_bias_2[i], i + offset / 2),
        arrowprops=dict(arrowstyle="<-", color="blue"),
    )
    ax2.scatter(
        [in_start_2[i], in_start_2[i] + in_group_bias_2[i]],
        [i + offset / 2, i + offset / 2],
        color="black",
        s=10,
    )
    ax2.annotate(
        f"{in_group_bias_2[i]:.2f}",
        (in_start_2[i] + in_group_bias_2[i], i + offset * 0.75),
        color="blue",
        ha="left",
        va="center",
    )

# set y-axis limits
ax1.set_ylim(0, len(languages_1))
ax2.set_ylim(0, len(languages_2))

# Set x-axis limits uniformly
ax1.set_xlim(0, 10)
ax2.set_xlim(0, 10)

# Adjust the y-axis tick positions
ax1.set_yticks([i + offset for i in range(len(languages_1))])
ax1.set_yticklabels(languages_1)
ax2.set_yticks([i + offset for i in range(len(languages_2))])
ax2.set_yticklabels(languages_2)
ax2.yaxis.tick_right()
ax2.yaxis.set_label_position("right")

# Offset grid lines on the y-axis
ax1.set_yticks([i for i in range(len(languages_1))], minor=True)
ax2.set_yticks([i for i in range(len(languages_2))], minor=True)
ax1.yaxis.grid(True, which="minor", linewidth=0.5, alpha=0.7, color="black")
ax2.yaxis.grid(True, which="minor", linewidth=0.5, alpha=0.7, color="black")

# add x-axis grid lines and set gap is 1
ax1.xaxis.set_major_locator(plt.MultipleLocator(1))
ax2.xaxis.set_major_locator(plt.MultipleLocator(1))
ax1.grid(axis="x", linestyle="--", linewidth=0.5)
ax2.grid(axis="x", linestyle="--", linewidth=0.5)

# Create arrow-shaped legend entries with a line that aligns with the arrowhead
red_arrow = mlines.Line2D(
    [],
    [],
    color="red",
    marker=">",
    linestyle="-",
    markersize=8,
    label=ax1_labels[0],
    linewidth=2,
    markeredgewidth=2,
    markevery=(1, 1),
)
blue_arrow = mlines.Line2D(
    [],
    [],
    color="blue",
    marker=">",
    linestyle="-",
    markersize=8,
    label=ax1_labels[1],
    linewidth=2,
    markeredgewidth=2,
    markevery=(1, 1),
)
fig.legend(handles=[red_arrow, blue_arrow], bbox_to_anchor=(0.45, 0), ncol=2)

red_arrow = mlines.Line2D(
    [],
    [],
    color="red",
    marker=">",
    linestyle="-",
    markersize=8,
    label=ax2_labels[0],
    linewidth=2,
    markeredgewidth=2,
    markevery=(1, 1),
)
blue_arrow = mlines.Line2D(
    [],
    [],
    color="blue",
    marker=">",
    linestyle="-",
    markersize=8,
    label=ax2_labels[1],
    linewidth=2,
    markeredgewidth=2,
    markevery=(1, 1),
)
fig.legend(handles=[red_arrow, blue_arrow], bbox_to_anchor=(0.85, 0), ncol=2)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save the plot
plt.tight_layout()
plt.savefig('quiver_1.pdf', bbox_inches='tight')
