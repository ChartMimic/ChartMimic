
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0); np.random.seed(0)

# ===================
# Part 2: Data Preparation
# ===================
# Data
conditions = ["City", "Highway", "Combined", "Off-road", "Average"]
Sedan = [30.5, 40.6, 35.3, 20.1, 31.6]
SUV = [22.3, 28.8, 25.5, 15.4, 23.0]
Truck = [18.4, 25.0, 21.5, 14.2, 19.8]
Hybrid = [50.2, 45.6, 48.0, 30.8, 43.7]
Electric = [99.0, 120.3, 110.0, 85.8, 103.8]

# Plot labels
xlabel = "Driving Conditions"
ylabel = "Fuel Efficiency (MPG)"
title = None
barWidth = 0.16
xticks = [r + barWidth * 2 for r in range(len(Sedan))]
xtickslabel = conditions
yticks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130]
ylim = (10, 130)

# Legend labels
Sedan_label = "Sedan"
SUV_label = "SUV"
Truck_label = "Truck"
Hybrid_label = "Hybrid"
Electric_label = "Electric"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Set figure size to match the original image's dimensions
plt.figure(figsize=(10, 4))

# # Bar width
# barWidth = 0.16

# Set position of bar on X axis
r1 = np.arange(len(conditions))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
r4 = [x + barWidth for x in r3]
r5 = [x + barWidth for x in r4]

# Make the plot
plt.bar(
    r1,
    Sedan,
    color="#b4cbda",
    width=barWidth,
    edgecolor="white",
    label=Sedan_label,
)
plt.bar(
    r2,
    SUV,
    color="#44739d",
    width=barWidth,
    edgecolor="white",
    label=SUV_label,
)
plt.bar(
    r3,
    Truck,
    color="#bad39b",
    width=barWidth,
    edgecolor="white",
    label=Truck_label,
)
plt.bar(
    r4,
    Hybrid,
    color="#569046",
    width=barWidth,
    edgecolor="white",
    label=Hybrid_label,
)
plt.bar(
    r5, Electric, color="#e4a9a7", width=barWidth, edgecolor="white", label=Electric_label
)

# Add labels
for i in range(len(conditions)):
    plt.text(
        r1[i],
        Sedan[i] + 1,
        str(Sedan[i]),
        ha="center",
        fontsize=6,
        rotation=45,
    )
    plt.text(
        r2[i],
        SUV[i] + 1,
        str(SUV[i]),
        ha="center",
        fontsize=6,
        rotation=45,
    )
    plt.text(
        r3[i],
        Truck[i] + 1,
        str(Truck[i]),
        ha="center",
        fontsize=6,
        rotation=45,
    )
    plt.text(
        r4[i],
        Hybrid[i] + 1,
        str(Hybrid[i]),
        ha="center",
        fontsize=6,
        rotation=45,
    )
    plt.text(
        r5[i], Electric[i] + 1, str(Electric[i]), ha="center", fontsize=6, rotation=45
    )

# Add xticks on the middle of the group bars
plt.xlabel(xlabel, fontsize=12)
plt.xticks(xticks, xtickslabel)

# Create legend & Show graphic
plt.ylabel(ylabel, fontsize=12)
plt.ylim(ylim)
plt.yticks(yticks)
plt.legend(loc="upper center", bbox_to_anchor=(0.5, 1.2), frameon=False, ncol=5)

plt.tick_params(axis="x", which="both", length=0)
plt.tick_params(axis="y", color="gray")

# Add y grid
plt.gca().yaxis.grid(True)
plt.gca().set_axisbelow(True)

# Remove top and right borders
plt.gca().spines["top"].set_visible(False)
plt.gca().spines["right"].set_visible(False)
plt.gca().spines["bottom"].set_visible(False)
plt.gca().spines["left"].set_color("gray")

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig('bar_17.pdf', bbox_inches='tight')
