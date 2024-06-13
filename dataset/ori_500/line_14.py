# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Sample data
weeks = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28]
auto_profiled = np.array([0.05, 0.2, 0.2, 0.25, 0.80, 1.0, 0.70, 0.25, 0.1, 0.1])
manually_analyzed = np.array(
    [0.02, 0.15, 0.10, 0.12, 0.08, 0.06, 0.10, 0.05, 0.02, 0.02]
)

# Axes Limits and Labels
xlabel_value = "Week"
xlim_values = [5, 25]

ylabel_value = "Normalized Value"
ylim_values = [0, 1.25]
yticks_values = [0, 0.25, 0.5, 0.75, 1.0]

axvspan1_l,axvspan1_r = 10, 19
axvspan2_l,axvspan2_r = 19, 26

# Labels
label_1 = "Auto-profiled"
label_2 = "Manually-analyzed"


# Annotations
annotation_1 = "Realize\nthe trend"
annotation_2 = "Release\nnew product"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create figure and axis
fig, ax = plt.subplots(figsize=(6, 4))

# Plot the data
ax.plot(weeks, auto_profiled, "r-x", label=label_1)
ax.plot(weeks, manually_analyzed, "o-.", label=label_2)

# Highlight specific regions
ax.axvspan(axvspan1_l,axvspan1_r, color="peachpuff", alpha=0.5)
ax.axvspan(axvspan2_l,axvspan2_r, color="paleturquoise", alpha=0.5)

# Annotations
ax.annotate(
    annotation_1,
    xy=(10, 0.25),
    xytext=(12, 0.25),
    arrowprops=dict(facecolor="yellow", shrink=0.05),
)
ax.annotate(
    annotation_2,
    xy=(19, 0.7),
    xytext=(21, 0.8),
    arrowprops=dict(facecolor="cyan", shrink=0.05),
)

# Set labels and title
ax.set_xlabel(xlabel_value)
ax.set_ylim(ylim_values)
ax.set_yticks(yticks_values)
ax.set_xticks(weeks)
ax.set_ylabel(ylabel_value)

# Add legend
ax.legend(loc="upper left")

# ===================
# Part 4: Saving Output
# ===================
# Show the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig('line_14.pdf', bbox_inches='tight')
