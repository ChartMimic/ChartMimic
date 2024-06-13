import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Sample data
x_green = np.random.normal(50, 10, 10)
y_green = np.random.normal(100, 20, 10)
x_green_additional = np.random.normal(300, 50, 10)
y_green_additional = np.random.normal(600, 100, 10)
x_green_total = np.concatenate([x_green, x_green_additional])
y_green_total = np.concatenate([y_green, y_green_additional])
x_blue = np.random.normal(45, 5, 5)
y_blue = np.random.normal(110, 15, 5)
x_orange = np.random.normal(70, 7, 5)
y_orange = np.random.normal(150, 10, 5)
xlabel = "Age (Years)"
ylabel = "Height (cm)"
ax1xlim = [0, 400]
ax1ylim = [50, 800]
diffline1 = [[0, 0],[50,800],[100, 400]]
diffline2 = [[0, 0], [100, 200], [150, 300]]
annotaterecx1 = [40, 90]
annotaterecy1 = [80, 160]
ax2xlim = [40, 80]
ax2ylim = [90, 160]
plotup1 = [40, 165]
plotdown1 = [40, 90]

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
ax1.fill_betweenx(y=[100, ax1ylim[1]], x1=50, x2=400, color="red", alpha=0.2)
ax1.fill_betweenx(y=[0, 100], x1=0, x2=50, color="green", alpha=0.2)

# Axis limits and aspect ratio
ax1.set_xlim(ax1xlim)
ax1.set_ylim(ax1ylim)
ax1.plot([50,50], [800,0], color="black", lw=0.5)
ax1.plot([0,400], [100,100], color="black", lw=0.5)

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
ax2.fill_betweenx(y=[100,400], x1=50, x2=400, color="red", alpha=0.2)
ax2.fill_betweenx(y=[0, 100], x1=0, x2=50, color="green", alpha=0.2)
# Axis limits and aspect ratio
ax2.set_xlim(ax2xlim)
ax2.set_ylim(ax2ylim)
ax2.plot([40,80], [100,100], color="black", lw=0.5)
ax2.plot([50,50], [90,160], color="black", lw=0.5)
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
