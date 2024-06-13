# ===================
# Part 1: Importing Libraries
# ===================

import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)

# ===================
# Part 2: Data Preparation
# ===================
t = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0]
y1 = [0.18, 0.52, 0.94, 1.22, 1.1, 0.5, 0.24, -0.37, -0.77, -0.94, -0.94, -0.56, -0.2, 0.23, 0.7, 0.97, 1.14, 0.78, 0.44, -0.16, -0.8]
y2 = [1.07, 0.96, 0.47, 0.3, -0.56, -0.8, -1.01, -0.78, -0.51, -0.2, 0.32, 0.62, 0.76, 0.94, 0.77, 0.47, -0.03, -0.64, -0.94, -1.1, -0.98]
y3 = [-0.17, 0.62, 0.67, 0.87, 0.9, 1.16, 0.94, 1.07, 0.96, 1.04, 0.89, 0.76, 0.81, 0.79, 0.69, 0.65, 0.49, 0.46, 0.38, 0.36, 0.28]
y4 = [-0.17, 0.42, 0.65, 0.75, 1.14, 1.16, 1.39, 1.58, 1.62, 1.82, 1.67, 1.91, 1.88, 1.93, 2.02, 2.11, 2.2, 2.13, 2.39, 2.4, 2.24]


# Labels for legend
label_sin_wave = "Sin Wave"
label_cos_wave = "Cos Wave"
label_exp_decay = "Exp Decay"
label_log_growth = "Log Growth"

# Plot configuration
xlim_values = (0, 10)
ylim_values_sin_cos = (-1.5, 1.5)
ylim_values_exp = (-0.2, 1.2)
ylim_values_log = (0, 2.5)

xlabel_value = "Time"
ylabel_value = "Amplitude"
ylabel_value_exp_log = "Value"

title_sin = "Sinusoidal Pattern"
title_cos = "Cosine Pattern"
title_exp = "Exponential Decay"
title_log = "Logarithmic Growth"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
fig, axs = plt.subplots(4, 1, figsize=(6, 12))

axs[0].plot(t, y1, label=label_sin_wave, color="magenta")
axs[0].set_xlim(*xlim_values)
axs[0].set_ylim(*ylim_values_sin_cos)
axs[0].set_title(title_sin, y=1.1)
axs[0].set_xlabel(xlabel_value)
axs[0].set_ylabel(ylabel_value)

axs[1].plot(t, y2, label=label_cos_wave, color="green")
axs[1].set_xlim(*xlim_values)
axs[1].set_ylim(*ylim_values_sin_cos)
axs[1].set_title(title_cos, y=1.1)
axs[1].set_xlabel(xlabel_value)
axs[1].set_ylabel(ylabel_value)

axs[2].plot(t, y3, label=label_exp_decay, color="blue")
axs[2].set_xlim(*xlim_values)
axs[2].set_ylim(*ylim_values_exp)
axs[2].set_title(title_exp, y=1.1)
axs[2].set_xlabel(xlabel_value)
axs[2].set_ylabel(ylabel_value_exp_log)

axs[3].plot(t, y4, label=label_log_growth, color="red")
axs[3].set_xlim(*xlim_values)
axs[3].set_ylim(*ylim_values_log)
axs[3].set_title(title_log, y=1.1)
axs[3].set_xlabel(xlabel_value)
axs[3].set_ylabel(ylabel_value_exp_log)

for ax in axs.flat:
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, 1.15), frameon=False)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig('line_51.pdf', bbox_inches='tight')
