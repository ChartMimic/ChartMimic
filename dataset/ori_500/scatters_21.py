# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data for plotting
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
additional_data1 = np.clip(
    np.sin(np.linspace(0, 1 * np.pi, len(microphones)))
    + np.random.normal(0, 0.1, len(microphones)),
    0.3,
    0.8,
)
additional_data2 = np.clip(
    np.cos(np.linspace(0, 1.5 * np.pi, len(microphones)))
    + np.random.normal(0, 0.05, len(microphones)),
    0.4,
    0.9,
)
titles = ["LibriCSS vs Additional Data 1", "AMI vs Additional Data 2"]
figure1_scatter_labels = ["LibriCSS WER", "Additional Data 1"]
figure2_scatter_labels = ["AMI WER", "Additional Data 2"]
xlabel = "Number of Microphones"
ylabel = "WER(%)"
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# The first subplot plots LibriCSS data and Additional Data 1
ax1.scatter(
    microphones,
    libricss_wer,
    color="cyan",
    label=figure1_scatter_labels[0],
    marker="o",
    s=80,
    edgecolor="black",
)
ax1.scatter(
    microphones,
    additional_data1,
    color="blue",
    label=figure1_scatter_labels[1],
    marker="s",
    s=80,
    edgecolor="black",
)
ax1.set_title(titles[0], fontsize=14)
ax1.set_xlabel(xlabel, fontsize=12)
ax1.set_ylabel(ylabel, fontsize=12)
ax1.legend(loc="upper right")

# The second subplot plots AMI data and Additional Data 2
ax2.scatter(
    microphones,
    ami_wer,
    color="magenta",
    label=figure2_scatter_labels[0],
    marker="^",
    s=80,
    edgecolor="black",
)
ax2.scatter(
    microphones,
    additional_data2,
    color="red",
    label=figure2_scatter_labels[1],
    marker="d",
    s=80,
    edgecolor="black",
)
ax2.set_title(titles[1], fontsize=14)
ax2.set_xlabel(xlabel, fontsize=12)
ax2.set_ylabel(ylabel, fontsize=12)
ax2.legend(loc="upper right")

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save the figure
plt.tight_layout()
plt.savefig('scatters_21.pdf', bbox_inches='tight')
