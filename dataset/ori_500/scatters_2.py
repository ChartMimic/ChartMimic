# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Data for plotting
x_solar = [200, 250, 300]
y_solar = [150, 180, 220]
sizes_solar = [100, 200, 300]

x_wind = [180, 230, 280]
y_wind = [140, 170, 210]
sizes_wind = [100, 200, 300]

x_hydro = [160, 210, 260]
y_hydro = [130, 160, 200]
sizes_hydro = [100, 200, 300]

legend_labels = ["Solar Energy", "Wind Energy", "Hydropower"]
title = "Energy Production Trends"
xlabel = "Installed Capacity (GW)"
ylabel = "Energy Output (TWh)"
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create the plot
fig, ax = plt.subplots(
    figsize=(4, 8)
)  # Adjust the size to match the original image's dimensions

# Scatter points
solar_scatter = ax.scatter(x_solar, y_solar, s=sizes_solar, alpha=0.8, color="lightblue")
wind_scatter = ax.scatter(x_wind, y_wind, s=sizes_wind, alpha=0.8, color="salmon")
hydro_scatter = ax.scatter(x_hydro, y_hydro, s=sizes_hydro, alpha=0.8, color="grey")

# Connect points with dashed lines
ax.plot(x_solar, y_solar, linestyle="--", color="lightblue", alpha=0.8)
ax.plot(x_wind, y_wind, linestyle="--", color="salmon", alpha=0.8)
ax.plot(x_hydro, y_hydro, linestyle="--", color="grey", alpha=0.8)

# Legend
legend = ax.legend(
    [solar_scatter, wind_scatter, hydro_scatter],
    legend_labels,
    title=title,
    loc="upper left",
)
legend.get_frame().set_alpha(1)  # Make legend background opaque

# Axes labels
ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)

# ===================
# Part 4: Saving Output
# ===================
# Show the plot with tight layout
plt.tight_layout()
plt.savefig('scatters_2.pdf', bbox_inches='tight')
