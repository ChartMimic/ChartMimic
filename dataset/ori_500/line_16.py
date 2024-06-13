# ===================
# Part 1: Importing Libraries
# ===================

import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)

# ===================
# Part 2: Data Preparation
# ===================
# Data for plotting
uncertainty_threshold = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
oesense_accuracy = [1.00, 0.97, 0.96, 0.97, 0.98, 0.96]
kws_accuracy = [0.97, 0.95, 0.93, 0.92, 0.94, 0.95]
ecg5000_accuracy = [0.96, 0.94, 0.92, 0.90, 0.88, 0.86]

# Extracted variables
oesense_label = "Oesense"
kws_label = "KWS"
ecg5000_label = "ECG5000"

ylim_values = [0.84, 1.02]
yticks_values = [0.84, 0.87, 0.9, 0.93, 0.96, 0.99, 1.02]
yticks_labels = ["$0.84$", "$0.87$", "$0.9$", "$0.93$", "$0.96$", "$0.99$", "$1.02$"]
xlabel_value = "Uncertainty threshold"
ylabel_value = "Accuracy"
xlim_values = [0, 1]
xticks_fontsize = "16"
yticks_fontsize = "16"
xlabel_fontsize = "14"
ylabel_fontsize = "14"
legend_location = "lower left"
legend_ncol = 3
legend_bbox_to_anchor = (0, -0.2)
legend_frameon = False

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create figure and axis
fig, ax = plt.subplots(figsize=(8, 6))

# Plot the data
ax.plot(uncertainty_threshold, oesense_accuracy, "o-", label=oesense_label, clip_on=False, zorder=10, color="blue", linewidth=1.6, markersize=12)
ax.plot(uncertainty_threshold, kws_accuracy, "d-", label=kws_label, clip_on=False, zorder=10, color="red", linewidth=1.6, markersize=12)
ax.plot(uncertainty_threshold, ecg5000_accuracy, "^-", label=ecg5000_label, clip_on=False, zorder=10, color="green", linewidth=1.6, markersize=12)

plt.ylim(ylim_values)
plt.yticks(yticks_values, yticks_labels, fontsize=yticks_fontsize)

# Set x-axis to only display specific ticks and extend x-axis to leave space at right
plt.xticks(fontsize=xticks_fontsize)
plt.xlim(xlim_values)
plt.tick_params(axis="both", which="both", color="gray")

# Add legend, labels, and grid
ax.legend(loc=legend_location, ncol=legend_ncol, bbox_to_anchor=legend_bbox_to_anchor, frameon=legend_frameon)
ax.set_xlabel(xlabel_value, fontsize=xlabel_fontsize)
ax.set_ylabel(ylabel_value, fontsize=ylabel_fontsize)
ax.grid(True)

# ===================
# Part 4: Saving Output
# ===================
# Adjusting layout to add more space on the right
plt.tight_layout()
plt.savefig('line_16.pdf', bbox_inches='tight')
