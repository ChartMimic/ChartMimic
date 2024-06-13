# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data for the plot
microphones = np.array([2, 3, 4, 5, 6, 7, 8])
libricss_wer = np.clip(
    np.sin(np.linspace(0, 2 * np.pi, len(microphones)))
    + np.random.normal(0, 0.9, len(microphones)),
    0.2,
    0.9,
)
ami_wer = np.clip(
    np.cos(np.linspace(0, 3 * np.pi, len(microphones)))
    + np.random.normal(0, 5, len(microphones)),
    0.3,
    1,
)
highlight = [3, 5, 6]

# Axes Limits and Labels
xlabel_value = "Number of Microphones"

ylabel_value_1 = "WER(%)"
ylabel_value_2 = "AMI WER(%)"

# Labels
label_1 = "AMI WER"
label_2 = "Threshold"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create a figure with a 1x2 grid
fig, axs = plt.subplots(1, 2, figsize=(12, 5))

# Plot the LibriCSS data
(libricss_line,) = axs[0].plot(
    microphones,
    libricss_wer,
    "o-",
    color="#ffd638",
    label="LibriCSS WER",
    markersize=8,
    linewidth=2,
)
axs[0].set_xlabel(xlabel_value, fontsize=12)
axs[0].set_ylabel(ylabel_value_1, fontsize=12)
axs[0].tick_params(axis="y", direction="in", labelsize=10)
axs[0].tick_params(axis="x", direction="in", labelsize=10)

# Plot the AMI data
(ami_line,) = axs[1].plot(
    microphones,
    ami_wer,
    "s--",
    color="green",
    label=label_1,
    markersize=8,
    linewidth=2,
)
axs[1].set_xlabel(xlabel_value, fontsize=12)

# Add a legend to the plot
threshold = 0.7
axs[0].axhline(
    y=threshold, color="red", linestyle="-", linewidth=1.5, label=label_2
)
axs[1].axhline(
    y=threshold, color="red", linestyle="-", linewidth=1.5, label=label_2
)

# Highlight the data points above the threshold
for ax in axs:
    for mic in highlight:
        ax.plot(
            mic, libricss_wer[np.where(microphones == mic)], "ro"
        )  # Highlight LibriCSS WER
        ax.annotate(
            f"Highlight {mic}",
            (mic, libricss_wer[np.where(microphones == mic)]),
            textcoords="offset points",
            xytext=(0, -20),
            ha="center",
        )

# Customize the plot with labels, title, and legend
axs[0].legend()
axs[1].legend()

# Add a grid to the plot
for ax in axs:
    ax.grid(True, linestyle="--", alpha=0.6)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout for better spacing and display
plt.tight_layout()
plt.savefig('line_70.pdf', bbox_inches='tight')
