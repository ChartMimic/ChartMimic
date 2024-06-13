# ===================
# Part 1: Importing Libraries
# ===================

import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)

# ===================
# Part 2: Data Preparation
# ===================
# Variable extraction
line_label_base = "base"
line_label_ours = "ours"
xlim_values = (0, 200)
ylim_values_fid = (0.1, 0.6)
ylim_values_is = (0, 0.4)
ylim_values_cwfid = (0.1, 0.4)
ylim_values_cas = (0.1, 0.4)
xlabel_value = "Training iterations"
ylabel_value_fid = "FID (↓)"
ylabel_value_is = "IS (↑)"
ylabel_value_cwfid = "CW-FID (↓)"
ylabel_value_cas = "CAS (↑)"
yticks_values_fid = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]
yticks_values_is = [0, 0.1, 0.2, 0.3, 0.4]
yticks_values_cwfid = [0.1, 0.2, 0.3, 0.4]
yticks_values_cas = [0.1, 0.2, 0.3, 0.4]
legend_location = "upper center"
legend_bbox_to_anchor = (0.5, 1.2)
legend_frameon = False
legend_ncol = 2
grid_value = True

# Create subplots
fig, axs = plt.subplots(4, 1, figsize=(8, 10))

# FID
# Simulated data to match the reference picture
iterations = np.linspace(0, 200, 21)
iterations = [0., 10., 20., 30., 40., 50., 60., 70., 80., 90., 100., 110., 120., 130.,
 140., 150., 160., 170., 180., 190., 200.]
base_data = [0.54, 0.49, 0.49, 0.5, 0.48, 0.41, 0.43, 0.39, 0.38, 0.37, 0.35, 0.36, 0.34, 0.31,
 0.3, 0.28, 0.29, 0.24, 0.24, 0.2, 0.15]
ours_data = [0.41, 0.41, 0.38, 0.43, 0.35, 0.38, 0.37, 0.4, 0.39, 0.36, 0.36, 0.33, 0.3, 0.33,
 0.33, 0.35, 0.34, 0.31, 0.3, 0.28, 0.27]
# IS
# Simulated data to match the reference picture
base_data_is = [0.27, 0.33, 0.27, 0.26, 0.23, 0.27, 0.21, 0.23, 0.2, 0.22, 0.19, 0.17, 0.18, 0.18,
 0.16, 0.16, 0.13, 0.12, 0.11, 0.1, 0.08]
ours_data_is = [0.17, 0.21, 0.2, 0.18, 0.23, 0.21, 0.23, 0.25, 0.24, 0.27, 0.23, 0.26, 0.25, 0.25,
 0.26, 0.27, 0.28, 0.26, 0.31, 0.3, 0.27]

# CW-FID
base_data_cwfid = [0.33, 0.34, 0.32, 0.3, 0.28, 0.32, 0.29, 0.32, 0.3, 0.32, 0.31, 0.31, 0.3, 0.34,
 0.3, 0.31, 0.34, 0.27, 0.27, 0.32, 0.28]
ours_data_cwfid = [0.24, 0.19, 0.19, 0.24, 0.23, 0.24, 0.22, 0.18, 0.24, 0.19, 0.22, 0.22, 0.2, 0.21,
 0.22, 0.21, 0.18, 0.21, 0.23, 0.19, 0.2]

# CAS
base_data_cas = [0.19, 0.24, 0.21, 0.21, 0.18, 0.21, 0.19, 0.2, 0.19, 0.21, 0.21, 0.2, 0.21, 0.18,
 0.17, 0.21, 0.2, 0.21, 0.25, 0.22, 0.18]
ours_data_cas = [0.32, 0.27, 0.29, 0.3, 0.33, 0.29, 0.28, 0.3, 0.29, 0.32, 0.28, 0.28, 0.29, 0.29,
 0.34, 0.32, 0.3, 0.28, 0.32, 0.28, 0.27]
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plotting FID
axs[0].plot(iterations, base_data, label=line_label_base, color="blue")
axs[0].plot(iterations, ours_data, label=line_label_ours, color="orange")
axs[0].set_xlabel(xlabel_value)
axs[0].set_ylabel(ylabel_value_fid)
axs[0].set_xlim(*xlim_values)
axs[0].set_yticks(yticks_values_fid)
axs[0].tick_params(axis="both", which="both", color="gray")

# Plotting IS
axs[1].plot(iterations, base_data_is, label=line_label_base, color="blue")
axs[1].plot(iterations, ours_data_is, label=line_label_ours, color="orange")
axs[1].set_xlabel(xlabel_value)
axs[1].set_ylabel(ylabel_value_is)
axs[1].set_xlim(*xlim_values)
axs[1].set_yticks(yticks_values_is)
axs[1].tick_params(axis="both", which="both", color="gray")

# Plotting CW-FID
axs[2].plot(iterations, base_data_cwfid, label=line_label_base, color="blue")
axs[2].plot(iterations, ours_data_cwfid, label=line_label_ours, color="orange")
axs[2].set_xlabel(xlabel_value)
axs[2].set_ylabel(ylabel_value_cwfid)
axs[2].set_xlim(*xlim_values)
axs[2].set_yticks(yticks_values_cwfid)
axs[2].tick_params(axis="both", which="both", color="gray")

# Plotting CAS
axs[3].plot(iterations, base_data_cas, label=line_label_base, color="blue")
axs[3].plot(iterations, ours_data_cas, label=line_label_ours, color="orange")
axs[3].set_xlabel(xlabel_value)
axs[3].set_ylabel(ylabel_value_cas)
axs[3].set_xlim(*xlim_values)
axs[3].set_yticks(yticks_values_cas)
axs[3].tick_params(axis="both", which="both", color="gray")

# Add legends and gridlines to each subplot
for ax in axs.flat:
    ax.legend(loc=legend_location, bbox_to_anchor=legend_bbox_to_anchor, frameon=legend_frameon, ncol=legend_ncol)
    ax.grid(grid_value)  # Enable the grid

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save the plot
plt.tight_layout()
plt.savefig('line_13.pdf', bbox_inches='tight')
