# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data for the plot
microphones = np.array([2, 3, 4, 5, 6, 7, 8])
libricss_wer = np.clip(
    np.linspace(7, 3.2, len(microphones)) + np.random.normal(0, 0.2, len(microphones)),
    3,
    None,
)
ami_wer = np.clip(
    np.linspace(28, 21, len(microphones)) + np.random.normal(0, 0.5, len(microphones)),
    21,
    28,
)
ihm_wer = [2.5] * len(microphones)  # IHM constant error rates
sdm_wer = [10] * len(microphones)  # SDM constant error rates

# Axes Limits and Labels
xlabel_value = "Number of microphones"

ylabel_value_1 = "WER(%)"
ylabel_value_2 = "AMI WER(%)"
ylim_values_1 = [2, 10]
ylim_values_2 = [20, 30]
yticks_values_1 = range(2, 10, 1)
yticks_values_2 = range(20, 30, 2)

# Labels
label_1 = "LibriCSS (test)"
label_2 = "AMI (dev)"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create a figure and axis
fig, ax1 = plt.subplots(figsize=(6, 5))

# LibriCSS and AMI WER plots
(libricss_line,) = ax1.plot(
    microphones,
    libricss_wer,
    "o-",
    color="#377eb8",
    label=label_1,
    markersize=10,
    linewidth=3,
    mec="black",
)
ax1.set_xlabel(xlabel_value, fontsize=14)
ax1.set_ylabel(ylabel_value_1, fontsize=14, color="#377eb8")
ax1.tick_params(
    axis="y", labelcolor="#377eb8", direction="in", rotation=90, labelsize=12
)
ax1.tick_params(axis="x", direction="in", labelsize=12)
ax1.set_yticks(yticks_values_1)
ax1.set_ylim(ylim_values_1)

ax2 = ax1.twinx()
(ami_line,) = ax2.plot(
    microphones,
    ami_wer,
    "^-",
    color="#ff7f00",
    label=label_2,
    markersize=10,
    linewidth=3,
    mec="black",
)
ax2.set_ylabel(ylabel_value_2, color="#ff7f00", fontsize=14)
ax2.tick_params(
    axis="y", labelcolor="#ff7f00", direction="in", rotation=90, labelsize=12
)
ax2.set_yticks(yticks_values_2)
ax2.set_ylim(ylim_values_2)

# IHM and SDM constant error rates
ax1.axhline(y=2.5, color="#377eb8", linestyle=":", linewidth=2)
ax1.axhline(y=10, color="#ff7f00", linestyle="--", linewidth=2)

# Custom legend for the plot
ihm_legend = Line2D([0], [0], color="black", linestyle=":", linewidth=2, label="IHM")
sdm_legend = Line2D([0], [0], color="black", linestyle="--", linewidth=2, label="SDM")

# Add the legend to the plot
first_legend = ax1.legend(
    handles=[ihm_legend, sdm_legend],
    loc="upper left",
    ncol=2,
    fontsize=14,
    edgecolor="black",
)
ax1.add_artist(first_legend)

# ===================
# Part 4: Saving Output
# ===================
# Add the second legend to the plot
plt.tight_layout()
plt.savefig('line_67.pdf', bbox_inches='tight')
