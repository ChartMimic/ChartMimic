# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Placeholder data for confusion matrices
data_live = np.array([[44, 12, 0, 0], [5, 42, 3, 0], [0, 8, 23, 9], [0, 0, 2, 44]])
data_csiq = np.array([[35, 8, 0, 0], [4, 24, 13, 1], [2, 8, 13, 18], [0, 0, 3, 31]])
data_tid2013 = np.array(
    [[115, 28, 3, 6], [26, 81, 33, 18], [0, 21, 80, 42], [0, 0, 25, 112]]
)
data_kadid = np.array(
    [[360, 108, 23, 13], [61, 263, 141, 27], [3, 60, 305, 155], [0, 7, 102, 388]]
)
data_live_c = np.array(
    [[33, 17, 5, 3], [13, 24, 16, 7], [5, 14, 21, 18], [1, 11, 16, 20]]
)
data_koniq = np.array(
    [[339, 121, 23, 13], [100, 220, 90, 67], [27, 164, 143, 184], [7, 67, 88, 347]]
)
data_live_m = np.array([[20, 0, 0, 0], [8, 8, 6, 0], [1, 1, 11, 5], [0, 0, 4, 18]])
data_pipal = np.array(
    [[754, 271, 96, 43], [180, 498, 362, 133], [48, 278, 472, 321], [25, 109, 300, 750]]
)

# Titles for the subplots
titles = ["LIVE", "CSIQ", "TID2013", "KADID", "LIVE-C", "KonIQ", "LIVE-M", "PIPAL"]
xlabel = "Predicted category"
ylabel = "Ground truth category"
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
fig, axes = plt.subplots(nrows=2, ncols=4, figsize=(12, 6))  # Adjusted for 1080x2376


# Function to create a single confusion matrix plot
def plot_confusion_matrix(ax, data, title):
    im = ax.imshow(data, interpolation="nearest", cmap="viridis")
    ax.figure.colorbar(im, ax=ax)
    ax.set(
        title=title,
        xlabel=xlabel,
        ylabel=ylabel,
        xticks=np.arange(data.shape[1]),
        yticks=np.arange(data.shape[0]),
    )
    # Loop over data dimensions and create text annotations.
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            ax.text(j, i, data[i, j], ha="center", va="center", color="w")


# Plot each confusion matrix
plot_confusion_matrix(axes[0, 0], data_live, titles[0])
plot_confusion_matrix(axes[0, 1], data_csiq, titles[1])
plot_confusion_matrix(axes[0, 2], data_tid2013, titles[2])
plot_confusion_matrix(axes[0, 3], data_kadid, titles[3])
plot_confusion_matrix(axes[1, 0], data_live_c, titles[4])
plot_confusion_matrix(axes[1, 1], data_koniq, titles[5])
plot_confusion_matrix(axes[1, 2], data_live_m, titles[6])
plot_confusion_matrix(axes[1, 3], data_pipal, titles[7])

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout for better fit and save the figure
plt.tight_layout()
plt.savefig("heatmap_5.pdf", bbox_inches="tight")
