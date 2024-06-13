import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Data for plotting
categories = [
    "AI ETHICS",
    "REMOTE WORK",
    "HEALTHCARE",
    "CYBERSECURITY",
    "CLIMATE ACTION",
]  # Capitalized category labels
means = [0.10, 0.35, 0.20, 0.15, 0.17]
errors = [0.04, 0.03, 0.05, 0.06, 0.02]
downerrors = [0.02, 0.02, 0.03, 0.04, 0.05]
legendtitles = ["Dataset mean", "Mean"]
texttitle = "Dataset mean"
ylabel = "Male Speaker presence (Fraction of reports)"
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plotting the data
fig, ax = plt.subplots(
    figsize=(8, 6)
)  # Adjusting figure size to match original image dimensions
ax.errorbar(
    categories,
    means,
    yerr=[errors, downerrors],
    fmt="o",
    color="blue",
    ecolor="blue",
    capsize=5,
)

# Adding a legend with both "Mean" and "Dataset mean"
dataset_mean = 0.253
mean_line = ax.errorbar(
    [], [], yerr=[], fmt="o", color="blue", ecolor="blue", capsize=5
)
dataset_mean_line = ax.axhline(
    y=dataset_mean, color="gray", linestyle="--", linewidth=1
)
ax.legend(
    [dataset_mean_line, mean_line],
    legendtitles,
    loc="upper right",
    fancybox=True,
    framealpha=1,
    shadow=True,
    borderpad=1,
)
# Adding a horizontal line for dataset mean and text annotation with a white background
ax.text(
    0.95,
    dataset_mean,
    texttitle,
    va="center",
    ha="right",
    backgroundcolor="white",
    transform=ax.get_yaxis_transform(),
)
# Setting labels
ax.set_ylabel(ylabel)
ax.set_title("")
plt.xticks(rotation=30)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig('errorpoint_5.pdf', bbox_inches='tight')
