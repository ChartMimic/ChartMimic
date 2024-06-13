# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data for plotting
fraction_of_training_data = np.array([0.01, 0.1, 1])
full_accuracy = np.array([60, 70, 80])
spt_accuracy = np.array([55, 65, 78])
vpt_accuracy = np.array([42, 53, 65])

# Axes Limits and Labels
xlabel_value = "fraction of training data (log scale)"
xlim_values = [5, 25]

ylabel_value = "test accuracy (%)"
ylim_values = [38, 84]
yticks_values = np.arange(40, 82, 10)

# Labels
label_Full = "Full"
label_SPT = "SPT"
label_VPT = "VPT"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plotting the data
plt.figure(figsize=(5, 4))  # Adjusting figure size to match original image dimensions
plt.plot(fraction_of_training_data, full_accuracy, "o-", color="green", label=label_Full)
plt.plot(fraction_of_training_data, spt_accuracy, "o-", color="red", label=label_SPT)
plt.plot(fraction_of_training_data, vpt_accuracy, "o-", color="blue", label=label_VPT)

# Set y-axis to only display specific ticks and extend y-axis to leave space at top
plt.yticks(yticks_values, fontsize=16)
plt.ylim(ylim_values)  # Adjusted y-axis limit

# Set x-axis fontsize
plt.xticks(fontsize=16)

# Setting the x-axis to log scale
plt.xscale("log")

# Adding labels and title
plt.xlabel(xlabel_value, fontsize=16)
plt.ylabel(ylabel_value, fontsize=16)

# Adding grid
plt.grid(True, which="both", ls="-", linewidth=0.8)

# Adding legend, show it horizontally and place it at the lower right corner
plt.legend(loc="lower right", fontsize=12, ncol=3, columnspacing=0.5, edgecolor="black")

# ===================
# Part 4: Saving Output
# ===================
# Adjusting layout to add more space on the right
plt.tight_layout()
plt.savefig('line_19.pdf', bbox_inches='tight')
