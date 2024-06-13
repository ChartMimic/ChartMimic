# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Sample data
x_green = np.random.normal(-4, 1, 10)
y_green = np.random.normal(2, 1, 10)
x_green_additional = np.random.normal(-30, 10, 10)
y_green_additional = np.random.normal(20, 10, 10)
x_green_total = np.concatenate([x_green, x_green_additional])
y_green_total = np.concatenate([y_green, y_green_additional])
x_blue = np.random.normal(-5, 1, 5)
y_blue = np.random.normal(3, 1, 5)
x_orange = np.random.normal(-1, 0.5, 5)
y_orange = np.random.normal(0, 0.5, 5)
xlabel="Δ Robust Accuracy (%)"
ylabel="Δ RNFR (%)"
ax1xlim = [-40, 5]
ax1ylim = [-5, 40]
diffline1 =[[0,0],[-40,5],[-5,40]]
diffline2 =[[0,0],[-8,3],[-8,6]]
annotaterecx1 = [-8, 3]
annotaterecy1 = [-3, 6]
ax2xlim = [-8, 1]
ax2ylim = [-3, 6]
plotup1=[-8, 6]
plotdown1=[-8, -3]


# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plot
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
# Scatter plots
ax1.scatter(x_green_total, y_green_total, marker="^", color="green")
ax1.scatter(x_blue, y_blue, marker="v", color="blue")
ax1.scatter(x_orange, y_orange, marker="D", color="orange")

# Shaded regions
ax1.fill_betweenx(y=[0, ax1ylim[1]], x1=ax1xlim[0], x2=0, color="red", alpha=0.2)
ax1.fill_betweenx(y=[0, ax1ylim[0]], x1=0, x2=ax1xlim[1], color="green", alpha=0.2)

# Axis limits and aspect ratio
ax1.set_xlim(ax1xlim)
ax1.set_ylim(ax1ylim)
ax1.plot(diffline1[1], diffline1[0], color="black", lw=0.5)
ax1.plot(diffline1[0], diffline1[2], color="black", lw=0.5)

ax1.plot([annotaterecx1[0], annotaterecx1[1]], [annotaterecy1[1], annotaterecy1[1]], color="black", lw=0.5)
ax1.plot([annotaterecx1[0], annotaterecx1[1]], [annotaterecy1[0], annotaterecy1[0]], color="black", lw=0.5)
ax1.plot([annotaterecx1[0], annotaterecx1[0]], [annotaterecy1[0], annotaterecy1[1]], color="black", lw=0.5)
ax1.plot([annotaterecx1[1], annotaterecx1[1]], [annotaterecy1[0], annotaterecy1[1]], color="black", lw=0.5)

ax1.set_xlabel(xlabel)
ax1.set_ylabel(ylabel)
ax1.grid(True, which="both", linestyle="--", lw=0.5)

# Scatter plots
ax2.scatter(x_green_total, y_green_total, marker="^", color="green")
ax2.scatter(x_blue, y_blue, marker="v", color="blue")
ax2.scatter(x_orange, y_orange, marker="D", color="orange")

# Shaded regions
ax2.fill_betweenx(y=[ax2ylim[1], 0], x1=ax2xlim[0], x2=0, color="red", alpha=0.2)
ax2.fill_betweenx(y=[0, ax2ylim[0]], x1=0, x2=ax2xlim[1], color="green", alpha=0.2)
# Axis limits and aspect ratio
ax2.set_xlim(ax2xlim)
ax2.set_ylim(ax2ylim)
ax2.plot(diffline2[1], diffline2[0], color="black", lw=0.5)
ax2.plot(diffline2[0], diffline2[2], color="black", lw=0.5)
ax2.grid(True, which="both", linestyle="--", lw=0.5)

# Coordinates of the main plot corners
ax1_plot_up = ax1.transData.transform_point(plotup1)
ax1_plot_down = ax1.transData.transform_point(plotdown1)

# Coordinates of the inset corners
ax2_up = ax2.transData.transform_point(plotup1)
ax2_down = ax2.transData.transform_point(plotdown1)

# Transform to figure coordinates for annotation
main_plot_up = fig.transFigure.inverted().transform(ax1_plot_up)
main_plot_down = fig.transFigure.inverted().transform(ax1_plot_down)
inset_up = fig.transFigure.inverted().transform(ax2_up)
inset_down = fig.transFigure.inverted().transform(ax2_down)

# Draw lines connecting corners
fig.add_artist(
    plt.Line2D(
        (main_plot_up[0], inset_up[0]), (main_plot_up[1], inset_up[1]), color="gray"
    )
)
fig.add_artist(
    plt.Line2D(
        (main_plot_down[0], inset_down[0]),
        (main_plot_down[1], inset_down[1]),
        color="gray",
    )
)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig('PIP_1.pdf', bbox_inches='tight')
