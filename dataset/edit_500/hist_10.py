import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Sample data (replace with actual data)
# Updated data for a different domain: Sports Performance
intra_team_performance = np.random.normal(0.5, 0.1, 1000)  # Simulated performance similarity within the same team
inter_team_performance = np.random.normal(0.7, 0.2, 1000)  # Simulated performance similarity between different teams
intra_game_performance = np.random.normal(0.4, 0.1, 1000)  # Simulated performance similarity within the same game
inter_game_performance = np.random.normal(0.6, 0.2, 1000)  # Simulated performance similarity between different games
xlabel = "Performance Similarity"
ylabel = "Frequency"
binslist = [30, 30, 30, 30]
labels = ["Inter Team", "Intra Team"]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Set the figure size to match the original image's dimensions
plt.figure(figsize=(10, 3))

# Left subplot
ax_left = plt.subplot(1, 2, 1)
plt.hist(
    inter_team_performance, bins=binslist[0], alpha=0.5, label=labels[0], color="#4498c8", zorder=2
)
plt.hist(
    intra_team_performance, bins=binslist[1], alpha=0.5, label=labels[1], color="#5ac4a2", zorder=3
)
leg = plt.legend(
    frameon=False
)  # Make legend background transparent and remove the border
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.tick_params(axis="both", which="both", length=0)
plt.gca().set_facecolor("#eaeaf1")
plt.grid(True, color="white", zorder=0)
for spine in plt.gca().spines.values():
    spine.set_visible(False)

# Right subplot
ax_right = plt.subplot(1, 2, 2)
plt.hist(
    inter_game_performance,
    bins=binslist[2],
    alpha=0.5,
    label=labels[0],
    color="#4498c8",
    zorder=2,
)
plt.hist(
    intra_game_performance,
    bins=binslist[3],
    alpha=0.5,
    label=labels[1],
    color="#5ac4a2",
    zorder=3,
)
leg = plt.legend(frameon=False)
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.tick_params(axis="both", which="both", length=0)
plt.gca().set_facecolor("#eaeaf1")
plt.grid(True, color="white", zorder=0)
for spine in plt.gca().spines.values():
    spine.set_visible(False)

# Set axis spine colors to black
for ax in [ax_left, ax_right]:
    for spine in ax.spines.values():
        spine.set_edgecolor("black")

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout to prevent overlap
plt.tight_layout()

# Display the figure
plt.savefig('hist_10.pdf', bbox_inches='tight')
