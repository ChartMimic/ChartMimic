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
categories = ["λ=0.06", "λ=0.08", "λ=0.1"]
values1 = [39.4, 35.18, 34.06]
values2 = [32.84, 20.84, 30.84]
values3 = [19.66, 28.0, 24.27]
values4 = [26.82, 30, 34.06]
values5 = [22, 22, 22]

values1minus = [-17, -19, -16]
values2minus = [-9, -12, -14]
values3minus = [-11, -14, -20]
values4minus = [-20, -30, -35]
values5minus = [0, 0, 0]

# Set up the bar width
barWidth = 0.15

# Set position of bar on X axis
r1 = np.arange(len(values1))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
r4 = [x + barWidth for x in r3]
r5 = [x + barWidth for x in r4]

labels = ["E16.6", "L26.8", "D19.7", "L22.2", "L22.2"]
xlabel = "Categories"
ylabel = "Reward Values"
yticks = np.arange(-40, 41, 10)

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Set up the figure size
plt.figure(figsize=(6, 5))

# Make the plot
plt.bar(r1, values1, color="#f6c3cb", width=barWidth, edgecolor="black", label=labels[0])
plt.bar(r2, values2, color="#fbe5c8", width=barWidth, edgecolor="black", label=labels[1])
plt.bar(r3, values3, color="#55b0aa", width=barWidth, edgecolor="black", label=labels[2])
plt.bar(r4, values4, color="#6f94e7", width=barWidth, edgecolor="black", label=labels[3])
plt.bar(r5, values5, color="#e6e6f9", width=barWidth, edgecolor="black", label=labels[4])
plt.bar(
    r1,
    values1minus,
    color="#f6c3cb",
    width=barWidth,
    edgecolor="grey",
    label=labels[0],
    alpha=0.5,
)
plt.bar(
    r2,
    values2minus,
    color="#fbe5c8",
    width=barWidth,
    edgecolor="grey",
    label=labels[1],
    alpha=0.5,
)
plt.bar(
    r3,
    values3minus,
    color="#55b0aa",
    width=barWidth,
    edgecolor="grey",
    label=labels[2],
    alpha=0.5,
)
plt.bar(
    r4,
    values4minus,
    color="#6f94e7",
    width=barWidth,
    edgecolor="grey",
    label=labels[3],
    alpha=0.5,
)
plt.bar(
    r5,
    values5minus,
    color="#e6e6f9",
    width=barWidth,
    edgecolor="grey",
    label=labels[4],
    alpha=0.5,
)

# Add text on the top of each bar
for i in range(len(r1)):
    plt.text(
        r1[i], values1[i] - 1, str(values1[i]), ha="center", va="top", rotation=-90
    )
    plt.text(
        r2[i], values2[i] - 1, str(values2[i]), ha="center", va="top", rotation=-90
    )
    plt.text(
        r3[i], values3[i] - 1, str(values3[i]), ha="center", va="top", rotation=-90
    )
    plt.text(
        r4[i], values4[i] - 1, str(values4[i]), ha="center", va="top", rotation=-90
    )
    plt.text(
        r5[i], values5[i] - 1, str(values5[i]), ha="center", va="top", rotation=-90
    )
    plt.text(
        r1[i],
        values1minus[i] + 1,
        str(-values1minus[i]),
        ha="center",
        va="bottom",
        rotation=-90,
    )
    plt.text(
        r2[i],
        values2minus[i] + 1,
        str(-values2minus[i]),
        ha="center",
        va="bottom",
        rotation=-90,
    )
    plt.text(
        r3[i],
        values3minus[i] + 1,
        str(-values3minus[i]),
        ha="center",
        va="bottom",
        rotation=-90,
    )
    plt.text(
        r4[i],
        values4minus[i] + 1,
        str(-values4minus[i]),
        ha="center",
        va="bottom",
        rotation=-90,
    )
    plt.text(
        r5[i],
        values5minus[i] - 1,
        str(-values5minus[i]),
        ha="center",
        va="top",
        rotation=-90,
    )

# Add xticks on the middle of the group bars
plt.xlabel(xlabel)
plt.xticks([r + 2 * barWidth for r in range(len(values1))], categories)
plt.yticks(yticks)
# Create legend & Show graphic
plt.ylabel(ylabel)

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig("bar_50.pdf", bbox_inches="tight")
