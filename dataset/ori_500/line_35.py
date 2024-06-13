# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data for plotting
quantization_error = np.array(
    [10 ** (-7), 10 ** (-6.4), 10 ** (-5.7), 10 ** (-5.2), 10 ** (-4.5), 10 ** (-3.8)]
)
search_window_ratio = np.array([1, 1.05, 1.15, 1.2, 2, 6.6])

# Labels and Plot Types
x_M_LVQ_4x8_10 = 10 ** (-4.9)
label_M_LVQ_4x8_10 = "M-LVQ-4x8-10"
x_M_LVQ_4x8_100 = 10 ** (-4.8)
label_M_LVQ_4x8_100 = "M-LVQ-4x8-100"
x_M_LVQ_4x8_256 =10 ** (-4.6)
label_M_LVQ_4x8_256 = "M-LVQ-4x8-256"
x_M_LVQ_4x8 = 10 ** (-4.5)
label_M_LVQ_4x8 = "M-LVQ-4x8"
label_empirical_relat_B2_8_0 = "empirical relat. (B2=8.0)"

# Axes Limits and Labels
yticks_values = np.arange(0, 8, 1)
ylim_values = [0, 7]
xlabel_value = "Quantization error"
ylabel_value = "Search window size ratio"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create figure and axis
fig, ax = plt.subplots(figsize=(6, 4))

# Add vertical lines
ax.axvline(
    x=x_M_LVQ_4x8_10, color="#d86810", linestyle="--", label=label_M_LVQ_4x8_10, linewidth=3
)
ax.axvline(
    x=x_M_LVQ_4x8_100, color="#029e73", linestyle="--", label=label_M_LVQ_4x8_100, linewidth=3
)
ax.axvline(
    x=x_M_LVQ_4x8_256, color="#de8f05", linestyle="--", label=label_M_LVQ_4x8_256, linewidth=3
)
ax.axvline(
    x=x_M_LVQ_4x8, color="#cc78bc", linestyle="--", label=label_M_LVQ_4x8, linewidth=3
)

# Plot the empirical relationship line
ax.plot(
    quantization_error,
    search_window_ratio,
    label=label_empirical_relat_B2_8_0,
    color="#0173b2",
    marker="o",
    markersize=8,
    mec="white",
    linewidth=3,
)

# Set yticks
plt.yticks(yticks_values, fontsize=10)
plt.ylim(ylim_values)  # Adjusted y-axis limit

# Customize the plot
ax.set_xscale("log")
ax.set_xlabel(xlabel_value, fontsize=16)
ax.set_ylabel(ylabel_value, fontsize=16)

# Remove x-axis minor ticks
ax.tick_params(axis="x", which="minor", bottom=False)

# Add grid for major ticks only
ax.grid(True, which="major", linestyle="-", linewidth=0.5)

# Add legend
ax.legend(loc="upper left", bbox_to_anchor=(0, 1), fontsize=13)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()  # Adjust layout to not cut off legend
plt.savefig('line_35.pdf', bbox_inches='tight')
