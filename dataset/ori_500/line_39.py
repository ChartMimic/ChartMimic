# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data for each subplot
x = [96, 192, 336, 512, 720]
y1_0 = [0.135, 0.136, 0.139, 0.141, 0.140]  # Example data for pred_length=96
y2_0 = [0.152, 0.153, 0.154, 0.157, 0.157]  # Example data for pred_length=192
y3_0 = [0.142, 0.144, 0.135, 0.136, 0.132]  # Example data for pred_length=336
y4_0 = [0.164, 0.163, 0.160, 0.162, 0.165]  # Example data for pred_length=720

y1_1 = [0.08, 0.075, 0.09, 0.072, 0.083]  # Example data for pred_length=96
y2_1 = [0.15, 0.142, 0.165, 0.170, 0.179]  # Example data for pred_length=192
y3_1 = [0.112, 0.106, 0.133, 0.114, 0.125]  # Example data for pred_length=336
y4_1 = [0.1, 0.092, 0.075, 0.105, 0.062]  # Example data for pred_length=720

y1_2 = [0.22, 0.20, 0.21, 0.19, 0.18]  # Example data for pred_length=96
y2_2 = [0.18, 0.17, 0.19, 0.175, 0.168]  # Example data for pred_length=192
y3_2 = [0.14, 0.145, 0.155, 0.135, 0.145]  # Example data for pred_length=336
y4_2 = [0.165, 0.125, 0.139, 0.129, 0.135]  # Example data for pred_length=720

y1_3 = [0.27, 0.29, 0.256, 0.278, 0.261]  # Example data for pred_length=96
y2_3 = [0.351, 0.388, 0.345, 0.366, 0.375]  # Example data for pred_length=192
y3_3 = [0.41, 0.406, 0.389, 0.400, 0.421]  # Example data for pred_length=336
y4_3 = [0.302, 0.312, 0.298, 0.325, 0.302]  # Example data for pred_length=720

# Axes Limits and Labels
xlim_values = [5, 25]
xticks_values = [96, 192, 336, 512, 720]

ylabel_value = "MSE"
ylim_values_1 = [0.128, 0.167]
yticks_values_1 = np.arange(0.130, 0.166, 0.005)
ylim_values_2 = [0.057, 0.185]
yticks_values_2 = np.arange(0.06, 0.19, 0.02)
ylim_values_3 = [0.117, 0.23]
yticks_values_3 = np.arange(0.12, 0.23, 0.02)
ylim_values_4 = [0.245, 0.427]
yticks_values_4 = np.arange(0.250, 0.426, 0.025)
# Labels
label_1 = "pred_length=96"
label_2 = "pred_length=192"
label_3 = "pred_length=336"
label_4 = "pred_length=720"

# Titles
title_1 = "Serial (n=8, m=1)"
title_2 = "Parallel (n=2, m=4)"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create figure and subplots
fig, axs = plt.subplots(1, 4, figsize=(15, 4))

# Plot data on each subplot
datasets = ["Traffic", "ETMm2", "ETTh2", "ECL"]

# Plot data on each subplot
axs[0].plot(x, y1_0, "o--", label=label_1, color="#4c92c3", markersize=10)
axs[0].plot(x, y2_0, "^--", label=label_2, color="#ff993e", markersize=10)
axs[0].plot(x, y3_0, "s--", label=label_3, color="#56b356", markersize=10)
axs[0].plot(x, y4_0, "*--", label=label_4, color="#de5253", markersize=10)
axs[0].set_xticks(xticks_values)
axs[0].set_title(datasets[0], fontsize=14)
axs[0].set_ylabel(ylabel_value, fontsize=14)
axs[0].set_yticks(yticks_values_1)
axs[0].set_ylim(ylim_values_1)

axs[1].plot(x, y1_1, "o--", label=label_1, color="#4c92c3", markersize=10)
axs[1].plot(x, y2_1, "^--", label=label_2, color="#ff993e", markersize=10)
axs[1].plot(x, y3_1, "s--", label=label_3, color="#56b356", markersize=10)
axs[1].plot(x, y4_1, "*--", label=label_4, color="#de5253", markersize=10)
axs[1].set_xticks(xticks_values)
axs[1].set_title(datasets[1], fontsize=14)
axs[1].set_ylabel("MSE", fontsize=14)
axs[1].set_yticks(yticks_values_2)
axs[1].set_ylim(ylim_values_2)

axs[2].plot(x, y1_2, "o--", label=label_1, color="#4c92c3", markersize=10)
axs[2].plot(x, y2_2, "^--", label=label_2, color="#ff993e", markersize=10)
axs[2].plot(x, y3_2, "s--", label=label_3, color="#56b356", markersize=10)
axs[2].plot(x, y4_2, "*--", label=label_4, color="#de5253", markersize=10)
axs[2].set_xticks(xticks_values)
axs[2].set_title(datasets[2], fontsize=14)
axs[2].set_ylabel(ylabel_value, fontsize=14)
axs[2].set_yticks(yticks_values_3)
axs[2].set_ylim(ylim_values_3)

axs[3].plot(x, y1_3, "o--", label=label_1, color="#4c92c3", markersize=10)
axs[3].plot(x, y2_3, "^--", label=label_2, color="#ff993e", markersize=10)
axs[3].plot(x, y3_3, "s--", label=label_3, color="#56b356", markersize=10)
axs[3].plot(x, y4_3, "*--", label=label_4, color="#de5253", markersize=10)
axs[3].set_xticks(xticks_values)
axs[3].set_title(datasets[3], fontsize=14)
axs[3].set_ylabel(ylabel_value, fontsize=14)
axs[3].set_yticks(yticks_values_4)
axs[3].set_ylim(ylim_values_4)

plt.legend(loc="center", bbox_to_anchor=(-1.6, -0.2), ncol=4, fontsize=14)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and show plot
plt.tight_layout()
plt.savefig('line_39.pdf', bbox_inches='tight')
