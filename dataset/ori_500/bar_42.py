# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Data
tasks = [
    "AI2sci-middle",
    "PROST",
    "ARC-easy",
    "COMVE(Task A)",
    "COPA",
    "OpenBookQA",
    "SciQ",
    "NumSense",
    "CoQA",
    "ComQA2.0",
    "QuARTz",
    "CycIC",
    "Winogventi",
    "Com2Sense",
    "CODAH",
    "WSC",
    "ARC-challenge",
    "SocialIQA",
    "CommonsenseQA",
    "HellaSWAG-wikiHow",
    "AI2Sci-elem",
    "Winogrande",
    "PIQA",
    "QuaRel",
    "SCT",
    "alphaNLI",
    "SWAG",
    "HellaSWAG-actnet",
]
delta_accuracy = [
    -8,
    -6.5,
    -5,
    -5,
    -4.5,
    -4,
    -3.7,
    -3.7,
    -2.5,
    -2.5,
    -2,
    -2,
    -2,
    -2,
    -1.7,
    -1.5,
    -1,
    -1,
    0.7,
    0.8,
    0.9,
    1.2,
    2,
    2.3,
    3,
    3,
    4,
    5,
]

# Colors based on delta accuracy
colors = [
    "#346c98" if x < 0 else "#bb8b39" if 0 <= x <= 1 else "#41886c"
    for x in delta_accuracy
]

# Extracted variables
xlim_values = (-1, len(tasks))
ylim_values = (-8, 6)
ylabel_text = "ΔAcc (with Stories) - Acc (without Rules)"
title_text = "Model = Vicuna"
legend_labels = ["ΔAcc < -1", "-1 <= ΔAcc <= 1", "ΔAcc > 1"]
yticks_values = [-8, -6, -4, -2, 0, 2, 4, 6]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plot
fig, ax = plt.subplots(figsize=(8, 5))  # Convert mm to inches for figsize
bars = ax.bar(tasks, delta_accuracy, color=colors)

# Labels and Title
ax.set_xlim(*xlim_values)
ax.set_xticks([])
ax.set_ylim(*ylim_values)
ax.set_yticks(yticks_values)
ax.set_ylabel(ylabel_text)
ax.set_title(title_text)

# Add text labels
for bar, task in zip(bars, tasks):
    y = bar.get_height()
    if y < 0:
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            0.2,
            task,
            rotation=90,
            ha="center",
            va="bottom",
        )
    else:
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            -0.2,
            task,
            rotation=90,
            ha="center",
            va="top",
        )

# Legend
blue_patch = plt.Rectangle((0, 0), 1, 1, fc="blue", edgecolor="none")
orange_patch = plt.Rectangle((0, 0), 1, 1, fc="orange", edgecolor="none")
green_patch = plt.Rectangle((0, 0), 1, 1, fc="green", edgecolor="none")
ax.legend(
    [blue_patch, orange_patch, green_patch],
    legend_labels,
    loc="lower center",
    bbox_to_anchor=(0.5, -0.1),
    ncol=3,
    frameon=False,
)

plt.tick_params(axis="both", which="both", length=0)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout
plt.tight_layout()
plt.savefig("bar_42.pdf", bbox_inches="tight")
