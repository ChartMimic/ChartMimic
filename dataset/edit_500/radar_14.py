import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
labels = np.array(
    [
        "Top Speed",
        "Fuel Efficiency",
        "Passenger Capacity",
        "Maintenance Cost",
        "Safety Rating",
        "Fuel Consumption",
        "CO2 Emissions",
        "Maximum Range",
    ]
)
Electric_Sedan = np.array([0.75, 0.85, 0.65, 0.9, 0.95, 0.8, 0.6, 0.85])
Hybrid_SUV = np.array([0.6, 0.7, 0.55, 0.75, 0.85, 0.7, 0.55, 0.75])
Diesel_Truck = np.array([0.7, 0.8, 0.6, 0.85, 0.9, 0.75, 0.6, 0.8])
Gasoline_Coupe = np.array([0.85, 0.9, 0.8, 0.95, 0.98, 0.85, 0.75, 0.9])
yticks = [0.2, 0.4, 0.6, 0.8, 1.0]
labels2 = ["Electric Sedan", "Hybrid SUV", "Diesel Truck", "Gasoline Coupe"]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

# Number of variables
num_vars = len(labels)

# Compute angle for each axis
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# The plot is made circular, so we need to complete the loop
Electric_Sedan = np.concatenate((Electric_Sedan, [Electric_Sedan[0]]))
Hybrid_SUV = np.concatenate((Hybrid_SUV, [Hybrid_SUV[0]]))
Diesel_Truck = np.concatenate((Diesel_Truck, [Diesel_Truck[0]]))
Gasoline_Coupe = np.concatenate((Gasoline_Coupe, [Gasoline_Coupe[0]]))
angles += angles[:1]

# Draw one axe per variable and add labels
plt.xticks(angles[:-1], labels, color="black", size=10)
ax.tick_params(pad=10)  # Increase the distance of the label from the axis

# Draw ylabels
ax.set_rlabel_position(0)
plt.yticks(yticks, [], color="grey", size=7)
plt.ylim(0, 1)

# Plot data
ax.plot(
    angles,
    Electric_Sedan,
    color="#5471ab",
    linewidth=2,
    linestyle="solid",
    label=labels2[0],
    marker="o",
)
ax.plot(
    angles,
    Hybrid_SUV,
    color="#d1885c",
    linewidth=2,
    linestyle="solid",
    label=labels2[1],
    marker="o",
)
ax.plot(
    angles,
    Diesel_Truck,
    color="#6aa66e",
    linewidth=2,
    linestyle="solid",
    label=labels2[2],
    marker="o",
)
ax.plot(
    angles,
    Gasoline_Coupe,
    color="#b65655",
    linewidth=2,
    linestyle="solid",
    label=labels2[3],
    marker="o",
)

# Add legend
plt.legend(loc="upper left", bbox_to_anchor=(1, 1))

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout for better fit and save the plot
plt.tight_layout()
plt.savefig('radar_14.pdf', bbox_inches='tight')
