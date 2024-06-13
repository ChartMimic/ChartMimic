import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Generate random data for demonstration
data1 = np.random.normal(2.5, 0.5, 500)
data2 = np.random.normal(3.0, 0.5, 1000)
labels = ["Healthy", "Unhealthy"]
xlabel = "Caloric Intake"
ylabel = "Population Density"
titlelist = ["(a) Study 1", "(b) Study 2", "(c) Study 3", "(d) Study 4"]
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Set figure size to match the original image's dimensions
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Plot histograms for each subplot
for i, ax in enumerate(axs.flatten()):
    ax.hist(
        data1,
        bins=30,
        density=True,
        alpha=0.6,
        color="#f1a43a",
        label=labels[0],
        edgecolor="black",
        linewidth=0.5,
    )
    ax.hist(
        data2,
        bins=30,
        density=True,
        alpha=0.6,
        color="#3172bb",
        label=labels[1],
        edgecolor="black",
        linewidth=0.5,
    )
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.legend()

# Set titles for each subplot
axs[0, 0].set_title(titlelist[0])
axs[0, 1].set_title(titlelist[1])
axs[1, 0].set_title(titlelist[2])
axs[1, 1].set_title(titlelist[3])

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save the plot
plt.tight_layout()
plt.savefig('hist_11.pdf', bbox_inches='tight')
