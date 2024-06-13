# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Data
vehicle_trainable_parameter_size = [5, 15, 25, 35, 45]
efficiency_7b = [60, 62, 65, 70, 75]
vehicle_type_size = [50]
efficiency_13b = [80]
models_7b = ["Car A", "Car B", "Car C", "Car D", "Car E"]
models_13b = ["Truck A"]
labels = ["Cars", "Trucks"]
ylabel = "Efficiency (%)"
xlabel = "Vehicle Parameter Size (units)"
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plotting
fig, ax = plt.subplots(
    figsize=(7, 7)
)  # Adjusting figure size to match original dimensions
ax.plot(
    vehicle_trainable_parameter_size,
    efficiency_7b,
    "o-r",
    label=labels[0],
    marker="o",
    markersize=5,
)
ax.plot(
    vehicle_type_size,
    efficiency_13b,
    "o-b",
    label=labels[1],
    marker="*",
    markersize=10,
)

# Annotating data points
for i, txt in enumerate(models_7b):
    ax.annotate(
        f"{efficiency_7b[i]}\n{txt}",
        (vehicle_trainable_parameter_size[i], efficiency_7b[i]),
        textcoords="offset points",
        xytext=(0, 10),
        ha="center",
    )

for i, txt in enumerate(models_13b):
    ax.annotate(
        f"{efficiency_13b[i]}\n{txt}",
        (vehicle_type_size[i], efficiency_13b[i]),
        textcoords="offset points",
        xytext=(0, 10),
        ha="center",
    )

# Legend
ax.legend(loc="lower right")

# Labels and Title
ax.set_ylabel(ylabel)
ax.set_xlabel(xlabel)
# ax.set_title('Vehicle Performance by Parameter Size')
ax.set_yticks([50, 55, 60, 65, 70, 75, 80, 85])
ax.set_ylim([48, 85])
ax.set_xlim([-5, 55])

# ===================
# Part 4: Saving Output
# ===================
# Show plot
plt.tight_layout()
plt.savefig("CB_19.pdf", bbox_inches="tight")
