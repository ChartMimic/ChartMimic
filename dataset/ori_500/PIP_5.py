# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data for plotting
x = 2 ** np.arange(6, 12)
cos_n200 = np.array([100000, 150000, 200000, 250000, 300000, 350000])
cos_n400 = np.array([110000, 160000, 210000, 260000, 310000, 360000])
relu_n200 = np.array([1, 2, 4, 6, 10, 14])
relu_n400 = np.array([1, 3, 5, 8, 12, 16])

labels=["Cos | n0 = 200", "Cos | n0 = 400", "ReLU | n0 = 200", "ReLU | n0 = 400"]
xlabel="Width of Layer"
ylabel="Empirical Lipschitz Constant"
xilm =[-10000, 500000]
ylim =[-10000, 500000]
yticks =[0, 100000, 200000, 300000, 400000]
insetaxes =[0.6, 0.2, 0.35, 0.3]
yinsetlim=[0, 18]
xtickslabels=[f"$2^{i}$" for i in range(6, 12)]
xinsetxtickslabels=[f"$2^{i}$" for i in range(6, 12)]
yinsetyticks=[5, 10, 15]
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create the main figure and axis
fig, ax = plt.subplots(
    figsize=(6, 6)
)  # Adjusted to match the original image's dimensions

# Plot the data
ax.plot(x, cos_n200, "o-", label=labels[0], color="green")
ax.plot(x, cos_n400, "x-", label=labels[1], color="green")
ax.plot(x, relu_n200, "o-", label=labels[2], color="blue")
ax.plot(x, relu_n400, "x-", label=labels[3], color="blue")

# Set the x-axis to be logarithmic
ax.set_xscale("log")

# Set labels and title
ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)

# Adjust y-axis limits
ax.set_ylim(ylim)
ax.set_yticks(yticks)

# Add a legend
ax.legend()

# Create an inset axis for the ReLU data
ax_inset = fig.add_axes(
    insetaxes
)  # Adjusted to match the original image's inset position and size
ax_inset.plot(x, relu_n200, "o-", color="blue")
ax_inset.plot(x, relu_n400, "x-", color="blue")
ax_inset.set_xscale("log")

# Adjust y-axis limits for inset
ax_inset.set_ylim(yinsetlim)

# Set the same x-axis limits for the inset as the main plot
ax_inset.set_xlim(ax.get_xlim())
ax_inset.set_yticks(yinsetyticks)

# Change x-axis tick labels to powers of 2 notation
ax.set_xticks(x)
ax.set_xticklabels(xtickslabels)
ax_inset.set_xticks(x)
ax_inset.set_xticklabels(xinsetxtickslabels)

# ===================
# Part 4: Saving Output
# ===================
# Show the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig('PIP_5.pdf', bbox_inches='tight')
