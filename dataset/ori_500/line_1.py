# ===================
# Part 1: Importing Libraries
# ===================

import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)

# ===================
# Part 2: Data Preparation
# ===================
# Data (example values, the actual data should be extracted from the paper)
snr_values = [5, 10, 15, 20, 25]
jpeg_ldpc = [10, 30, 50, 70, 90]
deepjscc_wo_ofdm = [5, 15, 25, 35, 45]
deepjscc_w_ofdm = [20, 40, 60, 80, 95]
ours = [30, 60, 80, 95, 100]

# Labels and Plot Types
label_jpeg_ldpc = "JPEG+LDPC"
label_deepjscc_wo_ofdm = "DEEPJSCC w/o ofdm"
label_deepjscc_w_ofdm = "DEEPJSCC w/ ofdm"
label_ours = "OURS"

# Axes Limits and Labels
xlim_values = [5, 25]
ylim_values = [0, 100]
xlabel_value = "SNR"
ylabel_value = "Classification Accuracy (%)"
xticks_values = np.arange(5, 25, 5)
yticks_values = np.arange(0, 101, 20)
xtickslabel_values = None  # Not specified in the code
ytickslabel_values = None  # Not specified in the code
title_value = None  # Not specified in the code
axhiline_value = None  # Not specified in the code
axvline_value = None  # Not specified in the code

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plotting
plt.figure(figsize=(8, 6))  # Adjusting figure size to match original image dimensions
plt.plot(
    snr_values,
    jpeg_ldpc,
    "-o",
    label=label_jpeg_ldpc,
    color="#1f77b4",
    clip_on=False,
    zorder=10,
)
plt.plot(
    snr_values,
    deepjscc_wo_ofdm,
    "-^",
    label=label_deepjscc_wo_ofdm,
    color="#ff7f0e",
    clip_on=False,
    zorder=10,
)
plt.plot(
    snr_values,
    deepjscc_w_ofdm,
    "-x",
    label=label_deepjscc_w_ofdm,
    color="#2ca02c",
    clip_on=False,
    zorder=10,
)
plt.plot(snr_values, ours, "-x", label=label_ours, color="#d62728")

# Set y-axis to only display specific ticks and extend y-axis to leave space at top
plt.yticks(yticks_values)
plt.ylim(ylim_values)  # Adjusted y-axis limit
plt.xticks(xticks_values)
plt.xlim(xlim_values)

# Adding grid, legend, and labels
plt.grid(True)
plt.legend(loc="upper center", bbox_to_anchor=(0.5, 1.08), ncol=4, frameon=False)
plt.xlabel(xlabel_value)
plt.ylabel(ylabel_value)

# ===================
# Part 4: Saving Output
# ===================
# Adjusting layout to reduce white space
plt.tight_layout()
plt.savefig('line_1.pdf', bbox_inches='tight')
