# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)

from matplotlib.lines import Line2D

# ===================
# Part 2: Data Preparation
# ===================
# Data for the plot
microphones = np.array([2, 3, 4, 5, 6, 7, 8])
libricss_wer = np.clip(
    np.linspace(7, 3.2, len(microphones)) + np.random.normal(0, 0.2, len(microphones)),
    3,
    8,
)
ami_wer = np.clip(
    np.linspace(28, 21, len(microphones)) + np.random.normal(0, 0.5, len(microphones)),
    20,
    28,
)
ihm_wer = [2.5, 2.6, 2.7, 2.8, 2.9, 3.0, 3.1]  # Slightly changing IHM error rates
sdm_wer = [9.5, 9.0, 8.5, 8.0, 7.5, 7.0, 6.5]  # Decreasing SDM error rates

# Axes Limits and Labels
xlabel_value = "Number of microphones"

ylabel_value_1 = "WER(%)"
ylabel_value_2 = "AMI WER(%)"
ylim_values_1 = [2, 10]
ylim_values_2 = [20, 30]
yticks_values_1 = np.arange(2, 10, 1)
yticks_values_2 = np.arange(20, 30, 2)

# Labels
label_1 = "LibriCSS (test)"
label_2 = "ImageNet-C/P (Fog)"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create a figure and axis
fig, ax1 = plt.subplots(figsize=(8, 7))

# LibriCSS and AMI WER plots
(libricss_line,) = ax1.plot(
    microphones,
    libricss_wer,
    color="#377eb8",
    label=label_1,
    markersize=10,
    linewidth=3,
    mec="black",
    linestyle="-.",
    marker="o",
)
ax1.set_xlabel(xlabel_value, fontsize=14)
ax1.set_ylabel(ylabel_value_1, fontsize=14, color="#377eb8")
ax1.tick_params(
    axis="y", labelcolor="#377eb8", direction="in", rotation=90, labelsize=12
)
ax1.tick_params(axis="x", direction="in", labelsize=12)
ax1.set_yticks(yticks_values_1)
ax1.set_ylim(ylim_values_1)

# Create a secondary y-axis for AMI WER
ax2 = ax1.twinx()
(ami_line,) = ax2.plot(
    microphones,
    ami_wer,
    color="#ff7f00",
    label="AMI (dev)",
    markersize=10,
    linewidth=3,
    mec="black",
    linestyle=":",
    marker="^",
)
ax2.set_ylabel(ylabel_value_2, color="#ff7f00", fontsize=14)
ax2.tick_params(
    axis="y", labelcolor="#ff7f00", direction="in", rotation=90, labelsize=12
)
ax2.set_yticks(yticks_values_2)
ax2.set_ylim(ylim_values_2)

# IHM and SDM constant error rates
ax1.plot(microphones, ihm_wer, ":", color="green", linewidth=2, label="IHM Trend")
ax1.plot(microphones, sdm_wer, "--", color="purple", linewidth=2, label="SDM Trend")

# Custom legend for the plot
ihm_legend = Line2D(
    [0], [0], color="green", linestyle=":", linewidth=2, label="IHM Trend"
)
sdm_legend = Line2D(
    [0], [0], color="purple", linestyle="--", linewidth=2, label="SDM Trend"
)

# Add the legend to the plot
first_legend = ax1.legend(
    handles=[ihm_legend, sdm_legend],
    loc="upper left",
    ncol=2,
    fontsize=14,
    edgecolor="black",
)
ax1.add_artist(first_legend)  # Add the first legend back to the plot
second_legend = ax1.legend(
    handles=[libricss_line, ami_line], loc="upper right", fontsize=14, edgecolor="black"
)  # Add the second legend

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout for better spacing and display
plt.tight_layout()
plt.savefig('line_68.pdf', bbox_inches='tight')
