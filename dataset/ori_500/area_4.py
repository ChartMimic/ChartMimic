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
n_aug = ["0", "0.125", "0.25", "0.5", "1", "2", "4", "8"]
content = np.array([1, 3, 6, 4, 2, 1, 0.5, 0.2])
organization = np.array([0.5, 1, 1.5, 2, 1.5, 1, 0.5, 0.25])
language = np.array([0, 0.5, 1, 2, 4, 3, 2, 1])

# Calculate cumulative values for stacked area chart
cumulative_content = content
cumulative_organization = cumulative_content + organization
cumulative_language = cumulative_organization + language

# Positions for the bars on the x-axis
ind = np.arange(len(n_aug))

# Variables for plot configuration
content_label = "Content"
organization_label = "Organization"
language_label = "Language"
xlim_values = (0, 7)
ylim_values = (0, 10)
xlabel_text = "n"
ylabel_text = "Performance Gain (%)"
title_text = "Cumulative Performance Gain by Augmentation Level"
yticks_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
legend_location = "upper center"
legend_fontsize = 12
legend_frameon = False
legend_shadow = True
legend_facecolor = "#ffffff"
legend_ncol = 3
legend_bbox_to_anchor = (0.5, 1.2)

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plot
fig, ax = plt.subplots(figsize=(8, 4))  # Adjusted for better aspect ratio
ax.fill_between(
    n_aug, 0, cumulative_content, label=content_label, color="#0173b2", alpha=0.7
)
ax.fill_between(
    n_aug,
    cumulative_content,
    cumulative_organization,
    label=organization_label,
    color="#de8f05",
    alpha=0.7,
)
ax.fill_between(
    n_aug,
    cumulative_organization,
    cumulative_language,
    label=language_label,
    color="#20a983",
    alpha=0.7,
)

# Enhancing the plot with additional visuals
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.set_yticks(yticks_values)
# Setting the x-axis and y-axis limits dynamically
ax.set_ylim(*ylim_values)  # Ensure all data fits well
ax.set_xlim(*xlim_values)
# Labels, Title and Grid
ax.set_xlabel(xlabel_text, fontsize=14)
ax.set_ylabel(ylabel_text, fontsize=14)
ax.set_title(title_text, fontsize=16, y=1.2)
ax.tick_params(axis="both", which="both", color="gray")
# Custom legend
ax.legend(
    loc=legend_location,
    fontsize=legend_fontsize,
    frameon=legend_frameon,
    shadow=legend_shadow,
    facecolor=legend_facecolor,
    ncol=legend_ncol,
    bbox_to_anchor=legend_bbox_to_anchor,
)

# Grid
ax.grid(True, linestyle="--", alpha=0.5, which="both")

# ===================
# Part 4: Saving Output
# ===================
# Adjusting layout to reduce white space
plt.tight_layout()
plt.savefig("area_4.pdf", bbox_inches="tight")
