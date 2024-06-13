# ===================
# Part 1: Importing Libraries
# ===================

import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Data for plotting
test_case_index = [1, 2, 3, 4, 5]
single_lstm_error = [0.08, 0.06, 0.07, 0.05, 0.05]
ensemble_lstm_error = [0.04, 0.03, 0.04, 0.03, 0.04]
cae_reconstruction_error = [0.01, 0.02, 0.01, 0.02, 0.01]

# Labels and Titles
xlabel = "Test Case Index"
ylabel = "Average Relative Error, u"
title = "Average Relative Error, u"

# Legend labels
single_lstm_label = "Single LSTM"
ensemble_lstm_label = "Ensemble LSTM"
cae_reconstruction_label = "CAE Reconstruction"

# Plot limits
xlim_values = (1.0, 5.0)
ylim_values = (0.01, 0.08)

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Set figure size in inches to match the original image's dimensions
plt.figure(figsize=(8, 6))

# Plotting the data with adjusted marker sizes
plt.scatter(
    test_case_index,
    single_lstm_error,
    label=single_lstm_label,
    color="blue",
    clip_on=False,
    zorder=10,
    marker="^",
    s=150,
)  # Adjusted marker size
plt.scatter(
    test_case_index,
    ensemble_lstm_error,
    label=ensemble_lstm_label,
    clip_on=False,
    zorder=10,
    color="green",
    marker="s",
    s=150,
)  # Adjusted marker size
plt.scatter(
    test_case_index,
    cae_reconstruction_error,
    label=cae_reconstruction_label,
    clip_on=False,
    zorder=10,
    color="black",
    marker="o",
    s=100,
)  # Adjusted marker size

# Adding labels and title
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.title(title, y=1.1)

# Adding a legend with adjusted order
handles, labels = plt.gca().get_legend_handles_labels()
order = [2, 1, 0]  # Adjusted order to match the reference picture
plt.legend([handles[idx] for idx in order], [labels[idx] for idx in order])

plt.legend(loc="upper right", ncol=3, bbox_to_anchor=(1, 1.08), frameon=False)
plt.xlim(*xlim_values)
plt.ylim(*ylim_values)
# Show grid
plt.grid(True)

# ===================
# Part 4: Saving Output
# ===================
# Show the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig('scatters_13.pdf', bbox_inches='tight')
