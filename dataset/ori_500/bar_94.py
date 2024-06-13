# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

import matplotlib.gridspec as gridspec

# ===================
# Part 2: Data Preparation
# ===================
# Sample data
brightness_values = np.linspace(0.5, 1.4, 10)
scale_values = np.linspace(0.75, 1.2, 10)
rotation_values = np.linspace(-150, 120, 10)

# Sample gain change rates for 'Ours' and 'Saliency-based Sampling'
gain_change_brightness_ours = np.random.uniform(-30, 0, 10)
gain_change_scale_ours = np.random.uniform(-50, 100, 10)
gain_change_rotation_ours = np.random.uniform(-20, 40, 10)

gain_change_brightness_saliency = np.random.uniform(-30, 0, 10)
gain_change_scale_saliency = np.random.uniform(-50, 100, 10)
gain_change_rotation_saliency = np.random.uniform(-20, 40, 10)

labels = ["Ours", "Saliency-based Sampling"]
xlabels = ["Brightness", "Scale", "Rotation Angle [°]"]
ylabel = "Rate of Gain Change[%]"
ylims = [(-35, 8), (-60, 120), (-25, 45)]
xlims = [(0.4, 1.6), (0.7, 1.3), (-170, 170)]
yticks = [[-30, -20, -10, 0], [-50, 0, 50, 100], [-20, 0, 20, 40]]
xticks = [[0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4], [0.75, 0.8, 0.85, 0.9, 0.95, 1.0, 1.05, 1.1, 1.15, 1.2], [-150, -120, -90, -60, -30, 0, 30, 60, 90, 120]
]

# Create a gridspec
gs = gridspec.GridSpec(2, 2)  # Adjust the height ratios for each row

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
fig = plt.figure(figsize=(10, 6))

# Create axes using the gridspec
axs = [plt.subplot(gs[0, :]), plt.subplot(gs[1, 0]), plt.subplot(gs[1, 1])]

# Top chart - Brightness
axs[0].bar(
    brightness_values - 0.02,
    gain_change_brightness_ours,
    width=0.04,
    color="#ee8882",
    label=labels[0],
)
axs[0].bar(
    brightness_values + 0.02,
    gain_change_brightness_saliency,
    width=0.04,
    color="#8db7db",
    label=labels[1],
)
axs[0].set_xlabel(xlabels[0])
axs[0].set_ylabel(ylabel)
axs[0].set_ylim(ylims[0])
axs[0].set_xlim(xlims[0])
axs[0].set_yticks(yticks[0])
axs[0].set_xticks(xticks[0])
axs[0].grid(True)

# Middle chart - Scale
axs[1].bar(scale_values - 0.01, gain_change_scale_ours, width=0.02, color="#ee8882")
axs[1].bar(scale_values + 0.01, gain_change_scale_saliency, width=0.02, color="#8db7db")
axs[1].set_xlabel(xlabels[1])
axs[1].set_ylabel(ylabel)
axs[1].set_ylim(ylims[1])
axs[1].set_xlim(xlims[1])
axs[1].set_yticks(yticks[1])
axs[1].set_xticks(xticks[1])
axs[1].grid(True)

# Bottom chart - Rotation Angle
axs[2].bar(rotation_values - 5, gain_change_rotation_ours, width=10, color="#ee8882")
axs[2].bar(
    rotation_values + 5, gain_change_rotation_saliency, width=10, color="#8db7db"
)
axs[2].set_xlabel(xlabels[2])
axs[2].set_ylabel(ylabel)
axs[2].set_ylim(ylims[2])
axs[2].set_xlim(xlims[2])
axs[2].set_yticks(yticks[2])
axs[2].set_xticks(xticks[2])
axs[2].grid(True)

# Add legend
fig.legend(loc="upper center", ncol=2, bbox_to_anchor=(0.5, 1.03))

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save the figure
plt.tight_layout()
plt.savefig("bar_94.pdf", bbox_inches="tight")
