import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Define the data for each method
labels = np.array(
    ["Accuracy", "Efficiency", "Scalability", "Security", "Usability"]
)
stats = np.array([[4, 3, 5, 2, 4], [3, 4, 4, 3, 5], [5, 2, 3, 4, 3]])
titles = ["Bayesian Network (ε = ∞)", "Differential Privacy Synthesizer (ε = ∞)", "Tabular Variational Autoencoder"]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Set the figure size
fig, ax = plt.subplots(figsize=(10, 6), nrows=1, ncols=3, subplot_kw=dict(polar=True))

# Define the number of variables
num_vars = len(labels)
# Compute angle for each axis
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
# The plot is made circular
stats = np.concatenate((stats, stats[:, [0]]), axis=1)
angles += angles[:1]


# Draw one radar chart for each method
for idx, (title, case_data) in enumerate(
    zip(titles, stats)
):
    thisColor = np.random.rand(
        3,
    )
    #    ax[idx].fill(angles, case_data, color=thisColor, alpha=0.1)
    ax[idx].plot(
        angles, case_data, color=thisColor, linewidth=2
    )  # Change the color for each method
    ax[idx].set_yticks([1, 2, 3, 4, 5])
    ax[idx].set_xticks(angles[:-1])
    ax[idx].set_xticklabels(labels)
    ax[idx].set_title(title, size=14, color="black", position=(0.5, -0.1))

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout for better fit
plt.tight_layout()

# Show the plot
plt.savefig('radar_4.pdf', bbox_inches='tight')
