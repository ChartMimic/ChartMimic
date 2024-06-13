# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data
judges = ["GPT-3.5-Turbo", "Claude 2.1", "GPT-4-Turbo", "Human"]
protocols = [
    "Expert",
    "Blind",
    "Consultancy",
    "Interactive Consultancy",
    "Debate",
    "Interactive Debate",
]
accuracy_means = np.array(
    [
        [100, 50, 60, 70, 80, 90],  # GPT-3.5-Turbo
        [105, 55, 65, 75, 85, 95],  # Claude 2.1
        [110, 60, 70, 80, 90, 100],  # GPT-4-Turbo
        [115, 65, 75, 85, 95, 105],  # Human
    ]
)
accuracy_std = np.array(
    [
        [5, 5, 5, 5, 5, 5],  # GPT-3.5-Turbo
        [5, 5, 5, 5, 5, 5],  # Claude 2.1
        [5, 5, 5, 5, 5, 5],  # GPT-4-Turbo
        [5, 5, 5, 5, 5, 5],  # Human
    ]
)
legendtitle = "Protocol"
xlabel = "Judge"
ylabel = "Judge Accuracy (%)"
ylim = [0, 120]


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
bar_width_expert = 0.75

# Set position of bar on X axis
r = np.arange(len(judges))

# Draw bars for 'Expert' protocol
i = protocols.index("Expert")
ax.bar(
    r + (i + 3) * bar_width,
    accuracy_means[:, i],
    yerr=accuracy_std[:, i],
    width=bar_width_expert,
    label=protocols[i],
    capsize=5,
    color=colors[i],
    hatch="//",
    edgecolor="black",
)

# Draw bars for other protocols
for i in range(len(protocols)):
    if protocols[i] == "Expert":
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
plt.savefig("errorbar_2.pdf", bbox_inches="tight")
