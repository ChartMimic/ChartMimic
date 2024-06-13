# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data for the plots
models1 = [
    "Zhang2020",
    "Addelpalli2021",
    "Rice2020",
    "Rade2021",
    "Engstrom2019",
    "Hendrycks2019",
]
models2 = [
    "Engstrom2019",
    "Zhang2020",
    "Rice2020",
    "Rade2021",
    "Henriques2021",
    "Addelpalli2021",
]
accuracy = [75.32, 77.11, 77.03, 76.86, 75.34, 74.52]
robust_accuracy = [60.5, 59.3, 59.1, 58.35, 55.95, 55.5]
accuracy_diff = np.array(
    [
        [0, 1.79, 1.71, 1.54, 0.02, -0.8],
        [-1.79, 0, 0.08, -0.17, -1.69, -2.51],
        [-1.71, -0.08, 0, 0.17, -1.52, -2.34],
        [-1.54, 0.17, -0.17, 0, -1.52, -2.34],
        [-0.02, 1.69, 1.52, 1.52, 0, -0.82],
        [0.8, 2.51, 2.34, 2.34, 0.82, 0],
    ]
)
robust_accuracy_diff = np.array(
    [
        [0, 1.2, 0.2, 0.75, 2.4, -2.85],
        [-1.2, 0, -0.2, -0.95, -3.35, -3.8],
        [-0.2, 0.2, 0, -0.75, -3.15, -3.6],
        [-0.75, 0.95, 0.75, 0, -2.4, -2.85],
        [-2.4, 3.35, 3.15, 2.4, 0, 0.45],
        [2.85, 3.8, 3.6, 2.85, -0.45, 0],
    ]
)
nfr = np.array(
    [
        [0, 4.09, 4.17, 3.57, 3.33, 3.26],
        [-4.09, 0, -0.08, -0.17, -0.25, -3.03],
        [-4.17, 0.08, 0, -0.25, -0.17, -2.13],
        [-3.57, 0.17, 0.25, 0, -0.2, -2.64],
        [-3.33, 0.25, 0.17, 0.2, 0, -3.62],
        [-3.26, 3.03, 2.13, 2.64, 3.62, 0],
    ]
)
robust_nfr = np.array(
    [
        [0, 5.25, 6.45, 3.85, 4.8, 3.65],
        [-5.25, 0, -1.2, -5.55, -7.25, -5.4],
        [-6.45, 1.2, 0, -1.4, -6.95, -5.25],
        [-3.85, 5.55, 1.4, 0, -5.5, -2.75],
        [-4.8, 7.25, 6.95, 5.5, 0, -5.3],
        [-3.65, 5.4, 5.25, 2.75, 5.3, 0],
    ]
)
titles=["Accuracy (%)", "Robust Accuracy (%)", "Accuracy Diff. (%)", "Robust Accuracy Diff. (%)", "NFR (%)", "Robust NFR (%)"]
xlim1=[0, 100]
xlim2=[0, 100]
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
