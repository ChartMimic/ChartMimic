# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)

from matplotlib.ticker import FuncFormatter, FixedLocator

# ===================
# Part 2: Data Preparation
# ===================
# Data for plotting
N = np.array([4, 6, 10, 15, 30])
standard = np.array([1e-8, 1e-3, 1e-5, 1e-4, 1e-6])
constrained = np.array([1e-12, 1e-13, 1e-12, 1e-11, 1e-10])

# Axes Limits and Labels
xlabel_value = "N"

yticks_values = [10**-2, 10**-4, 10**-6, 10**-8, 10**-10, 10**-12, 10**-14]
yticks_labels = [
        "$10^{-2}$",
        "$10^{-4}$",
        "$10^{-6}$",
        "$10^{-8}$",
        "$10^{-10}$",
        "$10^{-12}$",
        "$10^{-14}$",
    ]
ylim_values = [0.5e-15, 5e-2]

axvline_x = 10**1
        
# Labels
label_Standard = "Standard"
label_Constrained = "Constrained"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plotting the data
plt.figure(figsize=(9, 6))
plt.plot(
    N, standard, "o-", label=label_Standard, color="#1f77b4", linewidth=1.4, markersize=4
)
plt.plot(
    N,
    constrained,
    "x-",
    label=label_Constrained,
    color="#ff7f0e",
    markersize=6,
    markeredgewidth=1,
)

# Setting the x-axis and y-axis to log scale
plt.xscale("log")
plt.yscale("log")

# Set y-axis to only display specific ticks and extend y-axis to leave space at top
plt.yticks(
    yticks_values,
    yticks_labels,
)
plt.ylim(ylim_values)  # Extend y-axis to leave some space above 10^-1

# Disable the automatic grid for x-axis
plt.grid(True, which="both", ls="--", axis="y")  # Only enable y-axis grid

# Manually add a grid line for x=10**1
plt.axvline(x=axvline_x, color="grey", linestyle="--", linewidth=0.5)

# Adjusting x-axis ticks to only show x=10**1
plt.gca().xaxis.set_major_locator(FixedLocator([10**1]))

# Formatting the x-axis and y-axis tick labels
plt.gca().xaxis.set_major_formatter(FuncFormatter(lambda value, _: "10"))
plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda y, _: "{:.0e}".format(y)))

# Adding labels and title
plt.xlabel(xlabel_value, fontsize=12)

# Adding a legend at the center right
plt.legend(loc="center left", bbox_to_anchor=(0.67, 0.5), fontsize=18)

# ===================
# Part 4: Saving Output
# ===================
# Adjusting layout to reduce white space
plt.tight_layout()
plt.savefig('line_9.pdf', bbox_inches='tight')
