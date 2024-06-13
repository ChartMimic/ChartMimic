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
    for (i, std) in enumerate(np.random.choice(range(10, 20), 7, replace=False))
]
data2 = [
    np.random.normal(0, std, 50)
    for (i, std) in enumerate(np.random.choice(range(10, 20), 7, replace=False))
]
data3 = [
    np.random.normal(0, std, 50)
    for (i, std) in enumerate(np.random.choice(range(10, 20), 7, replace=False))
]
labels = [
    "θmax",
    "Optimization Infeasible",
    "SOCP Learning (Proposed)",
    "SOCP No Learning",
    "FMPC",
]
xlabel = "Angular Frequency [rad/s]"
ylabel = "Thrust Angle [°]"
ylim = [-60, 70]
axhlines = [-42, 42]


# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Boxplot
fig, ax = plt.subplots(
    figsize=(8, 6)
)  # Adjust figure size to match original dimensions
bp1 = ax.boxplot(
    data1,
    positions=np.array(range(len(data1))) * 2.0 - 0.4,
    widths=0.3,
    patch_artist=True,
    showfliers=False,
)
bp2 = ax.boxplot(
    data2,
    positions=np.array(range(len(data2))) * 2.0,
    widths=0.3,
    patch_artist=True,
    showfliers=False,
)
bp3 = ax.boxplot(
    data3,
    positions=np.array(range(len(data3))) * 2.0 + 0.4,
    widths=0.3,
    patch_artist=True,
    showfliers=False,
)

# Set properties for each boxplot
for bp, color in zip([bp1, bp2, bp3], ["#4d67f6", "#f5bf5b", "#c62f5b"]):
    for patch in bp["boxes"]:
        patch.set_facecolor(color)
    for whisker in bp["whiskers"]:
        whisker.set(color="black", linewidth=1)
    for cap in bp["caps"]:
        cap.set(color="black", linewidth=1)
    for median in bp["medians"]:
        median.set(color="black", linewidth=2)
    # for flier in bp['fliers']:
    #     flier.set(marker='x', color='black', alpha=0.5)

# Get the bottom and height of the boxes in bp2
box_data = [
    np.abs(box.get_path().vertices[1][1] - box.get_path().vertices[2][1])
    for box in bp2["boxes"]
]

# Find the maximum and minimum values of the boxes
max_box = np.max(box_data)  # The top of the box is h
min_box = np.min(box_data)  # The bottom of the box is y

# Find the positions of the maximum and minimum boxes
max_pos = np.argmax(box_data)
min_pos = np.argmin(box_data)

# Add cross markers at the maximum and minimum values
ax.plot(
    max_pos * 2.0,
    bp2["medians"][max_pos].get_ydata()[0],
    marker="x",
    color="black",
    markersize=14,
)
ax.plot(
    min_pos * 2.0,
    bp2["medians"][min_pos].get_ydata()[0],
    marker="x",
    color="black",
    markersize=14,
)

# Add dashed line for θmax
ax.axhline(y=axhlines[0], color="black", linestyle="--", label="θmax")
ax.axhline(y=axhlines[1], color="black", linestyle="--", label="θmax")

# Add legend
# Create a Line2D instance for the axhline legend
axhline_legend = mlines.Line2D([], [], color="black", linestyle="-", label=labels[0])
marker_legend = mlines.Line2D(
    [], [], color="black", marker="x", linestyle="None", label=labels[1]
)
# Add the legends to the plot
patch1 = mpatches.Patch(color="#4d67f6", label=labels[2])
patch2 = mpatches.Patch(color="#f5bf5b", label=labels[3])
patch3 = mpatches.Patch(color="#c62f5b", label=labels[4])

ax.legend(
    handles=[patch1, patch2, patch3, axhline_legend, marker_legend],
    loc="upper center",
    ncol=2,
    frameon=False,
)
# Set x and y axis labels
ax.set_ylim(ylim)
ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)

# Set x-axis tick positions and labels
ax.set_xticks(range(0, len(data1) * 2, 2))
ax.set_xticklabels(["2.0", "2.5", "3.0", "3.5", "4.0", "4.5", "5.0"])

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig("box_5.pdf", bbox_inches="tight")
