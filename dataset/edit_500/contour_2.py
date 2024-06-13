import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0); np.random.seed(0)

# ===================
# Part 2: Data Preparation
# ===================
# Create a grid of x and y values representing longitude and latitude
longitude = np.linspace(-180, 180, 100)
latitude = np.linspace(-90, 90, 100)
Longitude, Latitude = np.meshgrid(longitude, latitude)

# Adjust the lambda function to reflect the 3 different regions in traffic density
def traffic_density(Longitude, Latitude):
    # Parameters for the traffic density distribution (arbitrary values for illustration)
    return (
        np.exp(-((Longitude - (-100)) ** 2 + (Latitude - 40) ** 2) / 1000)
        + np.exp(-((Longitude - 0) ** 2 + (Latitude - 0) ** 2) / 5000)
        + np.exp(-((Longitude - 80) ** 2 + (Latitude - (-30)) ** 2) / 2000)
    )

# Calculate the traffic density values on the grid
Density_values = traffic_density(Longitude, Latitude)
xlabel = "Longitude"
ylabel = "Latitude"
title = "Traffic Density Distribution"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create the contour plot
plt.figure(figsize=(8, 6))

# Using a discrete colormap instead of 'viridis'
n_colors = 10  # Number of discrete colors in the colormap
discrete_cmap = plt.cm.get_cmap("summer", n_colors)

contour = plt.contourf(Longitude, Latitude, Density_values, levels=n_colors, cmap=discrete_cmap)

# Add a color bar
cbar = plt.colorbar(
    contour, ticks=np.linspace(Density_values.min(), Density_values.max(), n_colors)
)

# Label the axes
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.title(title)

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
# Show the plot
plt.savefig('contour_2.pdf', bbox_inches='tight')
