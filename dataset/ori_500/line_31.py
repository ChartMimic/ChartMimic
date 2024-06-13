# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Placeholder data
digit_length = np.arange(6, 10)
direct_accuracy = [1.05, 0.95, 0.7, 0.75]
rfft_accuracy = [1.0, 0.9, 0.88, 0.6]
scratchpad_100_accuracy = [0.72, 0.52, 0.45, 0.38]
scratchpad_5000_accuracy = [0.65, 0.75, 0.8, 0.95]

# Placeholder error values
direct_error = np.random.uniform(0.01, 0.05, len(digit_length))
rfft_error = np.random.uniform(0.01, 0.05, len(digit_length))
scratchpad_100_error = np.random.uniform(0.01, 0.05, len(digit_length))
scratchpad_5000_error = np.random.uniform(0.01, 0.05, len(digit_length))

# Axes Limits and Labels
xlabel_value = "Digit Length"

ylabel_value = "Accuracy"
ylim_values = [0.5, 1.1]
yticks_values = np.arange(0.3, 1.1, 0.1)

# Labels
label_1 = "Direct (100 samples)"
label_2 = "RFFT (100 samples)"
label_3 = "Scratchpad (100 samples)"
label_4 = "Scratchpad (5000 samples)"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plotting the data
plt.figure(figsize=(8, 6))  # Adjusting figure size to match original image dimensions
plt.errorbar(
    digit_length,
    direct_accuracy,
    yerr=direct_error,
    fmt="-o",
    label=label_1,
    color="blue",
    linestyle="dashed",
)
plt.errorbar(
    digit_length,
    rfft_accuracy,
    yerr=rfft_error,
    fmt="-s",
    label=label_2,
    color="green",
    linestyle="dashed",
)
plt.errorbar(
    digit_length,
    scratchpad_100_accuracy,
    yerr=scratchpad_100_error,
    fmt="-^",
    label=label_3,
    color="orange",
    linestyle="dashed",
)
plt.errorbar(
    digit_length,
    scratchpad_5000_accuracy,
    yerr=scratchpad_5000_error,
    fmt="-d",
    label=label_4,
    color="red",
    linestyle="dashed",
)

# Adding labels and title
plt.xlabel(xlabel_value)
plt.ylabel(ylabel_value)
plt.xticks(digit_length)
plt.ylim(ylim_values)
plt.yticks(yticks_values)

# Adding legend, lower left corner
plt.legend(loc="lower left")

# Moving axes spines
ax = plt.gca()  # get current axes
ax.spines["right"].set_color("none")  # hide the right spine
ax.spines["top"].set_color("none")  # hide the top spine
ax.grid(
    True, which="both", axis="both", color="lightgray", linestyle="--", linewidth=0.5
)

# ===================
# Part 4: Saving Output
# ===================
# Display the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig('line_31.pdf', bbox_inches='tight')
