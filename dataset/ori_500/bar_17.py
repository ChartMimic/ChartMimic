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
tasks = ["ARC", "MMLU", "TruthfulQA", "Winogrande", "Average"]
LLaMA_2_7B = [53.0, 46.6, 45.3, 73.1, 53.1]
Evol_Instruct_70k = [51.3, 45.8, 44.5, 70.4, 54.5]
Evol_Instruct_AlpaGasus_1k = [56.4, 48.0, 48.5, 73.2, 53.7]
Evol_Instruct_1k_longest = [56.2, 46.6, 39.0, 72.8, 53.1]
LIMA_1k = [56.4, 46.7, 50.1, 71.8, 53.9]

# Plot labels
xlabel = "Tasks"
ylabel = "Accuracy (%)"
title = None
barWidth = 0.16
xticks = [r + barWidth * 2 for r in range(len(LLaMA_2_7B))]
xtickslabel = tasks
yticks = [20, 30, 40, 50, 60, 70, 80, 90]
ytickslabel = None
xlim = None
ylim = (20, 90)

# Legend labels
LLaMA_2_7B_label = "LLaMA-2-7B"
Evol_Instruct_70k_label = "Evol-Instruct-70k"
Evol_Instruct_AlpaGasus_1k_label = "Evol-Instruct-AlpaGasus-1k"
Evol_Instruct_1k_longest_label = "Evol-Instruct-1k-longest"
LIMA_1k_label = "LIMA-1k"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Set figure size to match the original image's dimensions
plt.figure(figsize=(10, 4))

# # Bar width
# barWidth = 0.16

# Set position of bar on X axis
r1 = np.arange(len(LLaMA_2_7B))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
r4 = [x + barWidth for x in r3]
r5 = [x + barWidth for x in r4]

# Make the plot
plt.bar(
    r1,
    LLaMA_2_7B,
    color="#b4cbda",
    width=barWidth,
    edgecolor="white",
    label=LLaMA_2_7B_label,
)
plt.bar(
    r2,
    Evol_Instruct_70k,
    color="#44739d",
    width=barWidth,
    edgecolor="white",
    label=Evol_Instruct_70k_label,
)
plt.bar(
    r3,
    Evol_Instruct_AlpaGasus_1k,
    color="#bad39b",
    width=barWidth,
    edgecolor="white",
    label=Evol_Instruct_AlpaGasus_1k_label,
)
plt.bar(
    r4,
    Evol_Instruct_1k_longest,
    color="#569046",
    width=barWidth,
    edgecolor="white",
    label=Evol_Instruct_1k_longest_label,
)
plt.bar(
    r5, LIMA_1k, color="#e4a9a7", width=barWidth, edgecolor="white", label=LIMA_1k_label
)

# Add labels
for i in range(len(tasks)):
    plt.text(
        r1[i],
        LLaMA_2_7B[i] + 1,
        str(LLaMA_2_7B[i]),
        ha="center",
        fontsize=6,
        rotation=45,
    )
    plt.text(
        r2[i],
        Evol_Instruct_70k[i] + 1,
        str(Evol_Instruct_70k[i]),
        ha="center",
        fontsize=6,
        rotation=45,
    )
    plt.text(
        r3[i],
        Evol_Instruct_AlpaGasus_1k[i] + 1,
        str(Evol_Instruct_AlpaGasus_1k[i]),
        ha="center",
        fontsize=6,
        rotation=45,
    )
    plt.text(
        r4[i],
        Evol_Instruct_1k_longest[i] + 1,
        str(Evol_Instruct_1k_longest[i]),
        ha="center",
        fontsize=6,
        rotation=45,
    )
    plt.text(
        r5[i], LIMA_1k[i] + 1, str(LIMA_1k[i]), ha="center", fontsize=6, rotation=45
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
plt.savefig("bar_17.pdf", bbox_inches="tight")
