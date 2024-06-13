# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

from scipy.stats import gaussian_kde

# ===================
# Part 2: Data Preparation
# ===================
# Generating sample data representing historical trends for three different periods
y1 = np.random.normal(1900, 10, 100)  # Early 20th century trend
y2 = np.random.normal(1950, 15, 100)  # Mid 20th century trend
y3 = np.random.normal(2000, 20, 100)  # Turn of the century trend

# Creating KDE for each sample data set to estimate the density of data points
kde1 = gaussian_kde(y1)
kde2 = gaussian_kde(y2)
kde3 = gaussian_kde(y3)

y_range = np.linspace(1850, 2050, 50)  # Defining the range of years for plotting
labels = ["Early 20th Century", "Mid 20th Century", "Turn of the Century"]
ax1_legend_title = "Era"
ax1_xlabel = "Density"
ax2_ylabel = "Year"
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Setting up the figure and axes for a 1 x 2 layout
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# First subplot: Fill between plot along y-axis (KDE Plot)
ax1.fill_betweenx(y_range, kde1(y_range), color="skyblue", alpha=0.4)
ax1.fill_betweenx(y_range, kde2(y_range), color="sandybrown", alpha=0.5)
ax1.fill_betweenx(y_range, kde3(y_range), color="olivedrab", alpha=0.3)
ax1.plot(kde1(y_range), y_range, label=labels[0], color="blue")
ax1.plot(kde2(y_range), y_range, label=labels[1], color="orange")
ax1.plot(kde3(y_range), y_range, label=labels[2], color="green")
ax1.legend(title=ax1_legend_title, loc="upper right")
ax1.set_xlabel(ax1_xlabel)
ax1.set_yticks([])  # Hiding y-axis ticks for clarity

# Second subplot: Box plot for the same datasets along y-axis
box = ax2.boxplot(
    [y1, y2, y3], vert=True, patch_artist=True, medianprops={"color": "black"}
)
colors = ["skyblue", "sandybrown", "olivedrab"]  # Color matching with KDE plot
for patch, color in zip(box["boxes"], colors):
    patch.set_facecolor(color)

ax2.set_ylabel(ax2_ylabel)
ax2.set_xticks([])  # Hiding x-axis ticks for clarity
ax2.set_ylim(1850, 2050)  # Setting limits for y-axis to align with the KDE plot

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig("CB_28.pdf", bbox_inches="tight")
