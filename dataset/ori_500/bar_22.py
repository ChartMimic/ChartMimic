# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

np.random.seed(0)

# ===================
# Part 2: Data Preparation
# ===================
# Sample data
brightness_values = np.linspace(0.5, 1.5, 11)
scale_values = np.linspace(0.75, 1.25, 11)
rotation_values = np.linspace(-150, 150, 11)

# Sample gain change rates for 'Ours' and 'Saliency-based Sampling'
gain_change_brightness_ours = np.random.uniform(-30, 0, 11)
gain_change_scale_ours = np.random.uniform(-50, 10, 11)
gain_change_rotation_ours = np.random.uniform(-20, 40, 11)

gain_change_brightness_saliency = np.random.uniform(-30, 0, 11)
gain_change_scale_saliency = np.random.uniform(-50, 10, 11)
gain_change_rotation_saliency = np.random.uniform(-20, 40, 11)


brightness_values = np.array([0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5])
scale_values = np.array([0.75, 0.8, 0.85, 0.9, 0.95, 1.0, 1.05, 1.1, 1.15, 1.2, 1.25])
rotation_values = np.array(
    [
        -150.0,
        -120.0,
        -90.0,
        -60.0,
        -30.0,
        0.0,
        30.0,
        60.0,
        90.0,
        120.0,
        150.0,
    ]
)
gain_change_brightness_ours = np.array(
    [
        -13.54,
        -8.54,
        -11.92,
        -13.65,
        -17.29,
        -10.62,
        -16.87,
        -3.25,
        -1.09,
        -18.5,
        -6.25,
    ]
)
gain_change_scale_ours = np.array(
    [
        -18.27,
        -15.92,
        5.54,
        -45.74,
        -44.77,
        -48.79,
        -0.04,
        -3.31,
        2.2,
        8.72,
        -2.05,
    ]
)
gain_change_rotation_ours = np.array(
    [
        7.69,
        26.83,
        -12.9,
        18.4,
        -11.4,
        36.68,
        11.31,
        4.88,
        -4.13,
        26.45,
        7.37,
    ]
)
gain_change_brightness_saliency = np.array(
    [
        -12.95,
        -29.44,
        -11.47,
        -11.64,
        -11.49,
        -1.69,
        -9.55,
        -19.21,
        -16.89,
        -9.07,
        -28.19,
    ]
)
gain_change_scale_saliency = np.array(
    [
        -9.99,
        -9.76,
        -37.38,
        -42.26,
        -31.07,
        -28.18,
        -15.79,
        -23.68,
        9.3,
        -43.88,
        -37.47,
    ]
)
gain_change_rotation_saliency = np.array(
    [
        -10.32,
        19.19,
        -4.8,
        7.98,
        -5.33,
        -10.46,
        -13.38,
        19.38,
        -11.71,
        -8.21,
        2.12,
    ]
)
# Extracted variables
label_ours = "Ours"
label_saliency = "Saliency-based Sampling"
xlabel_brightness = "Brightness"
ylabel_gain_change = "Rate of Gain Change[%]"
xlabel_scale = "Scale"
xlabel_rotation = "Rotation Angle [°]"
ylim_brightness = (-30, 0)
xlim_brightness = (0.46, 1.54)
yticks_brightness = [-30, -20, -10, 0]
xticks_brightness = [0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5]
ylim_scale = (-50, 10)
xlim_scale = (0.73, 1.27)
yticks_scale = [-50, -40, -30, -20, -10, 0, 10]
xticks_scale = [0.75, 0.8, 0.85, 0.9, 0.95, 1.0, 1.05, 1.1, 1.15, 1.2, 1.25]
ylim_rotation = (-20, 40)
xlim_rotation = (-165, 165)
yticks_rotation = [-20, -10, 0, 10, 20, 30, 40]
xticks_rotation = [-150, -120, -90, -60, -30, 0, 30, 60, 90, 120, 150]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create figure and subplots
fig, axs = plt.subplots(3, 1, figsize=(6, 10))

# Top chart - Brightness
axs[0].bar(
    brightness_values - 0.02,
    gain_change_brightness_ours,
    width=0.04,
    zorder=10,
    color="#4c4cf6",
    label=label_ours,
)
axs[0].bar(
    brightness_values + 0.02,
    gain_change_brightness_saliency,
    width=0.04,
    zorder=10,
    color="#b2b2fa",
    label=label_saliency,
)
axs[0].set_xlabel(xlabel_brightness)
axs[0].set_ylabel(ylabel_gain_change)
axs[0].set_ylim(ylim_brightness)
axs[0].set_xlim(xlim_brightness)
axs[0].set_yticks(yticks_brightness)
axs[0].xaxis.set_major_locator(ticker.FixedLocator(xticks_brightness))
axs[0].xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f"{x}"))
offsetticks2 = [0.45] + [i + 0.05 for i in xticks_brightness]
axs[0].xaxis.set_minor_locator(ticker.FixedLocator(offsetticks2))
axs[0].grid(True, which="minor", axis="x", color="gray")
axs[0].grid(True, which="major", axis="y", color="gray")
axs[0].tick_params(axis="x", which="major", length=0)

# Middle chart - Scale
axs[1].bar(
    scale_values - 0.01,
    gain_change_scale_ours,
    width=0.02,
    zorder=10,
    color="#4c4cf6",
)
axs[1].bar(
    scale_values + 0.01,
    gain_change_scale_saliency,
    width=0.02,
    zorder=10,
    color="#b2b2fa",
)
axs[1].set_xlabel(xlabel_scale)
axs[1].set_ylabel(ylabel_gain_change)
axs[1].set_ylim(ylim_scale)
axs[1].set_xlim(xlim_scale)
axs[1].set_yticks(yticks_scale)
axs[1].xaxis.set_major_locator(ticker.FixedLocator(xticks_scale))
axs[1].xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f"{x}"))
offsetticks1 = [0.725] + [i + 0.025 for i in xticks_scale]
axs[1].xaxis.set_minor_locator(ticker.FixedLocator(offsetticks1))
axs[1].grid(True, which="minor", axis="x", color="gray")
axs[1].grid(True, which="major", axis="y", color="gray")
axs[1].tick_params(axis="x", which="major", length=0)

# Bottom chart - Rotation Angle
axs[2].bar(
    rotation_values - 5,
    gain_change_rotation_ours,
    width=10,
    zorder=10,
    color="#4c4cf6",
)
axs[2].bar(
    rotation_values + 5,
    gain_change_rotation_saliency,
    width=10,
    zorder=10,
    color="#b2b2fa",
)
axs[2].set_xlabel(xlabel_rotation)
axs[2].set_ylabel(ylabel_gain_change)
axs[2].set_ylim(ylim_rotation)
axs[2].set_xlim(xlim_rotation)
axs[2].set_yticks(yticks_rotation)
axs[2].tick_params(axis="x", which="major", length=0)

axs[2].xaxis.set_major_locator(ticker.FixedLocator(xticks_rotation))
axs[2].xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f"{int(x)}"))
offsetticks = [-165, -135, -105, -75, -45, -15, 15, 45, 75, 105, 135, 165]
axs[2].xaxis.set_minor_locator(ticker.FixedLocator(offsetticks))
axs[2].grid(True, which="minor", axis="x", color="gray")
axs[2].grid(True, which="major", axis="y", color="gray")

# Add legend
fig.legend(loc="upper center", ncol=2, bbox_to_anchor=(0.5, 1.03), frameon=False)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save the figure
plt.tight_layout()
plt.savefig("bar_22.pdf", bbox_inches="tight")
