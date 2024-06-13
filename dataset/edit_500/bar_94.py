import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0); np.random.seed(0)

import matplotlib.gridspec as gridspec

# ===================
# Part 2: Data Preparation
# ===================
# Sample data
# New domain: Agricultural yield optimization

# Variable ranges for different parameters
water_usage = np.linspace(10, 100, 10)  # in liters
fertilizer_amount = np.linspace(10, 50, 10)  # in kg
temperature = np.linspace(15, 30, 10)  # in degrees Celsius

# Sample yield change rates for 'Organic Methods' and 'Conventional Methods'

yield_change_water_organic =[10.98, 14.3, 12.06, 10.9, 8.47, 12.92, 8.75, 17.84, 19.27, 7.67]
yield_change_fertilizer_organic = [41.67, 31.16, 32.72, 47.02, 12.84, 13.49, 10.81, 43.3, 41.13, 44.8]
yield_change_temperature_organic = [9.57, 5.98, -0.77, 5.61, -7.63, 2.8, -7.13, 8.89, 0.44, -1.71]

yield_change_water_conventional = [-2.06, 13.23, 3.68, 7.05, -9.44, 8.53, 8.36, 8.51, 18.31, 10.45]
yield_change_fertilizer_conventional = [11.57, 16.22, 31.86, -6.39, 30.01, 30.24, 2.62, -2.26, 8.93, 11.82]
yield_change_temperature_conventional = [1.4, -1.23, 9.77, -7.96, -5.82, -6.77, 3.06, -4.93, -0.67, -5.11]

labels = ["Organic Methods", "Conventional Methods"]
xlabels = ["Water Usage [liters]", "Fertilizer Amount [kg]", "Temperature [°C]"]
ylabel = "Yield Change Rate [%]"
ylims = [[-100, 100], [-60, 60], [-15, 15]]
xlims = [[10, 110], [8, 52], [13, 32]]
yticks = [[-100,-50,0, 50,100], [-50, -25, 0, 25, 50], [-10, -5, 0, 5, 10]]
xticks = [[0,30,50,80,110],
          [10, 15, 20, 25, 30, 35, 40, 45, 50],
          [15, 18, 21, 24, 27, 30]]

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
    water_usage - 2,
    yield_change_fertilizer_organic,
    width=4,
    color="#ee8882",
    label=labels[0],
)
axs[0].bar(
    water_usage + 2,
    yield_change_water_conventional,
    width=4,
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
axs[1].bar(fertilizer_amount - 0.5, yield_change_fertilizer_organic, width=1, color="#ee8882")
axs[1].bar(fertilizer_amount + 0.5, yield_change_fertilizer_conventional, width=1, color="#8db7db")
axs[1].set_xlabel(xlabels[1])
axs[1].set_ylabel(ylabel)
axs[1].set_ylim(ylims[1])
axs[1].set_xlim(xlims[1])
axs[1].set_yticks(yticks[1])
axs[1].set_xticks(xticks[1])
axs[1].grid(True)

# Bottom chart - Rotation Angle
axs[2].bar(temperature - 0.5, yield_change_temperature_organic, width=0.6, color="#ee8882")
axs[2].bar(
    temperature + 0.3, yield_change_temperature_conventional, width=0.6, color="#8db7db"
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
plt.savefig('bar_94.pdf', bbox_inches='tight')
