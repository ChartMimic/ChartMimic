import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)

from matplotlib.gridspec import GridSpec

# ===================
# Part 2: Data Preparation
# ===================
# ========== Bar with Error Data (AI Task Success Rates) ==========

# Medical tasks and their success rates
medical_tasks = ["Diagnosis", "Treatment Plan", "Follow-up Care", "Emergency Response"]
success_rates = [95, 90, 82, 80]
errors = [7, 4, 8, 4]

# ========== Scatter with Error Data (Treatment Algorithm Efficiency) ==========
# Algorithms
algorithms = ["Alg1", "Alg2", "Alg3", "Alg4"]
# Efficiency scores
efficiency = np.random.uniform(50, 90, len(algorithms))
# Standard deviations
std_devs = np.random.uniform(10, 20, len(algorithms))

# ========== Line with Error Data (Treatment Model Adaptability) ==========
# Models
models = ["Model A", "Model B", "Model C", "Model D"]
# Adaptability scores in different conditions
adaptability_normal = np.random.uniform(110, 85, len(models))
adaptability_stress = np.random.uniform(85, 115, len(models))
# Error
error = np.random.uniform(1, 2, len(models))

# Titles and labels for the plots
titles = ["Medical Task Success Rates", "Treatment Algorithm Efficiency Scores", "Treatment Model Adaptability"]
ylabels = ["Success Rate (%)", "Efficiency (%)", "Adaptability Score (%)"]
ax2ylim = [30, 110]
ax3labels = ["Normal Conditions", "Stress Conditions"]

# Placeholder to show where the bar plot, scatter plot, and line plot would be displayed. Actual plotting code is not included.
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Bar with Error Plot
# Create figure and grid layout
fig = plt.figure(figsize=(10, 10))
gs = GridSpec(2, 2, figure=fig)

ax1 = fig.add_subplot(gs[0, :])
ax1.bar(medical_tasks, success_rates, yerr=errors, color="skyblue", capsize=5, ecolor="grey")
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
    adaptability_normal,
    yerr=error,
    fmt="o-",
    color="green",
    ecolor="grey",
    capsize=5,
    label=ax3labels[0],
)
ax3.errorbar(
    models,
    adaptability_stress,
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
