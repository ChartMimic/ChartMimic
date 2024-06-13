# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data
x = ["BFloat16", "INT8", "INT4", "INT2"]
y1 = [9, 6.2, 8.0, 9.1]
y2 = [8, 6.3, 8.2, 9.2]
y3 = [7, 6.4, 8.4, 9.0]
y4 = [2, 6.0, 7.8, 8.9]
labels= ["Qwen-7B-Chat", "Llama2-7B-Chat", "MPT-7B-Chat", "CodeLlama-7B-Instruct"]
insertax1=[0.45, 0.2, 0.1, 0.3]
insertylim1=[5.9, 6.5]
insertxlim1=[0.5, 1.5]
insertax2=[0.8, 0.4, 0.1, 0.3]
insertylim2=[8.8, 9.3]
insertxlim2=[2.5, 3.5]
xlabel="Data Type"
ylabel="Bias Score"
title="Bias Score by Data Type and Model"
insetaxes=[0.45, 0.2, 0.1, 0.3]
arrowend1 = [0.48, 0.5]
arrowend2 = [0.85, 0.75]


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
    xy=(x[1], y4[1]),
    xytext=arrowend1,
    textcoords="axes fraction",
    arrowprops=dict(facecolor="black", lw=0.1, shrink=0.01),
)
ax.annotate(
    "",
    xy=(x[3], y4[3]),  # Start from the Qwen-7B-Chat line at INT2
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
