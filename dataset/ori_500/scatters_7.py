# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Data points for models, their parameters, and NMAE (approximated from the image).
models = ["GPW-NO", "LNO", "GNO", "InfGCN", "DeepDFT2", "FNO"]
params = [0.7, 1.0, 3.0, 2.0, 10.0, 20.0]  # Number of parameters (in millions)
nmae = [0.7, 10.0, 5.0, 2.0, 1.0, 20.0]  # Normalized Mean Absolute Error (%)
colors = ["red", "grey", "brown", "purple", "green", "purple"]
xlabel = "Number of parameters (M)"  # X-axis label for number of parameters.
ylabel = "NMAE (%)"  # Y-axis label for NMAE.
title = "Number of params. vs. NMAE on QM9"  # Title of the plot.
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create a figure and a subplot with a specific size.
fig, ax = plt.subplots(figsize=(6, 3))

# Scatter plot each model's data point and add text annotation.
for i in range(len(models)):
    ax.scatter(
        params[i], nmae[i], color=colors[i]
    )  # Plot data points with specific color.
    # Align text annotations based on position for better readability.
    ax.text(
        params[i] + 0.1, nmae[i] + 0.1, models[i], fontsize=10, ha="left", va="bottom"
    )

# Add a horizontal and a vertical dashed reference line.
ax.axhline(
    y=0.7, color="gray", linestyle="--", linewidth=1
)  # Horizontal line at NMAE=0.7
ax.axvline(
    x=0.7, color="gray", linestyle="--", linewidth=1
)  # Vertical line at Params=0.7M

# Set the scales of the axes to logarithmic.
ax.set_xscale("log")
ax.set_yscale("log")

# Set the labels for the axes.
ax.set_xlabel(xlabel)  # X-axis label for number of parameters.
ax.set_ylabel(ylabel)  # Y-axis label for NMAE.

# Set the title of the plot.
ax.set_title(title)  # Title of the plot.

# Adjust the tick labels to match the reference image.
# Define major ticks for both axes.
ax.set_xticks([0.6, 1, 2, 3, 10, 20, 33])
ax.get_xaxis().set_major_formatter(
    plt.ScalarFormatter()
)  # Format the tick labels as scalar values.
ax.set_yticks([0.7, 1, 2, 3, 10, 20, 40])
ax.get_yaxis().set_major_formatter(
    plt.ScalarFormatter()
)  # Format the tick labels as scalar values.

# ===================
# Part 4: Saving Output
# ===================
# Show the plot with a tight layout to ensure all elements fit within the figure area.
plt.tight_layout()
plt.savefig('scatters_7.pdf', bbox_inches='tight')
