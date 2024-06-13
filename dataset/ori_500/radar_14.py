# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# Data for each model
labels = np.array(
    [
        "Humanities",
        "Writing",
        "Roleplay",
        "Reasoning",
        "Math",
        "Coding",
        "Extraction",
        "STEM",
    ]
)
GPT_J_6B = np.array([0.8, 0.9, 0.7, 0.85, 0.9, 0.75, 0.8, 0.85])
TinyLLaMA_1_1B = np.array([0.6, 0.65, 0.5, 0.7, 0.75, 0.6, 0.65, 0.7])
OpenLLaMA_3B = np.array([0.7, 0.8, 0.6, 0.75, 0.8, 0.65, 0.7, 0.75])
OpenMoE_8B_32E = np.array([0.9, 0.95, 0.85, 0.9, 0.95, 0.8, 0.9, 0.95])
yticks=[0.2, 0.4, 0.6, 0.8]
labels2=["GPT-J-6B","TinyLLaMA-1.1B","OpenLLaMA-3B","OpenMoE-8B/32E"]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

# Number of variables
num_vars = len(labels)

# Compute angle for each axis
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# The plot is made circular, so we need to complete the loop
GPT_J_6B = np.concatenate((GPT_J_6B, [GPT_J_6B[0]]))
TinyLLaMA_1_1B = np.concatenate((TinyLLaMA_1_1B, [TinyLLaMA_1_1B[0]]))
OpenLLaMA_3B = np.concatenate((OpenLLaMA_3B, [OpenLLaMA_3B[0]]))
OpenMoE_8B_32E = np.concatenate((OpenMoE_8B_32E, [OpenMoE_8B_32E[0]]))
angles += angles[:1]

# Draw one axe per variable and add labels
plt.xticks(angles[:-1], labels, color="black", size=10)
ax.tick_params(pad=10)  # Increase the distance of the label from the axis

# Draw ylabels
ax.set_rlabel_position(0)
plt.yticks(yticks, [], color="grey", size=7)
plt.ylim(0, 1)

# Plot data
ax.plot(
    angles,
    GPT_J_6B,
    color="#5471ab",
    linewidth=2,
    linestyle="solid",
    label=labels2[0],
    marker="o",
)
ax.plot(
    angles,
    TinyLLaMA_1_1B,
    color="#d1885c",
    linewidth=2,
    linestyle="solid",
    label=labels2[1],
    marker="o",
)
ax.plot(
    angles,
    OpenLLaMA_3B,
    color="#6aa66e",
    linewidth=2,
    linestyle="solid",
    label=labels2[2],
    marker="o",
)
ax.plot(
    angles,
    OpenMoE_8B_32E,
    color="#b65655",
    linewidth=2,
    linestyle="solid",
    label=labels2[3],
    marker="o",
)

# Add legend
plt.legend(loc="upper left", bbox_to_anchor=(1, 1))

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout for better fit and save the plot
plt.tight_layout()
plt.savefig('radar_14.pdf', bbox_inches='tight')
