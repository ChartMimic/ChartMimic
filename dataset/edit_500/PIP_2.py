import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Generate some dummy data
category1 = [
    450,
    530,
    310,
    420,
    510,
    540,
    620,
    850,
    1010,
    2020,
    8050,
]  # Male population in a city
category2 = [
    1120,
    710,
    330,
    440,
    580,
    810,
    1040,
    2040,
    3050,
    4090,
    7050,
]  # Female population in a city
bins = [0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9]
labels=["Male", "Female"]
xlabel="Population density"
xlim=[-0.1, 1.1]
ylim=[0, 20000]
ylabel="Number of individuals"
xticks=[0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
yticks=[0, 5000, 10000, 15000, 20000]
left, bottom, width, height = [0.3, 0.3, 0.3, 0.4]
insetxlim=[0.35, 0.7]
insetxticks=[0.35, 0.40, 0.45, 0.50, 0.55, 0.60, 0.65, 0.70]
insetylim=[0, 2000]
insetyticks=[0, 1000, 2000]
mainpointleft = [0.39, 0.74]
mainpointright = [0.74, 1000]
insetleft=[0.35, 0]
insetright=[0.7, 0]
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
    color="green",
    align="center",
    label=labels[0],
    edgecolor="white",
)
ax_main.bar(
    bins,
    category2,
    width=bar_width,
    color="blue",
    align="center",
    bottom=category1,
    label=labels[1],
    edgecolor="white",
)
ax_main.set_xlabel(xlabel)
ax_main.set_xlim(xlim)
ax_main.set_xticks(xticks)
ax_main.set_ylabel(ylabel)
ax_main.set_ylim(ylim)
ax_main.set_yticks(yticks)
ax_main.legend(loc="upper left", prop={"size": 16})
ax_main.grid()

# Create inset plot with adjusted bar widths and white borders

ax_inset = fig.add_axes([left, bottom, width, height])
ax_inset.bar(
    bins[:6],
    category1[:6],
    width=bar_width,
    color="green",
    align="center",
    edgecolor="white",
)
ax_inset.bar(
    bins[:6],
    category2[:6],
    width=bar_width,
    color="blue",
    align="center",
    bottom=category1[:6],
    edgecolor="white",
)
ax_inset.set_xlim(insetxlim)  # Zoom in on the right part of the data
ax_inset.set_xticks(
    insetxticks
)  # Zoom in on the right part of the data
ax_inset.set_ylim(insetylim)
ax_inset.set_yticks(insetyticks)
ax_inset.grid()

# Adding lines to connect the plots.
# Coordinates of the main plot corners
main_plot_left = ax_main.transData.transform_point(mainpointleft)
main_plot_right = ax_main.transData.transform_point(mainpointright)

# Coordinates of the inset corners
inset_left = ax_inset.transData.transform_point(insetleft)
inset_right = ax_inset.transData.transform_point(insetright)

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
plt.savefig('PIP_2.pdf', bbox_inches='tight')
