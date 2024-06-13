# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D  # Importing Line2D for creating custom legend items

# ===================
# Part 2: Data Preparation
# ===================
# Data
microphones = [2, 3, 4, 5, 6, 7, 8]
libricss_wer = [
    6.74,
    4.54,
    3.96,
    3.71,
    3.49,
    3.34,
    None,
]  # The None value will be handled in the plot commands
ami_wer = [27.44, 24.75, 23.38, 22.77, 22.32, 21.47, 21.51]
ihm_wer = [3] * len(microphones)
sdm_wer = [10] * len(microphones)

# Axes Limits and Labels
xlabel_value = "Number of microphones"

ylabel_value_1 = "WER(%)"
ylabel_value_2 = "AMI WER(%)"
ylim_values_1 = [1, 11]
ylim_values_2 = [15, 32]
yticks_values_1 = range(2, 11, 2)
yticks_values_2 = range(15, 31, 5)

# Labels
label_1 = "LibriCSS (test)"
label_2 = "ImageNet-C/P (Fog)"
label_3 = "AMI (dev)"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plot
fig, ax1 = plt.subplots(figsize=(8, 7))

# LibriCSS plot
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
ax1.tick_params(
    axis="x",
    direction="in",
    labelsize=12,
)
ax1.set_yticks(yticks_values_1)
ax1.set_ylim(ylim_values_1)

# Adding WER values to the plot for libricss
for i, txt in enumerate(libricss_wer):
    if txt is not None:  # Skip plotting the text for None values
        ax1.annotate(
            f"{txt}%",
            (microphones[i], txt),
            textcoords="offset points",
            xytext=(10, 10),
            ha="center",
            fontsize=12,
        )

# AMI plot with a secondary y-axis
ax2 = ax1.twinx()
(ami_line,) = ax2.plot(
    microphones,
    ami_wer,
    "^-",
    color="#ff7f00",
    label=label_3,
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

# Adding WER values to the plot for ami
for i, txt in enumerate(ami_wer):
    ax2.annotate(
        f"{txt}%",
        (microphones[i], txt),
        textcoords="offset points",
        xytext=(0, -30),
        ha="center",
        fontsize=12,
    )

# IHM dashed lines
ax1.axhline(y=2.2, color="#377eb8", linestyle=":", linewidth=2)
ax1.axhline(y=2.4, color="#ff7f00", linestyle=":", linewidth=2)

# SDM dashed lines
ax1.axhline(y=9.6, color="#377eb8", linestyle="--", linewidth=2)
ax1.axhline(y=9.4, color="#ff7f00", linestyle="--", linewidth=2)

# Creating custom legend items
ihm_legend = Line2D([0], [0], color="black", linestyle=":", linewidth=2, label="IHM")
sdm_legend = Line2D([0], [0], color="black", linestyle="--", linewidth=2, label="SDM")

# Adding legends
first_legend = ax1.legend(
    handles=[ihm_legend, sdm_legend],
    loc="upper left",
    ncol=2,
    fontsize=14,
    edgecolor="black",
)
ax1.add_artist(first_legend)  # Add the first legend manually
second_legend = ax1.legend(
    handles=[libricss_line, ami_line], loc="upper right", fontsize=14, edgecolor="black"
)  # Add the second legend

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig('line_34.pdf', bbox_inches='tight')
