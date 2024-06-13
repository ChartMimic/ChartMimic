# ===================
# Part 1: Importing Libraries
# ===================

import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Data for plotting
sample_ratio = [0.25, 0.50, 0.75, 1.00]
std_acc_512 = [0.07, 0.06, 0.01, 0.05]
std_acc_1024 = [0.055, 0.045, 0.04, 0.035]
std_acc_2048 = [0.03, 0.025, 0.02, 0.015]

# Extracted variables
line_label_512 = "MAXN=512"
line_label_1024 = "MAXN=1024"
line_label_2048 = "MAXN=2048"
xlim_values = (0.25, 1)
ylim_values = (0.00, 0.08)
xlabel_value = "Sample Ratio"
ylabel_value = "Std of ACC"
xticks_values = sample_ratio
yticks_values = None  # Not explicitly set in the code
xtickslabel_fontsize = 14
ytickslabel_fontsize = 14
title_value = None  # Not explicitly set in the code
axhline_value = None  # Not explicitly set in the code
axvline_value = None  # Not explicitly set in the code

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plotting the lines with increased marker size and line width
plt.figure(figsize=(8, 6))
plt.plot(
    sample_ratio,
    std_acc_512,
    marker="*",
    markersize=10,
    linewidth=2,
    color="#2ab34a",
    label=line_label_512,
    clip_on=False,
    zorder=10,
)
plt.plot(
    sample_ratio,
    std_acc_1024,
    marker="^",
    markerfacecolor="white",
    markersize=10,
    linewidth=2,
    markeredgecolor="#ee756e",
    color="#ee756e",
    clip_on=False,
    zorder=10,
    label=line_label_1024,
)
plt.plot(
    sample_ratio,
    std_acc_2048,
    marker="o",
    markerfacecolor="white",
    markersize=10,
    linewidth=2,
    markeredgecolor="#4995c6",
    color="#4995c6",
    clip_on=False,
    zorder=10,
    label=line_label_2048,
)

# Setting the x-axis and y-axis limits
plt.ylim(*ylim_values)  # Set y-axis to go from 0 to 7
plt.yticks(fontsize=ytickslabel_fontsize)
plt.xlim(*xlim_values)  # Set y-axis to go from 0 to 7
# Set x-axis to show only the values in the sample_ratio list
plt.xticks(xticks_values, fontsize=xtickslabel_fontsize)

# Adding labels and title
plt.xlabel(xlabel_value, fontsize=18)
plt.ylabel(ylabel_value, fontsize=18)

# Adding legend with increased font size
plt.legend(
    fontsize="large",
    loc="upper center",
    ncol=3,
    frameon=False,
    bbox_to_anchor=(0.5, 1.1),
)

# Adding grid
plt.grid(True, alpha=0.6)

# ===================
# Part 4: Saving Output
# ===================
# Adjusting layout to reduce white space
plt.tight_layout()
plt.savefig('line_12.pdf', bbox_inches='tight')
