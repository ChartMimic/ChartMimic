# ===================
# Part 1: Importing Libraries
# ===================
import numpy as np; np.random.seed(0)

import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Data for the radar chart
labels = np.array(
    [
        "fairy tale",
        "universe",
        "programming world",
        "video game",
        "novel",
        "mythology",
        "general",
        "movie",
        "city",
        "landscape",
        "cultural event",
        "special place",
        "country",
    ]
)
stats_llama = np.array(
    [0.6, 0.7, 0.8, 0.5, 0.6, 0.7, 0.8, 0.5, 0.6, 0.7, 0.8, 0.5, 0.6]
)
stats_gpt = np.array([0.7, 0.8, 0.9, 0.6, 0.7, 0.8, 0.9, 0.6, 0.7, 0.8, 0.9, 0.6, 0.7])
xticks=[0.2, 0.4, 0.6, 0.8]
xtickslabel=["0.2", "0.4", "0.6", "0.8"]
label="Llama-2-70B"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

# Number of variables
num_vars = len(labels)

# Compute angle for each axis
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# The plot is circular, so we need to "complete the loop" and append the start to the end.
stats_llama = np.concatenate((stats_llama, [stats_llama[0]]))
stats_gpt = np.concatenate((stats_gpt, [stats_gpt[0]]))
angles += angles[:1]

# Draw one axe per variable and add labels
plt.xticks(angles[:-1], labels, color="black", size=10)
ax.tick_params(pad=20)  # Increase the distance of the label from the axis

# Draw ylabels
ax.set_rscale("linear")
plt.yticks(xticks, xtickslabel, color="grey", size=7)
plt.ylim(0, 1)

# Plot data
ax.plot(
    angles,
    stats_llama,
    linewidth=1,
    linestyle="solid",
    label=label,
    marker="o",
    color="#3b75af",
)

# Add legend
plt.legend(loc="lower center", bbox_to_anchor=(0.5, -0.2), ncol=2)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout for better fit and save the plot
plt.tight_layout()
plt.savefig('radar_13.pdf', bbox_inches='tight')
