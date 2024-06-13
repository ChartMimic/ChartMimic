# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)

import matplotlib.patches as mpatches

# ===================
# Part 2: Data Preparation
# ===================
# Data
labels = ["E. coli", "S. aureus", "B. subtilis", "P. aeruginosa"]
antibiotic_a = [
    0.6,
    0.7,
    0.65,
    0.75,
]
antibiotic_b = [
    0.55,
    0.75,
    0.7,
    0.8,
]
antibiotic_c = [
    0.65,
    0.6,
    0.75,
    0.7,
]

colors = ["#919fc7", "#ed936b", "#c8686d"]
legendlabel = ["Antibiotic A", "Antibiotic B", "Antibiotic C"]
ylabel1 ="Inhibition Zone (mm)"
ylabel2 ="Inhibition Zone (mm)"
xlabel1="Test 1"
xlabel2="Test 2"
ylim1=[0.5, 0.8]
ylim2=[0.5, 0.8]
yticks1=[0.5, 0.6, 0.7, 0.8]
yticks2=[0.6, 0.7, 0.8]
ytickslabel1=["0.5", "0.6", "0.7", "0.8"]
ytickslabel2=["0.6", "0.7", "0.8"]

x = np.arange(len(labels))  # the label locations
width = 0.25  # the width of the bars

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# Upper plot
rects1 = ax1.bar(
    x - width, antibiotic_a, width, label=legendlabel[0], color=colors[0], edgecolor="black"
)
rects2 = ax1.bar(x, antibiotic_b, width, label=legendlabel[1], color=colors[1], edgecolor="black")
rects3 = ax1.bar(
    x + width, antibiotic_c, width, label=legendlabel[2], color=colors[2], edgecolor="black"
)
# Lower plot
rects4 = ax2.bar(x - width, antibiotic_a, width, color=colors[0], edgecolor="black")
rects5 = ax2.bar(x, antibiotic_b, width, color=colors[1], edgecolor="black")
rects6 = ax2.bar(x + width, antibiotic_c, width, color=colors[2], edgecolor="black")

# Add some text for labels, title and custom x-axis tick labels, etc.
ax1.set_ylabel(ylabel1)
ax2.set_ylabel(ylabel2)
ax1.set_xlabel(xlabel1)
ax2.set_xlabel(xlabel2)
ax1.set_xticks(x)
ax1.set_xticklabels(labels)
ax2.set_xticks(x)
ax2.set_xticklabels(labels)
# Set y-axis limit to match the reference picture
ax1.set_ylim(ylim1)
ax2.set_ylim(ylim2)

ax1.set_yticks(yticks1)
ax1.set_yticklabels(ytickslabel1)
ax2.set_yticks(yticks2)
ax2.set_yticklabels(ytickslabel2)

# Set grid color and style
ax2.grid(axis="y", color="gray", linestyle="--", linewidth=0.5)

ax1.set_axisbelow(True)
ax2.set_axisbelow(True)

# Remove top and right borders
ax1.spines["top"].set_visible(False)
ax1.spines["right"].set_visible(False)
ax2.spines["top"].set_visible(False)
ax2.spines["right"].set_visible(False)
# Add legend
legend_handles = [
    mpatches.Patch(color=color, label=label)
    for color, label in zip(colors, legendlabel)
]
# Create legend
fig.legend(
    handles=legend_handles, loc="upper center", ncol=3, bbox_to_anchor=(0.5, 1.15)
)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig('bar_91.pdf', bbox_inches='tight')
