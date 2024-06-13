import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Define the new data for each method (plastic processing techniques)
labels = np.array(
    ["Cardio", "Strength", "Flexibility", "Endurance", "Balance"]
)
stats = np.array(
    [
        [3, 4, 5, 2, 4],  # Cardio
        [5, 3, 4, 5, 3],  # Strength
        [4, 3, 2, 4, 5],  # Flexibility
    ]
)
titles = ["Cardio", "Strength Training", "Flexibility"]
rticks = [1, 2, 3, 4, 5]
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Set the figure size
fig, ax = plt.subplots(figsize=(10, 8), nrows=1, ncols=3, subplot_kw=dict(polar=True))
# Define the number of variables
num_vars = len(labels)

# Compute angle for each axis
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# The plot is made circular
stats = np.concatenate((stats, stats[:, [0]]), axis=1)
angles += angles[:1]
# Define colors
colors = ["red", "green", "blue"]

# Draw one radar chart for each plastic processing technique
for idx, (title, case_data) in enumerate(
    zip(titles, stats)
):
    ax[idx].fill(angles, case_data, color=colors[idx], alpha=0.25)
    ax[idx].plot(angles, case_data, color=colors[idx])
    ax[idx].set_rticks(rticks)
    ax[idx].set_xticks(angles[:-1])
    ax[idx].set_xticklabels(labels)
    ax[idx].set_title(title, color=colors[idx])

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout for better fit
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

plt.savefig('radar_17.pdf', bbox_inches='tight')
