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
    + np.random.normal(0, 0.1, len(microphones)),
    0.2,
    0.9,
)
ami_wer = np.clip(
    np.cos(np.linspace(0, 2 * np.pi, len(microphones)))
    + np.random.normal(0, 0.1, len(microphones)),
    0.3,
    1,
)
# Axes Limits and Labels
xlabel_value = "Number of Microphones"

ylabel_value_1 = "WER(%)"
ylabel_value_2 = "AMI WER(%)"

# Labels
label_1 = "LibriCSS WER"
label_2 = "AMI WER"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create a figure and axis
fig, ax = plt.subplots(figsize=(8, 5))

(libricss_line,) = ax.plot(
    microphones,
    libricss_wer,
    "o-",
    color="#ff8b26",
    label=label_1,
    markersize=8,
    linewidth=2,
)
ax.set_xlabel(xlabel_value, fontsize=12)
ax.set_ylabel(ylabel_value_1, fontsize=12)
ax.tick_params(axis="y", direction="in", labelsize=10)
ax.tick_params(axis="x", direction="in", labelsize=10)

# Create a secondary y-axis for AMI WER
(ami_line,) = ax.plot(
    microphones,
    ami_wer,
    "s--",
    color="#0392fb",
    label=label_2,
    markersize=8,
    linewidth=2,
)

# Add a legend to the plot
threshold = 0.7
ax.axhline(y=threshold, color="red", linestyle="-", linewidth=1.5, label="Threshold")

# Highlight the data points above the threshold
highlight = [3, 5, 7]  # Microphones to highlight
for mic in highlight:
    ax.plot(
        mic, libricss_wer[np.where(microphones == mic)], "ro"
    )  # Highlight LibriCSS WER
    ax.annotate(
        f"Highlight {mic}",
        (mic, libricss_wer[np.where(microphones == mic)]),
        textcoords="offset points",
        xytext=(0, 10),
        ha="center",
    )

# Customize the plot with labels, title, and legend
ax.legend()

# Add a grid to the plot
ax.grid(True, linestyle="--", alpha=0.6)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout for better spacing and display
plt.tight_layout()
plt.savefig('line_69.pdf', bbox_inches='tight')
