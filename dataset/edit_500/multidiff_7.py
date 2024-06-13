import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data for the plots
models1 = [
    "Sprinter2020",
    "Runner2021",
    "Athlete2020",
    "Competitor2021",
    "Track2019",
    "Racer2019",
]
models2 = [
    "Track2019",
    "Sprinter2020",
    "Athlete2020",
    "Competitor2021",
    "Runner2021",
    "Racer2019",
]

# Updated performance scores
accuracy = [88.12, 87.35, 86.78, 89.01, 84.60, 83.45]
robust_accuracy = [81.0, 79.9, 78.5, 80.4, 76.3, 75.1]

# Updated performance score differences for pairwise comparisons
accuracy_diff = np.array(
    [
        [0, 0.77, 1.34, -0.89, 3.52, 4.67],
        [-0.77, 0, 2.11, -1.66, 4.29, 5.44],
        [-1.34, -2.11, 0, -3.77, 2.18, 3.33],
        [0.89, 1.66, 3.77, 0, 5.95, 7.10],
        [-3.52, -4.29, -2.18, -5.95, 0, 1.15],
        [-4.67, -5.44, -3.33, -7.10, -1.15, 0],
    ]
)
robust_accuracy_diff = np.array(
    [
        [0, 1.1, 2.5, 0.6, 4.7, 5.9],
        [-1.1, 0, 3.6, -0.5, 5.8, 7.0],
        [-2.5, -3.6, 0, -4.1, 2.2, 3.4],
        [-0.6, 0.5, 4.1, 0, 6.3, 7.5],
        [-4.7, -5.8, -2.2, -6.3, 0, 1.2],
        [-5.9, -7.0, -3.4, -7.5, -1.2, 0],
    ]
)

# Updated normalized performance ratings
nfr = np.array(
    [
        [0, 1.25, 0.75, 1.1, 0.9, 0.85],
        [-1.25, 0, -0.5, -0.15, -0.35, -1.9],
        [-0.75, 0.5, 0, 0.35, 0.4, -1.4],
        [-1.1, 0.15, -0.35, 0, -0.6, -1.3],
        [-0.9, 0.35, -0.4, 0.6, 0, -2.2],
        [-0.85, 1.9, 1.4, 1.3, 2.2, 0],
    ]
)
robust_nfr = np.array(
    [
        [0, 2.15, 1.85, 2.4, 3.0, 2.65],
        [-2.15, 0, -1.3, -1.55, -2.25, -1.4],
        [-1.85, 1.3, 0, -1.25, -1.95, -0.35],
        [-2.4, 1.55, 1.25, 0, -1.0, -0.65],
        [-3.0, 2.25, 1.95, 1.0, 0, -0.55],
        [-2.65, 1.4, 0.35, 0.65, 0.55, 0],
    ]
)

titles = ["Speed (%)", "Consistency (%)", "Speed Diff. (%)", "Consistency Diff. (%)", "Fatigue Resistance (%)", "Robust Fatigue Resistance (%)"]
xlim1 = [0, 100]
xlim2 = [0, 100]
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create subplots
fig, axs = plt.subplots(2, 3, figsize=(10, 7))

# Plot Accuracy
axs[0, 0].barh(models1, accuracy, color="green")
axs[0, 0].set_title(titles[0])
axs[0, 0].set_xlim(xlim1)
axs[0, 0].invert_yaxis()  # Reverse the order to match the reference
# annotate the bars with the values
for i, v in enumerate(accuracy):
    axs[0, 0].text(v + 0.4, i, str(v), color="black", va="center")

# Plot Robust Accuracy
axs[1, 0].barh(models2, robust_accuracy, color="red")
axs[1, 0].set_title(titles[1])
axs[1, 0].set_xlim(xlim2)
axs[1, 0].invert_yaxis()  # Reverse the order to match the reference
# annotate the bars with the values
for i, v in enumerate(robust_accuracy):
    axs[1, 0].text(v + 0.4, i, str(v), color="black", va="center")

# Plot Accuracy Diff.
im1 = axs[0, 1].imshow(accuracy_diff, cmap="PiYG", aspect="auto")
axs[0, 1].set_title(titles[2])
for i in range(len(models1)):
    for j in range(len(models1)):
        text = axs[0, 1].text(
            j,
            i,
            accuracy_diff[i, j],
            ha="center",
            va="center",
            color="black" if abs(accuracy_diff[i, j]) < 3 else "white",
        )
axs[0, 1].axis("off")

# Plot Robust Accuracy Diff.
im2 = axs[1, 1].imshow(robust_accuracy_diff, cmap="PiYG", aspect="auto")
axs[1, 1].set_title(titles[3])
for i in range(len(models2)):
    for j in range(len(models2)):
        text = axs[1, 1].text(
            j,
            i,
            robust_accuracy_diff[i, j],
            ha="center",
            va="center",
            color="black" if abs(robust_accuracy_diff[i, j]) < 3 else "white",
        )
axs[1, 1].axis("off")

# Plot NFR
im3 = axs[0, 2].imshow(nfr, cmap="PiYG", aspect="auto")
axs[0, 2].set_title(titles[4])
for i in range(len(models1)):
    for j in range(len(models1)):
        text = axs[0, 2].text(
            j,
            i,
            nfr[i, j],
            ha="center",
            va="center",
            color="black" if abs(nfr[i, j]) < 3 else "white",
        )
axs[0, 2].axis("off")

# Plot Robust NFR
im4 = axs[1, 2].imshow(robust_nfr, cmap="PiYG", aspect="auto")
axs[1, 2].set_title(titles[5])
for i in range(len(models2)):
    for j in range(len(models2)):
        text = axs[1, 2].text(
            j,
            i,
            robust_nfr[i, j],
            ha="center",
            va="center",
            color="black" if abs(robust_nfr[i, j]) < 3 else "white",
        )
axs[1, 2].axis("off")

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save the plot
plt.tight_layout()
plt.savefig('multidiff_7.pdf', bbox_inches='tight')
