import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data
x = ["Spring", "Summer", "Fall", "Winter"]
y1 = [12.5, 15.0, 10.0, 8.0]
y2 = [14.0, 16.5, 11.5, 7.8]
y3 = [13.5, 14.5, 12.0, 9.0]
y4 = [11.0, 17.0, 9.5, 6.5]
labels = ["North Region", "South Region", "East Region", "West Region"]
insertax1 = [0.2, 0.2, 0.1, 0.3]
insertylim1 = [10.0, 18.0]
insertxlim1 = [0.5, 1.5]
insertax2 = [0.8, 0.5, 0.1, 0.3]
insertylim2 = [6.0, 10.0]
insertxlim2 = [2.5, 3.5]
xlabel = "Season"
ylabel = "Average Temperature (°C)"
title = "Average Temperature by Season and Region"
insetaxes = [0.45, 0.2, 0.1, 0.3]
arrowend1 = [0.45, 0.48]
arrowend2 = [0.90, 0.45]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plot
fig, ax = plt.subplots(
    figsize=(10, 6)
)  # Adjust figure size to match original image's dimensions

ax.plot(x, y1, "r-*", label=labels[0])
ax.plot(x, y2, "b-v", label=labels[1])
ax.plot(x, y3, "g--o", label=labels[2])
ax.plot(x, y4, "y-.s", label=labels[3])

# Create the inset with the zoomed-in view
ax_inset1 = fig.add_axes(
    insetaxes
)  # Adjust the position to align with the right side of the main plot
ax_inset1.plot(x, y1, "r-*")
ax_inset1.plot(x, y2, "b-v")
ax_inset1.plot(x, y3, "g--o")
ax_inset1.plot(x, y4, "y-.s")
ax_inset1.spines["bottom"].set_color("black")  # Add black border to the inset
ax_inset1.spines["left"].set_color("black")
ax_inset1.spines["top"].set_color("black")
ax_inset1.spines["right"].set_color("black")
ax_inset1.set_ylim(insertylim1)
ax_inset1.set_xlim(insertxlim1)

# Create the inset with the zoomed-in view
ax_inset2 = fig.add_axes(
    insertax2
)  # Adjust the position to align with the right side of the main plot
ax_inset2.plot(x, y1, "r-*")
ax_inset2.plot(x, y2, "b-v")
ax_inset2.plot(x, y3, "g--o")
ax_inset2.plot(x, y4, "y-.s")
ax_inset2.spines["bottom"].set_color("black")  # Add black border to the inset
ax_inset2.spines["left"].set_color("black")
ax_inset2.spines["top"].set_color("black")
ax_inset2.spines["right"].set_color("black")
ax_inset2.set_ylim(insertylim2)
ax_inset2.set_xlim(insertxlim2)

# Customizing the plot
ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)
ax.set_title(title)
ax.legend(loc="lower right")
ax.grid(True)

# Annotate with arrows
ax.annotate(
    "",
    xy=(x[1], y3[1]),
    xytext=arrowend1,
    textcoords="axes fraction",
    arrowprops=dict(facecolor="black", lw=0.1, shrink=0.01),
)
ax.annotate(
    "",
    xy=(x[3], y3[3]),  # Start from the Qwen-7B-Chat line at INT2
    xytext=arrowend2,  # Adjust these values as needed to point to your inset
    textcoords="axes fraction",
    arrowprops=dict(facecolor="black", lw=0.1, shrink=0.01),
)

# ===================
# Part 4: Saving Output
# ===================
# Show plot
plt.tight_layout()
plt.savefig('PIP_3.pdf', bbox_inches='tight')
