# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Generate data
x = np.linspace(70, 90, 9)
y1 = x * np.random.uniform(0.3, 0.5, 9) + np.random.normal(0, 2, 9)
y2 = x * np.random.uniform(0.2, 0.4, 9) + np.random.normal(0, 2, 9)
y3 = x * np.random.uniform(0.1, 0.3, 9) + np.random.normal(0, 2, 9)

sizes = np.linspace(50, 150, 9)  # Define marker sizes

# Define color gradients for visual appeal
colors = ["deepskyblue", "magenta", "limegreen"]
titles = ["Scatter Plot - deepskyblue", "Scatter Plot - magenta", "Scatter Plot - limegreen"]
xlabel = "X Values"
ylabel = "Y Values"
cbar_label = "Color scale for X"
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create figure and axes objects
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

# Plot scatter plots
for ax, y, color in zip(axs, [y1, y2, y3], colors):
    sc = ax.scatter(
        x,
        y,
        s=sizes,
        c=x,
        cmap="viridis",
        alpha=0.6,
        edgecolor="black",
    )
    ax.plot(
        x, y, color=color, linestyle="--", alpha=0.6
    )  # Connect points with dashed lines
    ax.set_title(f"Scatter Plot - {color}")
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_ylim(min(y) - 5, max(y) + 5)

# Add color bars to each subplot for color mapping explanation
for ax in axs:
    cb = plt.colorbar(sc, ax=ax, orientation="vertical")
    cb.set_label(cbar_label)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.savefig('scatters_24.pdf', bbox_inches='tight')
