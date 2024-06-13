# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

import matplotlib.cm as cm
import matplotlib.colors as colors


# ===================
# Part 2: Data Preparation
# ===================
# Function to draw ellipses with varying radii and colors
xlim = [-6, 6]
ylim = [-6, 6]
xlabel = "Variable 1"
ylabel = "Variable 2"
num_ellipses = 10
a_start = 1
b_start = 1
a_end = 5
b_end = 2
# ===================
# Part 3: Plot Configuration and Rendering
# ===================


def draw_colored_ellipses(num_ellipses, a_start, b_start, a_end, b_end):
    t = np.linspace(0, 2 * np.pi, 100)
    fig, ax = plt.subplots(figsize=(6, 6))

    # Create a colormap
    cmap = cm.get_cmap("jet", num_ellipses)
    norm = colors.BoundaryNorm(np.arange(num_ellipses + 1), cmap.N)

    for i in range(num_ellipses):
        # Interpolate the semi-major and semi-minor axes
        a = np.linspace(a_start, a_end, num_ellipses)[i]
        b = np.linspace(b_start, b_end, num_ellipses)[i]

        # Parametric equations for the ellipse
        x = a * np.cos(t)
        y = b * np.sin(t)

        # Use a colormap to determine the color
        color = cmap(i)
        ax.set_xlim(xlim)
        ax.set_ylim(ylim)
        ax.plot(x, y, color=color)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)

    x_center = 0.6 * np.cos(t)
    y_center = 2.5 * np.sin(t)
    ax.plot(x_center, y_center, color="black")

    # Set the same scaling for both axes
    ax.set_aspect("equal")
    # Create a mappable object for the colorbar
    sm = cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])

    # Add the colorbar
    cbar = plt.colorbar(sm, ticks=np.arange(0.5, num_ellipses, 1), label="Time", ax=ax)
    cbar.set_ticklabels(np.arange(num_ellipses))  # set tick labels to 0 to 9
    cbar.ax.tick_params(length=0)


# Show the plot
draw_colored_ellipses(
    num_ellipses=num_ellipses,
    a_start=a_start,
    b_start=b_start,
    a_end=a_end,
    b_end=b_end,
)
plt.tight_layout()

# ===================
# Part 4: Saving Output
# ===================
plt.savefig("HR_2.pdf", bbox_inches="tight")
