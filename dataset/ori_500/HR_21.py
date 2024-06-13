# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
broken_barh_datax1 = [(10, 30), (50, 10), (70, 20)]
broken_barh_datay1 = (10, 9)
broken_barh_datax2 = [(110, 10)]
broken_barh_datay2 = (10, 9)
broken_barh_datax3 = [(40, 10), (60, 10)]
broken_barh_datay3 = (20, 9)
broken_barh_datax4 = [(0, 10), (120, 20), (150, 30)]
broken_barh_datay4 = (20, 9)
labels = ["Running", "Interrupted", "Rest", "Running2"]
datalabels = ["Athlete Bill", "Athlete Jim"]
yticks = [15, 25]
ylim = [5, 35]
xlim = [0, 200]
xlabel = "Seconds Since Start"
annotations = "Race interrupted due to weather"
annotatestart = (61, 25)
annotateend = (0.8, 0.9)
title = "Endurance Race Performance Analysis"
facecolors = ["#739e47", "#e25d33", "#f19d38"]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Horizontal bar plot with gaps to show different race phases
fig, ax = plt.subplots(figsize=(7, 5))
ax.broken_barh(
    broken_barh_datax1, broken_barh_datay1, facecolors=facecolors[0], label=labels[0]
)
ax.broken_barh(
    broken_barh_datax2, broken_barh_datay2, facecolors=facecolors[1], label=labels[1]
)
ax.broken_barh(
    broken_barh_datax3, broken_barh_datay3, facecolors=facecolors[2], label=labels[2]
)
ax.broken_barh(
    broken_barh_datax4,
    broken_barh_datay4,
    facecolors=facecolors,
    label=labels[3],
)

ax.set_ylim(ylim)
ax.set_xlim(xlim)
ax.set_xlabel(xlabel)
ax.set_yticks(yticks, labels=datalabels)  # More descriptive labels
ax.grid(True)  # Make grid lines visible
ax.annotate(
    annotations,
    annotatestart,
    xytext=annotateend,
    textcoords="axes fraction",
    arrowprops=dict(facecolor="black", shrink=0.05),
    fontsize=12,
    horizontalalignment="right",
    verticalalignment="top",
)

# Title and legend
ax.set_title(title)
ax.legend(loc="lower right")

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig("HR_21.pdf", bbox_inches="tight")
