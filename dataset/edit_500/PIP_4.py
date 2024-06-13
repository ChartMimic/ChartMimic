import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Generate some dummy data
category1 = [
    15000,
    8000,
    2500,
    2000,
    1500,
    1200,
    1000,
    800,
    1500,
    5000,
    4000,
]  # Known category
category2 = [
    10000,
    7000,
    5000,
    3000,
    2000,
    1000,
    1000,
    2000,
    1600,
    2400,
    2100,
]  # Unknown category
bins = [0.0, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.5]
labels = ["Known", "Unknown"]
xmainlabel = "Predicted Probability"
xmainlim = [-0.1, 0.8]
xmainticks = [0.0, 0.2, 0.4, 0.6]
ymainlabel = "Number of Observations"
ymainlim = [0, 30000]
ymainticks = [0, 10000, 20000, 30000]

xinsetlim = [0.20, 0.55]
xinsetticks = [0.25, 0.30, 0.35, 0.40, 0.45, 0.50]
yinsetlim = [0, 8000]
yinsetticks = [0, 3000, 6000, 8000]
# Create inset plot with adjusted bar widths and white borders
left, bottom, width, height = [0.5, 0.4, 0.3, 0.4]
mainplotline = [(0.235, 1500), (0.4, 1000)]
maininsetline = [(0.20, 0), (0.55, 0)]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create main plot with adjusted bar widths and white borders
fig, ax_main = plt.subplots(figsize=(10, 6))
bar_width = 0.05  # Slightly less than the bin width to create a gap
ax_main.bar(
    bins,
    category1,
    width=bar_width,
    color="#FC8D59",
    align="center",
    label=labels[0],
    edgecolor="white",
)
ax_main.bar(
    bins,
    category2,
    width=bar_width,
    color="#98C3DD",
    align="center",
    bottom=category1,
    label=labels[1],
    edgecolor="white",
)
ax_main.set_xlabel(xmainlabel)
ax_main.set_xlim(xmainlim)
ax_main.set_xticks(xmainticks)
ax_main.set_ylabel(ymainlabel)
ax_main.set_ylim(ymainlim)
ax_main.set_yticks(ymainticks)
ax_main.legend(loc="upper right", prop={"size": 16})
ax_main.grid()

ax_inset = fig.add_axes([left, bottom, width, height])
ax_inset.bar(
    bins[5:],
    category1[5:],
    width=bar_width,
    color="#FC8D59",
    align="center",
    edgecolor="white",
)
ax_inset.bar(
    bins[5:],
    category2[5:],
    width=bar_width,
    color="#98C3DD",
    align="center",
    bottom=category1[5:],
    edgecolor="white",
)
ax_inset.set_xlim(xinsetlim)  # Zoom in on the right part of the data
ax_inset.set_xticks(
    xinsetticks
)  # Zoom in on the right part of the data
ax_inset.set_ylim(yinsetlim)
ax_inset.set_yticks(yinsetticks)
ax_inset.grid()

# Adding lines to connect the plots.
# Coordinates of the main plot corners
main_plot_left = ax_main.transData.transform_point(mainplotline[0])
main_plot_right = ax_main.transData.transform_point(mainplotline[1])

# Coordinates of the inset corners
inset_left = ax_inset.transData.transform_point(maininsetline[0])
inset_right = ax_inset.transData.transform_point(maininsetline[1])

# Transform to figure coordinates for annotation
main_plot_left = fig.transFigure.inverted().transform(main_plot_left)
main_plot_right = fig.transFigure.inverted().transform(main_plot_right)
inset_left = fig.transFigure.inverted().transform(inset_left)
inset_right = fig.transFigure.inverted().transform(inset_right)

# Draw lines connecting corners
fig.add_artist(
    plt.Line2D(
        (main_plot_left[0], inset_left[0]),
        (main_plot_left[1], inset_left[1]),
        color="gray",
    )
)
fig.add_artist(
    plt.Line2D(
        (main_plot_right[0], inset_right[0]),
        (main_plot_right[1], inset_right[1]),
        color="gray",
    )
)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig('PIP_4.pdf', bbox_inches='tight')
