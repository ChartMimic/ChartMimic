# ===================
# Part 1: Importing Libraries
# ===================

import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)

# ===================
# Part 2: Data Preparation
# ===================
# Data
n_aug = ["0", "0.125", "0.25", "0.5", "1", "2", "4", "8"]
content = [1, 3, 6, 4, 2, 1, 0.5, 0.2]
organization = [0.5, 1, 1.5, 2, 1.5, 1, 0.5, 0.25]
language = [0, 0.5, 1, 2, 4, 3, 2, 1]

# Positions for the bars on the x-axis
ind = np.arange(len(n_aug))

# Labels and Legend
xlabel = "n"
ylabel = "Performance Gain (%)"
content_label = "Content"
organization_label = "Organization"
language_label = "Language"

# Limits
xlim = (n_aug[0], n_aug[-1])
ylim = (0, 7)

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plot
fig, ax = plt.subplots(figsize=(8, 6))  # Adjust the size to match the original image's dimensions
ax.plot(n_aug, content, label=content_label, color="#0173b2")
ax.plot(n_aug, organization, label=organization_label, color="#de8f05")
ax.plot(n_aug, language, label=language_label, color="#20a983")

# Setting the x-axis and y-axis limits
ax.set_ylim(*ylim)  # Set y-axis to go from 0 to 7
ax.set_xlim(*xlim)  # Set x-axis limits to cover the range of n_aug without extra space

# Labels and Title
ax.set_xlabel(xlabel, fontsize=14)
ax.set_ylabel(ylabel, fontsize=14)

# Legend
ax.legend(loc="upper center", fontsize=14, frameon=False, ncol=3, bbox_to_anchor=(0.5, 1.1))

# Grid
ax.grid(True, ls="--", alpha=0.5)

# ===================
# Part 4: Saving Output
# ===================
# Adjusting layout to reduce white space
plt.tight_layout()
plt.savefig('line_10.pdf', bbox_inches='tight')
