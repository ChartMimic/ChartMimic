# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Data for plotting
categories = ["0-9", "10-19", "20-29", "30-39", "40-49"]
values = [0.60, -0.55, -0.76, -0.80, -0.85]

# Plot configuration variables
ylabel = "spearman"
xlabel = "length"
xlim = (-0.5, 4.5)
ylim = (-1, 0.75)
yticks = [-1.00, -0.75, -0.5, -0.25, 0, 0.25, 0.50, 0.75]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create the figure and the bar chart
fig, ax = plt.subplots(figsize=(6, 6))
bars = ax.bar(categories, values, color="#44739d", edgecolor="white", width=1, zorder=3)

# Set labels and title
ax.set_ylabel(ylabel)
ax.set_xlabel(xlabel)
ax.set_xlim(xlim)
ax.set_ylim(ylim)
ax.tick_params(axis="y", which="both", length=0)
ax.tick_params(axis="x", which="both", length=0)
ax.set_yticks(yticks)
ax.set_facecolor("#eaeaf2")  # Set the axes background color
ax.yaxis.grid(True, color="white", zorder=2)  # Add grid lines

# Remove the border around the chart area
for spine in ax.spines.values():
    spine.set_visible(False)

# Ensure that the bars for negative values start from zero
for bar in bars:
    if bar.get_height() < 0:
        bar.set_y(0)

# Add padding around the chart
plt.subplots_adjust(left=0.15, right=0.95, top=0.95, bottom=0.15)

# ===================
# Part 4: Saving Output
# ===================
# Show the plot
plt.tight_layout()
plt.savefig("bar_11.pdf", bbox_inches="tight")
