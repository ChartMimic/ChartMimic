# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Sample data
ensemble_size = np.arange(5, 31, 1)
accuracy_mean = np.array(
    [
        75.2,
        76.1,
        76.7,
        77.0,
        77.2,
        77.3,
        77.4,
        77.5,
        77.5,
        77.5,
        77.5,
        77.5,
        77.5,
        77.5,
        77.5,
        77.5,
        77.5,
        77.5,
        77.5,
        77.5,
        77.5,
        77.5,
        77.5,
        77.5,
        77.5,
        77.5,
    ]
)
accuracy_std = np.array(
    [
        1.0,
        0.9,
        0.8,
        0.7,
        0.6,
        0.5,
        0.4,
        0.3,
        0.3,
        0.3,
        0.3,
        0.3,
        0.3,
        0.3,
        0.3,
        0.3,
        0.3,
        0.3,
        0.3,
        0.3,
        0.3,
        0.3,
        0.3,
        0.3,
        0.3,
        0.3,
    ]
)

# Axes Limits and Labels
xlabel_value = "Ensemble Size"
xlim_values = [3.5, 32]
xticks_values = np.arange(6, 31, 3)

ylabel_value = "Accuracy"
ylim_values = [74.5, 78.0]


# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plotting the mean accuracy with the standard deviation as a shaded area
plt.figure(figsize=(6, 5))
plt.plot(ensemble_size, accuracy_mean, color="#1f77b4")
plt.fill_between(
    ensemble_size,
    accuracy_mean - accuracy_std,
    accuracy_mean + accuracy_std,
    color="#1f77b4",
    alpha=0.2,
)

# Set x-axis to only display specific ticks and extend y-axis to leave space at top
plt.xticks(xticks_values, fontsize=12)
plt.yticks(fontsize=12)
plt.xlim(xlim_values)  # Adjusted x-axis limit
plt.ylim(ylim_values)  # Adjusted y-axis limit

# Labeling the axes
plt.xlabel(xlabel_value, fontsize=16)
plt.ylabel(ylabel_value, fontsize=16)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save plot
plt.tight_layout()
plt.savefig('line_37.pdf', bbox_inches='tight')
