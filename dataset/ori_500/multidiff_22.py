# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)

from matplotlib.gridspec import GridSpec

# ===================
# Part 2: Data Preparation
# ===================

# ========== Bar with Error Data (AI Task Success Rates) ==========
# AI Tasks
ai_tasks = ["Image Recog.", "Speech Recog.", "Language Proc.", "Game AI"]
# Success rates
success_rates = [85, 78, 92, 88]
# Error margins
errors = [5, 7, 4, 6]

# ========== Scatter with Error Data (Algorithm Efficiency) ==========
# Algorithms
algorithms = ["Alg1", "Alg2", "Alg3", "Alg4"]
# Efficiency scores
efficiency = np.random.uniform(70, 100, len(algorithms))
# Standard deviations
std_devs = np.random.uniform(5, 10, len(algorithms))

# ========== Line with Error Data (AI Model Adaptability) ==========
# Models
models = ["Model A", "Model B", "Model C", "Model D"]
# Adaptability scores
adaptability_dry = np.random.uniform(80, 95, len(models))
adaptability_wet = np.random.uniform(75, 90, len(models))
# Error
error = np.random.uniform(1, 2, len(models))
titles = ["AI Task Success Rates", "Algorithm Efficiency Scores", "AI Model Adaptability"]
ylabels=["Success Rate (%)", "Efficiency (%)", "Adaptability Score (%)"]
ax2ylim=[60, 110]
ax3labels=["Dry Conditions", "Wet Conditions"]
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create figure and grid layout
fig = plt.figure(figsize=(10, 10))
gs = GridSpec(2, 2, figure=fig)

# Bar with Error Plot
ax1 = fig.add_subplot(gs[0, :])
ax1.bar(ai_tasks, success_rates, yerr=errors, color="skyblue", capsize=5, ecolor="grey")
ax1.set_title(titles[0])
ax1.set_ylabel(ylabels[0])
ax1.grid(True)

# Scatter with Error Plot
ax2 = fig.add_subplot(gs[1, 0])
ax2.errorbar(
    algorithms,
    efficiency,
    yerr=std_devs,
    fmt="o",
    color="#e5989b",
    ecolor="grey",
    capsize=5,
    ms=10,
)
ax2.set_title(titles[1])
ax2.set_ylabel(ylabels[1])
ax2.set_ylim(ax2ylim)
ax2.grid(True)

# Line with Error Plot
ax3 = fig.add_subplot(gs[1, 1])
ax3.errorbar(
    models,
    adaptability_dry,
    yerr=error,
    fmt="o-",
    color="green",
    ecolor="grey",
    capsize=5,
    label=ax3labels[0],
)
ax3.errorbar(
    models,
    adaptability_wet,
    yerr=error,
    fmt="s-",
    color="blue",
    ecolor="grey",
    capsize=5,
    label=ax3labels[1],
)
ax3.set_title(titles[2])
ax3.set_ylabel(ylabels[2])
ax3.legend(title="Conditions")
ax3.grid(True)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save the figure
plt.tight_layout()
plt.savefig('multidiff_22.pdf', bbox_inches='tight')
