# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data
x = [0, 25, 50, 75, 100, 125, 150, 175, 200]
pilote_y = [0.85, 0.88, 0.90, 0.92, 0.93, 0.94, 0.80, 0.75, 0.70]
retrained_y = [0.78, 0.80, 0.83, 0.85, 0.87, 0.88, 0.89, 0.90, 0.91]
pretrained_accuracy = 0.75

# Axes Limits and Labels
xlabel_value = "Number of exemplars in class 'Run'"
xlim_values = [-10, 215]
xticks_values = np.arange(25, 201, 25)

ylabel_value = "avg. accuracy of five rounds"
ylim_values = [0, 100]
yticks_values = np.arange(0.60, 1.00, 0.05)

# Labels
label_1 = "PILOTE"
label_2 = "Re-trained model"
label_3 = "Pre-trained model accuracy"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plot
fig, ax = plt.subplots(
    figsize=(6, 4)
)  # Adjusting figure size to match original image dimensions

# Line charts
ax.plot(x, pilote_y, marker="s", color="#d62728", label=label_1)
ax.plot(
    x, retrained_y, marker="p", color="#1f77b4", label=label_2, markersize=8
)

# Set x,y-axis to only display specific ticks and extend y-axis to leave space at top
plt.yticks(yticks_values, fontsize=12)
plt.xticks(xticks_values, fontsize=12)
plt.xlim(xlim_values)  # Adjusted y-axis limit

# Horizontal dashed line
ax.axhline(
    y=pretrained_accuracy,
    color="green",
    linestyle="-.",
    label=label_3,
)

# Legend
ax.legend(loc="lower right")

# Labels
ax.set_xlabel(xlabel_value)
ax.set_ylabel(ylabel_value)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and show plot
plt.tight_layout()
plt.savefig('line_28.pdf', bbox_inches='tight')
