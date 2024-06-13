# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Updated gradient steps
gradient_steps = np.linspace(0, 200, 50)

# Generate different trends for each line
line1_values = np.sin(gradient_steps * 0.1) + 1.0  # Sinusoidal trend
line2_values = np.array(gradient_steps) ** 2 * 0.0001 + 0.5  # Quadratic growth
line3_values = np.random.normal(
    loc=1.5, scale=0.2, size=len(gradient_steps)
)  # Random noise
line4_values = np.exp(0.01 * gradient_steps)  # Exponential growth

# Simulate standard deviations for error
std_dev = 0.1
line1_std = np.full_like(line1_values, std_dev)
line2_std = np.full_like(line2_values, std_dev)
line3_std = np.full_like(line3_values, std_dev)
line4_std = np.full_like(line4_values, std_dev)
xlabel="Gradient Steps (x 62.5K)"
labels =["Line 3 (Random Noise)","Line 4 (Exponential Focus)"]
ylabel="Exponential Scale"
xticks=np.linspace(0, 200, 9)
yticks=np.arange(0, 9, 1)
axesinset= [0.2, 0.5, 0.4, 0.2]
insetxlim=[25, 75]
insetylim=[1, 2]
insetxticks=[25, 50, 75]
insetyticks=[1, 1.5, 2]
arrowstart=(50, 3.5)
arrowend=(0.274, 0.22)
annotaterecx = [25,75]
annotaterecy = [1,2]


# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create a figure with a single plot
fig, ax = plt.subplots(figsize=(6, 6))

# Plot the third line on the main plot
ax.plot(
    gradient_steps, line3_values, "^--", color="green", label=labels[0]
)
ax.fill_between(
    gradient_steps,
    line3_values - line3_std,
    line3_values + line3_std,
    color="green",
    alpha=0.2,
)

# Plot the fourth line on the main plot
ax.plot(
    gradient_steps, line4_values, "*-", color="red", label=labels[1]
)
ax.fill_between(
    gradient_steps,
    line4_values - line4_std,
    line4_values + line4_std,
    color="red",
    alpha=0.2,
)

# Set labels, ticks, legend and grid for the main plot
ax.set_xlabel(xlabel, fontsize=12)
ax.set_ylabel(ylabel, fontsize=12)
ax.set_xticks(xticks)
ax.set_yticks(yticks)
ax.legend(loc="upper left", shadow=True, frameon=True, framealpha=0.9)
ax.grid(
    True, which="both", axis="both", color="lightgray", linestyle="--", linewidth=0.5
)
ax.set_facecolor("#f9f9f9")

# Draw a rectangle on the main plot to indicate the area of zoom-in
ax.plot([annotaterecx[0], annotaterecx[1]], [annotaterecy[1], annotaterecy[1]], color="black", lw=1)
ax.plot([annotaterecx[0], annotaterecx[1]], [annotaterecy[0], annotaterecy[0]], color="black", lw=1)
ax.plot([annotaterecx[0], annotaterecx[0]], [annotaterecy[0], annotaterecy[1]], color="black", lw=1)
ax.plot([annotaterecx[1], annotaterecx[1]], [annotaterecy[0], annotaterecy[1]], color="black", lw=1)

# Create the inset with the zoomed-in view
ax_inset = fig.add_axes(
    axesinset
)  # Adjust the position to align with the right side of the main plot

# Plot the third line on the inset
ax_inset.plot(
    gradient_steps, line3_values, "^--", color="green", label=labels[0]
)
ax_inset.fill_between(
    gradient_steps,
    line3_values - line3_std,
    line3_values + line3_std,
    color="green",
    alpha=0.2,
)

# Plot the fourth line on the inset
ax_inset.plot(
    gradient_steps, line4_values, "*-", color="red", label=labels[1]
)
ax_inset.fill_between(
    gradient_steps,
    line4_values - line4_std,
    line4_values + line4_std,
    color="red",
    alpha=0.2,
)

# Set limits, ticks and border color for the inset
ax_inset.set_xlim(insetxlim)
ax_inset.set_ylim(insetylim)
ax_inset.set_xticks(insetxticks)
ax_inset.set_yticks(insetyticks)
ax_inset.spines["bottom"].set_color("black")  # Add black border to the inset
ax_inset.spines["left"].set_color("black")
ax_inset.spines["top"].set_color("black")
ax_inset.spines["right"].set_color("black")

# Add an arrow from the rectangle on the main plot to the inset
ax.annotate(
    "",
    xy=arrowstart,  # Arrow start point (on the main plot)
    xytext=arrowend,  # Arrow end point (on the inset)
    textcoords="axes fraction",
    arrowprops=dict(facecolor="black", lw=0.1),
)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and display the plot
plt.tight_layout()
plt.savefig('PIP_10.pdf', bbox_inches='tight')
