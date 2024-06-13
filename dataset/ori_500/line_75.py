# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data generation with non-linear trends
ensemble_size = np.arange(5, 31, 1)
accuracy_mean_model1 = (
    70 + np.log(ensemble_size) * 5 + np.random.normal(0, 0.5, len(ensemble_size))
)
accuracy_mean_model2 = (
    65 + np.sqrt(ensemble_size) * 2 + np.random.normal(0, 0.5, len(ensemble_size))
)

# Adding some standard deviation visualisation
accuracy_std_model1 = np.linspace(0.8, 1.2, len(ensemble_size))
accuracy_std_model2 = np.linspace(0.6, 1.0, len(ensemble_size))
# Axes Limits and Labels
xlabel_value = "Ensemble Size"
xticks_values = np.arange(min(ensemble_size), max(ensemble_size) + 1, 2)

ylabel_value = "Accuracy"
yticks_values = np.arange(60, 90, 5)
yticklabels = [f"{i}%" for i in np.arange(60, 90, 5)]

# Labels
label_1 = "Model 1 Mean Accuracy"
label_2 = "Model 2 Mean Accuracy"

# Titles
title = "Comparison of Model Accuracies"
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Background and title
ax.set_facecolor("#f9f9f9")
ax.set_title(title, fontsize=16)

# Plotting the mean accuracies with standard deviation as a shaded area
ax.plot(
    ensemble_size,
    accuracy_mean_model1,
    "o-",
    color="#3498db",
    linewidth=2,
    markersize=5,
    label=label_1,
)
ax.fill_between(
    ensemble_size,
    accuracy_mean_model1 - accuracy_std_model1,
    accuracy_mean_model1 + accuracy_std_model1,
    color="#3498db",
    alpha=0.2,
)

ax.plot(
    ensemble_size,
    accuracy_mean_model2,
    "s-",
    color="#e74c3c",
    linewidth=2,
    markersize=5,
    label=label_2,
)
ax.fill_between(
    ensemble_size,
    accuracy_mean_model2 - accuracy_std_model2,
    accuracy_mean_model2 + accuracy_std_model2,
    color="#e74c3c",
    alpha=0.2,
)

# Enhancing the x and y ticks and labels
ax.set_xticks(xticks_values)
ax.set_xticklabels(
    [str(i) for i in np.arange(min(ensemble_size), max(ensemble_size) + 1, 2)],
    fontsize=12,
)
ax.set_yticks(yticks_values)
ax.set_yticklabels(yticklabels, fontsize=12)

# Axis labels and grid
ax.set_xlabel(xlabel_value, fontsize=16)
ax.set_ylabel(ylabel_value, fontsize=16)
ax.grid(True, linestyle="--", which="both", alpha=0.5)

# Legend and layout adjustments
ax.legend()

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig('line_75.pdf', bbox_inches='tight')
