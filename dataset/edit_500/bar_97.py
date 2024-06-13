# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Seed for reproducibility

# Sample data
annotators = ["Wang", "Li", "Zhang", "Chen", "Liu", "Yang"]
base_scores = {
    "Factory Alpha": np.random.randint(50, 100, (7, 5)),
    "Factory Beta": np.random.randint(50, 100, (7, 5)),
    "Factory Gamma": np.random.randint(50, 100, (7, 5)),
    "Factory Delta": np.random.randint(50, 100, (7, 5)),
}
title = "Quality Inspection Scores Across Factories"
xlabel = "Inspector"
ylabel = "Inspection Scores"
ylim = [0, 60]
legendlabels = ["Safety", "Efficiency", "Compliance", "Maintenance", "Overall"]
legendtitle = "Inspection Criteria"

# New colors for each score - pastel shades
colors = ["#ff9999", "#66b3ff", "#99ff99", "#ffcc99", "#c2c2f0"]

# Normalize the scores for each dataset so that each annotator's scores sum to 60
normalized_scores = {}
for key, data in base_scores.items():
    normalized_scores[key] = np.array([60 * score / np.sum(score) for score in data])

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create a 2x2 subplot layout
fig, axes = plt.subplots(2, 2, figsize=(10, 8))
axes = axes.ravel()  # Flatten the 2D array of axes for easy iteration

# Plotting the stacked bar chart for each dataset
for ax, (key, scores) in zip(axes, normalized_scores.items()):
    for i in range(len(annotators)):
        bottom = 0
        for j, score in enumerate(scores[i]):
            ax.bar(i, score, bottom=bottom, color=colors[j])
            bottom += score

# Adding titles and labels
for i, ax in enumerate(axes):
    ax.set_title(f"{title} {i+1}")
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_xticks(range(len(annotators)))
    ax.set_xticklabels(annotators)
    ax.set_ylim(ylim)  # Increase y-limit to comfortably fit stacked bars

# Adding legend to the last subplot for clarity
fig.legend(
    legendlabels,
    title=legendtitle,
    bbox_to_anchor=(0.5, 1.05),
    ncol=5,
    loc="upper center",
)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig('bar_97.pdf', bbox_inches='tight')
