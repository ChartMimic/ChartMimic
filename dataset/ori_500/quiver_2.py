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

languages_2 = ["Japanese", "Korean", "Chinese"]
out_start_2 = [7.2, 6.2, 7.1]
out_group_bias_2 = [-4.75, -0.50, -4.00]
in_start_2 = [7.2, 7, 7.2]
in_group_bias_2 = [0.78, 0.25, 1.11]

# Axes Limits and Labels
xlim_values = [0, 10]
label = "Out-group bias\n(Collectivism)"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create figure with two subplots
fig, ax1 = plt.subplots(figsize=(5, 4))

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

# set y-axis limits
ax1.set_ylim(0, len(languages_1))

# Set x-axis limits uniformly
ax1.set_xlim(xlim_values)

# Adjust the y-axis tick positions
ax1.set_yticks([i + offset for i in range(len(languages_1))])
ax1.set_yticklabels(languages_1)

# Offset grid lines on the y-axis
ax1.set_yticks([i for i in range(len(languages_1))], minor=True)

ax1.yaxis.grid(True, which="minor", linewidth=0.5, alpha=0.7, color="black")

# add x-axis grid lines and set gap is 1
ax1.xaxis.set_major_locator(plt.MultipleLocator(1))

ax1.grid(axis="x", linestyle="--", linewidth=0.5)

# Create arrow-shaped legend entries with a line that aligns with the arrowhead
red_arrow = mlines.Line2D(
    [],
    [],
    color="red",
    marker=">",
    linestyle="-",
    markersize=8,
    label=label,
    linewidth=2,
    markeredgewidth=2,
    markevery=(1, 1),
)

fig.legend(handles=[red_arrow], bbox_to_anchor=(0.45, 0), ncol=2)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save the plot
plt.tight_layout()
plt.savefig('quiver_2.pdf', bbox_inches='tight')
