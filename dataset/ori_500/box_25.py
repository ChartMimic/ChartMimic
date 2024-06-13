# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

import matplotlib.lines as mlines
import matplotlib.patches as mpatches

# ===================
# Part 2: Data Preparation
# ===================
# Sample data for demonstration purposes
data1 = [
    np.random.normal(0, std, 50)
    for std in np.random.choice(range(10, 20), 5, replace=False)
]
data2 = [
    np.random.normal(0, std, 50)
    for std in np.random.choice(range(10, 20), 5, replace=False)
]
data3 = [
    np.random.normal(0, std, 50)
    for std in np.random.choice(range(10, 20), 5, replace=False)
]
labels = [
    "SOCP Learning (Proposed)",
    "SOCP No Learning",
    "FMPC",
    "Optimization Infeasible",
]
vlines = [-32, 32]
xlim = [-50, 50]
ylabel = "Angular Frequency [rad/s]"
xlabel = "Thrust Angle [°]"
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Boxplot
fig, ax = plt.subplots(figsize=(10, 6))  # Adjust figure size
bp1 = ax.boxplot(
    data1,
    positions=np.array(range(len(data1))) * 2.0 - 0.4,
    widths=0.3,
    patch_artist=True,
    vert=False,
    showfliers=False,
)
bp2 = ax.boxplot(
    data2,
    positions=np.array(range(len(data2))) * 2.0,
    widths=0.3,
    patch_artist=True,
    vert=False,
    showfliers=False,
)
bp3 = ax.boxplot(
    data3,
    positions=np.array(range(len(data3))) * 2.0 + 0.4,
    widths=0.3,
    patch_artist=True,
    vert=False,
    showfliers=False,
)

# New colors for the boxplots
new_colors = ["#a6cee3", "#1f78b4", "#b2df8a"]

# Set properties for each boxplot
for bp, color in zip([bp1, bp2, bp3], new_colors):
    for patch in bp["boxes"]:
        patch.set_facecolor(color)
    for whisker in bp["whiskers"]:
        whisker.set(color="black", linewidth=1)
    for cap in bp["caps"]:
        cap.set(color="black", linewidth=1)
    for median in bp["medians"]:
        median.set(color="black", linewidth=2)

# Add dashed line for θmax adjusted for horizontal layout
ax.axvline(
    x=vlines[0], color="#8a4e6e", linestyle="--", linewidth=1.5, label="$θ_{max}$"
)
ax.axvline(
    x=vlines[1], color="#4e7d8a", linestyle="--", linewidth=1.5, label="$θ_{min}$"
)

# Add legend with updated colors and markers
legend_elements = [
    mpatches.Patch(color="#a6cee3", label=labels[0]),
    mpatches.Patch(color="#1f78b4", label=labels[1]),
    mpatches.Patch(color="#b2df8a", label=labels[2]),
    mlines.Line2D([], [], color="#8a4e6e", linestyle="--", label="$θ_{max}$"),
    mlines.Line2D(
        [],
        [],
        color="black",
        marker="x",
        linestyle="None",
        markersize=10,
        label=labels[3],
    ),
    mlines.Line2D([], [], color="#4e7d8a", linestyle="--", label="$θ_{min}$"),
]

# Place legend outside the plot area
ax.legend(
    handles=legend_elements,
    loc="upper center",
    bbox_to_anchor=(0.5, -0.15),
    ncol=3,
    frameon=False,
)

# Set y-axis labels and limits
ax.set_xlim(xlim)
ax.set_ylabel(ylabel)
ax.set_xlabel(xlabel)

# Set y-axis tick positions and labels
ax.set_yticks(range(0, len(data1) * 2, 2))

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig("box_25.pdf", bbox_inches="tight")
