import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)

import matplotlib.gridspec as gridspec

# ===================
# Part 2: Data Preparation
# ===================
# Data for Picture in Picture bar plot

# Known and unknown test scores distribution for different subjects
known_scores = np.array(
    [37, 45, 78, 75, 70, 65, 60, 38, 55, 60, 75]
)
unknown_scores = np.array(
    [60, 55, 53, 50, 48, 45, 40, 48, 35, 30, 25]
)
bins = np.linspace(0, 100, 11)  # Exam scores ranging from 0 to 100

# Data for the heatmap representing university ratings across different regions
university_ratings = np.array(
    [
        [98, 92, 85, 78, 72, 65],
        [95, 90, 82, 75, 70, 60],
        [92, 88, 80, 72, 68, 55],
        [90, 85, 78, 70, 65, 50],
        [88, 82, 75, 68, 62, 45],
    ]
)
x_labels = [
    "Uni A",
    "Uni B",
    "Uni C",
    "Uni D",
    "Uni E",
    "Uni F",
]
y_labels = ["Region 1", "Region 2", "Region 3", "Region 4", "Region 5"]
bar_labels = ["Known Scores", "Unknown Scores"]
xlabels = ["Score Range", "Universities"]
ylabels = ["Number of Students", "Regions"]
cbarlabel = "University Ratings"
insetaxes = [0.251, 0.65, 0.1, 0.2]
insetxlim = [40, 80]

# Data for bar chart showing student enrollment by field
fields = ["Science", "Engineering", "Arts", "Business", "Law", "Medicine"]
enrollment = [520, 470, 510, 390, 350, 400]

# Redefined data for histogram representing student enrollment distribution by region
urban_enrollment = np.random.normal(1000, 200, 1000)  # Enrollment in urban areas
rural_enrollment = np.random.normal(600, 150, 1000)  # Enrollment in rural areas
bins_enrollment = np.linspace(0, 2000, 30)  # Uniform bin size for histograms

# Titles for the plots
titles = ["Student Scores Distribution", "University Ratings by Region", "Student Enrollment Distribution"]
xlabels = ["Score Range", "Universities", "Enrollment Count"]
ylabels = ["Number of Students", "Regions", "Frequency"]

# Placeholder to show where histograms, bar charts, and heatmaps would be displayed. Actual plotting code is not included.


# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create a figure with GridSpec
fig = plt.figure(figsize=(10, 5))
gs = gridspec.GridSpec(1, 2, width_ratios=[1, 1.5])

# Picture in Picture bar plot
ax0 = plt.subplot(gs[0])
ax0.bar(
    bins,
    known_scores,
    width=8,
    color="#8ac926",
    align="center",
    label=bar_labels[0],
    edgecolor="black",
)
ax0.bar(
    bins,
    unknown_scores,
    width=8,
    color="#1982c4",
    align="center",
    bottom=known_scores,
    label=bar_labels[1],
    edgecolor="black",
)
ax0.set_xlabel(xlabels[0])
ax0.set_ylabel(ylabels[0])
ax0.legend(loc="upper right")
ax0.grid(True)
ax0.set_ylim(40,150)

# Add inset
ax_inset = fig.add_axes(insetaxes)
ax_inset.bar(
    bins[5:],
    known_scores[5:],
    width=8,
    color="#8ac926",
    align="center",
    edgecolor="black",
)
ax_inset.bar(
    bins[5:],
    unknown_scores[5:],
    width=8,
    color="#1982c4",
    align="center",
    bottom=known_scores[5:],
    edgecolor="black",
)
ax_inset.set_xlim(insetxlim)

# Heatmap plot
ax1 = plt.subplot(gs[1])
cmap = plt.cm.coolwarm_r
norm = plt.Normalize(vmin=university_ratings.min(), vmax=university_ratings.max())
heatmap = ax1.imshow(university_ratings, cmap=cmap, norm=norm, aspect="auto")

# Add color bar
cbar = plt.colorbar(heatmap, ax=ax1, orientation="vertical", pad=0.1)
cbar.set_label(cbarlabel)

# Set x and y labels
ax1.set_xticks(np.arange(len(x_labels)))
ax1.set_yticks(np.arange(len(y_labels)))
ax1.set_xticklabels(x_labels, rotation=45)
ax1.set_yticklabels(y_labels)
ax1.set_xlabel(xlabels[1])
ax1.set_ylabel(ylabels[1])


# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig('multidiff_25.pdf', bbox_inches='tight')
