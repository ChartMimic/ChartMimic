import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data for plotting
x = 2 ** np.arange(4, 10)
savings_plan_2020 = np.array([50000, 75000, 100000, 125000, 150000, 175000])
savings_plan_2021 = np.array([55000, 80000, 105000, 130000, 155000, 180000])
investment_plan_2020 = np.array([2, 4, 6, 8, 12, 16])
investment_plan_2021 = np.array([3, 5, 7, 10, 14, 18])

labels = ["Savings Plan | 2020", "Savings Plan | 2021", "Investment Plan | 2020", "Investment Plan | 2021"]
xlabel = "Investment in Thousands (in 2^x)"
ylabel = "Projected Returns"
xlim = [0, 200000]
ylim = [0, 250000]
yticks = [0, 50000, 100000, 150000, 200000]
insetaxes = [0.6, 0.2, 0.35, 0.3]
yinsetlim = [0, 20]
xtickslabels = [f"$2^{i}$" for i in range(1, 7)]
xinsetxtickslabels = [f"$2^{i}$" for i in range(1, 7)]
yinsetyticks = [5, 10, 15]
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create the main figure and axis
fig, ax = plt.subplots(
    figsize=(6, 6)
)  # Adjusted to match the original image's dimensions

# Plot the data
ax.plot(x, savings_plan_2020, "o-", label=labels[0], color="green")
ax.plot(x, savings_plan_2021, "x-", label=labels[1], color="green")
ax.plot(x, investment_plan_2020, "o-", label=labels[2], color="blue")
ax.plot(x, investment_plan_2021, "x-", label=labels[3], color="blue")

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
ax_inset.plot(x, investment_plan_2020, "o-", color="blue")
ax_inset.plot(x, investment_plan_2021, "x-", color="blue")
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
