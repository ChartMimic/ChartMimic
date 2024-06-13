# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Prepare data
x_sc = np.array([70, 74, 78, 82, 86])  # Increased data points
y_sc = np.array([27.5, 32.5, 40, 45, 50])
sizes_sc = np.random.randint(100, 300, size=len(x_sc))

x_ft = np.array([71, 75, 79, 83, 87])
y_ft = np.array([28, 36, 38, 42, 46])
sizes_ft = np.random.randint(100, 300, size=len(x_ft))

x_vl = np.array([73, 77, 81, 85, 89])
y_vl = np.array([29, 34, 42.5, 47, 51.5])
sizes_vl = np.random.randint(100, 300, size=len(x_vl))
labels = ["ViTPose (sc)", "ViTPose (ft)", "VLPose"]
titles = ["ViTPose (sc) Performance", "ViTPose (ft) Performance", "VLPose Performance"]
xlabel = "Average Precision on MSCOCO (%)"
ylabel = "Average Precision on HumanArt (%)"
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create subplots with 1 row and 3 columns
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

# Define a color gradient
colors = ["cyan", "magenta", "lime"]


# Plot each dataset in a separate subplot with gradient colors
for ax, x, y, sizes, color, label, title in zip(
    axs,
    [x_sc, x_ft, x_vl],
    [y_sc, y_ft, y_vl],
    [sizes_sc, sizes_ft, sizes_vl],
    colors,
    labels,
    titles,
):
    scatter = ax.scatter(
        x,
        y,
        s=sizes,
        c=np.linspace(0.1, 1, len(x)),
        cmap="spring",
        alpha=0.6,
        label=label,
    )
    ax.plot(x, y, linestyle="-", color=color, alpha=0.5)  # Use lighter alpha for lines
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.legend()

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout for better presentation
plt.tight_layout()
# Show the plot
plt.savefig('scatters_25.pdf', bbox_inches='tight')
