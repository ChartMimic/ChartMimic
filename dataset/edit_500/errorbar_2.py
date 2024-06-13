import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data
judges = ["Mona", "Lisa", "Charlie", "Alex"]
protocols = [
    "Screening",
    "Evaluation",
    "Consultation",
    "Interactive Review",
    "Discussion",
    "Interactive Discussion",
]

accuracy_means = np.array(
    [
        [100, 72, 65, 78, 84, 90],  # Mona
        [99, 75, 68, 81, 86, 93],  # Lisa
        [98, 78, 70, 83, 88, 95],  # Charlie
        [99, 80, 72, 85, 90, 98],  # Alex
    ]
)

accuracy_std = np.array(
    [
        [4, 4, 4, 4, 4, 4],  # Mona
        [4, 4, 4, 4, 4, 4],  # Lisa
        [4, 4, 4, 4, 4, 4],  # Charlie
        [4, 4, 4, 4, 4, 4],  # Alex
    ]
)

legendtitle = "Review Protocol"
xlabel = "Reviewer"
ylabel = "Reviewer Accuracy (%)"
ylim = [0, 110]


# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Set figure size to match the original image's dimensions
fig, ax = plt.subplots(figsize=(10, 6))

# colors
colors = [
    "white",
    "#3171ad",
    "#d39334",
    "#469c76",
    "#c76526",
    "#c17cb9",
]  

# Bar width
bar_width = 0.15
bar_width_screen = 0.75

# Set position of bar on X axis
r = np.arange(len(judges))

# Draw bars for 'Screening' protocol
i = 0
ax.bar(
    r + (i + 3) * bar_width,
    accuracy_means[:, i],
    yerr=accuracy_std[:, i],
    width=bar_width_screen,
    label=protocols[i],
    capsize=5,
    color=colors[i],
    hatch="//",
    edgecolor="black",
)

# Draw bars for other protocols
for i in range(len(protocols)):
    if protocols[i] == protocols[0]:
        continue
    ax.bar(
        r + i * bar_width,
        accuracy_means[:, i],
        yerr=accuracy_std[:, i],
        width=bar_width,
        label=protocols[i],
        capsize=5,
        color=colors[i],
        edgecolor="black",
    )

# Add xticks on the middle of the group bars
ax.set_xlabel(xlabel)
ax.set_xticks(r + bar_width * (len(protocols) - 1) / 2)
ax.set_xticklabels(judges)

# Create legend & Show graphic
handles, labels = ax.get_legend_handles_labels()
order = [0, 1, 2, 4, 3, 5]  # Reordering the legend
ax.legend(
    [handles[idx] for idx in order],
    [labels[idx] for idx in order],
    loc="upper center",
    bbox_to_anchor=(0.5, 1.15),
    ncol=6,
    title=legendtitle,
)
ax.set_ylabel(ylabel)
ax.set_ylim(ylim)  # Adjust y-axis limit to accommodate error bars

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig('errorbar_2.pdf', bbox_inches='tight')
